"""
render_resume.py
- Loads resume.json
- Renders resume_template.tex (Jinja2) using a registered `latex_escape` filter
- Writes output_resume.tex
- Attempts to compile PDF using tectonic
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from pylatexenc.latexencode import utf8tolatex

from setup_tectonic import get_tectonic_exe_path, setup_tectonic

setup_tectonic()

TEMPLATES_DIR = Path("templates")

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_FILE = str(TEMPLATES_DIR / "jakes-resume-template-jinja.tex")
INPUT_JSON = "resume.json"
OUTPUT_TEX = "output_resume.tex"
OUTPUT_PDF = "output_resume.pdf"


def latex_escape(s):
    if s is None:
        return ""
    return utf8tolatex(str(s), non_ascii_only=False)


# add this function to your render_resume.py (above render_tex)
def sanitize_string(s: str) -> str:
    if s is None:
        return ""
    s = str(s).strip()
    # Replace literal backslash-n, backslash-r, backslash-t with spaces
    # and collapse multiple whitespace into single spaces.
    s = s.replace("\\n", " ").replace("\\r", " ").replace("\\t", " ")
    # Replace literal double backslashes (\\) with a single backslash or a space.
    s = s.replace("\\\\", "\\")
    # Optional: collapse multiple newlines/carriage returns (if actual newlines exist)
    s = " ".join(s.split())
    return s


def sanitize_structure(obj):
    if isinstance(obj, dict):
        return {k: sanitize_structure(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [sanitize_structure(v) for v in obj]
    if isinstance(obj, str):
        return sanitize_string(obj)
    return obj


def render_tex(context):
    env = Environment(
        loader=FileSystemLoader(str(BASE_DIR)),
        undefined=StrictUndefined,
        block_start_string="{%",
        block_end_string="%}",
        variable_start_string="{{",
        variable_end_string="}}",
        autoescape=False,
    )
    # Register filter available in the template: {{ value | latex_escape }}
    env.filters["latex_escape"] = latex_escape

    template = env.get_template(TEMPLATE_FILE)
    rendered = template.render(**context)
    (BASE_DIR / OUTPUT_TEX).write_text(rendered, encoding="utf-8")
    print(f"\n[ok] Wrote {OUTPUT_TEX}")


def compile_pdf():
    cmd = [get_tectonic_exe_path(), "--print", OUTPUT_TEX]

    if shutil.which(cmd[0]) is None:
        print(f"[error] Tectonic not found: {cmd[0]}")
        return False

    print(f"[info] Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
        candidate = Path(OUTPUT_TEX).with_suffix(".pdf")
        if candidate.exists():
            candidate.rename(OUTPUT_PDF)
        print(f"\n[ok] PDF generated: {OUTPUT_PDF}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[warn] command failed: {' '.join(cmd)}; {e}")

        return False


def main():
    if not (BASE_DIR / TEMPLATE_FILE).exists():
        print(f"[error] Missing template: {TEMPLATE_FILE}")
        sys.exit(1)
    if not (BASE_DIR / INPUT_JSON).exists():
        print(f"[error] Missing JSON: {INPUT_JSON}")
        sys.exit(1)

    raw = json.loads((BASE_DIR / INPUT_JSON).read_text(encoding="utf-8"))
    clean = sanitize_structure(raw)
    # Pass raw JSON directly; template should call | latex_escape where needed.
    render_tex(clean)

    if not compile_pdf():
        print(
            "\n[hint] Check if setup of tectonic was successful. If not try reinstalling tectonic manually as store as `tectonic`."
        )


if __name__ == "__main__":
    main()

"""
render_resume.py
- Loads resume.json
- Renders resume_template.tex (Jinja2) using a registered `latex_escape` filter
- Writes output_resume.tex
- Attempts to compile PDF using tectonic
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import NamedTemporaryFile

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


def render_tex(
    context,
    input_template_file: Path,
    output_tex_file: Path,
):
    env = Environment(
        loader=FileSystemLoader(str(input_template_file.parent)),
        undefined=StrictUndefined,
        block_start_string="{%",
        block_end_string="%}",
        variable_start_string="{{",
        variable_end_string="}}",
        autoescape=False,
    )
    # Register filter available in the template: {{ value | latex_escape }}
    env.filters["latex_escape"] = latex_escape

    template = env.get_template(str(input_template_file.absolute().name))
    rendered = template.render(**context)
    (output_tex_file).write_text(rendered, encoding="utf-8")
    print(f"\n[ok] Wrote {output_tex_file}")


def compile_pdf(generated_tex: Path, output_pdf: Path):
    cmd = [get_tectonic_exe_path(), "--print", str(generated_tex.absolute())]

    if shutil.which(cmd[0]) is None:
        print(f"[error] Tectonic not found: {cmd[0]}")
        return False

    print(f"[info] Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
        candidate = Path(generated_tex).with_suffix(".pdf")
        if candidate.exists():
            shutil.move(str(candidate), str(output_pdf))
        print(f"\n[ok] PDF generated: {output_pdf}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[warn] command failed: {' '.join(cmd)}; {e}")

        return False


def main(input_template_file: Path, resume_json: Path, output_pdf: Path):
    if not (input_template_file).exists():
        print(f"[error] Missing template: {input_template_file}")
        sys.exit(1)
    if not (resume_json).exists():
        print(f"[error] Missing JSON: {resume_json}")
        sys.exit(1)

    raw = json.loads((resume_json).read_text(encoding="utf-8"))
    clean = sanitize_structure(raw)
    # Pass raw JSON directly; template should call | latex_escape where needed.
    output_tex_file = NamedTemporaryFile(suffix=".tex", delete=False).name
    render_tex(
        clean,
        input_template_file=Path(input_template_file),
        output_tex_file=Path(output_tex_file),
    )

    if not compile_pdf(
        generated_tex=Path(output_tex_file),
        output_pdf=Path(output_pdf),
    ):
        print(
            "\n[hint] Check if setup of tectonic was successful. If not try reinstalling tectonic manually as store as `tectonic`."
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Render resume from JSON to LaTeX and compile to PDF."
    )
    parser.add_argument(
        "--resume-json", type=str, default=INPUT_JSON, help="Path to resume JSON file."
    )
    parser.add_argument(
        "--output-pdf", type=str, default=OUTPUT_PDF, help="Output PDF file name."
    )
    args = parser.parse_args()

    main(
        resume_json=Path(args.resume_json),
        input_template_file=Path(TEMPLATE_FILE),
        output_pdf=Path(args.output_pdf),
    )

## jinja2-latex-resume

> Generate professional, highly customizable resumes with Python, Jinja2 templating, LaTeX, and automatic PDF export. Effortlessly create data-driven, beautiful CVs with modern, automated workflows.

**In simple terms:** \
➡️ You upload a json (relatively easy structure to latex) with your professional details \
➡️ This project uses the existing template .tex (latex file converted to jinja2 template) \
➡️ Renders a .tex file with your details \
➡️ Compiles to a beautiful PDF resume.


### Example Usage:

Given that you already have a resume json file named `resume-jim-halpert.json`, you can generate a PDF resume by running the following command:

```bash
python render_resume.py --resume-json resume-jim-halpert.json --output-pdf jim-halpert.pdf
```

Check out the generated PDF resume: [jim-halpert.pdf](examples/output_resume_pdf/jim-halpert.pdf)



### Coming up soon:

- more templates 🥳
- better documentation 
- tested report for windows devices (currently only tested on linux - windows setup code is LLM generated but untested)

> ⚠️ Still working on it. ⚠️
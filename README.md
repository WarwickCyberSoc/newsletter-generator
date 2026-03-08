# Email newsletter generator
A script used to generate a HTML email newsletter from a template HTML file and
some markdown files.


The script is based on Warwick Computer Science Society's script, found
[here](https://github.com/d1s4rr4y/Newsletters)

## Requirements:
  Python 3

  The Markdown Python module (see below).

## Installation
Clone this repo:
```bash
  git clone https://github.com/OscarTopliss/newsletter-generator
```
Install the requirements (reccommended method using a virtual environment):
```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
 ```
Whenever you run `generate.py`, make sure to source the venv (`source .venv/bin/activate`)
beforehand.

## Usage
The script take your specified markdown file and inserts it into a provided HTML
template. The template needs to have {{ content }} somewhere in it, as this is
what will be replaced by the markdown file.

### Sections
You can split your newsletter into multiple sections. This is useful for
sections which don't often change, e.g. sponsorships. To do this,
{{ section }} somewhere in your main markdown file. The script will look for
a file called section.md, and insert it into the newsletter before converting it
to HTML.

Note: Sections can't currently be embedded inside other sections. e.g. you can't
have {{ section1 }} in your main markdown file, and {{ section2 }} in
`section1.md`.

You can speicify where the script should look for section files with the -s
or --section flag. By default it will search the current directory.

### Embedded HTML
You can embed normal HTML tags into markdown, which will be kept when the
markdown is converted into HTML with the script. It's a good idea to try this if
things aren't formatting the way you expect in the newsletter.

### Flags
`-h`, `--help`
  Outputs a help message, detailing usage and flags.

`-o`, `--output`
  The output file. By default, the same as the file but with a .html extension.

`-t`,`--template`
  The template file. By default the script looks for template.html

`-s`, `--sections`
  The folder/directory containing any markdown files for specific sections.
  Checks the current directory by default.

## Example
```bash
python3 generate.py newsletter.md
python3 generate.py newsletter.md -o output.html
python3 genreate.py newsletter.md -t knit-soc.html -s ./sections
```

### Example Weekly Newsletter
The repo includes an example weekly newsletter in the format which was used for CyberSoc 2025/2026.
You can geenrate it with `python3 generate.py example-newsletter.md`.

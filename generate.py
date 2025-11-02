import markdown
import sys
from pathlib import Path
import re

# opens a markdown file, reads its markdown, and returns it as HTML.
# The


USAGE_STRING = '''
Example usage:
    python3 generate.py <filename>.md
Help:
    python3 generate.py --help
'''

HELP_STRING = '''
Newsletter generator script v1.0
Script for generating HTML for email newsletters from markdown files.

Example usage:
    python3 generator.py newsletter-name.md
    python3 generator.py newsletter.md -o output.html
    python3 generator.py newsletter.md -t template-2.html -s ./sections

will create newsletter-name.html

This script requires the Markdown module.
Recommended method is to install the module using a virtual environment and pip.
Steps:
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 generator.py newsletter-name.md

will create newsletter-name.html

Optional flags:
    -h, --help              Prints this help text.
    -o, --output            The filename/path for the rendered HTML file.
                            By default, the same as the input file but with a
                            .html extension.
    -t --template           The HTML template the content will be inserted into.
                            By default looks for template.html

    -s --sections           The directory to look for newsletters sections in.
                            By default uses the current directory.

You can split sections (e.g. sponsorship sections, signature etc) into seperate
markdown files. You can reference them in your main markdown file like this:

# Example title
{{ section1 }}
{{ section2 }}

The script will look for files called section1.md and section2.md in the
sections directory specified by the -s flag.
'''
# Gets the value for a flag, returning None if the flag is never used.
# If the flag is used, but there isn't a value after it, sys.exit() with a
# printed error message.
def get_flag_value_or_exit(flag1 : str, flag2: str):
    if flag1 in sys.argv:
        flag1_index = sys.argv.index(flag1)
        if len(sys.argv) <= flag1_index:
            print(f"Error! No value supplied for flag {flag1}")
            print(USAGE_STRING)
            sys.exit()
        return sys.argv[flag1_index + 1]

    elif flag2 in sys.argv:
        flag2_index = sys.argv.index(flag2)
        if len(sys.argv) <= flag2_index:
            print(f"Error! No value supplied for flag {flag2}")
            print(USAGE_STRING)
            sys.exit()
        return sys.argv[flag2_index + 1]

    else:
        return None
# Opens a markdown file and renders it to HTML. if the main flag is set, it
# checks for sections in the {{ section }} syntax, and inserts markdown from
# other files into them.

def open_section(section_name : str, section_dir : str):
    file = Path(section_dir) / section_name
    if not file.is_file():
        print(f"Error! No section file for \
              {{{{ {section_name.removesuffix(".md")} }}}} ")
        print(USAGE_STRING)
        sys.exit()

    with file.open() as section_file:
        return section_file.read()

# Renders the newsletter, including any section replacement. returns the
# rendered HTML as a string.
def render_newsletter(filename : str , section_dir : str , template : str ):
    with open(filename, encoding="utf8") as in_file:
        input_markdown = in_file.read()

        sections = re.findall("{{ [a-z0-9_-]+ }}", input_markdown)

        for section in sections:
            section_file_name = section.replace("{{","").replace("}}","")\
            .replace(" ","") + ".md"
            input_markdown = input_markdown.replace(
                f"{section}",
                open_section(section_file_name, section_dir)
            )

        input_html = markdown.markdown(input_markdown)

        with open(template) as template_file:
            template_content = template_file.read()

            return template_content.replace("{{ content }}", input_html)

        # markdown.markdown renders markdown as HTML.


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print(USAGE_STRING)
        sys.exit()
    if "--help" in sys.argv or '-h' in sys.argv:
        print(HELP_STRING)
        sys.exit()

    input_file = sys.argv[1]

    if not Path(input_file).is_file():
        print(f"Error! File {input_file} doesn't exist.")
        print(USAGE_STRING)
        sys.exit()

    if not input_file.endswith(".md"):
        print(USAGE_STRING)
        sys.exit

    output_file = get_flag_value_or_exit("-o","--output")
    if output_file == None:
        output_file = input_file.removesuffix(".md") + ".html"

    template_file = get_flag_value_or_exit("-t", "--template")
    if template_file == None:
        template_file = "template.html"

    if not Path(template_file).is_file():
        print(f"Error! Template {template_file} doesn't exist.")
        print(USAGE_STRING)
        sys.exit()

    section_dir = get_flag_value_or_exit("-s", "--sections")
    if section_dir == None:
        section_dir = '.'

    if not Path(section_dir).is_dir():
        print(f"Error! {section_dir} isn't a valid folder/directory.")
        print(USAGE_STRING)
        sys.exit()

    newsletter_html = render_newsletter(input_file,
        section_dir,
        template_file
    )

    with open(output_file, "w") as output:
        output.write(newsletter_html)

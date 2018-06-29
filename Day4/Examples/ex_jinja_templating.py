# templating is a way to dynamically generate HTML based on the python code
# it also incorporates the python variables etc. inside the HTML document
# such HTML documents are called templates
from jinja2 import Template


def string_template():
    template = Template('Hello {{ name }}!')
    print(template.render(name='John Doe'))


def html_template():
    template = Template(open('jinja_template.html').read())
    print(template.render({'heading': 'this is a heading', 'values': [1,2,3]}))


if __name__ == "__main__":
    string_template()
    html_template()

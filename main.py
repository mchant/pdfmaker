from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from jinja2 import Environment, FileSystemLoader


font_config = FontConfiguration()
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")
template_vars = {
    'title': 'my documents',
    'name': 'mick',
    'number': 12,
    'managers': [{'name':'dave', 'car':'honda', 'data': ['a', 'b', 'r', 'a']},
                 {'name':'nick', 'car':'toyota', 'data': ['d', 'f', 'x', 'b']},
                 {'name':'jim', 'car':'ford', 'data': ['q', 'r', 's', 'd']}],
}
html_out = template.render(template_vars)
HTML(string=html_out).write_pdf(target="myreport.pdf",
# stylesheets=["style.css"]
)

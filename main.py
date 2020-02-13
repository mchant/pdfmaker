from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from jinja2 import Environment, FileSystemLoader
import os
import logging


logger = logging.getLogger('weasyprint')
logger.addHandler(logging.FileHandler('weasyprint.log'))

# def generate_outline_str(bookmarks, indent=0):
#     outline_str = ""
#     for i, (label, (page, _, _), children) in enumerate(bookmarks, 1):
#         outline_str += ('%s%d. %s (page %d)' % (
#             ' ' * indent, i, label.lstrip('0123456789. '), page))
#         outline_str += generate_outline_str(children, indent + 2)
#     return outline_str

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
    'image': 'images/rooster.png',
}

css = [CSS(filename="css/mystyle.css"),
       CSS(filename="css/bootstrap.min.css"),
       ]
html_out = template.render(template_vars)
document = HTML(string=html_out, base_url=__file__)
rendered_doc = document.render(stylesheets=css)
# table_of_contents_string = generate_outline_str(rendered_doc.make_bookmark_tree())
# table_of_contents_document = HTML(string=table_of_contents_string).render()
# table_of_contents_page = table_of_contents_document.pages[0]
# rendered_doc.pages.insert(0, table_of_contents_page)
rendered_doc.write_pdf(target="myreport.pdf")
os.system("myreport.pdf")

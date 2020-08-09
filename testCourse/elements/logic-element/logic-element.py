import chevron
import lxml.html
import prairielearn as pl

def prepare(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    optional_attribs = ['logic-ops']
    pl.check_attribs(element, [], optional_attribs)

    logic_ops = [ { "op": op.strip().lower() } for op in pl.get_string_attrib(element, 'logic-ops').split(",") ]
    data['params']['input_nodes'] = [{"node": "A"}, {"node": "B"}, {"node": "C"}]
    data['params']['output_nodes'] = [{"node": "X"}]
    data['params']['logic_ops'] = logic_ops


    return data

def render(element_html, data):
    html_params = {
        'input_nodes': data['params']['input_nodes'],
        'output_nodes': data['params']['output_nodes'],
        'logic_ops': data['params']['logic_ops'],
        'image_url': data['options']['client_files_element_url']
    }
    with open('logic-element.mustache', 'r') as f:
        return chevron.render(f, html_params).strip()
import chevron

def prepare(element_html, data):
    data['params']['input_nodes'] = [{"node": "A"}, {"node": "B"}, {"node": "C"}]
    return data

def render(element_html, data):
    html_params = {
        'input_nodes': data['params']['input_nodes']
    }
    with open('logic-element.mustache', 'r') as f:
        return chevron.render(f, html_params).strip()
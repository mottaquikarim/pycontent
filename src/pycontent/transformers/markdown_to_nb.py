import nbformat

from string import Template

from nbconvert import HTMLExporter
from nbconvert.preprocessors import CellExecutionError, ExecutePreprocessor
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell


html = """${BODY}"""


def get_cell(line, block):
    if "python" in line:
        return new_markdown_cell(block)

    return new_code_cell(block)


def tform(content, path):
    path_bits = path.split('.')
    path = ".".join(path_bits[0:-1]) + ".html"

    nb = new_notebook()
    current_cell = []
    all_cells = []
    for line in content.splitlines():
        if line.startswith('```'):
            block = "\n".join(current_cell)
            nb.cells.append(get_cell(line, block))
            all_cells.append(block)
            current_cell = []
            continue

        current_cell.append(line)

    try:
        ep = ExecutePreprocessor(timeout=10, kernel_name='python', allow_errors=True)
        ep.preprocess(nb, {'metadata': {'path': ''}})
    except:
        pass

    html_exporter = HTMLExporter()
    html_exporter.template_file = 'full'
    (body, resources) = html_exporter.from_notebook_node(nb)
    with open(path, "w") as f:
        f.write(Template(html).substitute({'BODY': body}))

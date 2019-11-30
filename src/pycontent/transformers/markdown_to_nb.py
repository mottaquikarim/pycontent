import nbformat

from string import Template

from nbconvert import HTMLExporter
from nbconvert.preprocessors import CellExecutionError, ExecutePreprocessor
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

from pycontent.bucket.enums import SupportedExtensions

html = """${BODY}"""
CODE_BLOCK = "```"
COLAB_BASE = "https://colab.research.google.com"
GITHUB_REPO_NAME = "github/mottaquikarim/pycontent"


def chainable(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return args[0]

    return wrapper


class NotebookBuilder:
    EP_TIMEOUT = 1
    EP_KERNAL_NAME = 'python'
    EP_ALLOW_ERRORS = True
    EP_EXECUTE_NB = False

    @staticmethod
    def get_cell(line, block):
        if "python" in line:
            return new_markdown_cell(block)

        return new_code_cell(block)

    @staticmethod
    def get_supported_extension(content_type):
        if content_type == SupportedExtensions.HTML:
            return "html"
        if content_type == SupportedExtensions.IPYNB:
            return "ipynb"

    @staticmethod
    def get_path(base_path, extension_type):
        return f"{base_path}.{NotebookBuilder.get_supported_extension(extension_type)}"

    def get_colab_cell(self):
        ext = self.get_supported_extension(SupportedExtensions.IPYNB)
        colab_url = f"{COLAB_BASE}/{GITHUB_REPO_NAME}/blob/master/{self.base_path}.{ext}"
        colab_img_url = f"{COLAB_BASE}/assets/colab-badge.svg"
        mrkdown = f"[![Open In Colab]({colab_img_url})]({colab_url})"
        return new_markdown_cell(mrkdown)

    def __init__(self, base_path, content_type=SupportedExtensions.HTML):
        self.base_path = base_path
        self.content_type = content_type

        self.content_path = NotebookBuilder.get_path(base_path, content_type)

        self.nb = new_notebook()

        self.current_cell = []
        self.all_cells = []

    @chainable
    def build_notebook(self, content):
        self.nb.cells.append(self.get_colab_cell())
        for line in content.splitlines():
            if line.startswith(CODE_BLOCK):
                block = "\n".join(self.current_cell)
                self.nb.cells.append(self.get_cell(line, block))
                self.all_cells.append(block)
                self.current_cell = []
                continue

            self.current_cell.append(line)

        if self.current_cell:
            block = "\n".join(self.current_cell)
            self.nb.cells.append(self.get_cell('python', block))
        # self.nb.cells.append(self.get_cell(line, block))

    @chainable
    def write_content(self):
        """
        # TODO: handle html generation at some point
        ```
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'full'
        (body, resources) = html_exporter.from_notebook_node(nb)
        with open(path, "w") as f:
            f.write(Template(html).substitute({'BODY': body}))
        ```
        """
        with open(self.content_path, "w") as f:
            nbformat.write(self.nb, f)

    @chainable
    def execute_nb(self):
        if not EP_EXECUTE_NB:
            return

        try:
            ep = ExecutePreprocessor(
                timeout=self.EP_TIMEOUT,
                kernel_name=self.EP_KERNAL_NAME,
                allow_errors=self.EP_ALLOW_ERRORS,)
            ep.preprocess(self.nb, {'metadata': {'path': ''}})
        except:
            pass


def tform(content, path):
    nbuilder = NotebookBuilder(path, content_type=SupportedExtensions.IPYNB)
    nbuilder \
        .build_notebook(content) \
        .execute_nb() \
        .write_content()

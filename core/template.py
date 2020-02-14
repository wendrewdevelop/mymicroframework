import os
from typing import Dict
from config import BASEDIR


class Template:
    def __init__(self, template_folder="views") -> None:
        self.template_folder = template_folder

    def render(self, filename: str, context: Dict[str, str]):
        current_path = os.path.join(BASEDIR, self.template_folder, filename)

        if not os.path.isdir(self.template_folder):
            raise NotADirectoryError(f"Diretório {self.template_folder} não existe!")

        if not os.path.isfile(current_path):
            raise FileExistsError(f"Arquivo {filename} não existe!")

        with open(current_path, "r") as f:
            html = f.read()

        for k, v in context.items():
            html = html.replace(f"@{k}", v)

        return html.encode()
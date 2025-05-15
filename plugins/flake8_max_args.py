# archivo: flake8_max_args.py

import ast


class MaxArgsChecker:
    name = "flake8-max-args"
    version = "0.1.0"

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                arg_count = len(node.args.args)

                # Excluir 'self' o 'cls' si es método de clase/instancia
                if node.args.args:
                    first_arg = node.args.args[0].arg
                    if first_arg in ("self", "cls"):
                        arg_count -= 1

                if arg_count > 4:
                    yield (
                        node.lineno,
                        node.col_offset,
                        f"MAA100 Too many arguments in function "
                        f"'{node.name}' ({arg_count} arguments)",
                        type(self),
                    )

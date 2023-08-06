import json
from reorder_python_imports import (
    fix_file_contents,
    Replacements,
    REMOVALS,
    import_obj_from_str,
    REPLACES,
    _validate_replace_import,
)
import typing as t
from IPython.core import getipython
from IPython.core.display import HTML, Javascript
from IPython.core.interactiveshell import ExecutionInfo
from IPython.display import display
from IPython.terminal.interactiveshell import TerminalInteractiveShell as Ipt

formatter = None


class ReorderPythonImports:
    """Formatter that stores config and call `black.format_cell`."""

    def __init__(
        self,
        ip: Ipt,
        is_lab: bool = True,
        min_python_version: t.Optional[t.Tuple[int]] = None,
    ) -> None:
        """Initialize the class with the passed in config.
        Notes on the JavaScript stuff for notebook:
            - Requires:
                - update=False for the `html` part
            - Doesn't seem to matter:
                - trailing semicolon
            - Other:
                - Can use `jb_cells.find` instead of the for loop if you set the main function to `text/html` and set `raw=True`
            def display:
                https://github.com/ipython/ipython/blob/77e188547e5705a0e960551519a851ac45db8bfc/IPython/core/display_functions.py#L88  # noqa
        Arguments:
            ip: ipython shell
            is_lab: whether running in jupyterlab as opposed to ipython
                notebook
            black_config: Dictionary for black config options
        """
        self.shell = ip
        self.min_python_version = min_python_version
        if self.min_python_version is None:
            versions = sorted(REMOVALS.keys() | REPLACES.keys())
            self.min_python_version = versions[0]

        self.is_lab = is_lab
        if is_lab:
            js_func = """
                <script type="application/javascript" id="jupyter_reorder_python_imports">
                (function() {
                    if (window.IPython === undefined) {
                        return
                    }
                    var msg = "WARNING: it looks like you might have loaded " +
                        "jupyter_reorder_python_imports in a non-lab notebook with " +
                        "`is_lab=True`. Please double check, and if " +
                        "loading with `%load_ext` please review the README!"
                    console.log(msg)
                    alert(msg)
                })()
                </script>
                """
        else:
            js_func = """
                <script type="application/javascript" id="jupyter_reorder_python_imports">
                function jb_set_cell(
                        jb_formatted_code
                        ) {
                    for (var cell of Jupyter.notebook.get_cells()) {
                        if (cell.input_prompt_number == "*") {
                            cell.set_text(jb_formatted_code)
                            return
                        }
                    }
                }
                </script>
                """
        display(
            HTML(js_func),  # type: ignore
            display_id="jupyter_reorder_python_imports",
            update=False,
        )

    def _set_cell(self, cell_content: str) -> None:
        if self.is_lab:
            self.shell.set_next_input(cell_content, replace=True)
        else:
            js_code = f"""
            (function() {{
                jb_set_cell({json.dumps(cell_content)})
            }})();
            """
            display(  # type: ignore
                Javascript(js_code),  # type: ignore
                display_id="jupyter_reorder_python_imports",
                update=True,
            )

    def _format_cell(self, cell_info: ExecutionInfo) -> None:
        cell_content = str(cell_info.raw_cell)

        try:
            to_remove = {
                import_obj_from_str(s).key
                for k, v in REMOVALS.items()
                if self.min_python_version >= k
                for s in v
            }
            replace_import: t.List[str] = []
            for k, v in REPLACES.items():
                if self.min_python_version >= k:
                    replace_import.extend(
                        _validate_replace_import(replace_s) for replace_s in v
                    )
            to_replace = Replacements.make(replace_import)
            formatted_code = fix_file_contents(
                cell_content,
                to_replace=to_replace,
                to_remove=to_remove,
            )
        except Exception:
            return

        self._set_cell(formatted_code)


def load_ipython_extension(
    ip: Ipt,
) -> None:
    """Load the extension via `%load_ext jupyter_reorder_python_imports`.
    https://ipython.readthedocs.io/en/stable/config/extensions/#writing-extensions  # noqa
    """
    load(ip=ip)


def load(
    ip: t.Optional[Ipt] = None,
    lab: bool = True,
    min_python_version: t.Optional[t.Tuple[int]] = None,
) -> None:
    """Load the extension via `jupyter_reorder_python_imports.load`.
    This allows passing in custom configuration.
    Arguments:
        ip: iPython interpreter -- you should be able to ignore this
        lab: Whether this is a jupyterlab session
        line_length: preferred line length
        target_version: preferred python version
        verbosity: logging verbosity
        **black_config: Other arguments you want to pass to black. See:
            https://github.com/psf/black/blob/911470a610e47d9da5ea938b0887c3df62819b85/src/black/mode.py#L99
    """
    global formatter

    if not ip:
        ip = getipython.get_ipython()  # type: ignore
    if not ip:
        return

    if formatter is None:
        formatter = ReorderPythonImports(
            ip, is_lab=lab, min_python_version=min_python_version
        )
    ip.events.register("pre_run_cell", formatter._format_cell)  # type: ignore


def unload_ipython_extension(ip: Ipt) -> None:
    """Unload the extension.
    https://ipython.readthedocs.io/en/stable/config/extensions/#writing-extensions
    """
    global formatter

    if formatter:
        ip.events.unregister("pre_run_cell", formatter._format_cell)  # type: ignore
        formatter = None

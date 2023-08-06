"""Tests for jupyter_black running in jupyter notebook."""

import typing as t

from conftest import source_from_cell


def test_load(notebook: t.Callable[..., t.Dict[str, t.Any]]) -> None:
    """Test loading with `jupyter_reorder_python_imports.load()`."""
    cells = [
        {
            "source": ["import jupyter_reorder_python_imports"],
        },
        {
            "source": ["jupyter_reorder_python_imports.load(lab=False)"],
        },
        {
            "id": "imports1",
            "source": ["import re\nimport datetime"],
        },
        {
            "id": "imports2",
            "source": ["import datetime\nimport re"],
        },
    ]
    output = notebook(cells)
    cell_imports1 = source_from_cell(output, "imports1")
    assert "".join(cell_imports1) == "import datetime\nimport re\n"
    cell_imports2 = source_from_cell(output, "imports2")
    assert "".join(cell_imports2) == "import datetime\nimport re\n"

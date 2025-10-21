from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.columns import Columns

import os
from rich.align import Align


console = Console()


def border(story, title="", subtitle=""):
    os.system("cls" if os.name == "nt" else "clear")
    content = Columns(
        [f"[#ffffff]{story}[/#ffffff]"], expand=True, equal=False
    )

    panel = Panel(
        content,
        title=title,
        subtitle=subtitle,
        border_style="#0317fc",
        padding=(1, 2),
        width=80,
        box=box.DOUBLE,
    )

    console.print(panel, justify="center")

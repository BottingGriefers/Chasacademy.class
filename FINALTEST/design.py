from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.columns import Columns
import time
import os
from rich.align import Align


console = Console()


def border(story, title="", subtitle="", stats=None):
    os.system("cls" if os.name == "nt" else "clear")
    stats_text = ""
    if stats:
        stats_text = "\n".join(
            [f"[#ff5555]{k}: {v}[/#ff5555]" for k, v in stats.as_dict().items()]
        )
    content = Columns(
        [stats_text, f"[#ffffff]{story}[/#ffffff]"], expand=True, equal=False
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

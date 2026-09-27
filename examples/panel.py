"""
Demonstrates the Panel feature for drawing bordered boxes around content.
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# Basic panel
console.print(Panel("Hello, World!", title="Welcome"))

# Panel with subtitle
console.print(Panel("This is a subtitle", title="Title", subtitle="Footer"))

# Panel with custom border style
console.print(Panel("Custom border", title="Styled", border_style="bright_blue"))

# Panel with padding
console.print(Panel("Padded content", title="Padding", padding=(1, 2)))

# Panel with Rich Text
rich_text = Text()
rich_text.append("Bold ", style="bold")
rich_text.append("italic ", style="italic")
rich_text.append("underline", style="underline")
console.print(Panel(rich_text, title="Rich Text"))

# Panel with expand=False (fit content)
console.print(Panel("Fits content", title="Compact", expand=False))

# Multiple panels side by side would need Columns, but here's a simple demo
console.print(Panel("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    title="Lorem Ipsum", width=60))
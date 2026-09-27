"""
Demonstrates the Rule feature for drawing horizontal rules.
"""

from rich.console import Console
from rich.rule import Rule

console = Console()

# Default rule
console.print("Default rule:")
console.print(Rule())

# Rule with title
console.print("\nRule with title:")
console.print(Rule("Section Header"))

# Rule with title and style
console.print("\nRule with custom style:")
console.print(Rule("Important", style="bold red"))

# Rule with alignment
console.print("\nLeft aligned:")
console.print(Rule("Left", align="left"))

console.print("\nRight aligned:")
console.print(Rule("Right", align="right"))

# Rule with different characters
console.print("\nDouble line:")
console.print(Rule("Double", characters="="))

console.print("\nCustom character:")
console.print(Rule("Custom", characters="~"))

# Thick rule
console.print("\nThick rule:")
console.print(Rule("Thick", style="blue", characters="█"))
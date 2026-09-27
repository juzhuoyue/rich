"""
Demonstrates the Markdown feature for rendering markdown text.
"""

from rich.console import Console
from rich.markdown import Markdown

console = Console()

markdown_text = """
# Heading 1
## Heading 2
### Heading 3

This is **bold** text and this is *italic* text.

> This is a blockquote.
> It can span multiple lines.

**Unordered list:**
- First item
- Second item
  - Nested item
- Third item

**Ordered list:**
1. First item
2. Second item
3. Third item

**Code block:**
```python
def hello():
    print("Hello, World!")
```

**Inline code:** `print("hello")`

**Table:**
| Name | Age | City |
|------|-----|------|
| Alice | 30 | New York |
| Bob | 25 | London |
| Charlie | 35 | Tokyo |

**Links:** [Rich Documentation](https://rich.readthedocs.io/)

---

**Horizontal rule above**
"""

md = Markdown(markdown_text)
console.print(md)
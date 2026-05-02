import unittest

from blocktohtml import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        node = markdown_to_html_node("This is a paragraph.")
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph.</p></div>")

    def test_heading(self):
        node = markdown_to_html_node("# Heading")
        self.assertEqual(node.to_html(), "<div><h1>Heading</h1></div>")

    def test_code_block(self):
        md = "```\nprint('hello')\n```"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><pre><code>print('hello')\n</code></pre></div>",
        )

    def test_quote(self):
        md = "> This is a quote\n> still a quote"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>This is a quote still a quote</blockquote></div>",
        )

    def test_unordered_list(self):
        md = "- item one\n- item two"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>item one</li><li>item two</li></ul></div>",
        )

    def test_ordered_list(self):
        md = "1. first\n2. second"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>first</li><li>second</li></ol></div>",
        )

    def test_inline_markdown(self):
        md = "This is **bold** and _italic_ and `code`"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is <b>bold</b> and <i>italic</i> and <code>code</code></p></div>",
        )


if __name__ == "__main__":
    unittest.main()
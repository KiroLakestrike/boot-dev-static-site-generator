import unittest

from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_spli_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node],"`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.PLAIN),
            ]
        )

    def test_split_bold(self):
        node = TextNode("This is **bold** text", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.PLAIN),
            ],
        )

    def test_split_italic(self):
        node = TextNode("This is _italic_ text", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.PLAIN),
            ],
        )

    def test_split_multiple_formatted_sections(self):
        node = TextNode("A `code` and `more code` here", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("A ", TextType.PLAIN),
                TextNode("code", TextType.CODE),
                TextNode(" and ", TextType.PLAIN),
                TextNode("more code", TextType.CODE),
                TextNode(" here", TextType.PLAIN),
            ],
        )

    def test_non_text_nodes_unchanged(self):
        node = TextNode("bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("bold", TextType.BOLD)])

    def test_raises_invalid_markdown(self):
        node = TextNode("This is `broken markdown", TextType.PLAIN)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()
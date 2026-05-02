import unittest

from markdowntoblocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        self.assertEqual(
            markdown_to_blocks(md),
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_strips_whitespace(self):
        md = """
        
First block

Second block
        
"""
        self.assertEqual(
            markdown_to_blocks(md),
            ["First block", "Second block"],
        )

    def test_markdown_to_blocks_multiple_blank_lines(self):
        md = "Block one\n\n\nBlock two"
        self.assertEqual(
            markdown_to_blocks(md),
            ["Block one", "Block two"],
        )

    def test_markdown_to_blocks_single_block(self):
        md = "Just one block"
        self.assertEqual(
            markdown_to_blocks(md),
            ["Just one block"],
        )


if __name__ == "__main__":
    unittest.main()
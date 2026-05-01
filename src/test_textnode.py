import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a different text node", TextType.BOLD)
    
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is a italic text node", TextType.ITALIC)
        node5 = TextNode("This is a italic text node", TextType.ITALIC)
        node6 = TextNode("This is a different italic text node", TextType.ITALIC)

        self.assertEqual(node4, node5)
        self.assertNotEqual(node4, node6)

        node7 = TextNode("This is a link text node", TextType.LINK)
        node7.url = "https://www.example.com"
        node8 = TextNode("This is a link text node", TextType.LINK)
        node8.url = "https://www.example.com"
        node9 = TextNode("This is a link text node", TextType.LINK)
        node9.url = "https://www.different.com"

        self.assertEqual(node7, node8)
        self.assertNotEqual(node7, node9)

if __name__ == "__main__":
    unittest.main()

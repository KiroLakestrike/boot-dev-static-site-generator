import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_image, split_nodes_link
from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodesImagesAndLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://www.example.com/zjjcJKZ.png) and another ![second image](https://www.example.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://www.example.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://www.example.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_single_image(self):
        node = TextNode(
            "Before ![alt](https://example.com/img.png) after",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Before ", TextType.PLAIN),
                TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
                TextNode(" after", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_image_no_images(self):
        node = TextNode("Just plain text", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("Just plain text", TextType.PLAIN)], new_nodes)

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.PLAIN),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.PLAIN),
                TextNode(
                    "to youtube",
                    TextType.LINK,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
            new_nodes,
        )

    def test_split_single_link(self):
        node = TextNode(
            "Go to [Boot.dev](https://www.boot.dev) now",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Go to ", TextType.PLAIN),
                TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" now", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_link_no_links(self):
        node = TextNode("Just plain text", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("Just plain text", TextType.PLAIN)], new_nodes)

    def test_split_images_preserves_non_text(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("already bold", TextType.BOLD)], new_nodes)

    def test_split_links_preserves_non_text(self):
        node = TextNode("already code", TextType.CODE)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("already code", TextType.CODE)], new_nodes)

    def test_split_image_at_start(self):
        node = TextNode(
            "![alt](https://example.com/img.png) after",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
                TextNode(" after", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_link_at_end(self):
        node = TextNode(
            "before [site](https://example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("before ", TextType.PLAIN),
                TextNode("site", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
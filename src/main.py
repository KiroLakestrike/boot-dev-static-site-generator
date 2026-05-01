from textnode import TextNode, TextType

def main():
    node1 = TextNode("Hello, World!", TextType.PLAIN)
    node2 = TextNode("This is a bold text.", TextType.BOLD)
    node3 = TextNode("This is an italic text.", TextType.ITALIC)
    node4 = TextNode("This is a code text.", TextType.CODE)
    node5 = TextNode("This is a link.", TextType.LINK)
    node5.url = "https://www.example.com"
    node6 = TextNode("This is an image.", TextType.IMAGE)
    node6.url = "https://www.example.com/image.png"

    print(node1)
    print(node2)
    print(node3)
    print(node4)
    print(node5)
    print(node6)

main()
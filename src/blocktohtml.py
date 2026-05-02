from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from blocktype import BlockType
from markdowntoblocks import markdown_to_blocks 
from blocktoblocktype import block_to_block_type
from texttotextnodes import text_to_textnodes
from textnodetohtmlnode import text_node_to_html_node


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        paragraph = " ".join(block.split("\n"))
        return ParentNode("p", text_to_children(paragraph))

    if block_type == BlockType.HEADING:
        level = 0
        for char in block:
            if char == "#":
                level += 1
            else:
                break
        text = block[level + 1:]
        return ParentNode(f"h{level}", text_to_children(text))

    if block_type == BlockType.CODE:
        text = block[3:-3]
        if text.startswith("\n"):
            text = text[1:]
        return ParentNode("pre", [LeafNode("code", text)])

    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        stripped_lines = [line.lstrip(">").strip() for line in lines]
        text = " ".join(stripped_lines)
        return ParentNode("blockquote", text_to_children(text))

    if block_type == BlockType.UNORDERED_LIST:
        items = []
        for line in block.split("\n"):
            text = line[2:]
            items.append(ParentNode("li", text_to_children(text)))
        return ParentNode("ul", items)

    if block_type == BlockType.ORDERED_LIST:
        items = []
        for line in block.split("\n"):
            text = line[3:]
            items.append(ParentNode("li", text_to_children(text)))
        return ParentNode("ol", items)

    raise ValueError("invalid block type")
from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        images = extract_markdown_images(original_text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image_alt, image_link in images:
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown image syntax")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link_text, link_url in links:
            sections = original_text.split(f"[{link_text}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown link syntax")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN))

    return new_nodes
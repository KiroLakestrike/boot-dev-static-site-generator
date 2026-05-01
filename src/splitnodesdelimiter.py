from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        split_text = old_node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise Exception(f"Invalid markdown syntax, missing closing delimiter: {delimiter}")

        for i, part in enumerate(split_text):
            if part == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.PLAIN))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

    
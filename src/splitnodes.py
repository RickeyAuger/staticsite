from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        while delimiter in remaining_text:

            start_pos = remaining_text.find(delimiter)
            end_pos = remaining_text.find(delimiter, start_pos +len(delimiter))

            if end_pos == -1:
                raise ValueError(f"No closing delimiter found for {delimiter}")
        
            before_text = remaining_text[:start_pos]
            special_text = remaining_text[start_pos + len(delimiter):end_pos]
            after_text = remaining_text[end_pos + len(delimiter):]

            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))

            if special_text:
                new_nodes.append(TextNode(special_text, text_type))

            remaining_text = after_text
        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))


        
    return new_nodes
        
    
    
        

from textnode import TextType, TextNode
from extractmarkdown import extract_markdown_images, extract_markdown_links



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

            
            new_nodes.append(TextNode(special_text, text_type))

            remaining_text = after_text
        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))


        
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT or not extract_markdown_images(old_node.text):
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        while extract_markdown_images(remaining_text):

            md_image = extract_markdown_images(remaining_text)[0]
            image_alt = md_image[0]
            image_url = md_image[1]

            
            full_image = f"![{image_alt}]({image_url})"

            
            parts = remaining_text.split(full_image, 1)

            
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes





def split_nodes_link(old_nodes):
    new_nodes = []
    
    for old_node in old_nodes:
        
        if old_node.text_type != TextType.TEXT or not extract_markdown_links(old_node.text):
            new_nodes.append(old_node)
            continue
        
        
        remaining_text = old_node.text
        
        while extract_markdown_links(remaining_text):
            
            link = extract_markdown_links(remaining_text)[0]
            link_text = link[0]
            url = link[1]
            
            
            full_link = f"[{link_text}]({url})"
            
            
            parts = remaining_text.split(full_link, 1)
            
            
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            
            if len(parts) > 1:
                remaining_text = parts[1]  
            else:
                remaining_text = ""
        
      
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
    return new_nodes

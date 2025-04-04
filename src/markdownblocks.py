from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from splitnodes import text_to_textnodes
import re


def markdown_to_blocks(markdown):
    
    blocks = markdown.split("\n\n")
    
    cleaned_blocks = []
    
    for block in blocks:
        
        block = block.strip()
       
        if block:
            
            lines = block.split("\n")
            
            cleaned_block = "\n".join(map(str.strip,lines))
            
            cleaned_blocks.append(cleaned_block)

    return cleaned_blocks



def markdown_to_html_node(markdown):
    cleaned_blocks = markdown_to_blocks(markdown)

    if not cleaned_blocks:
        return None

    children = []
    is_code_block = False
    code_block_lines = []

    for block in cleaned_blocks:
        block_type = block_to_block_type(block)

        
        if block_type == BlockType.PARAGRAPH:
            paragraph = paragraph_to_html_node(block)
            children.append(paragraph)

        elif block_type == BlockType.HEADING:
            heading = heading_to_html_node(block)
            children.append(heading)

        elif block_type == BlockType.CODE:
            code = code_to_html_node(block)
            children.append(code)

        elif block_type == BlockType.QUOTE:
            quotes = quote_to_html_node(block)
            children.append(quotes)

        elif block_type == BlockType.UNORDERED_LIST:
            unordered_list = unordered_list_to_html_node(block)
            children.append(unordered_list)

        elif block_type == BlockType.ORDERED_LIST:
            ordered_list = ordered_list_to_html_node(block)
            children.append(ordered_list)

    parent_node = ParentNode(tag="div", children=children)
    return parent_node
        
        




def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes



def paragraph_to_html_node(block):
    paragraph_text = " ".join(line.strip() for line in block.split("\n"))
    html_nodes = text_to_children(paragraph_text)
    return ParentNode(tag= "p", children=html_nodes)
   


def quote_to_html_node(block):
    lines = block.split("\n")
    
    cleaned_lines = []
    
    for line in lines:
        
        if line.startswith(">"):
            cleaned_line = line[1:].strip()
            cleaned_lines.append(cleaned_line)

        else:
            cleaned_lines.append(line)

    cleaned_block = " ".join(cleaned_lines)
    
    html_nodes = text_to_children(cleaned_block)
    
    return ParentNode(tag="blockquote", children=html_nodes)


def heading_to_html_node(block):
    match = re.match(r"^(#+)\s+(.*)", block)
    
    if not match or not match.group(2).strip():
        raise ValueError("Invalid heading format")
    
    count = len(match.group(1))  
    cleaned_text = match.group(2).strip() 
    
    html_nodes = text_to_children(cleaned_text)
    
    return ParentNode(tag=f"h{count}", children=html_nodes)



def code_to_html_node(block):
    if "```" in block:
        code_text = "\n".join(block.split("\n")[1:-1]).strip()
        
        text_node = TextNode(code_text, TextType.TEXT)
    
        html_text_node = text_node_to_html_node(text_node)

        code_node = ParentNode(tag="code", children=[html_text_node])
        
        return ParentNode("pre", children = [code_node])
    
    else:
        raise ValueError("invalid code block!")
   


def unordered_list_to_html_node(block):
    lines = block.split("\n")
    line_html_nodes = []

    for line in lines:
        if not line.strip():
            continue
        
        if line.startswith("* ") or line.startswith("- "):
            cleaned_line = line[2:].strip()
            li_children = text_to_children(cleaned_line)
            line_html_nodes.append(ParentNode(tag="li", children=li_children))
        
    return ParentNode(tag="ul", children=line_html_nodes)



def ordered_list_to_html_node(block):
    lines = block.split("\n")
    line_html_nodes = []

    for line in lines:
        match = re.search(r"^\d+\.\s*", line)
        
        if match:
            cleaned_line =line[match.end():].strip()
            li_children = text_to_children(cleaned_line)
            line_html_nodes.append(ParentNode(tag="li", children=li_children))
        
    return ParentNode(tag="ol", children=line_html_nodes)

        



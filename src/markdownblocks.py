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
    parent_node = HTMLNode("div", None, [], None)
    
    for block in cleaned_blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            paragraph = paragraph_to_html_node(block)
            parent_node.children.append(paragraph)
        
        elif block_type == BlockType.HEADING:
            heading = heading_to_html_node(block)
            parent_node.children.append(heading)
        
        elif block_type == BlockType.CODE:
            code = code_to_html_node(block)
            parent_node.children.append(code)
        
        elif block_type == BlockType.QUOTE:
            quotes = quote_to_html_node(block)
            parent_node.children.append(quotes)
        
        elif block_type == BlockType.UNORDERED_LIST:
            unordered_list = unordered_list_to_html_node(block)
            parent_node.children.append(unordered_list)
        
        elif block_type == BlockType.ORDERED_LIST:
            ordered_list = ordered_list_to_html_node(block)
            parent_node.children.append(ordered_list)
    
    return parent_node




def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes



def paragraph_to_html_node(block):
    html_nodes = text_to_children(block)
    return HTMLNode(tag= "p", children=html_nodes)
   


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
    
    return HTMLNode(tag="blockquote", children=html_nodes)


def heading_to_html_node(block):
    count = 0
    
    for char in block:
        if char == "#":
            count += 1
    
    cleaned_text = block[count:].strip()
    
    html_nodes = text_to_children(cleaned_text)
    
    return HTMLNode(tag=f"h{count}",children=html_nodes)


def code_to_html_node(block):
    code_text = block.split("```")[1]
    
    text_node = TextNode(code_text, TextType.TEXT)
    
    html_text_node = text_node_to_html_node(text_node)

    code_node = HTMLNode(tag="code", children=[html_text_node])
    
    return HTMLNode("pre", children = [code_node])


    



def unordered_list_to_html_node(block):
    lines = block.split("\n")
    line_html_nodes = []

    for line in lines:
        if not line.strip():
            continue
        
        if line.startswith("* "):
            cleaned_line = line[2:].strip()
            li_children = text_to_children(cleaned_line)
            line_html_nodes.append(HTMLNode(tag="li", children=li_children))
        
    return HTMLNode(tag="ul", children=line_html_nodes)



def ordered_list_to_html_node(block):
    lines = block.split("\n")
    line_html_nodes = []

    for line in lines:
        match = re.search(r"^\d+\.\s*", line)
        
        if match:
            cleaned_line =line[match.end():].strip()
            li_children = text_to_children(cleaned_line)
            line_html_nodes.append(HTMLNode(tag="li", children=li_children))
        
    return HTMLNode(tag="ol", children=line_html_nodes)

        



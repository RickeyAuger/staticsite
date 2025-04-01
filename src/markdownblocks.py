from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


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
            html_nodes = text_to_children(block)
            paragraph = HTMLNode(tag= "p", children=html_nodes)
            parent_node.children.append(paragraph)
        
        if block_type == BlockType.HEADING:
            HTMLNode("h1",)
        
        if block_type == BlockType.CODE:
            HTMLNode("code",)
        
        if block_type == BlockType.QUOTE:
            HTMLNode("blockquote",)
        
        if block_type == BlockType.UNORDERED_LIST:
            HTMLNode("ul",)
        
        if block_type == BlockType.ORDERED_LIST:
            HTMLNode("ol",)
    
    return parent_node




def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes
    




        



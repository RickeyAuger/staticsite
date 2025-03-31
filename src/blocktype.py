from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown):
    lines = markdown.split("\n")
    
    if markdown.startswith(("# ","## ","### ", "#### ", "##### ","###### ")):
        return BlockType.HEADING
    
    
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    
   
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    
    if all(re.search(r"^\d+\. ", line) for line in lines):
        numbers = []
        
        for line in lines:
            match = re.search(r"^(\d+)\. ", line)
            if match:
                numbers.append(int(match.group(1)))
        
        expected_sequence = list(range(1, len(numbers) + 1))
        
        if numbers == expected_sequence:
            return BlockType.ORDERED_LIST
            
          
    return BlockType.PARAGRAPH



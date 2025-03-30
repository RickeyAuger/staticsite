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




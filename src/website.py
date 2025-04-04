import os
import shutil
from markdownblocks import markdown_to_html_node


def copy_static(src, dst):
    
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    
    
    copy_recursive(src, dst)

def copy_recursive(src_path, dst_path):
    
    for item in os.listdir(src_path):
        src_item_path = os.path.join(src_path, item)
        dst_item_path = os.path.join(dst_path, item)
        
        
        if os.path.isfile(src_item_path):
            shutil.copy(src_item_path, dst_item_path)
            print(f"Copied file: {src_item_path} to {dst_item_path}")
            

        else:
            os.mkdir(dst_item_path)
            print(f"Created directory: {dst_item_path}")
            copy_recursive(src_item_path, dst_item_path)

def extract_title(markdown):
    for line in markdown.splitlines():
       stripped_line = line.strip()
       if stripped_line.startswith("#"):
            if (len(stripped_line) == 1 or stripped_line[1] == " "):
                return stripped_line[1:].strip() or ""
           
    raise Exception("markdown has no title")

def generate_page(from_path, template_path, dest_path):
   
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    with open(template_path, 'r') as f:
        template_content = f.read()

    title = extract_title(markdown_content)
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    dest_dir = os.path.dirname(dest_path)
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    with open (dest_path, 'w') as file:
        file.write(full_html)
import os
import shutil
from markdownblocks import markdown_to_html_node
from main import basepath


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

def generate_page(from_path, template_path, dest_path, basepath):
   
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
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')
    dest_dir = os.path.dirname(dest_path)
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    with open (dest_path, 'w') as file:
        file.write(full_html)

    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for file_name in os.listdir(dir_path_content):
            
        full_path = os.path.join(dir_path_content, file_name)
        relative_path = os.path.relpath(full_path, dir_path_content)
        dest_full_path = os.path.join(dest_dir_path, relative_path)
            
        if os.path.isfile(full_path):
                dest_file_path = dest_full_path.replace('.md', '.html') 
                generate_page(full_path, template_path, dest_file_path, basepath)
            
        elif os.path.isdir(full_path):
                os.makedirs(dest_full_path, exist_ok=True)
                generate_pages_recursive(full_path, template_path, dest_full_path, basepath)

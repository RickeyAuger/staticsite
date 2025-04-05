from website import *
import os






def main():
    copy_static("static", "public")
    
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/contact/index.md", "template.html", "public/contact/index.html")
    
    
    for file_name in os.listdir('content/blog'):
        full_content_path = f"content/blog/{file_name}/index.md"
        full_public_path = f"public/blog/{file_name}/index.html"
        
     
        generate_page(full_content_path, "template.html", full_public_path )

    
    
   
    

if __name__ == "__main__":
    main()


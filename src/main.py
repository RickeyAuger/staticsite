from website import *
import sys


if len(sys.argv) > 1 and sys.argv[1]:
    basepath = sys.argv[1]
else:
    basepath = "/"


def main():
    copy_static("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

    
    
   
    

if __name__ == "__main__":
    main()


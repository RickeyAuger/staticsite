import unittest
from markdownblocks import markdown_to_blocks
from main import extract_title

class Test_Markdown_To_Blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
                                [
                                    "This is **bolded** paragraph",
                                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                                    "- This is a list\n- with items",
                                ],
                        )
        
    def test_empty_string(self):
        md = ""
        self.assertEqual(markdown_to_blocks(md), [])

    
    def test_only_newlines(self):
        md = "\n\n\n"
        self.assertEqual(markdown_to_blocks(md), [])

    
    def test_single_line(self):
        md = "A single line of text"
        self.assertEqual(markdown_to_blocks(md), ["A single line of text"])


    def test_multiple_paragraphs(self):
        md = """Paragraph one.

        Paragraph two.

        Paragraph three."""
        self.assertEqual(markdown_to_blocks(md), ["Paragraph one.", "Paragraph two.", "Paragraph three."])

    def test_mixed_spacing(self):
        md = """  Extra spaces before this paragraph.  

        This paragraph has trailing spaces.  

        This one is fine.
        
        """
        self.assertEqual(markdown_to_blocks(md), [
            "Extra spaces before this paragraph.",
            "This paragraph has trailing spaces.",
            "This one is fine."
        ])
    
    def test_headers_and_paragraphs(self):
        md = """# Header 1

        Some paragraph text.

        ## Header 2

        More text under another header."""
        self.assertEqual(markdown_to_blocks(md), ["# Header 1", "Some paragraph text.", "## Header 2", "More text under another header."])

    def test_extract_title_markdown(self):
        md = """# Header 1

        Some paragraph text.

        ## Header 2

        More text under another header."""
        self.assertEqual(extract_title(md), "Header 1")

    def test_extract_title_extra_spaces(self):
        md = "#    Title with extra spaces"
        self.assertEqual(extract_title(md), "Title with extra spaces")


    def test_extract_title_no_h1(self):
        md = """## Header 2
        
        This markdown has no H1 header.
        
        ### Header 3
        """
        with self.assertRaises(Exception):
            extract_title(md)

    def test_extract_title_empty_header(self):
        md = """# 
        
        Just a hash with no title text.
        """
        self.assertEqual(extract_title(md), "")

    def test_extract_title_multiple_h1(self):
        md = """# First Title
        
        Some content.
        
        # Second Title
        """
        self.assertEqual(extract_title(md), "First Title")
    







if __name__ == "__main__":
    unittest.main()
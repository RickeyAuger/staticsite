import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class Test_Split_Nodes_Delimiter(unittest.TestCase):
    def test_bold_text(self):
        node = TextNode("This has a **bold** word", TextType.TEXT)
        
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(result,[
                                    TextNode("This has a ", TextType.TEXT),
                                    TextNode("bold", TextType.BOLD),
                                    TextNode(" word", TextType.TEXT)
                                ])
    def test_italic_text(self):
        node = TextNode("This has a _italic_ word", TextType.TEXT)
        
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        
        self.assertEqual(result,[
                                    TextNode("This has a ", TextType.TEXT),
                                    TextNode("italic", TextType.ITALIC),
                                    TextNode(" word", TextType.TEXT)
                                ])

    def test_code_text(self):
        node = TextNode("This has a `code` word", TextType.TEXT)
        
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(result,[
                                    TextNode("This has a ", TextType.TEXT),
                                    TextNode("code", TextType.CODE),
                                    TextNode(" word", TextType.TEXT)
                                ])


    def test_delim_at_end(self):
        node = TextNode("Bold is at the **end**", TextType.TEXT)
        
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(result,[
                                    TextNode("Bold is at the ", TextType.TEXT),
                                    TextNode("end", TextType.BOLD),
                                ])

    
    def test_delim_at_start(self):
        node = TextNode("**Bold** is at the start", TextType.TEXT)
        
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(result,[
                                    TextNode("Bold", TextType.BOLD),
                                    TextNode(" is at the start", TextType.TEXT),
                                ])


    def test_mult_delim(self):
        node = TextNode("**There** are two bold **words**", TextType.TEXT)
        
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(result,[
                                    TextNode("There", TextType.BOLD),
                                    TextNode(" are two bold ", TextType.TEXT),
                                    TextNode("words", TextType.BOLD)
                                ])
    
    def test_non_text_node(self):
        node = TextNode("**Hello**", TextType.BOLD)
        
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(result, [node])

    
    def test_no_closing_delim(self):
        node = TextNode("This has a **bold word", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_empty_delimited_text(self):
        node = TextNode("This has an **** empty bold", TextType.TEXT)
    
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
    
        self.assertEqual(result, [
                                TextNode("This has an ", TextType.TEXT),
                                TextNode("", TextType.BOLD), 
                                TextNode(" empty bold", TextType.TEXT)
                                ])

    




if __name__ == "__main__":
    unittest.main()


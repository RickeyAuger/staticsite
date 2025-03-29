import unittest

from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

    

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                        "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
               ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links__with_empty_list(self):
        self.assertListEqual(split_nodes_link([]), [])

    
    def test_split_images__with_empty_list(self):
        self.assertListEqual(split_nodes_image([]), [])

    
    def test_split_images_no_links_or_images(self):
        node = TextNode("This is a normal text string", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [node])

    
    def test_split_links_no_links_or_images(self):
        node = TextNode("This is a normal text string", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [node])

    
    def test_split_images_mult_dif_inputs(self):
        node = [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
                TextNode("This has no image in it", TextType.TEXT),
                TextNode("This has text with one final ![image](https://i.imgur.com/zjjcJhY.png)", TextType.TEXT)
                ]
        new_nodes = split_nodes_image(node)
        self.assertListEqual(new_nodes, [
                                        TextNode("This is text with an ", TextType.TEXT),
                                        TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                                        TextNode(" and another ", TextType.TEXT),
                                        TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                                        TextNode("This has no image in it", TextType.TEXT),
                                        TextNode("This has text with one final ", TextType.TEXT),
                                        TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJhY.png")
                                        ])
    
    def test_split_links_mult_dif_inputs(self):
        node = [
            TextNode("This is text with a [link](https://example.com) and another [second link](https://example2.com)", TextType.TEXT),
            TextNode("This has no link in it", TextType.TEXT),
            TextNode("This has text with one final [link](https://example3.com)", TextType.TEXT)
        ]
    
        new_nodes = split_nodes_link(node)
        
        self.assertListEqual(new_nodes, [
                                        TextNode("This is text with a ", TextType.TEXT),
                                        TextNode("link", TextType.LINK, "https://example.com"),
                                        TextNode(" and another ", TextType.TEXT),
                                        TextNode("second link", TextType.LINK, "https://example2.com"),
                                        TextNode("This has no link in it", TextType.TEXT),
                                        TextNode("This has text with one final ", TextType.TEXT),
                                        TextNode("link", TextType.LINK, "https://example3.com")
                                        ])
        
    
    def test_link_at_beginning(self):
        node = [TextNode("[Start](https://start.com) of text", TextType.TEXT)]
        new_nodes = split_nodes_link(node)
        
        self.assertListEqual(new_nodes, [
            TextNode("Start", TextType.LINK, "https://start.com"),
            TextNode(" of text", TextType.TEXT)
        ])

    def test_image_at_beginning(self):
        node = [TextNode("![Logo](https://logo.com) is here", TextType.TEXT)]
        new_nodes = split_nodes_image(node)
        
        self.assertListEqual(new_nodes, [
            TextNode("Logo", TextType.IMAGE, "https://logo.com"),
            TextNode(" is here", TextType.TEXT)
        ])

    def test_link_at_end(self):
        node = [TextNode("Click this [link](https://end.com)", TextType.TEXT)]
        new_nodes = split_nodes_link(node)

        self.assertListEqual(new_nodes, [
            TextNode("Click this ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://end.com")
        ])

    def test_image_at_end(self):
        node = [TextNode("Check this ![pic](https://pic.com)", TextType.TEXT)]
        new_nodes = split_nodes_image(node)

        self.assertListEqual(new_nodes, [
            TextNode("Check this ", TextType.TEXT),
            TextNode("pic", TextType.IMAGE, "https://pic.com")
        ])

    def test_adjacent_links(self):
        node = [TextNode("[First](https://1.com)[Second](https://2.com)", TextType.TEXT)]
        new_nodes = split_nodes_link(node)

        self.assertListEqual(new_nodes, [
            TextNode("First", TextType.LINK, "https://1.com"),
            TextNode("Second", TextType.LINK, "https://2.com")
        ])

    def test_adjacent_images(self):
        node = [TextNode("![One](https://one.com)![Two](https://two.com)", TextType.TEXT)]
        new_nodes = split_nodes_image(node)

        self.assertListEqual(new_nodes, [
            TextNode("One", TextType.IMAGE, "https://one.com"),
            TextNode("Two", TextType.IMAGE, "https://two.com")
        ])

    def test_non_text_link_node(self):
        node = [TextNode("Already a link", TextType.LINK, "https://link.com")]
        new_nodes = split_nodes_link(node)

        self.assertListEqual(new_nodes, node)  

    def test_non_text_image_node(self):
        node = [TextNode("Already an image", TextType.IMAGE, "https://image.com")]
        new_nodes = split_nodes_image(node)

        self.assertListEqual(new_nodes, node)  

    def test_malformed_link(self):
        node = [TextNode("This [is broken(https://broken.com)", TextType.TEXT)]
        new_nodes = split_nodes_link(node)

    
        self.assertListEqual(new_nodes, node)

    def test_malformed_image(self):
        node = [TextNode("This ![is broken](https://broken.com", TextType.TEXT)]
        new_nodes = split_nodes_image(node)

        
    def test_special_chars_in_link(self):
        node = [TextNode("Check this [weird](https://example.com/?a=1&b=2) link", TextType.TEXT)]
        new_nodes = split_nodes_link(node)

        self.assertListEqual(new_nodes, [
            TextNode("Check this ", TextType.TEXT),
            TextNode("weird", TextType.LINK, "https://example.com/?a=1&b=2"),
            TextNode(" link", TextType.TEXT)
        ])

    #def test_special_chars_in_image(self):
        #node = [TextNode("![Bracket Test](https://example.com/image_(1).png)", TextType.TEXT)]
        #new_nodes = split_nodes_image(node)

        #self.assertListEqual(new_nodes, [
            #TextNode("Bracket Test", TextType.IMAGE, "https://example.com/image_(1).png")
        #])


if __name__ == "__main__":
    unittest.main()


import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_eq_with_default_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_eq_with_diff_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boots.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_with_diff_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boots.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    
    
    
        


if __name__ == "__main__":
    unittest.main()
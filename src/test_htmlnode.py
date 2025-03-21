import unittest

from htmlnode import HTMLNode

#tag value children props
class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p","Hello, world!")
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode("a", "Click me!", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_multiple_props(self):
        node = HTMLNode("a", "Click me!", props={"href": "https://example.com", "target": "_blank"})
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    
    
    
        


if __name__ == "__main__":
    unittest.main()
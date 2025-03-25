import unittest

from htmlnode import LeafNode



class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, world!")
        self.assertEqual(node.to_html(), "<span>Hello, world!</span>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_with_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_node_requires_value(self):
        with self.assertRaises(ValueError):
            LeafNode("a", None)

    def test_leaf_to_html_with_no_value(self):
        node = LeafNode("a", "Some value")  
        node.value = None  
        with self.assertRaises(ValueError):
            node.to_html()


    

    


    



    
    
    
        


if __name__ == "__main__":
    unittest.main()
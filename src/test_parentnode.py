import unittest

from htmlnode import ParentNode, LeafNode



class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("span", [])

    def test_to_html_with_no_children2(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("span", [child_node])
        parent_node.children = None
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_no_tag(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("span", "child")
            ParentNode(None, [child_node])

    def test_to_html_with_no_tag2(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("span", [child_node])
        parent_node.tag = None
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "First paragraph")
        child2 = LeafNode("p", "Second paragraph")
        parent = ParentNode("div", [child1, child2])

        self.assertEqual(parent.to_html(), "<div><p>First paragraph</p><p>Second paragraph</p></div>")

    def test_to_html_with_mixed_children(self):
        child1 = LeafNode("p", "Paragraph")
        child2 = ParentNode("div", [LeafNode("span", "Nested span")])
        parent = ParentNode("section", [child1, child2])

        self.assertEqual(parent.to_html(), "<section><p>Paragraph</p><div><span>Nested span</span></div></section>")

    def test_to_html_with_attributes(self):
        child = LeafNode("p", "Text")
        parent = ParentNode("div", [child], props={"class": "container", "id": "main"})
    
        self.assertEqual(parent.to_html(), '<div class="container" id="main"><p>Text</p></div>')

    def test_to_html_with_empty_props(self):
        child = LeafNode("p", "Text")
        parent = ParentNode("div", [child], props={})
    
        self.assertEqual(parent.to_html(), "<div><p>Text</p></div>")

    def test_to_html_with_children_having_props(self):
        child1 = LeafNode("a", "Click me", props={"href": "https://example.com"})
        parent = ParentNode("nav", [child1])
        
        self.assertEqual(parent.to_html(), '<nav><a href="https://example.com">Click me</a></nav>')

    def test_to_html_with_deep_nesting(self):
        deep_node = ParentNode("div", [
            ParentNode("section", [
                ParentNode("article", [
                    LeafNode("p", "Deep content")
                ])
            ])
        ])
    
        self.assertEqual(deep_node.to_html(), "<div><section><article><p>Deep content</p></article></section></div>")

    def test_to_html_with_invalid_child(self):
        with self.assertRaises(TypeError): 
            ParentNode("div", [123])

        


    





if __name__ == "__main__":
    unittest.main()
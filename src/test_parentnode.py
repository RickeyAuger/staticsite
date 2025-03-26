import unittest

from htmlnode import ParentNode



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
            ParentNode("span")

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






if __name__ == "__main__":
    unittest.main()
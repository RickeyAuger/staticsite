import unittest
from blocktype import BlockType, block_to_block_type

class Test_Block_To_Blocktype(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Subheading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Smallest Heading"), BlockType.HEADING)
    
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```python\ndef hello():\n    return 'Hello'\n```"), BlockType.CODE)
    
    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), BlockType.QUOTE)
    
    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- First\n- Second\n- Third"), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. One\n2. Two"), BlockType.ORDERED_LIST)
    
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Just some text without any special formatting."), BlockType.PARAGRAPH)

    def test_empty_string(self):
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)

    def test_mixed_list_formatting(self):
        self.assertEqual(block_to_block_type("- Item 1\n1. Item 2"), BlockType.PARAGRAPH)

    def test_incorrectly_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First\n3. Third\n2. Second"), BlockType.PARAGRAPH)
    
    def test_unordered_list_extra_spaces(self):
        self.assertEqual(block_to_block_type("-  Item 1\n-  Item 2"), BlockType.UNORDERED_LIST)

    def test_quote_mixed_formatting(self):
        self.assertEqual(block_to_block_type("> This is a quote\nNot a quote"), BlockType.PARAGRAPH)

    def test_unfinished_code_block(self):
        self.assertEqual(block_to_block_type("```\ndef hello():\n    return 'Hello'"), BlockType.PARAGRAPH)
    
    def test_heading_with_extra_spaces(self):
        self.assertEqual(block_to_block_type("  # Not a heading"), BlockType.PARAGRAPH)
    

    

if __name__ == "__main__":
    unittest.main()
        
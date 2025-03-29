import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links

class Test_Extract_Markdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_md_links_with_images_and_links(self):
        matches = extract_markdown_links(
            "Here is an image ![my image](https://image-url.com) and a link [to BootDev](https://www.boot.dev)."
        )
        self.assertListEqual(matches, [("to BootDev", "https://www.boot.dev")])

    def test_extract_md_images_with_images_and_links(self):
        matches = extract_markdown_images(
            "Here is an image ![my image](https://image-url.com) and a link [to BootDev](https://www.boot.dev)."
        )
        self.assertListEqual(matches, [("my image", "https://image-url.com")])

    def test_extract_md_images_with_empty_text(self):
        matches = extract_markdown_images("")
        self.assertListEqual(matches, [])

    def test_extract_md_links_with_empty_text(self):
        matches = extract_markdown_links("")
        self.assertListEqual(matches, [])

    def test_extract_md_images_with_no_images(self):
        matches = extract_markdown_images("Here is just some plain text with no markdown.")
        self.assertListEqual(matches, [])

    def test_extract_md_links_with_no_links(self):
        matches = extract_markdown_links("Here is just some plain text with no markdown.")
        self.assertListEqual(matches, [])








if __name__ == "__main__":
    unittest.main()


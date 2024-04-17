import unittest
import os

from markdown_cleaner import format_markdown

class TestMarkdownCleaner(unittest.TestCase):
    def setUp(self):
        # Create a sample input markdown file
        self.input_file = 'test_input.md'
        with open(self.input_file, 'w', encoding='utf-8') as f:
            f.write("This is a test [link](https://example.com)\n")
            f.write("This is another [link](https://example.com/image.png) with an image\n")
            f.write("This is an ![image](image.png)\n")

    def test_format_markdown(self):
        format_markdown(self.input_file)
        # Check if the output file exists
        output_file = self.input_file.replace('.md', '.clean.md')
        self.assertTrue(os.path.exists(output_file))
        # Check the content of the output file
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn("This is a test [link]\n", content)
            self.assertIn("This is another [link] with an image\n", content)
            self.assertIn("This is an ![image](image.png)\n", content)

    def tearDown(self):
        # Remove the sample input and output files
        os.remove(self.input_file)
        output_file = self.input_file.replace('.md', '.clean.md')
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == '__main__':
    unittest.main()

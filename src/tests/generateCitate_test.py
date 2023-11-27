import unittest
from services.generateCitate import GenerateCitate  

class TestGenerateCitate(unittest.TestCase):

    def test_generate_bibtex_with_all_fields(self):
        entry_type = "article"
        cite_key = "CitekeyArticle"
        fields = {
            "author": "Author Name",
            "title": "Article Title",
            "journal": "Journal Name",
            "year": 2021,
            "volume": "10",
            "number": "1",
            "pages": "100-110"
        }

        expected_output = (
            "@article{CitekeyArticle,\n"
            "  author = \"Author Name\",\n"
            "  title = \"Article Title\",\n"
            "  journal = \"Journal Name\",\n"
            "  year = 2021,\n"
            "  volume = \"10\",\n"
            "  number = \"1\",\n"
            "  pages = \"100-110\"\n"
            "}"
        )

        self.assertEqual(GenerateCitate.generate_bibtex(entry_type, cite_key, fields), expected_output)

    def test_generate_bibtex_with_some_empty_fields(self):
        entry_type = "article"
        cite_key = "CitekeyArticle"
        fields = {
            "author": "Author Name",
            "title": None,  # None value
            "journal": "Journal Name",
            "year": None,   # None value
            "volume": "",
            "number": "1",
            "pages": "100-110"
        }

        expected_output = (
            "@article{CitekeyArticle,\n"
            "  author = \"Author Name\",\n"
            "  journal = \"Journal Name\",\n"
            "  number = \"1\",\n"
            "  pages = \"100-110\"\n"
            "}"
        )

        self.assertEqual(GenerateCitate.generate_bibtex(entry_type, cite_key, fields), expected_output)

if __name__ == '__main__':
    unittest.main()

import unittest
from citationArticle import CitationArticle

class TestCitationArticle(unittest.TestCase):
    def test_citation_to_bibtex_entry(self):
        # Create an instance of CitationArticle
        citation = CitationArticle(
            "article", "CitekeyArticle", "P. J. Cohen", 
            "The independence of the continuum hypothesis", 
            "Proceedings of the National Academy of Sciences", 
            1963, "50", "6", "1143--1148"
        )

        # Expected BibTeX entry
        expected_output = (
            "@article{CitekeyArticle,\n"
            "  author = \"P. J. Cohen\",\n"
            "  title = \"The independence of the continuum hypothesis\",\n"
            "  journal = \"Proceedings of the National Academy of Sciences\",\n"
            "  year = 1963,\n"
            "  volume = \"50\",\n"
            "  number = \"6\",\n"
            "  pages = \"1143--1148\"\n"
            "}"
        )

        # Test if the output matches the expected output
        self.assertEqual(citation.citation_to_bibtex_entry(), expected_output)

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
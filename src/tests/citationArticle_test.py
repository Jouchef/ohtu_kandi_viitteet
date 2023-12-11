import unittest #pylint: disable:invalid-name
from entities.citationArticle import CitationArticle

class TestCitationArticle(unittest.TestCase):
    """Tests for the CitationArticle class"""
    def test_citation_to_bibtex_entry(self):
        """Tests the citation_to_bibtex_entry method"""
        citation = CitationArticle(
            "article", "CitekeyArticle", "P. J. Cohen", 
            "The independence of the continuum hypothesis", 
            "Proceedings of the National Academy of Sciences", 
            1963, "50", "6", None,
            "July", "10.1073/pnas.50.6.1143", "Important note", "Key1" 
        )

        expected_output = (
            "@article{CitekeyArticle,\n"
            "  author = \"P. J. Cohen\",\n"
            "  title = \"The independence of the continuum hypothesis\",\n"
            "  journal = \"Proceedings of the National Academy of Sciences\",\n"
            "  year = 1963,\n"
            "  volume = \"50\",\n"
            "  number = \"6\",\n"
            "  month = \"July\",\n"
            "  doi = \"10.1073/pnas.50.6.1143\",\n"
            "  note = \"Important note\",\n"
            "  key = \"Key1\"\n"
            "}"
        )

        self.assertEqual(citation.citation_to_bibtex_entry(), expected_output)

if __name__ == '__main__':
    unittest.main()

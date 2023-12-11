import unittest #pylint: disable:invalid-name
from entities.citationBook import CitationBook

class TestCitationBook(unittest.TestCase):
    """Tests for the CitationBook class"""
    def test_citation_to_bibtex_entry(self):
        """Tests the citation_to_bibtex_entry method"""
        citation = CitationBook(
            "book", "CitekeyBook", "Author Name", "Book Title", 
            "Publisher Name", 2021, volume="5", edition="2nd", 
            address="Location", month="July", note="Additional note"
        )

        expected_output = (
            "@book{CitekeyBook,\n"
            "  author = \"Author Name\",\n"
            "  title = \"Book Title\",\n"
            "  publisher = \"Publisher Name\",\n"
            "  year = 2021,\n"
            "  volume = \"5\",\n"
            "  address = \"Location\",\n"
            "  edition = \"2nd\",\n"
            "  month = \"July\",\n"
            "  note = \"Additional note\"\n"
            "}"
        )
        self.assertAlmostEqual(citation.generate_bibtex(), expected_output)

if __name__ == '__main__':
    unittest.main()
    
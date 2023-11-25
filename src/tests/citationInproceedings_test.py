import unittest
from entities.citationInproceedings import CitationInProceedings  

class TestCitationInProceedings(unittest.TestCase):
    def test_citation_to_bibtex_entry(self):
        citation = CitationInProceedings(
            "inproceedings", "CitekeyInproc", "Author Name", "Paper Title", 
            "Conference Name", 2021, pages="123-130", address="Location", 
            month="September", organization="Org Name", publisher="Publisher Name", 
            note="Additional note"
        )

        expected_output = (
            "@inproceedings{CitekeyInproc,\n"
            "  author = \"Author Name\",\n"
            "  title = \"Paper Title\",\n"
            "  booktitle = \"Conference Name\",\n"
            "  year = 2021,\n"
            "  pages = \"123-130\",\n"
            "  address = \"Location\",\n"
            "  month = \"September\",\n"
            "  organization = \"Org Name\",\n"
            "  publisher = \"Publisher Name\",\n"
            "  note = \"Additional note\"\n"
            "}"
        )

        self.assertEqual(citation.citation_to_bibtex_entry(), expected_output)

if __name__ == '__main__':
    unittest.main()
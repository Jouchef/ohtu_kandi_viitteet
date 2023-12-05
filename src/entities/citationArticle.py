"""Class for article citation.""" # pylint: disable=invalid-name
from services.generatecitate import GenerateCitate # pylint: disable=import-error
class CitationArticle(): # pylint: disable=too-few-public-methods too-many-instance-attributes
    """Class for article citation."""
    def __init__(self, entry_type, cite_key, author, title, journal,
                 year, volume, number, pages, month=None, doi=None,
                 note=None, key=None): # pylint: disable=too-many-arguments
        self.entry_type = entry_type
        self.cite_key = cite_key
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
        self.number = number
        self.pages = pages
        self.month = month
        self.doi = doi
        self.note = note
        self.key = key

    def citation_to_bibtex_entry(self):
        """Return a string in BibTeX format."""
        fields = {
                "author": self.author,
                "title": self.title,
                "journal": self.journal,
                "year": self.year,
                "volume": self.volume,
                "number": self.number,
                "pages": self.pages,
                "month": self.month,
                "doi": self.doi,
                "note": self.note,
                "key": self.key
            }
        return GenerateCitate.generate_bibtex(self.entry_type, self.cite_key, fields)

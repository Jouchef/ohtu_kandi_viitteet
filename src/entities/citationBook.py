"""Class for book citation.""" # pylint: disable=invalid-name
from services.generateCitate import GenerateCitate # pylint: disable=import-error
class CitationBook():
    """Class for book citation."""
    def __init__(self, entry_type, cite_key, author,
                 title, publisher, year, volume=None,
                 number=None, series=None, address=None,
                 edition=None, month=None, note=None, key=None, url=None): # pylint: disable=too-many-arguments
        self.entry_type = entry_type
        self.cite_key = cite_key
        self.author = author  # Can also be 'editor'
        self.title = title
        self.publisher = publisher
        self.year = year
        self.volume = volume
        self.number = number
        self.series = series
        self.address = address
        self.edition = edition
        self.month = month
        self.note = note
        self.key = key
        self.url = url

    def generate_bibtex(self):
        """Return a string in BibTeX format."""
        fields = {
                "author": self.author,
                "title": self.title,
                "publisher": self.publisher,
                "year": self.year,
                "volume": self.volume,
                "number": self.number,
                "series": self.series,
                "address": self.address,
                "edition": self.edition,
                "month": self.month,
                "note": self.note,
                "key": self.key,
                "url": self.url
            }
        return GenerateCitate.generate_bibtex(self.entry_type, self.cite_key, fields)

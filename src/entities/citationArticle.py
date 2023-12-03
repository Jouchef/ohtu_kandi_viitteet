"""Class for article citation.""" # pylint: disable=invalid-name

class CitationArticle(): # pylint: disable=too-many-public-methods
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

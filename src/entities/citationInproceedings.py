"""Proceedings, of a conference."""
class CitationInProceedings():
    """Proceedings, of a conference."""
    def __init__(self, entry_type, cite_key, author, title, booktitle, year, editor=None, volume=None, number=None, series=None, pages=None, address=None, month=None, organization=None, publisher=None, note=None, key=None):
        self.entry_type = entry_type
        self.cite_key = cite_key
        self.author = author
        self.title = title
        self.booktitle = booktitle
        self.year = year
        self.editor = editor
        self.volume = volume
        self.number = number
        self.series = series
        self.pages = pages
        self.address = address
        self.month = month
        self.organization = organization
        self.publisher = publisher
        self.note = note
        self.key = key

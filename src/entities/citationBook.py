"""Class for book citation.""" # pylint: disable=invalid-name
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

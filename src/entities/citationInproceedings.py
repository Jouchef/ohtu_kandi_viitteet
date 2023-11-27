from services.generateCitate import GenerateCitate

class CitationInProceedings():
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

    def citation_to_bibtex_entry(self):
        fields = {
            "author": self.author,
            "title": self.title,
            "booktitle": self.booktitle,
            "year": self.year,
            "editor": self.editor,
            "volume": self.volume,
            "number": self.number,
            "series": self.series,
            "pages": self.pages,
            "address": self.address,
            "month": self.month,
            "organization": self.organization,
            "publisher": self.publisher,
            "note": self.note,
            "key": self.key
        }

        return GenerateCitate.generate_bibtex(self.entry_type, self.cite_key, fields)

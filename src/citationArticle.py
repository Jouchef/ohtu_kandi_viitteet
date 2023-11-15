class CitationArticle():
    def __init__(self, entry_type, cite_key, author, title, journal, year, volume, number, pages):
        self.entry_type = entry_type
        self.cite_key = cite_key
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
        self.number = number
        self.pages = pages

    def citation_to_bibtex_entry(self):
        fields = {
            "author": self.author,
            "title": self.title,
            "journal": self.journal,
            "year": self.year,
            "volume": self.volume,
            "number": self.number,
            "pages": self.pages
        }

        bibtex_entry = f"@{self.entry_type}{{{self.cite_key},\n"
        for key, value in fields.items():
            if value:
                bibtex_entry += f"  {key} = \"{value}\",\n"
        bibtex_entry = bibtex_entry.rstrip(',\n') + "\n}"  # Remove last comma and newline, then close the brace

        return bibtex_entry



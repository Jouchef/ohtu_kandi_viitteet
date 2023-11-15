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
        return (
            f"@{self.entry_type}{{{self.cite_key},\n"
            f"  author = \"{self.author}\",\n"
            f"  title = \"{self.title}\",\n"
            f"  journal = \"{self.journal}\",\n"
            f"  year = {self.year},\n"
            f"  volume = \"{self.volume}\",\n"
            f"  number = \"{self.number}\",\n"
            f"  pages = \"{self.pages}\"\n"
            f"}}"
        )



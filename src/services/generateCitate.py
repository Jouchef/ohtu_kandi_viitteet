class GenerateCitate:
    """Class for generating citate to Bibtex from a given entry type, cite key and fields"""
    @staticmethod
    def generate_bibtex(entry_type, cite_key, fields):
        bibtex_entry = f"@{entry_type}{{{cite_key},\n"
        for key, value in fields.items():
            if value:
                if key == "year":
                    bibtex_entry += f"  {key} = {value},\n"  # No quotes for year
                else:
                    bibtex_entry += f"  {key} = \"{value}\",\n"
        bibtex_entry = bibtex_entry.rstrip(',\n') + "\n}"  # Remove last comma and newline, then close the brace
        return bibtex_entry
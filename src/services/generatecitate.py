"""Module to handle generating citate to Bibtex from a given entry type, cite key and fields"""
class GenerateCitate: 
    """Class for generating citate to Bibtex from a given entry type, cite key and fields"""
    @staticmethod
    def generate_bibtex(entry_type, cite_key, fields):
        """Generates a bibtex entry from a given entry type, cite key and fields"""
        bibtex_entry = f"@{entry_type}{{{cite_key},\n"
        for key, value in fields.items():
            if value:
                if key == "year":
                    bibtex_entry += f"  {key} = {value},\n"
                else:
                    bibtex_entry += f"  {key} = \"{value}\",\n"
        bibtex_entry = bibtex_entry.rstrip(',\n') + "\n}"
        return bibtex_entry

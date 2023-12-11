"""Reference services   """
import urllib.request
from repositories.reference_repository import reference_repository as default_reference_repository # pylint: disable=no-name-in-module, import-error line-too-long
from models.reference import Reference_model as Reference # pylint: disable=no-name-in-module, import-error line-too-long
from models.user_references import UserReferences_model # pylint: disable=no-name-in-module, import-error line-too-long
from entities.citationArticle import CitationArticle # pylint: disable=import-error no-name-in-module

class ReferenceService:
    """Reference services.
    Handles reference logic."""
    def __init__(self, reference_repository=default_reference_repository):
        """Constructor for ReferenceService."""
        self._reference_repository = reference_repository

    def create_reference(self, reference_type,
                         author=None, title=None, journal=None,
                         year=None, volume=None,
                         publisher = None, booktitle=None,
                         number=None,
                         pages=None, month=None, doi=None,
                         note=None, key=None, series=None,
                         address=None, edition=None, url=None,
                         editor=None, organization=None,
                         visible=True,
                         user_id = None): # pylint: disable=line-too-long
        """Create a new reference."""
        try :
            reference_new = Reference(reference_type = reference_type,
                                                           visible=visible,
                                                           author = author,
                                                           title = title,
                                                           journal = journal,
                                                           year = year,
                                                           volume = volume,
                                                           publisher = publisher,
                                                           booktitle = booktitle,
                                                           number = number,
                                                           pages = pages,
                                                           month = month,
                                                           doi = doi,
                                                           note = note,
                                                           key = key,
                                                           series = series,
                                                           address = address,
                                                           edition = edition,
                                                           url = url,
                                                           editor = editor,
                                                           organization = organization)

        except Exception as error:
            print(f"Error occurred: {error}")
            raise Exception("Error occurred: {error}") from error # pylint: disable=broad-exception-raised
        created_reference = self._reference_repository.create(reference=reference_new)
        self.add_reference_to_user(user_id, created_reference.id)
        return created_reference


    def add_reference_to_user(self, user_id, reference_id):
        """Adds a reference to a user
        by creating a new UserReferences_model object."""
        reference_user_new = UserReferences_model(user_id = user_id,
                                                  reference_id = reference_id)
        return self._reference_repository.add_reference_to_user(reference_user_new)

    def get_reference(self, reference_id):
        """Returns a citation with the reference given id."""
        return self._reference_repository.get_reference(reference_id)

    def get_all_references_by_user_id(self, user_id):
        """Returns all citations by the given user id.
        Returns only visible references."""
        references = self._reference_repository.get_all_references_by_user_id(user_id)
        return references

    def references_to_bibtex(self, user_id):
        """Converts references to bibtex format."""
        references = self._reference_repository.get_all_references_by_user_id(user_id)
        bibtex = "References\n\n"
        for reference in references:
            if reference.reference_type == "Article":
                citation = CitationArticle(reference.reference_type, reference.key,
                                           reference.author,
                                           reference.title,
                                           reference.journal,
                                           reference.year,
                                           reference.volume,
                                           reference.number,
                                           reference.pages,
                                           reference.month,
                                           reference.doi, reference.note, reference.key)
                bibtex += citation.citation_to_bibtex_entry()
                bibtex += "\n\n"
        return bibtex


    def edit_reference(self, reference_id, **kwargs):
        """INPUT:
        reference_id = the id of the reference to be edited
        kwargs = the new values for the reference
        DO: queries the reference with the given id and updates the values"""
        reference = self._reference_repository.get_reference(reference_id)
        if reference:
            for key, value in kwargs.items():
                setattr(reference, key, value)
            return self._reference_repository.edit_reference(reference)
        print("Error in editing reference")


    def delete_reference(self, reference_id):
        """Deletes a reference with the given id.
        changes the reference's visible attribute to False."""
        return self._reference_repository.delete_reference(reference_id)

    def get_from_doi(self, doi):
        """Returns a BibTeX entry from a given doi."""
        base_url = 'http://dx.doi.org/'
        url = base_url + doi
        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/x-bibtex')

        with urllib.request.urlopen(req) as f:
            bibtex = f.read().decode()
        return bibtex

    def parse_bibtex(self,bibtex):
        """Parses a BibTeX entry and returns a dictionary of its fields."""
        reference_type = bibtex.split('{', 1)[0].split('@', 1)[1]
        reference_type = reference_type[0].upper() + reference_type[1:]

        parts = bibtex.replace('@article{', '').rstrip(' }').split(', ')
        bibtex_dict = {}
        bibtex_dict = {'citation_key': parts[0],
                       'reference_type': reference_type}

        for part in parts[1:]:
            key_value = part.split('=', 1)
            if len(key_value) ==2:
                key, value = key_value
                bibtex_dict[key.strip()] = value.strip('{} ').replace('\n', ' ')
            else:
                last_key = list(bibtex_dict.keys())[-1]
                bibtex_dict[last_key] += ', ' + part.strip('{} ')
        return bibtex_dict

    def create_reference_from_doi(self, doi, user_id):
        """Creates a reference from a doi.
        Returns the reference."""
        bibtext = self.get_from_doi(doi)
        parced_dict = self.parse_bibtex(bibtext)
        if parced_dict['reference_type'] == "Article":
            return self.create_reference(reference_type = parced_dict['reference_type'],
                                     author = parced_dict['author'],
                                     title = parced_dict['title'],
                                     journal = parced_dict['journal'],
                                     year = parced_dict['year'],
                                     volume = parced_dict['volume'],
                                     number = parced_dict['number'],
                                     month = parced_dict['month'],
                                     key = parced_dict['citation_key'],
                                     visible = True,
                                     user_id = user_id)
        elif parced_dict['reference_type'] == "Book":
            return self.create_reference(reference_type = parced_dict['reference_type'],
                                     author = parced_dict['author'],
                                     title = parced_dict['title'],
                                     publisher = parced_dict['publisher'],
                                     year = parced_dict['year'],
                                     volume = parced_dict['volume'],
                                     series = parced_dict['series'],
                                     address = parced_dict['address'],
                                     edition = parced_dict['edition'],
                                     month = parced_dict['month'],
                                     key = parced_dict['citation_key'],
                                     url = parced_dict['url'],
                                     visible = True,
                                     user_id = user_id)
        else:
            return print("Error in creating reference from doi")





reference_service = ReferenceService() # pylint: disable=invalid-name

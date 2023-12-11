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

    def create_reference(self, reference_type, user_id, **kwargs):
        """Creates a new reference."""
        valid_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        try:
            reference_new = Reference(reference_type=reference_type, **valid_kwargs)
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
        """Gets a BibTeX entry from a doi."""
        print ("in get_from_doi")
        base_url = 'http://dx.doi.org/'
        url = base_url + doi
        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/x-bibtex')

        with urllib.request.urlopen(req) as f:
            bibtex = f.read().decode()
        return bibtex

    def parse_bibtex(self,bibtex):
        """Parses a BibTeX entry and returns a dictionary of its fields."""
        # add the article as the type  @article{ and }
        print ("in parse_bibtex")
        reference_type = bibtex.split('{', 1)[0].split('@', 1)[1]
        print(reference_type)
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
        print ("in create_reference_from_doi")
        bibtext = self.get_from_doi(doi)
        parsed_dict = self.parse_bibtex(bibtext)

        reference_type = parsed_dict.get('reference_type')
        print(reference_type)
        if reference_type == 'Book':
            return self.create_reference(reference_type=reference_type,
                                        author=parsed_dict.get('author'),
                                        title=parsed_dict.get('title'),
                                        publisher=parsed_dict.get('publisher'),
                                        year=parsed_dict.get('year'),
                                        volume=parsed_dict.get('volume'),
                                        series=parsed_dict.get('series'),
                                        address=parsed_dict.get('address'),
                                        edition=parsed_dict.get('edition'),
                                        month=parsed_dict.get('month'),
                                        note=parsed_dict.get('note'),
                                        key=parsed_dict.get('citation_key'),
                                        url=parsed_dict.get('url'),
                                        visible=True,
                                        user_id=user_id)
        elif reference_type == 'Inproceedings':
            return self.create_reference(reference_type=reference_type,
                                        author=parsed_dict.get('author'),
                                        title=parsed_dict.get('title'),
                                        booktitle=parsed_dict.get('booktitle'),
                                        year=parsed_dict.get('year'),
                                        editor=parsed_dict.get('editor'),
                                        volume=parsed_dict.get('volume'),
                                        series=parsed_dict.get('series'),
                                        pages=parsed_dict.get('pages'),
                                        address=parsed_dict.get('address'),
                                        month=parsed_dict.get('month'),
                                        organization=parsed_dict.get('organization'),
                                        publisher=parsed_dict.get('publisher'),
                                        note=parsed_dict.get('note'),
                                        key=parsed_dict.get('citation_key'),
                                        url=parsed_dict.get('url'),
                                        visible=True,
                                        user_id=user_id)
        else:
            return self.create_reference(reference_type=reference_type,
                                        author=parsed_dict.get('author'),
                                        title=parsed_dict.get('title'),
                                        journal=parsed_dict.get('journal'),
                                        year=parsed_dict.get('year'),
                                        volume=parsed_dict.get('volume'),
                                        number=parsed_dict.get('number'),
                                        pages=parsed_dict.get('pages'),
                                        month=parsed_dict.get('month'),
                                        doi=parsed_dict.get('doi'),
                                        note=parsed_dict.get('note'),
                                        key=parsed_dict.get('citation_key'),
                                        visible=True,
                                        user_id=user_id)

reference_service = ReferenceService() # pylint: disable=invalid-name

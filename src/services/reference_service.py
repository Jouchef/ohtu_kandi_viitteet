"""Reference services   """
from repositories.reference_repository import reference_repository as default_reference_repository # pylint: disable=no-name-in-module, import-error line-too-long
from models.reference import Reference_model as Reference # pylint: disable=no-name-in-module, import-error line-too-long
from models.user_references import UserReferences_model # pylint: disable=no-name-in-module, import-error line-too-long

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
                         user_id = None): # pylint: disable=too-many-arguments line-too-long
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
        """Adds a reference to a user."""
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


    def edit_reference(self, reference_id, **kwargs):
        """Edits a reference with the given id."""
        return self._reference_repository.edit_reference(reference_id, **kwargs)

    def delete_reference(self, reference_id):
        """Deletes a reference with the given id.
        changes the reference's visible attribute to False."""
        return self._reference_repository.delete_reference(reference_id)

reference_service = ReferenceService() # pylint: disable=invalid-name

"""Repository for citations."""
from src.models.reference import Reference_model as Reference # pylint: disable=import-error no-name-in-module
from src.models.user_references import UserReferences_model # pylint: disable=import-error no-name-in-module
from src.db import db # pylint: disable=import-error no-name-in-module

class ReferenceRepository:
    """Repository for citations.
    Handles database queries related to citations.
    """

    def find_all(self):
        """Returns all references from the database."""
        return Reference.query.all()
    def create(self, reference):
        """Creates a new reference and links it to a user."""
        print("Creating new reference in repository")
        db.session.add(reference)
        db.session.commit()
        return reference

    def add_reference_to_user(self, user_reference):
        """Adds a reference to a user."""
        print("Adding reference to user in repository")
        db.session.add(user_reference)
        db.session.commit()
        return user_reference


    def get_reference(self, reference_id):
        """Returns a citation with the reference given id."""
        return Reference.query.filter_by(id=reference_id).first()

    def get_all_references_by_user_id(self, user_id):
        """Returns all citations by the given user id."""
        references = Reference.query.join(UserReferences_model,
                                                UserReferences_model.reference_id
                                                == Reference.id).\
                                                    filter(UserReferences_model.user_id == user_id,
                                                           Reference.visible.is_(True)).all() # pylint: disable=line-too-long
        return references

    def edit_reference(self, reference_id, **kwargs):
        """Edits a reference with the given id."""
        reference = Reference.query.filter_by(id=reference_id).first()

        if reference:
            for key, value in kwargs.items():
                setattr(reference, key, value)
            db.session.commit()
            return True
        return False

    def delete_reference(self, reference_id):
        """Deletes a reference with the given id.
        changes the reference's visible attribute to False."""
        reference = Reference.query.filter_by(id=reference_id).first()
        if reference:
            reference.visible = False
            db.session.commit()
            return True
        return False

reference_repository = ReferenceRepository() # pylint: disable=invalid-name

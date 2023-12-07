"""Repository for citations."""
from models.reference import Reference_model as Reference  # pylint: disable=import-error no-name-in-module
from models.user_references import UserReferences_model  # pylint: disable=import-error no-name-in-module
from db import db  # pylint: disable=import-error no-name-in-module


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
        print(f"Getting from database reference with id {reference_id}")
        return Reference.query.filter_by(id=reference_id).first()

    def get_all_references_by_user_id(self, user_id):
        """Returns all citations by the given user id."""
        references = Reference.query.join(UserReferences_model,
                                          UserReferences_model.reference_id
                                          == Reference.id).\
            filter(UserReferences_model.user_id == user_id,
                   Reference.visible.is_(True)).all()  # pylint: disable=line-too-long
        return references

    def edit_reference(self, reference):
        """INPUT: reference object that has the new values
        DO: updates the reference with the given id with the new values to the database
        RETURNS: True if successful, False if not successful"""
        print("Editing reference in database")
        db.session.add(reference)
        db.session.commit()

    def delete_reference(self, reference_id):
        """Deletes a reference with the given id.
        changes the reference's visible attribute to False."""
        reference = Reference.query.filter_by(id=reference_id).first()
        if reference:
            reference.visible = False
            db.session.commit()
            return True
        return False

    def delete_all_references(self, user_id):
        """Deletes all references by the given user id."""
        references = Reference.query.join(UserReferences_model,
                                          UserReferences_model.reference_id
                                          == Reference.id).\
            filter(UserReferences_model.user_id == user_id).all()
        for reference in references:
            reference.visible = False
        db.session.commit()

reference_repository = ReferenceRepository()  # pylint: disable=invalid-name

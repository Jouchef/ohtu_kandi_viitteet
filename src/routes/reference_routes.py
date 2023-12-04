
from flask import (render_template,
                   redirect, session,
                   request,
                   Blueprint,
                     flash)


from services.reference_service import ReferenceService as reference_service # pylint: disable=import-error no-name-in-module
from services.user_service import UserService # pylint: disable=import-error no-name-in-module
reference_service = reference_service()
user_service = UserService()
references = Blueprint("references", __name__)


@references.route("/form", methods=["GET"])
def render_add_reference_form():
    """Render form for new reference."""
    return render_template("form.html")

@references.route("/export_bibtex")
def export_bibtex():
    """Export references in BibTeX format."""
    bibtex = reference_service.references_to_bibtex(session.get("user_id"))
    return render_template('bibtex_export.html', bibtex=bibtex)




@references.route("/form", methods=["POST"])
def create_reference():
    """Create a new reference."""
    reference_type = request.form.get("type")
    author = request.form.get("author")
    title = request.form.get("title")
    journal = request.form.get("journal")
    year = request.form.get("year")
    volume = request.form.get("volume")
    number = request.form.get("number")
    pages = request.form.get("pages")
    month = request.form.get("month")
    doi = request.form.get("doi")
    note = request.form.get("note")
    key = request.form.get("key")
    visible = True

    print(reference_type)
    try:
        user_name = session.get("username")
        user_id = session.get("user_id")
        print(user_name)
        if not user_name:
            raise Exception("You must be logged in to create a reference") # pylint: disable=broad-exception-raised

        reference_service.create_reference(reference_type = reference_type, author=author,
                                           title=title, journal=journal, year=year,
                                           volume=volume, number=number, pages=pages,
                                           month=month, doi=doi, note=note, key=key, visible=visible,
                                           user_id = user_id) # pylint: disable=line-too-long
        print ("reference created")
        return redirect("/")

    except Exception as error: # pylint: disable=broad-except
        print(f"Error occurred: {error}")
        flash(str(error))
        return render_template("form.html")

@references.route("/change_reference_type", methods=["POST"])
def change_reference_type():
    """Render form with correct fields."""
    if request.form.get('menu') == 'Article':
        return render_template("form.html", selected_type='Article')
    if request.form.get('menu') == 'Book':
        return render_template("form.html", selected_type='Book')
    if request.form.get('menu') == 'Inproceedings':
        return render_template("form.html", selected_type='Inproceedings')


    print("Error in changing reference type")
    return render_template("form.html")

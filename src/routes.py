from app import app
from flask import Flask, render_template, redirect, request
import sql_queries
from sql_queries import all_references_from_db


@app.route("/")
def index():
    """Render index"""
    citates = all_references_from_db()
    return render_template("index.html")


@app.route("/new_reference", methods=['GET', 'POST'])
def new_reference():
    """Render form."""
    selected_type = request.form.get('ra', 'Article')
    return render_template("form.html", selected_type=selected_type)


# @app.route("/add_reference", methods=["GET", "POST"])
# def add_reference():
#     """Render form."""
#     author = request.form.get("author")
#     title = request.form.get("title")
#     journal = request.form.get("journal")
#     year = request.form.get("year")
#     volume = request.form.get("volume")
#     number = request.form.get("number")  # Added field
#     pages = request.form.get("pages")
#     month = request.form.get("month")  # Added field
#     doi = request.form.get("doi")  # Added field
#     note = request.form.get("note")  # Added field
#     key = request.form.get("key")  # Added field
#     sql_queries.citate_to_db(
#         author, title, journal, year, volume, number, pages, publisher)
#     print("moi")
#     citates_dict = sql_queries.citates_to_list()
#     print(citates_dict)
#     return render_template("index.html", author=author, title=title, book_title=book_title, journal=journal, year=year, volume=volume, pages=pages, publisher=publisher, citates=citates_dict)


@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    if request.method == "POST":
        # Extract form data using the correct field names
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

        # Call a function to save the data to the database
        try:
            sql_queries.article_to_db(
                author, title, journal, year, volume, number, pages, month, doi, note, key
            )
            print("Reference added successfully.")
        except Exception as e:
            print("Error adding reference:", e)
            # Handle the error appropriately

        # Fetch updated list of citations
        citates_dict = sql_queries.citates_to_list()

        # Redirect to a different page after successful submission, or pass updated data to template
        return render_template("index.html")

@app.route("/edit_reference", methods=["GET", "POST"])
def edit_reference():
    # info = sql_queries.edit_reference()
    # pitää hakea halutun viitteen tiedot tietokannasta! -> tallenna tiedot listaan "info=[]"
    # info=info
    return render_template("edit.html")


@app.route("/make_changes", methods=["GET", "POST"])
def make_changes():
    author = request.form["name"]
    title = request.form["title"]
    book_title = request.form["book_title"]
    journal = request.form["journal"]
    year = request.form["year"]
    volume = request.form["volme"]
    pages = request.form["pages"]
    publisher = request.form["publisher"]
    sql_queries.make_changes(
        author, title, book_title, journal, year, volume, pages, publisher)
    return render_template("index.html")


@app.route("/delete_reference", methods=["GET", "POST"])
def delete_reference():
    pass

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Collecting data from the form
        name = request.form.get("name")
        email = request.form.get("email")
        book_title = request.form.get("bookTitle")
        review = request.form.get("review")
        rating = request.form.get("rating")

        # Just for demonstration, no database involved
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Book Title: {book_title}")
        print(f"Review: {review}")
        print(f"Rating: {rating} Stars")

        return "Thank you for submitting your review! We'll feature the best reviews on our site."

    # List of books and rating options for dropdowns
    books = [
        "The Great Gatsby by F. Scott Fitzgerald",
        "To Kill a Mockingbird by Harper Lee",
        "1984 by George Orwell",
        "The Catcher in the Rye by J.D. Salinger",
    ]
    ratings = ["1 Star", "2 Stars", "3 Stars", "4 Stars", "5 Stars"]

    return render_template("form.html", books=books, ratings=ratings)


if __name__ == "__main__":
    app.run(debug=True)

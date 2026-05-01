from flask import Flask, render_template

app = Flask(__name__)

profiles = [
    {"name": "jasurbeki", "surname": "iaxshiboevi", "img": "earth.jpg"},
    {"name": "iago", "surname": "xvichia", "img": "cat.jpg"}
]

books = [
    {"id": 1, "title": "Bible", "description": "The Bible is a foundational collection of sacred, divinely inspired texts for Judaism and Christianity...", "rating": "10⭐", "img": "book1.png"},
    {"id": 2, "title": "Война и мир", "description": "War and Peace by Leo Tolstoy is a masterpiece of world literature...", "rating": "3.6⭐", "img": "book2.png"},
    {"id": 3, "title": "1984", "description": "Nineteen Eighty-Four by George Orwell is a dystopian novel...", "rating": "2.6⭐", "img": "book3.png"}
]


@app.route("/")
def home():
    return render_template("index.html", books=books)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    if profile_id < 0 or profile_id >= len(profiles):
        return "Profile Not Found", 404
    profile = profiles[profile_id]
    return render_template("profile.html", profile=profile)


@app.route("/book/<int:book_id>")
def view_book_details(book_id):
    for book in books:
        if book["id"] == book_id:
            return render_template("book_details.html", book=book)
    return "Book Not Found", 404


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/genre/<category>")
def show_genre(category):
    return render_template("genre.html", c=category)


if __name__ == "__main__":
    app.run(debug=True)
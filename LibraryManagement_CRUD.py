from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample database (list)
books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Smith",
        "available": True
    },
    {
        "id": 2,
        "title": "Learning Flask",
        "author": "David Miller",
        "available": True
    },
    {
        "id": 3,
        "title": "Data Structures and Algorithms",
        "author": "Mark Allen",
        "genre": "Computer Science",
        "year": 2019,
        "available": False
    },
    {
        "id": 4,
        "title": "Introduction to Machine Learning",
        "author": "Andrew Cole",
        "genre": "Artificial Intelligence",
        "year": 2022,
        "available": True
    },
    {
        "id": 5,
        "title": "JavaScript Essentials",
        "author": "Sarah Johnson",
        "genre": "Web Development",
        "year": 2020,
        "available": True
    },
    {
        "id": 6,
        "title": "HTML and CSS Design",
        "author": "Robert Brown",
        "genre": "Web Development",
        "year": 2018,
        "available": False
    },
    {
        "id": 7,
        "title": "Database Management Systems",
        "author": "Thomas Lee",
        "genre": "Database",
        "year": 2017,
        "available": True
    },
    {
        "id": 8,
        "title": "Computer Networks",
        "author": "James Wilson",
        "genre": "Networking",
        "year": 2019,
        "available": True
    },
    {
        "id": 9,
        "title": "Operating System Concepts",
        "author": "Abraham Silberschatz",
        "genre": "Computer Science",
        "year": 2018,
        "available": False
    },
    {
        "id": 10,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "genre": "Software Engineering",
        "year": 2008,
        "available": True
    }
]

@app.route('/')
def home():
    return "Library API is running!"

# -----------------------------
# GET all books
# -----------------------------
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# -----------------------------
# GET book by ID
# -----------------------------
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book['id'] == id:
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# -----------------------------
# CREATE new book
# -----------------------------
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json

    new_book = {
        "id": data["id"],
        "title": data["title"],
        "author": data["author"],
        "available": data["available"]
    }

    books.append(new_book)

    return jsonify({
        "message": "Book added successfully",
        "book": new_book
    }), 201

# -----------------------------
# UPDATE book
# -----------------------------
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json

    for book in books:
        if book["id"] == id:
            book["title"] = data.get("title", book["title"])
            book["author"] = data.get("author", book["author"])
            book["available"] = data.get("available", book["available"])

            return jsonify({
                "message": "Book updated successfully",
                "book": book
            })

    return jsonify({"message": "Book not found"}), 404

# -----------------------------
# DELETE book
# -----------------------------
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):

    for book in books:
        if book["id"] == id:
            books.remove(book)

            return jsonify({
                "message": "Book deleted successfully"
            })

    return jsonify({"message": "Book not found"}), 404


# Run server
if __name__ == '__main__':
    app.run(debug=True)
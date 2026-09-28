# library/sample_data.py

books = [
    {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "available": True,
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "available": True,
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "available": False,
    },
]

members = [
    {
        "id": 1,
        "name": "Alice",
        "borrowed_books": [3], # کتاب با آی‌دی ۳ (The Great Gatsby) دست آلیس است
    },
    {
        "id": 2,
        "name": "Bob",
        "borrowed_books": [],
    },
]
# query_samples.py
import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# 1. Query all books by a specific author
# -----------------------------
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'.")


# -----------------------------
# 2. List all books in a library
# -----------------------------
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")


# -----------------------------
# 3. Retrieve the librarian for a library using Librarian.objects.get
# -----------------------------
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # ✅ direct query
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    books_by_author("Chinua Achebe")
    books_in_library("Accra Central Library")
    librarian_for_library("Accra Central Library")

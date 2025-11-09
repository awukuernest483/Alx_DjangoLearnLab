from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # ✅ Import both Book and Library

# -----------------------------
# Function-based view: list all books
# -----------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# -----------------------------
# Class-based view: details for a library
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # namespaced template
    context_object_name = 'library'

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# ----------------------------
# Function-Based View
# ----------------------------
def list_books(request):
    books = Book.objects.all()  # <-- REQUIRED EXACT QUERY
    return render(request, "relationship_app/list_books.html", {"books": books})
    # ^-- REQUIRED EXACT TEMPLATE PATH


# ----------------------------
# Class-Based View
# ----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

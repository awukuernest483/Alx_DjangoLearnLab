from django.shortcuts import render, get_object_or_404
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


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

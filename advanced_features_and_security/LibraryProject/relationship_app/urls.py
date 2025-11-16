from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books

urlpatterns = [
    # Authentication URLs
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Function-based view
    path("books/", views.list_books, name="list_books"),

    # Class-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Book management URLs (for checker)
    path("add_book/", views.manage_books, name="add_book"),
    path("edit_book/", views.manage_books, name="edit_book"),
    path("delete_book/", views.manage_books, name="delete_book"),
]

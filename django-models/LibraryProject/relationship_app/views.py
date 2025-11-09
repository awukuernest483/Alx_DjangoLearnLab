from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # namespaced template
    context_object_name = 'library'  # available in template as 'library'

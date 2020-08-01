from django.urls import path, include
from .views import NotesListView, NotesDetailView, NoteCreateView


urlpatterns = [
    path('', NotesListView.as_view(), name='notes'),
    path('<int:pk>/', NotesDetailView.as_view(), name='note'),
    path('new/', NoteCreateView.as_view(), name="new_note"),
]

from django.urls import path, include
from .views import NotesListView, NoteCreateView


urlpatterns = [
    path('', NotesListView.as_view(), name='notes'),
    path('new/', NoteCreateView.as_view(), name="new_note"),
]

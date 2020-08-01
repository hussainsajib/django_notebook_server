from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Note


class NotesListView(ListView):
    model = Note
    template_name = 'notes.html'


class NoteCreateView(CreateView):
    model = Note
    template_name = 'new.html'
    fields = ('title', 'body', 'subject', 'sub_subject', 'priority',)

from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .models import Note


class NotesListView(ListView):
    model = Note
    template_name = 'notes.html'


class NotesDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'


class NoteCreateView(CreateView):
    model = Note
    template_name = 'new.html'
    fields = ('title', 'body', 'subject', 'sub_subject', 'priority',)

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

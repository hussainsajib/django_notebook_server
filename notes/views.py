from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NoteForm


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes.html'


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'note_detail.html'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'new_note.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

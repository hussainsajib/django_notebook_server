from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Note
from .forms import NoteForm


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes.html'

    def get_queryset(self):
        return Note.objects.filter(creator=self.request.user)


class NotesDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note
    template_name = 'note_detail.html'

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'new_note.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'update_note.html'

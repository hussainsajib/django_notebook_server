from django.forms import ModelForm, Textarea
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'category', 'sub_category', 'priority', 'body', ]
        widgets = {
            'body': Textarea(attrs={'id': 'mytextarea', 'novalidate': 'true'}),
        }

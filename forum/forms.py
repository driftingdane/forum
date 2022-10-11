from django import forms
from django.forms import Textarea
from tinymce.widgets import TinyMCE


class DiscForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea)


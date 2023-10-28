from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta: 
        model = Author
        fields = '__all__'
        # fields = ['name', 'bio']
        # exclude = ['bio']

from django import forms
from .models import Movie
import datetime

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'MovieID': forms.TextInput(attrs={'placeholder': 'e.g. MV0001'}),
            'MovieTitle': forms.TextInput(),
            'Actor1Name': forms.TextInput(),
            'Actor2Name': forms.TextInput(),
            'DirectorName': forms.TextInput(),
            'MovieGenre': forms.Select(),
            'ReleaseYear': forms.NumberInput(attrs={
                'min': 1900,
                'max': datetime.date.today().year
            }),
        }

    def clean_ReleaseYear(self):
        y = self.cleaned_data['ReleaseYear']
        now = datetime.date.today().year
        if y < 1900 or y > now:
            raise forms.ValidationError(f"Year must be between 1900 and {now}.")
        return y


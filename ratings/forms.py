from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    score = forms.ChoiceField(
        choices=[(i, f"{i} ★") for i in range(1, 6)],
        widget=forms.RadioSelect
    )

    class Meta:
        model = Rating
        fields = ['score', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional feedback...'})
        }

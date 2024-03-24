from django import forms

from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url', 'short_link']
        error_messages = {
            'url': {
                'required': 'Введіть посилання ',
                'invalid': 'Введіть коректне посилання'
            },
            'short_link': {
                'max_length': 'Максисмум для короткого посилання 50 символів',
                'unique': 'Таке коротке посилання вже існує!',
            },
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update({'class': 'inp'})
        self.fields['short_link'].widget.attrs.update({'class': 'inp'})
        
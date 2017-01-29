from django import forms
from django.forms import SelectDateWidget
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from .models import Trip
from datetime import date

def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            _('This field must contain three or more characters')
        )

class TripForm(forms.ModelForm):
    destination = forms.CharField(max_length=100, validators=[validateLengthGreaterThanTwo])
    date_from = forms.DateField(widget=SelectDateWidget())
    date_to = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Trip
        fields = ['destination', 'description', 'date_from', 'date_to']

    def clean(self):
        super(TripForm, self).clean()
        if self.cleaned_data.get('date_from'):
            date_from = self.cleaned_data['date_from']
            if date_from < date.today():
                self.add_error('date_from', 'The date cannot be in the past.')
            if self.cleaned_data.get('date_to'):
                date_to = self.cleaned_data['date_to']
                if date_to < date_from:
                    self.add_error('date_to', 'The ending date cannot be earlier than the start date.')

    # def clean_date_from(self):
    #     date = self.cleaned_data['date_from']
    #     if date < date.today():
    #         raise forms.ValidationError("The date cannot be in the past!")
    #     return date
    #
    # def clean_date_to(self):
    #     date = self.cleaned_data['date_to']
    #     date_from = self['date_from']
    #     if date < date_from:
    #         raise forms.ValidationError("The ending date cannot be earlier than the starting date.")
    #     return date

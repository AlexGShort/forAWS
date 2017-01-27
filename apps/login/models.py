from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.forms import ModelForm
import re

def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            _('This field must contain three or more characters')
        )

def validateOnlyLetters(value):
    if not value.isalpha():
        raise ValidationError(
            _('This field must contain only letters')
        )
def validateLengthAtLeastEight(value):
    if len(value) < 8:
        raise ValidationError(
            _('This field must contain eight or more characters')
        )

def validateMustContainUpper(value):
    if not re.search(r'[A-Z]', value):
        raise ValidationError(
            _('This field must contain at least one upper case letter')
        )

def validateMustContainNumber(value):
    if not re.search(r'[0-9]', value):
        raise ValidationError(
            _('This field must contain at least one number')
        )

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45, validators=[validateLengthGreaterThanTwo, validateOnlyLetters])
    last_name = models.CharField(max_length=45, validators=[validateLengthGreaterThanTwo, validateOnlyLetters])
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

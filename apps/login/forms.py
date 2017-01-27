from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from .models import User
import bcrypt
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

# class RegistrationForm(forms.ModelForm):
#     confirm_password = forms.CharField(max_length = 255, widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        super(LoginForm, self).clean()
        password = self.cleaned_data.get('password').encode(encoding='utf-8', errors='strict')
        response = User.objects.filter(email = self.cleaned_data.get('email'))
        if (len(response) != 0):
            print "password: {}, hashed password: {}".format(password, response[0].password)
            password_db_hash = response[0].password.encode(encoding='utf-8', errors='strict')
            print "*"*50
            print "hashed pw: {}".format(bcrypt.hashpw(password, password_db_hash) == password_db_hash)
            if (bcrypt.hashpw(password, password_db_hash) == password_db_hash):
                print "*"*50
                # request.session['user_id'] = response[0].id
                # request.session['user_name'] = response[0].first_name
                # return render(request, 'login/success.html')
            else:
                msg = 'Email address and password do not match our records.'
                self.add_error('email', msg)

                # flash('Email address and password do not match our records.')
                # return False
        else:
            msg = 'Email address and passwords do not match our records.'
            self.add_error('email', msg)

            # flash('Email address does not match our records.  Please register or try again.')
            # return False




class RegistrationForm(forms.ModelForm):

    first_name = forms.CharField(max_length=45, validators=[validateLengthGreaterThanTwo, validateOnlyLetters])
    last_name = forms.CharField(max_length=45, validators=[validateLengthGreaterThanTwo, validateOnlyLetters])
    email = forms.EmailField(widget=forms.TextInput)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[validateLengthAtLeastEight, validateMustContainUpper, validateMustContainNumber])
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


    def clean(self):
        super(RegistrationForm, self).clean()
        # password = cleaned_data.get('password')
        # confirm_password = cleaned_data.get('confirm_password')
        # print "*"*50
        # print self.cleaned_data['password']
        if not self.data['password'] == self.data['confirm_password']:
            msg = 'Passwords must match'
            self.add_error('confirm_password', msg)
        else:
            # password = self.cleaned_data.get('password')
            password = self.data.get('password')
            # print "*"*50
            # print "data password: {}".format(password)
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            self.cleaned_data['password'] = hashed_password

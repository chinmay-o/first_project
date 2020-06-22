from django import forms
from django.contrib.auth.models import User as UserCred
from django.core import validators
from .models import Webpage, User, UserProfileInfo

class FormName(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Verify Email")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):

        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

class UsersForm(forms.ModelForm):

    class Meta:

        model = User
        fields = "__all__"

class UserSignIn(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():

        model = UserCred
        help_texts = {
            'username': None,
        }
        fields = ("first_name", "last_name", "username", "email", "password")

class UserProfileInfoForm(forms.ModelForm):

    class Meta():

        model = UserProfileInfo
        fields = ('url',)

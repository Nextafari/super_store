from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, required=True, help_text='Please enter your email')
    first_name = forms.CharField(max_length=200, required=True, help_text='Please enter your first name')
    last_name = forms.CharField(max_length=200, required=True, help_text='Please enter your last name')

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        )


        def save(self, commit=True):
            """function for saving user email where commit is sql syntax used to save."""
            user = super(SignUpForm, self).save(commit=False)   
            user.email = self.cleaned_data['email']
            #Getting the email and saving alongside user's credentials
            if commit:
                user.save()
                return user
from django import forms
from django.contrib.auth.models import User
# At this point user is a User object that has  already been saved to the database
#you can continue to change its attribute
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']


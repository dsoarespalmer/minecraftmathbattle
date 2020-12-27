from django import forms
from django.core import validators

#def check_answer(value):
    #if value != 14:
        #raise forms.ValidationError("try again!")
    #else:
        #raise forms.ValidationError("correct!")


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    answer = forms.IntegerField()
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

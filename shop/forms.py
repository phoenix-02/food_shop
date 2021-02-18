from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=False,label='',label_suffix='')

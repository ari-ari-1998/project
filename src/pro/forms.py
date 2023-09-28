from django import forms

class NippoFormClass(forms.Form):
    company = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'企業名...'}))
    company_id = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'ID...'}))
    company_password = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'パスワード...'}))


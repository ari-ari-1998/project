from django import forms

class NippoFormClass(forms.Form):
    company = forms.CharField(label="企業名",widget=forms.TextInput(attrs={'placeholder':'企業名...'}))
    company_id = forms.CharField(label="ID",widget=forms.TextInput(attrs={'placeholder':'ID...'}))
    company_password = forms.CharField(label="パスワード",widget=forms.TextInput(attrs={'placeholder':'パスワード...'}))
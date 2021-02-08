from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Content", widget= forms.Textarea)

# import form class from django
from django import forms


from website.models import Message




# create a ModelForm



class ContactForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"Nome"}),
            "email": forms.TextInput(attrs={"placeholder":"Email"}),
            "title": forms.TextInput(attrs={"placeholder":"Assunto"}),
            "description": forms.Textarea(attrs={"placeholder":"Messagem"}),
        }



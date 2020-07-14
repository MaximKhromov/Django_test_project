from .models import Answers
from django.forms import ModelForm, TextInput

class AnsForm(ModelForm):
    class Meta:
        model=Answers
        fields=['answ']
        widgets={'answ': TextInput(attrs={
            'class':'custom-control custom-radio'
        })}
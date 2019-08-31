from .models import ExtraInfo
from django import forms
from django.forms import ModelForm
import re

RGX_NUMBER = re.compile(r"(?:\+234)?(?:070|080|081|090)\d{8}")

def validate_number(value):
    if not RGX_NUMBER.match(value):
        raise forms.ValidationError('Please enter a valid phone number')

class NigerianField(forms.CharField):
    """
    A CharField that allows only nigerian phone numbers
    """

    default_validators = [validate_number]

    def __init__(self, *args, **kwargs):
        super(NigerianField, self).__init__(
            min_length=11,
            max_length=15,
            error_messages={
                "required": "You need to set this number field",
                "min_length": "Your phone number is too short",
                "max_length": "Your phone number is too big",
            }
        )


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    
    number = forms.CharField(validators=[validate_number], help_text="Phone number",
                            widget=forms.TextInput(attrs={'placeholder':'Phone number'}),
                            label='Phone number')
    
    code = forms.CharField(help_text="Enter your registration code",
                           widget=forms.TextInput(attrs={'placeholder':'0000'}),
                            label='code')
        
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['number'].error_messages = {
            "required": u"Please give us your number.",
            "invalid": u"Please use a valid nigerian phone number.",
        }
        

    class Meta(object):
        model = ExtraInfo
        fields = ('number', 'code')
        labels = {'number':'Mobile phone number'}

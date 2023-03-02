from django.forms import ModelForm
from . models import test

class testform(ModelForm):
    class Meta:
        model = test
        fields = '__all__'
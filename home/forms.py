from django.forms import ModelForm
from home.models import SyntaxPost

class SyntaxForm(ModelForm):
    class Meta:
        model = SyntaxPost
        fields = ['content']
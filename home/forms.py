from django.forms import ModelForm
from home.models import SyntaxPost, Suggestion, Contact

class SyntaxForm(ModelForm):
    class Meta:
        model = SyntaxPost
        fields = ['content']

class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        fields = ['langName','langVer','website','comments']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','mensaje']
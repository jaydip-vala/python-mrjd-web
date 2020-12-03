# from django import forms
# from .models import dreamreal


# class DreamrealForm(forms.Form):
#    class Meta:
#       model = dreamreal
#       fields = "__all__"

from django import forms
from .models import dreamreal


class DreamrealForm(forms.ModelForm):
   class Meta:
      model = dreamreal
      fields = "__all__" 
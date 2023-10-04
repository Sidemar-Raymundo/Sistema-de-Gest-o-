from django.forms import ModelForm
from .models import AvaliacaoFilme


class AvaliacaoFilmeForm(ModelForm):
    class Meta:
        model = AvaliacaoFilme
        fields = '__all__'
from django.forms import ModelForm
from .models import ReportCard

class ReportForm(ModelForm):
    class Meta:
        model = ReportCard
        fields = "__all__"

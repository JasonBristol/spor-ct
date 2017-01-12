from django import forms
from .models import BugCategory, BugReport

class BugReportForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=BugCategory.objects.order_by('name'))
    category.widget.attrs.update({'class': 'form-control'})
    description = forms.CharField(widget=forms.Textarea, required=True)
    description.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Description',
        'rows': 3
    })

    class Meta(object):
        model = BugReport
        fields = ['category', 'description',]
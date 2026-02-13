from django import forms
from rango.models import Category
from rango.models import Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        help_text="Please enter the category name."
    )

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128,
        help_text="Please enter the title of the page."
    )
    url = forms.CharField(max_length=200, help_text="Please enter the URL of the page.")

    views = forms.IntegerField(
        widget=forms.HiddenInput(),
        initial=0
    )

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://') and not url.startswith('https://'):
            cleaned_data['url'] = 'http://' + url

        return cleaned_data



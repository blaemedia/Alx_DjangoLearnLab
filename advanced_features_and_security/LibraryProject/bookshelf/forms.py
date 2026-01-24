from django import forms


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    # Basic validation example
    def clean_name(self):
        name = self.cleaned_data.get("name")
        return name.strip()
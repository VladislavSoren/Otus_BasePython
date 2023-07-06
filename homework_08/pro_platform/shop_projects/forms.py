from django import forms

from .models import (
    Project,
    Category,
)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "price",
            "description",
            "category",
            "status",
            "creator",
            "url",
            "other_contributors",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            "name",
            "description",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"

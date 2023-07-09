from django.contrib.auth.forms import (
    AuthenticationForm as AuthenticationFormGeneric,
)
from django import forms

class AuthenticationForm(AuthenticationFormGeneric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"


# from django import forms
#
# from .models import (
#     Project,
#     Category, Creator, Donat, Order,
# )
#
#
# class BaseForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for name, field in self.fields.items():
#             widget: forms.Widget = field.widget
#             widget.attrs["class"] = "form-control"
#
#
# class ProjectForm(BaseForm):
#     class Meta:
#         model = Project
#         fields = (
#             "name",
#             "price",
#             "description",
#             "category",
#             "status",
#             "creator",
#             "url",
#             "other_contributors",
#         )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
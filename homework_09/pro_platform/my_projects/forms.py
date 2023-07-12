from django import forms

from my_projects.models import ImageSexAgeDetect


class ImageSexAgeDetectForm(forms.ModelForm):
    class Meta:
        model = ImageSexAgeDetect
        # fields = ['name', 'ImgSexAgeDetect']
        fields = '__all__'

from django.http import HttpResponse
from django.shortcuts import render, redirect

from shop_projects.forms import ImageSexAgeDetectForm


# Create your views here.


def image_for_predict_view(request):
    if request.method == 'POST':
        form = ImageSexAgeDetectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageSexAgeDetectForm()
    return render(request, '/image_upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
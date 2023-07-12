from django.shortcuts import redirect, render
from my_projects.forms import ImageSexAgeDetectForm
import time

def image_request(request):
    if request.method == 'POST':
        form = ImageSexAgeDetectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            # time.sleep(5)

            return render(
                request,
                'my_projects/image_sex_age_detect.html',
                {'form': form, 'img_obj': img_object}
            )
    else:
        form = ImageSexAgeDetectForm()

    return render(
        request,
        'my_projects/image_sex_age_detect.html',
        {'form': form}
    )

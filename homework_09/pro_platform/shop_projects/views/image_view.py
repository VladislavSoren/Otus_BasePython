from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from shop_projects.forms import ImageSexAgeDetectForm


# Create your views here.


def image_for_predict_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ImageSexAgeDetectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('shop_projects:success')
    else:
        form = ImageSexAgeDetectForm()
    return render(
        request=request,
        template_name='/shop_projects/image_upload_new.html',
        context={
            "form": form,
        }
    )


# def shop_index(request: HttpRequest) -> HttpResponse:
#     projects = Project.objects.order_by("id").all()
#
#     return render(
#         request=request,
#         template_name="shop_projects/index.html",
#         context={
#             "projects": projects,
#         }
#     )


def success(request):
    return HttpResponse('successfully uploaded')

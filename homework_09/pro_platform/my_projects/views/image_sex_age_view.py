import base64
import io
import os

from django.shortcuts import redirect, render
from my_projects.forms import ImageSexAgeDetectForm

from PIL import Image
from aiohttp import ClientSession
from asgiref.sync import sync_to_async

from pro_platform.settings import BASE_DIR


async def get_prediction(url: str, data):
    async with ClientSession() as session:
        async with session.post(url, json=data) as response:
            data: dict = await response.json()
            return data


#
def image_bytes_to_str(im_path):
    with open(im_path, mode='rb') as file:
        image_bytes = file.read()
    image_str = base64.encodebytes(image_bytes).decode('utf-8')
    return image_str


def show_input_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    image.show()
    return image


SEX_AGE_HUMANS_DETECTION_SERVICE_URL = " http://127.0.0.1:9988/image"


async def image_request(request):
    if request.method == 'POST':
        form = ImageSexAgeDetectForm(request.POST, request.FILES)
        if form.is_valid():
            await sync_to_async(form.save)()

            # Getting the current instance object to display in the template
            img_object = form.instance

            im_path = img_object.ImgSexAgeDetect.url
            im_path_abs = BASE_DIR / im_path[1:]  # ignore first "/" in image path

            # serialization
            data = {}
            data['user'] = 'Soren'
            data['image'] = image_bytes_to_str(im_path_abs)
            data['image_name'] = os.path.basename(im_path_abs)

            # sending image to service and receiving  response with tagged image
            json_input: dict = await get_prediction(SEX_AGE_HUMANS_DETECTION_SERVICE_URL, data)

            #  deserialization
            image_bytes = base64.b64decode(json_input["tagged_img"])

            # displaying tagged image
            image_pillow = show_input_image(image_bytes)
            # absolute path
            path_tagged_img = BASE_DIR / 'media' / 'images_tagged' / data['image_name']
            image_pillow.save(path_tagged_img)

            # relative path
            path_tagged_img_for_form = path_tagged_img = f'''/media/images_tagged/{data['image_name']}'''

            return render(
                request,
                'my_projects/image_sex_age_detect.html',
                {'form': form, 'img_obj': img_object, 'path_tagged_img': path_tagged_img_for_form}
            )
    else:
        form = ImageSexAgeDetectForm()

    return render(
        request,
        'my_projects/image_sex_age_detect.html',
        {'form': form}
    )

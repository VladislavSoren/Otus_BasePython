import base64
import io
import os

from django.shortcuts import redirect, render
from my_projects.forms import ImageSexAgeDetectForm

from PIL import Image
from aiohttp import ClientSession
from asgiref.sync import sync_to_async

from pro_platform.settings import BASE_DIR


async def get_prediction(url: str, data: dict):
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


def save_tagged_image(image_bytes, path_tagged_image: str):
    image = Image.open(io.BytesIO(image_bytes))
    image.save(path_tagged_image)


SEX_AGE_HUMANS_DETECTION_SERVICE_URL = " http://127.0.0.1:9988/image"


async def image_request(request):
    if request.method == 'POST':
        form = ImageSexAgeDetectForm(request.POST, request.FILES)
        if form.is_valid():
            await sync_to_async(form.save)()

            # Getting the current instance object to display in the template
            image_object = form.instance

            # Getting path for saving input image
            path_input_image = image_object.ImgSexAgeDetect.url
            path_input_image_abs = BASE_DIR / path_input_image[1:]  # ignore first "/" in image path

            # serialization
            json_out = {}
            json_out['user'] = 'Soren'
            json_out['image'] = image_bytes_to_str(path_input_image_abs)
            json_out['image_name'] = os.path.basename(path_input_image_abs)

            # sending image to service and receiving  response with tagged image
            json_input: dict = await get_prediction(SEX_AGE_HUMANS_DETECTION_SERVICE_URL, json_out)

            #  deserialization
            image_bytes = base64.b64decode(json_input["tagged_image"])

            # absolute path
            path_tagged_image = BASE_DIR / 'media' / 'images_tagged' / json_out['image_name']
            save_tagged_image(image_bytes, path_tagged_image)

            # relative path
            path_tagged_image_for_form = f'''/media/images_tagged/{json_out['image_name']}'''

            return render(
                request,
                'my_projects/image_sex_age_detect.html',
                {'form': form, 'image_object': image_object, 'path_tagged_image': path_tagged_image_for_form}
            )
    else:
        form = ImageSexAgeDetectForm()

    return render(
        request,
        'my_projects/image_sex_age_detect.html',
        {'form': form}
    )

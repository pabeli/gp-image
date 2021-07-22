from django.shortcuts import render
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
import re

# Check MIME type
def check_mime(file):
    pass

@csrf_exempt
def post_image(request):
    image = request.FILES['image_file']
    image.name = image.name.replace(' ', '-')
    image_file = image.file.read()
    Post.objects.create(image=image_file, mime_type=image.content_type)
    return HttpResponse(status=204)


def get_image(request, pk):
    post = Post.objects.get(id=pk)
    image_bytes = post.image
    mime_type = str(post.mime_type)
    print(mime_type)
    return HttpResponse(image_bytes, content_type = 'image/jpeg')
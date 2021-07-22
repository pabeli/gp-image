from django.shortcuts import render
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Check MIME type
def check_mime(file):
    pass

@csrf_exempt
def post_image(request):
    image_file = request.FILES['image_file'].file.read()
    mime_type = request.FILES['image_file'].content_type
    Post.objects.create(image=image_file, mime_type=mime_type)
    return HttpResponse(status=204)

def get_image(request, pk):
    post = Post.objects.get(id=pk)
    image_bytes = post.image
    mime_type = str(post.mime_type)
    print(mime_type)
    return HttpResponse(image_bytes, content_type = 'image/jpeg')
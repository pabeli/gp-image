from django.shortcuts import render
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
@csrf_exempt
def post_image(request):
    image_file = request.FILES['image_file'].file.read()
    Post.objects.create(image=image_file)
    return HttpResponse(status=204)

def get_image(request, pk):
    post = Post.objects.get(id=pk)
    image_bytes = post.image
    return HttpResponse(image_bytes, content_type = 'image/jpeg')
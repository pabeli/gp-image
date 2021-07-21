from django.contrib import admin
from django.urls import path
from posts.views import post_image, get_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post_image/', post_image),
    path('get_image/<int:pk>/', get_image)
]

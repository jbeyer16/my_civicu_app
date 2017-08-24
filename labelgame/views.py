# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Image
from .forms import FileUploadForm
from .serializers import ImageSerializer

from rest_framework import generics
# Create your views here.


def index(request):
    images = Image.objects.all()
    return render(request, 'labelgame/index.html', {'images': images})
    # return HttpResponse("Hello, you're at the labelgame index page.")


def form_file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileUploadForm()
    return render(request, 'labelgame/form_file_upload.html', {'form': form})


class ListImages(generics.ListCreateAPIView):
    """ A class based view that inherits from the generics class.

    Creates REST views/forms for simple CRUD operations.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

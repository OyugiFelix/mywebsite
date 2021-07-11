from connect.models import Comment
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def formView(request):
    name = Comment.objects.get(id=1).name
    return render(request, 'form.html', {"name": name})

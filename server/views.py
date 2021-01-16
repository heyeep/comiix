from django.shortcuts import render
from django.http import HttpResponse

from .tasks.seeder import seed_db

from rest_framework import viewsets
from .serializers import AuthorSerializer
from .models import Author

def index(req):
    return HttpResponse('Sup')

def seed(request):
    if request.POST:
        task_type = request.POST.get('type')
        task = seed_db()
        return JsonResponse({'task_id': task.id, 'object': task}, status=202)

class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

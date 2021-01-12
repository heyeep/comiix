from django.shortcuts import render
from django.http import HttpResponse

from .tasks.seeder import seed_db

# Create your views here.
def index(req):
    return HttpResponse('Sup')
def seed(request):
    if request.POST:
        task_type = request.POST.get('type')
        task = seed_db()
        return JsonResponse({'task_id': task.id, 'object': task}, status=202)

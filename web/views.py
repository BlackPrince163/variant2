from django.shortcuts import render

from api.models import ToDoList


def main(request):
    context = {"queryset": ToDoList.objects.all()}
    return render(request, "web/main.html", context)


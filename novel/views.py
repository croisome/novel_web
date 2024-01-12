from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def get_novel_by_id(request, n_id: int):

    return HttpResponse("hello"+str(n_id))

from django.shortcuts import render
from django.forms.models import model_to_dict
# Create your views here.
from django.http import HttpResponse, JsonResponse

from .models import BookInfo, BookChapter


def get_book_info_by_id(request, book_id: int):
    try:
        value = model_to_dict(BookInfo.objects.get(id=book_id))
    except Exception as e:
        print(e)
        value = {}
    return JsonResponse(value)


from django.core import serializers


def get_chapters_list_by_id(request, book_id: int, start_index: int):
    val_set = BookChapter.objects.filter(book_id=book_id)[start_index:100]
    # print(val_set)
    res = serializers.serialize("json", val_set)

    return HttpResponse(res, content_type='application/json')

from django.urls import path
from . import views
urlpatterns = [
    path("novels/<int:book_id>/", views.get_book_info_by_id),
    path("chapters/<int:book_id>/<int:start_index>", views.get_chapters_list_by_id)
]

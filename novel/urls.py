from django.urls import path
from . import views
urlpatterns = [
    path("novels/<int:n_id>/", views.get_novel_by_id)
]


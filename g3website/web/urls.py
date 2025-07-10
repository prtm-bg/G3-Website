
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("subjects", views.subjects),
    path("social/<str:app1>", views.social),
    path("<str:subject>/types", views.types),
    path("<str:subject>/gdrive", views.gdrive),
    path("<str:subject1>/<str:types1>", views.materials),
    path("pdf/pdf/<str:pdf>", views.pdf_view),
    path("gallery", views.gallery),
    path("notice", views.notice_view),
    path('search/', views.search_post, name='search-view'),
]
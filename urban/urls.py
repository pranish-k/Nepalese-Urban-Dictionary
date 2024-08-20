from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('submit/',views.submit, name='submit'),
    path('search/', views.search, name='search'),
    path('define/<slug:word_slug>/', views.define, name='define'),
]
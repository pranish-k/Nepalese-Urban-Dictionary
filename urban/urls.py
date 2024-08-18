from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('submit/',views.submit, name='submit'),
    path('update/<str:pk>', views.update, name='update'),
    path('search/', views.search, name='search'),
    path('define/<str:word_title>', views.define_word, name='define_word'),

]

from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name='/index/'),
    path('names',views.name,name='names')
    # path()
]
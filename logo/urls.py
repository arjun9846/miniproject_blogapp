from django.urls import path
from .views import log

urlpatterns = [
    path('login/',log, name='login'),
    path('logout/',log, name='logout'),
 
]


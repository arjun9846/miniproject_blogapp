from django.urls import path
from.import views
from django.contrib import admin

from blogapp.views import frontpage
from blogapp.views import post_details
from django.urls import path


urlpatterns = [
    path('form/', views.base),
    path('', frontpage, name='frontpage'),
    path('<slug:posted>/', post_details, name='post_details'),
    path('admin/', admin.site.urls),
    # path('logout/', views.logout_view, name='logout'),
]

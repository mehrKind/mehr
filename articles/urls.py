from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.articles_list,name="list"),
    path('create',views.create_views, name="create"),
    path('<slug>',views.articles_details,name="detail"),
]

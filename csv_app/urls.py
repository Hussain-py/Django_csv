from django.urls import path
from csv_app import views

urlpatterns = [
    # CSV Read URLS
    path('', views.home_view),
    path('save/', views.save_file),
    path('table/', views.Table),
    # path('display/', views.display),
    # path('i/', views.index),
    # path('leads/', views.buisness_leads),

]


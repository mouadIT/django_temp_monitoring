from django.urls import path
from appdsb import views, api

urlpatterns = [
    path('', views.home, name='home'),
    path('second/', views.second, name='second'),
    path('data/', views.ds18b20, name='Data'),
    path('api/list/', api.Dlist, name='DSBList'),  # api
    path('api/post/', api.DSBViews.as_view(), name='DSB_post'),  # genericViews
    path('charts/', views.EditorChartView.as_view(), name='CH'),
    path('operation/', views.dboperation, name='operation'),
    path('csv/', views.exp_csv, name='exp-csv'),
]

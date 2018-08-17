from django.conf.urls import url
from assets import views

app_name = 'assets'

urlpatterns = [
    url('report/', views.report, name='report'),
    url('dashboard/', views.dashboard, name='dashboard'),
    url('index/', views.index, name='index'),
    url('detail/(?P<asset_id>[0-9]+)/', views.detail, name='detail'),
    url('', views.dashboard),
]
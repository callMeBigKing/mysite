from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:user_id>/user_msg/', views.user_msg, name='user_msg'),
    path('<int:user_id>/user_msg_change/', views.user_msg_change, name='user_msg_change'),
    path('user_msg_create/', views.user_msg_create, name='user_msg_create'),
    path('user_msg_add/', views.user_msg_add, name='user_msg_add'),
    path('upload/', views.uploadImg),
    path('show/', views.showImg),
]

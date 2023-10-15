from django.urls import path
from . import views
# . это текущая папка

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    # ''- путь к главной странице приложения shop
    path('<int:course_id>', views.single_course, name='single_course' )
]

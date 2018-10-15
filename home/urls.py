from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='web-home'),
    path('syntaxposts/',views.syntaxposts,name='syntaxpost'),
    path('favorites/',views.favorites,name='favorites')

]
#path('about/',views.about,name='web-about')

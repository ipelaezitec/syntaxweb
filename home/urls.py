from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='web-home'),
    path('syntaxposts/',views.syntaxposts,name='syntaxpost'),
    path('favorites/',views.favorites,name='favorites'),
    path('panel/', views.panel, name='panel'),
    path('panel/langpulls',views.langpulls,name='langpulls'),
    path('panel/languages',views.languages,name="langs"),
    path('panel/languages/<int:id>', views.lang, name="lang"),
    path('panel/langpulls/<int:id>',views.langpull,name="langpull"),
    path('panel/langpulls/update/<int:id>',views.updateLanguage,name='updatelang'),
    path('panel/reports/',views.reports,name='reports'),
    path('panel/report/<int:id>',views.report,name='report'),
    path('panel/reports/updatestate/<int:id>',views.changeToResolved,name='changeToResolved'),
    path('panel/reportsresolved/',views.reportsResolved,name='reportsResolved'),


]
#path('about/',views.about,name='web-about')

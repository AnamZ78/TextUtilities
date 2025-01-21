from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('removepunc', views.removepunc, name='removepunc'),
    # path('captalizefirst', views.capfirst, name='capfirst'),
    # path('newlineremove', views.newline, name='newlineremove'),
    # path('spaceremove', views.space, name='spaceremove'),
    # path('charcount', views.charcount, name='charcount'),
    path('analyze', views.analyze, name='analyze'),


]

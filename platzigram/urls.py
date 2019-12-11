#  PlatziGram URLs module
from django.contrib import admin

from django.urls import path
from platzigram import views as localViews
from post import views as postsViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', localViews.helloWorld),
    path('sorted/', localViews.sortIntegger),
    path('hi/<str:name>/<int:age>/', localViews.sayHi),
    path('post/', postsViews.listPost),
]

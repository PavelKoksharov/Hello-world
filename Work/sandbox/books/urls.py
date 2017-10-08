from django.conf.urls import url
from books.views import PublisherList

urlpatterns = [
    url(r'^publishers/$', PublisherList.as_view()),
]
urlpatterns = [
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
]

from django.urls import path
from .views import PageList, PageDetailView

app_name = 'wiki'

urlpatterns = [
    path('', PageList.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]

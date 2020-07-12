from django.urls import path
from .views import HomeView, EntryView, CreateEntryView

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('article/<int:pk>/', EntryView.as_view(), name='blog-article'),
    path('create_article/', CreateEntryView.as_view(success_url='/'), name='create-article')

]

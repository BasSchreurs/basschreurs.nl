from django.urls import path
from . import views

urlpatterns = [
    path('', views.guestbook_view, name='guestbook'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
]
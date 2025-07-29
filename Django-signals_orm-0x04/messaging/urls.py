from django.urls import path
from . import views

urlpatterns = [
    path('messages/<int:message_id>/', views.message_detail, name='message_detail'),
    path('delete_account/', views.delete_user, name='delete_account'),
]
    #path('messages/<int:pk>/', views.message_detail, name='message_detail'),
#]

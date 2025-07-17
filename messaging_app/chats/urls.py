from django.urls import path, include
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet


router = routers.SimpleRouter()
router.register(r'conversations', ConversationViewSet, basename='conversations')

# Nested messages under conversations
convo_router = routers.NestedSimpleRouter(router, r'conversations', lookup='conversation')
convo_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(convo_router.urls)),
]

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only allow owners of the object to access it
        return obj.user == request.user

class IsParticipantOrSender(permissions.BasePermission):
    """
    Custom permission to only allow users to view messages or conversations
    where they are a participant.
    """

    def has_object_permission(self, request, view, obj):
        # For Message model: check sender or receiver
        if hasattr(obj, 'sender') and hasattr(obj, 'receiver'):
            return obj.sender == request.user or obj.receiver == request.user

        # For Conversation model: check participants
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()

        return False
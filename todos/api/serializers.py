from rest_framework import serializers
from ..models import todo

class TodoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = todo
        fields = ('id', 'userId', 'title', 'text', 'created_at')
        # read_only_fields = ('date_created', 'date_modified')
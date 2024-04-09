from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image file too large')
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width too large'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height too large'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return obj.owner == request.user

    class Meta:
        model = Event
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'what_title',
            'what_content',
            'where_place',
            'where_address',
            'when_start',
            'when_end',
            'intention',
            'event_image',
            'is_owner',
            'profile_id',
            'profile_image',
        ]

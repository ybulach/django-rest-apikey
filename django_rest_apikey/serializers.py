from rest_framework import serializers

import models

class APIKeySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.APIKey
		fields = ('key', 'created_at')
		read_only_fields = ('key', 'created_at')

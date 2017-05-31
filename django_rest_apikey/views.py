from rest_framework import permissions, viewsets

import models
import serializers
import validators

class APIKeyViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.APIKeySerializer
	lookup_field = 'key'
	lookup_value_regex = validators.hexadecimal_regex
	permission_classes = (permissions.IsAuthenticated,)
	filter_backends = ()

	# Only return API keys owned by the user
	def get_queryset(self):
		return models.APIKey.objects.filter(user=self.request.user)

	# Add the user on creation
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

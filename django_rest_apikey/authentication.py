from rest_framework.authentication import TokenAuthentication

import models

class APIKeyAuthentication(TokenAuthentication):
	keyword = 'API-Key'

	def get_model(self):
		if self.model is not None:
			return self.model
		return models.APIKey

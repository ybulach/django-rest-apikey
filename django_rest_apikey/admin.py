from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

import models

admin.site.register(models.APIKey, TokenAdmin)

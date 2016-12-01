from django.contrib import admin

import models

class APIKeyAdmin(admin.ModelAdmin):
	list_display = ('key', 'user', 'created_at')
	fields = ('user',)
	ordering = ('-created_at',)

admin.site.register(models.APIKey, APIKeyAdmin)

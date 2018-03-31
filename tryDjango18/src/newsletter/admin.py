from django.contrib import admin

# Register your models here.
from .models import SignUp

class AdminSignUp(admin.ModelAdmin):
	list_display = ["__unicode__", "full_name", "timestamp", "updates"]
	class Meta:
		model = SignUp


admin.site.register(SignUp, AdminSignUp)
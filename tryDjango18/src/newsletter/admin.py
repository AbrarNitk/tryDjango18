from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm


class AdminSignUp(admin.ModelAdmin):
    list_display = ["__unicode__", "full_name", "timestamp", "updates"]
    form = SignUpForm

    # class Meta:
    #     model = SignUp


admin.site.register(SignUp, AdminSignUp)

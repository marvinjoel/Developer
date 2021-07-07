from apps.users.models import DetailsModel, UserModel
from django.contrib import admin

# Register your models here.

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name')


admin.site.register(DetailsModel)
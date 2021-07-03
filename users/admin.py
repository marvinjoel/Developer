from users.models import DetailsModel, UserModel
from django.contrib import admin



@admin.register(UserModel)
class UserModelsAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name')


admin.site.register(DetailsModel)

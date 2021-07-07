from apps.users.models import UserModel
from django.shortcuts import render
from django.views import View

# Create your views here.

class ListViews(View):
    template = 'content.html'

    def get(self,request):
        users = UserModel.objects.select_related('detail')
        return render(request, self.template, dict(users=users))

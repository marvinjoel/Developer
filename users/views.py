from users.models import UserModel
from django.shortcuts import render
from django.views import View



class ListViews(View):
    template = 'base.html'

    def get(self,request):
        users = UserModel.objects.all()
        return render(request, self.template, dict(users=users))

from django.shortcuts import render
from .models import FeedBack
from django.views.generic import View


# Create your views here.
class FeedBackView(View):
    def get(self,request):
        feedbacks = FeedBack.objects.all()
        return render(request,'feedback.html', {'feedbacks': feedbacks})
from django.shortcuts import render
from .models import FeedBack


# Create your views here.
class FeedBackView(View):
    def get(self,request):
        feedbacks = Feedback.objects.all()
        return render(request,'feedback.html', {'feedbacks': feedbacks})
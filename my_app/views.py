from django.shortcuts import render
from .models import FeedBack


# Create your views here.
class FeedBackView(View):
    def get(self, request):
        feedbacks = FeedBack.objects.all()
        return render(request, 'feedback.html', {'feedbacks': feedbacks})

    def post(self, request):
        name = request.POST.get('name')
        feed_back_text = request.POST.get('feed_back_text')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        feedback = FeedBack(
            name=name,
            feed_back_text=feed_back_text,
            phone_number=phone_number,
            email=email
        )
        feedback.save()

        return render(request, 'feedback.html', {'message': 'Feedback submitted successfully!'})
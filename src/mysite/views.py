from django.shortcuts import render
from user.models import Profile


def home(request):
	profile = Profile.objects.all()

	context = { 'user' : profile }
	return render(request, 'index.html', context)
from django.shortcuts import render
from django.views.generic.base import View

class UploadPin(View):

	def get(self, request):
		return render(request, 'upload.html')

	def post(self, request):
		return render(request, 'upload.html')

class Pin(View):

	def get(self, request):
		return render(request, 'pin_index.html')
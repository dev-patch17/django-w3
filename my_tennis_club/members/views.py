from django.shortcuts import render
from django.http import HttpResponse

# members view
def members(request):
  return HttpResponse('Hello World!')
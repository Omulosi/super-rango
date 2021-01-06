import os

from django.http import HttpResponse
from django.shortcuts import render

from rango.models import *


def index(request):

    return HttpResponse("Rango")

from django.shortcuts import render
import math
from .models import UserPassModels


def function(request):
    song = request.GET.get('song')
    if song is not None:
        return render(request, 'some_html.html', {'this_key': 'You just submitted ' + song})
    else:
        return render(request, 'some_html.html')

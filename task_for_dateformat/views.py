from django.shortcuts import render
from .models import TestModel


def test_view(request):
    objects = TestModel.objects.all()
    return render(request, 'my_template.html', {'objects': objects})

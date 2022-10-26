from django.shortcuts import render, redirect
from .forms import FillInsForm
from .models import Story
from .helpers import myRange
import numpy as np
import random

# Create your views here.


def index(request):
    form = FillInsForm(request.POST or None)

    if form.is_valid():
        form.save()
        fields = list(form.cleaned_data.values())

        return get_randomLibs(request, fields)

    return render(request, 'madlibs/index.html', {'form': form})


def get_randomLibs(request, fields):
    ids = Story.objects.all().values_list('id', flat=True)
    id = np.array(ids)[random.randint(0, len(ids) - 1)]
    story = Story.objects.get(id=id)

    i = 0
    while i < len(fields):
        if story.story_content.__contains__('-') and i == len(fields) - 1:
            i = 0
        elif not story.story_content.__contains__('-'):
            break
        story.story_content = story.story_content.replace('-', fields[i], 1)
        i += 1

    context = {'story': story}
    return render(request, 'madlibs/random_libs.html', context)

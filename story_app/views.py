from django.shortcuts import render

# Create your views here.

from .gemini_utils import generate_story
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        temperature = float(request.POST.get('temperature'))
        story = generate_story(title, user_temperature=temperature)
        return render(request, 'story_app/index.html', {'story': story})
    else:
        return render(request, 'story_app/index.html')

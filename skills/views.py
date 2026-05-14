from django.shortcuts import render, get_object_or_404
from .models import Skill, Category

def index(request):
    skills = Skill.objects.all()
    categories = Category.objects.all()

    search_query = request.GET.get('search')
    category_id = request.GET.get('category')

    if search_query:
        skills = skills.filter(name__icontains=search_query)

    if category_id:
        skills = skills.filter(category_id=category_id)

    return render(request, 'skills/index.html', {
        'skills': skills,
        'categories': categories
    })


def skill_detail(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    return render(request, 'skills/detailskill.html', {'skill': skill})
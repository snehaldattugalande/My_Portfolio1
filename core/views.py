from django.shortcuts import render
from .models import Profile, Stat, SkillCategory, Project, Certification, SocialLink


def index(request):
    """Render the portfolio page with all data from the database."""
    profile = Profile.objects.first()
    stats = Stat.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.prefetch_related('technologies').all()
    certifications = Certification.objects.all()
    social_links = SocialLink.objects.all()

    context = {
        'profile': profile,
        'stats': stats,
        'skill_categories': skill_categories,
        'projects': projects,
        'certifications': certifications,
        'social_links': social_links,
    }
    return render(request, 'core/index.html', context)

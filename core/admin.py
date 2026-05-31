from django.contrib import admin
from .models import (
    Profile, Stat, SkillCategory, Skill,
    Project, ProjectTech, Certification, SocialLink
)


# ── Inlines ──────────────────────────────────────────────────────────────────

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ProjectTechInline(admin.TabularInline):
    model = ProjectTech
    extra = 1


class StatInline(admin.TabularInline):
    model = Stat
    extra = 1


# ── Model Admins ─────────────────────────────────────────────────────────────

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')
    fieldsets = (
        ('Hero Section', {
            'fields': ('name', 'title', 'subtitle', 'greeting_code', 'terminal_command', 'terminal_output', 'cta_text')
        }),
        ('About Section', {
            'fields': ('about_text', 'about_text_2')
        }),
        ('Contact & Links', {
            'fields': ('email', 'contact_message', 'resume_link', 'footer_text')
        }),
    )

    def has_add_permission(self, request):
        # Only allow one Profile to exist
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'icon_color', 'order')
    list_editable = ('order',)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    inlines = [SkillInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    inlines = [ProjectTechInline]
    fieldsets = (
        ('Project Info', {
            'fields': ('title', 'description', 'github_url', 'live_url', 'order')
        }),
        ('Project Image', {
            'fields': ('image', 'image_url'),
            'description': 'Upload an image file OR provide an external URL. Uploaded file takes priority.',
        }),
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'icon_color', 'order')
    list_editable = ('order',)
    fieldsets = (
        ('Certification Info', {
            'fields': ('title', 'issuer', 'verify_url', 'icon', 'icon_color', 'order')
        }),
        ('Certification Image', {
            'fields': ('image', 'image_url'),
            'description': 'Upload a badge/certificate image OR provide an external URL. Uploaded file takes priority.',
        }),
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'order')
    list_editable = ('order',)
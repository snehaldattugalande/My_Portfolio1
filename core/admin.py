from django.contrib import admin
from django.utils.html import mark_safe
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
    list_display = ('title', 'image_thumbnail', 'order')
    list_editable = ('order',)
    inlines = [ProjectTechInline]
    readonly_fields = ('image_preview',)
    fieldsets = (
        ('Project Info', {
            'fields': ('title', 'description', 'github_url', 'live_url', 'order')
        }),
        ('Project Image', {
            'fields': ('image', 'image_url', 'image_preview'),
            'description': 'Upload an image file OR provide an external URL. Uploaded file takes priority.',
        }),
    )

    def image_preview(self, obj):
        img_url = obj.get_image()
        if img_url:
            return mark_safe(f'<img src="{img_url}" style="max-height: 150px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />')
        return "No image uploaded or linked."
    image_preview.short_description = "Image Preview"

    def image_thumbnail(self, obj):
        img_url = obj.get_image()
        if img_url:
            return mark_safe(f'<img src="{img_url}" style="max-height: 40px; border-radius: 4px;" />')
        return "No Image"
    image_thumbnail.short_description = "Thumbnail"


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'image_thumbnail', 'icon_color', 'order')
    list_editable = ('order',)
    readonly_fields = ('image_preview',)
    fieldsets = (
        ('Certification Info', {
            'fields': ('title', 'issuer', 'verify_url', 'icon', 'icon_color', 'order')
        }),
        ('Certification Image', {
            'fields': ('image', 'image_url', 'image_preview'),
            'description': 'Upload a badge/certificate image OR provide an external URL. Uploaded file takes priority.',
        }),
    )

    def image_preview(self, obj):
        img_url = obj.get_image()
        if img_url:
            return mark_safe(f'<img src="{img_url}" style="max-height: 100px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />')
        return "No image uploaded or linked."
    image_preview.short_description = "Image Preview"

    def image_thumbnail(self, obj):
        img_url = obj.get_image()
        if img_url:
            return mark_safe(f'<img src="{img_url}" style="max-height: 40px; border-radius: 4px;" />')
        return "No Image"
    image_thumbnail.short_description = "Thumbnail"


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'order')
    list_editable = ('order',)
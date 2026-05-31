from django.db import models


class Profile(models.Model):
    """Main profile info — only one record should exist."""
    name = models.CharField(max_length=100, default="Snehal Galande")
    title = models.CharField(max_length=200, default="Data Engineer")
    subtitle = models.CharField(max_length=300, default="Building scalable architectures & intelligent pipelines.")
    greeting_code = models.CharField(max_length=100, default="// SNEHAL.INIT()", help_text="The terminal-style greeting text")
    terminal_command = models.CharField(max_length=100, default="./execute_intro.sh")
    terminal_output = models.CharField(max_length=300, default="Hello, world! I engineer data ecosystems.")
    about_text = models.TextField(
        default="I am a passionate Data Engineer focused on transforming raw data into actionable insights. "
                "I design, build, and maintain robust, scalable data architectures and processing pipelines."
    )
    about_text_2 = models.TextField(
        default="My expertise bridges the gap between software engineering and data science, "
                "ensuring data is reliable, accessible, and high-quality for downstream analytics and machine learning models.",
        blank=True
    )
    resume_link = models.URLField(blank=True, default="", help_text="URL to your resume (e.g. Google Drive link)")
    email = models.EmailField(default="hello@example.com")
    contact_message = models.TextField(
        default="I'm currently open for new opportunities to build scalable systems. "
                "Whether you have a question or just want to say hi, my inbox is always open!"
    )
    footer_text = models.CharField(max_length=100, default="v2.0.0 — Django Powered", blank=True)
    cta_text = models.CharField(max_length=50, default="Explore Pipelines", blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class Stat(models.Model):
    """Stats shown in the About section (e.g. 10TB+ Data Processed)."""
    icon = models.CharField(max_length=100, help_text="FontAwesome class, e.g. 'fa-solid fa-database'")
    icon_color = models.CharField(max_length=20, choices=[('blue', 'Neon Blue'), ('purple', 'Neon Purple')], default='blue')
    value = models.CharField(max_length=50, help_text="e.g. '10TB+' or '99.9%'")
    label = models.CharField(max_length=100, help_text="e.g. 'Data Processed'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.value} {self.label}"


class SkillCategory(models.Model):
    """A group of related skills (e.g. 'Core Languages')."""
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Individual skill tag within a category."""
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name


class Project(models.Model):
    """A featured project/pipeline."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField(blank=True, default="")
    live_url = models.URLField(blank=True, default="")
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text="Upload an image file for this project"
    )
    image_url = models.CharField(
        max_length=500,
        blank=True,
        default="",
        help_text="OR provide an external image URL (used if no file is uploaded)"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_image(self):
        """Returns uploaded image URL first, falls back to image_url field."""
        if self.image:
            return self.image.url
        return self.image_url or None

    def __str__(self):
        return self.title


class ProjectTech(models.Model):
    """Technology tag for a project."""
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies')

    class Meta:
        verbose_name_plural = "Project Technologies"

    def __str__(self):
        return self.name


class Certification(models.Model):
    """A certification with a verify link."""
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, help_text="FontAwesome class, e.g. 'fa-solid fa-code'")
    icon_color = models.CharField(max_length=20, choices=[('blue', 'Neon Blue'), ('purple', 'Neon Purple')], default='blue')
    verify_url = models.URLField(help_text="Link to verify the certification")
    image = models.ImageField(
        upload_to='certifications/',
        blank=True,
        null=True,
        help_text="Upload a badge/certificate image"
    )
    image_url = models.CharField(
        max_length=500,
        blank=True,
        default="",
        help_text="OR provide an external image URL (used if no file is uploaded)"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_image(self):
        """Returns uploaded image URL first, falls back to image_url field."""
        if self.image:
            return self.image.url
        return self.image_url or None

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    """Social media links shown in the contact section."""
    platform = models.CharField(max_length=100, help_text="e.g. 'GitHub', 'LinkedIn'")
    url = models.URLField()
    icon = models.CharField(max_length=100, help_text="FontAwesome class, e.g. 'fa-brands fa-github'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.platform
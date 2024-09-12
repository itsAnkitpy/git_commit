from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    TEXT_C = [
        ("Vim", "Vim"),
        ("EMACS", "EMACS"),
        ("VS Code", "VS Code"),
        ("Sublime Text", "Sublime Text"),
        ("Atom", "Atom"),
        ("PyCharm", "PyCharm"),
        ("Notepad++", "Notepad++"),
        ("Other", "Other")
    ]
    GENDER_C = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    OS_C = [
        ("Windows", "Windows"),
        ("MacOS", "MacOS"),
        ("Linux", "Linux"),
        ("Ubuntu", "Ubuntu"),
        ("Fedora", "Fedora"),
        ("Solaris", "Solaris"),
        ("Other", "Other")
    ]
    SPACES_C = [
        ("Tabs", "Tabs"),
        ("Spaces", "Spaces")
    ]
    TECH_STACK_CHOICES = [
        ('mean', 'MEAN'),
        ('mern', 'MERN'),
        ('ruby_on_rails', 'Ruby on Rails'),
        ('lamp', 'LAMP'),
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('csharp', 'C#'),
        ('cpp', 'C++'),
        ('ruby', 'Ruby'),
        ('php', 'PHP'),
        ('swift', 'Swift'),
        ('go', 'Go'),
        ('rust', 'Rust'),
        ('other', 'Other'),
    ]
    SEEKING_CHOICES = [
        ('relationship', 'Relationship'),
        ('casual', 'Casual'),
        ('figuring_out', 'Figuring Out'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=50, blank=True, null=True, choices=GENDER_C)
    profile_image = models.ImageField(upload_to='profile_pic', default="default.jpg", null=True, blank=True)
    bio = models.TextField(null=True)
    tech_stack = models.CharField(max_length=20, choices=TECH_STACK_CHOICES, default='',null=True, blank=True)
    editor = models.CharField(max_length=20, choices=TEXT_C, default=None, null=True, blank=True)
    os = models.CharField(max_length=10, choices=OS_C, default=None, null=True, blank=True)
    spacing = models.CharField(max_length=10, choices=SPACES_C, default=None, null=True, blank=True)
    likeability = models.ManyToManyField(User, related_name="likes", blank=True)
    blocked_by = models.ManyToManyField(User, related_name="blocked", blank=True)
    interests = models.TextField(blank=True, null=True, help_text="Enter your interests, separated by commas")
    seeking = models.CharField(max_length=20, choices=SEEKING_CHOICES, blank=True, null=True)
    languages = models.TextField(blank=True, null=True, help_text="List of languages known")

    def __str__(self):
        return f"{self.full_name} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 200 or img.width > 200:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

    @property
    def num_likes(self):
        return self.likeability.all().count()
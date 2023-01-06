# Generated by Django 4.1.5 on 2023-01-03 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, null=True)),
                ('profile_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pic')),
                ('bio', models.TextField(null=True)),
                ('tech_stack', models.CharField(max_length=500, null=True)),
                ('editor', models.CharField(blank=True, choices=[('Vim', 'Vim'), ('EMACS', 'EMACS')], default=None, max_length=5, null=True)),
                ('os', models.CharField(blank=True, choices=[('Windows', 'Windows'), ('Mac', 'Mac'), ('Linux', 'Linux')], default=None, max_length=10, null=True)),
                ('spacing', models.CharField(blank=True, choices=[('Tabs', 'Tabs'), ('Spaces', 'Spaces')], default=None, max_length=10, null=True)),
                ('blocked_by', models.ManyToManyField(blank=True, related_name='blocked', to=settings.AUTH_USER_MODEL)),
                ('likeability', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
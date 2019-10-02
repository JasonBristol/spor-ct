# Generated by Django 2.2.6 on 2019-10-02 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('severity', models.CharField(choices=[('info', 'Info'), ('warning', 'Warning'), ('success', 'Good'), ('danger', 'Bad')], default='info', max_length=10)),
                ('header', models.CharField(help_text='Plain text or HTML input is accepted.', max_length=25)),
                ('body', models.TextField(help_text='Plain text or HTML input is accepted.')),
                ('dismissable', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('image', models.ImageField(upload_to='images/banners')),
                ('caption', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BugCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=25)),
                ('value', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Bug Categories',
            },
        ),
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('description', models.TextField()),
                ('severity', models.CharField(choices=[('none', 'Non-Issue'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')], default='low', max_length=25)),
                ('notes', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('review', 'Review'), ('scheduled_fix', 'Scheduled Fix'), ('in_progress', 'In Progress'), ('fixed', 'Fixed'), ('closed', 'Closed'), ('blocked', 'Blocked')], default='review', max_length=25)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.BugCategory')),
            ],
            options={
                'verbose_name': 'Bug Report',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('hours', models.CharField(max_length=255)),
                ('google_map_url', models.CharField(blank=True, help_text='You can override the provided value, or set it blank to regenerate it', max_length=255, null=True)),
                ('facebook', models.BooleanField(default=False)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter', models.BooleanField(default=False)),
                ('twitter_url', models.URLField(blank=True)),
                ('linkedin', models.BooleanField(default=False)),
                ('linkedin_url', models.URLField(blank=True)),
                ('gplus', models.BooleanField(default=False)),
                ('gplus_url', models.URLField(blank=True)),
                ('primary_contact', models.BooleanField(default=False, help_text='Primary contacts will show up on our contact page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('question', models.CharField(help_text='Plain text or HTML input is accepted.', max_length=255)),
                ('answer', models.TextField(help_text='Plain text or HTML input is accepted.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='Modal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('severity', models.CharField(choices=[('default', 'Default'), ('info', 'Info'), ('warning', 'Warning'), ('success', 'Good'), ('danger', 'Bad')], default='default', max_length=10)),
                ('header', models.CharField(max_length=25)),
                ('body', models.TextField(help_text='Plain text or HTML input is accepted.')),
                ('popup', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(help_text='500x300 works the best', upload_to='images/customers')),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('title', models.CharField(default='Member', max_length=50)),
                ('thumbnail', models.ImageField(help_text='750x450 works the best', upload_to='images/team')),
                ('description', models.TextField()),
                ('date_joined', models.DateField(blank=True)),
                ('facebook', models.BooleanField(default=False)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter', models.BooleanField(default=False)),
                ('twitter_url', models.URLField(blank=True)),
                ('linkedin', models.BooleanField(default=False)),
                ('linkedin_url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Team Member',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KnownIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('tagline', models.CharField(help_text='Plain text or HTML input is accepted.', max_length=255)),
                ('description', models.TextField(help_text='Plain text or HTML input is accepted.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('reference_bug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.BugReport')),
            ],
            options={
                'verbose_name': 'Known Issue',
            },
        ),
    ]

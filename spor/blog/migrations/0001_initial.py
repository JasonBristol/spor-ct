# Generated by Django 2.2.6 on 2019-10-02 01:03

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Blog Post', max_length=50)),
                ('tagline', models.CharField(max_length=100)),
                ('body', models.TextField(help_text='You can include HTML markup in the post body')),
                ('thumbnail', models.ImageField(blank=True, help_text='900x300 works the best', upload_to='images/posts')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=25)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(help_text='Only change this if you know what you are doing', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Category')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag')),
            ],
        ),
    ]
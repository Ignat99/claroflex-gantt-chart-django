# Generated by Django 3.1.5 on 2021-05-04 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_auto_20210410_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name="Comment's text")),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmed')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted?')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projects.project', verbose_name='Related project')),
                ('user_left', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_comment', to=settings.AUTH_USER_MODEL, verbose_name='User left')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-17 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('wagtailcore', '0048_taskstate_finished_by'),
        ('wagtail_review', '0009_wagtail_workflow'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupReviewTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Task')),
                ('groups', models.ManyToManyField(help_text='Pages at this step in a workflow will be commented on or approved by these groups of users', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Review task',
                'verbose_name_plural': 'Review tasks',
            },
            bases=('wagtailcore.task',),
        ),
    ]

# Generated by Django 3.2 on 2023-09-10 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20230910_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='degree',
        ),
        migrations.AddField(
            model_name='degree',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.employee', verbose_name='degree'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.PositiveSmallIntegerField(choices=[(4, 'help desk'), (5, 'software developer'), (6, 'financial'), (7, 'operator')], default=4, verbose_name='job title'),
        ),
    ]

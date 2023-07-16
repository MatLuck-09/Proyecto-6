# Generated by Django 4.1.5 on 2023-07-16 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfil', '0007_alter_infopersonal_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='descripcion',
            field=models.TextField(default='Descripción predeterminada'),
        ),
        migrations.AddField(
            model_name='avatar',
            name='enlace',
            field=models.URLField(default='https://example.com'),
        ),
        migrations.AlterField(
            model_name='infopersonal',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='infopersonal',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

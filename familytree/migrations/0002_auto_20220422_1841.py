# Generated by Django 3.0 on 2022-04-22 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('familytree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_user', to='familytree.MyUser'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parant_user', to='familytree.MyUser'),
        ),
        migrations.AlterField(
            model_name='sibling',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='siblings_user', to='familytree.MyUser'),
        ),
    ]

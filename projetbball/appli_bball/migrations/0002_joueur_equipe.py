# Generated by Django 4.0.3 on 2022-05-06 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appli_bball', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joueur',
            name='equipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appli_bball.equipe'),
        ),
    ]
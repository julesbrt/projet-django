# Generated by Django 4.0.3 on 2022-05-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('ville', models.CharField(max_length=30)),
                ('datecrea', models.DateField()),
                ('proprio', models.CharField(max_length=30)),
                ('sponsor', models.CharField(max_length=30)),
                ('coach', models.CharField(max_length=30)),
                ('nbrtrophee', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomj', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('taille', models.CharField(max_length=30)),
                ('poids', models.CharField(max_length=30)),
                ('poste', models.CharField(max_length=30)),
                ('numero', models.CharField(max_length=30)),
                ('nbrtropheej', models.IntegerField(blank=True)),
            ],
        ),
    ]

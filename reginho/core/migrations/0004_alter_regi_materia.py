# Generated by Django 4.0.4 on 2022-07-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_conter_regi_conteudo_regi_link_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regi',
            name='materia',
            field=models.CharField(choices=[('Matematica', 'matematica'), ('Física', 'fisica'), ('Biologia', 'biologia'), ('Química', 'quimica')], max_length=15),
        ),
    ]

# Generated by Django 5.2.1 on 2025-06-09 22:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_alter_aluno_data_final_alter_aluno_data_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_final',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 6, 9, 22, 32, 0, 403292, tzinfo=datetime.timezone.utc), help_text='Informe a data final do aluno', null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_inicial',
            field=models.DateField(default=datetime.datetime(2025, 6, 9, 22, 32, 0, 403292, tzinfo=datetime.timezone.utc), help_text='Informe a data de inicio do aluno'),
        ),
    ]

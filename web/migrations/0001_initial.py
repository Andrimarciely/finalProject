# Generated by Django 4.2 on 2023-05-06 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inital_date', models.DateField(help_text='data inicial')),
                ('final_date', models.DateField(help_text='data final')),
                ('responsible_technician', models.CharField(help_text='responsável técnico', max_length=80, verbose_name='técnico')),
                ('description', models.CharField(help_text='visita, coleta, ou relatório?', max_length=100, verbose_name='descrição')),
                ('priority', models.CharField(choices=[('0', 'Sem prioridade'), ('1', 'Normal'), ('2', 'Urgente'), ('3', 'Muito Urgente')], max_length=1, verbose_name='prioridade')),
                ('oppened_status', models.BooleanField(default=True, help_text='aberto ou fechado?', verbose_name='status')),
            ],
        ),
    ]

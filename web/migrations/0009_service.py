# Generated by Django 4.2 on 2024-11-18 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Descrição de Serviço', max_length=200, verbose_name='descricao de serviço')),
                ('price', models.DecimalField(decimal_places=2, help_text='valor do serviço', max_digits=10, verbose_name='preço')),
                ('matrix', models.ForeignKey(help_text='Tipo de matriz associada ao serviço', on_delete=django.db.models.deletion.CASCADE, to='web.matrix', verbose_name='tipo de matriz')),
            ],
        ),
    ]

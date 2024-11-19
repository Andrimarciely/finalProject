# Generated by Django 4.2 on 2024-11-19 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_proposal_client_nickname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='client',
            field=models.ForeignKey(blank=True, help_text='Cliente associado à proposta', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='web.client', verbose_name='cliente'),
        ),
    ]

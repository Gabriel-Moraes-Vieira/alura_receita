# Generated by Django 4.1.5 on 2023-02-14 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0006_alter_receita_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='imagem_receita',
        ),
    ]

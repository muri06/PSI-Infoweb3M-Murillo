# Generated by Django 5.1.3 on 2024-11-05 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categoria', models.CharField(max_length=100, verbose_name='null=False')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produto', models.CharField(max_length=100, verbose_name='null=False')),
                ('destaque', models.BooleanField(verbose_name='default=True')),
                ('promocao', models.BooleanField(verbose_name='default=True')),
                ('msgpromocao', models.CharField(max_length=100, verbose_name='null=True')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('criado_em', models.DateTimeField()),
                ('alterado_em', models.DateTimeField()),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categoria', to='loja.categoria')),
                ('fabricante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fabricante', to='loja.fabricante')),
            ],
        ),
    ]

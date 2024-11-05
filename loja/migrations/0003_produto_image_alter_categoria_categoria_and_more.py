# Generated by Django 5.1.3 on 2024-11-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_categoria_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='Categoria',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='alterado_em',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='Fabricante',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='alterado_em',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='Produto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='produto',
            name='alterado_em',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='destaque',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='msgpromocao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='promocao',
            field=models.BooleanField(default=True),
        ),
    ]

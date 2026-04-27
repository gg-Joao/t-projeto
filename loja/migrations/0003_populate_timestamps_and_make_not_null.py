from django.db import migrations, models
import django.utils.timezone


def populate_timestamps(apps, schema_editor):
    Categoria = apps.get_model('loja', 'Categoria')
    Fabricante = apps.get_model('loja', 'Fabricante')
    Produto = apps.get_model('loja', 'Produto')
    now = django.utils.timezone.now()
    Categoria.objects.filter(created_at__isnull=True).update(created_at=now)
    Categoria.objects.filter(updated_at__isnull=True).update(updated_at=now)
    Fabricante.objects.filter(created_at__isnull=True).update(created_at=now)
    Fabricante.objects.filter(updated_at__isnull=True).update(updated_at=now)
    Produto.objects.filter(created_at__isnull=True).update(created_at=now)
    Produto.objects.filter(updated_at__isnull=True).update(updated_at=now)


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_remove_produto_descricao_categoria_created_at_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_timestamps, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='categoria',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='produto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

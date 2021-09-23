# Generated by Django 3.1.1 on 2021-09-23 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Componentes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='almacenamiento',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='coolercpu',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='fuentepoder',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='gabinete',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='gpu',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='placamadre',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='procesador',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='nombre',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='build',
            name='cooler',
            field=models.ForeignKey(blank=True, default='default', null=True, on_delete=django.db.models.deletion.CASCADE, to='Componentes.coolercpu'),
        ),
        migrations.AlterField(
            model_name='build',
            name='disco0',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='Componentes.almacenamiento'),
        ),
        migrations.AlterField(
            model_name='build',
            name='fuente',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='Componentes.fuentepoder'),
        ),
        migrations.AlterField(
            model_name='build',
            name='gabinete',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='Componentes.gabinete'),
        ),
        migrations.AlterField(
            model_name='build',
            name='memoria',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='Componentes.ram'),
        ),
        migrations.AlterField(
            model_name='build',
            name='placamadre',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='Componentes.placamadre'),
        ),
        migrations.AlterField(
            model_name='build',
            name='procesador',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='Componentes.procesador'),
        ),
        migrations.AlterField(
            model_name='build',
            name='tarjetavideo',
            field=models.ForeignKey(blank=True, default='default', null=True, on_delete=django.db.models.deletion.CASCADE, to='Componentes.gpu'),
        ),
    ]
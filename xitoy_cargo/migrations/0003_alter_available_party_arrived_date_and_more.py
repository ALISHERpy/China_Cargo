# Generated by Django 5.0.4 on 2024-04-10 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xitoy_cargo', '0002_available_party_key_trek_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available_party',
            name='arrived_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='chine_db',
            name='id_raqam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xitoy_cargo.key'),
        ),
        migrations.AlterField(
            model_name='chine_db',
            name='trek_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chine_db', to='xitoy_cargo.trek'),
        ),
        migrations.AlterField(
            model_name='uzbek_db',
            name='id_raqam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xitoy_cargo.key'),
        ),
        migrations.AlterField(
            model_name='uzbek_db',
            name='trek_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uzbek_db', to='xitoy_cargo.trek'),
        ),
    ]
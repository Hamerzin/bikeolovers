# Generated by Django 4.0 on 2022-12-04 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_rename_user_id_bikegroupsmodel_user_menber_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bikegroupsmodel',
            old_name='name',
            new_name='name_group',
        ),
    ]
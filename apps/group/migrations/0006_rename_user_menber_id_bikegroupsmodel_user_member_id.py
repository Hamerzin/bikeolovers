# Generated by Django 4.0 on 2022-12-04 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_rename_name_bikegroupsmodel_name_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bikegroupsmodel',
            old_name='user_menber_id',
            new_name='user_member_id',
        ),
    ]
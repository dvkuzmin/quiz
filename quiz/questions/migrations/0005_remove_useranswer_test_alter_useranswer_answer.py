# Generated by Django 4.1.4 on 2022-12-15 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_useranswer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='test',
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.answer'),
        ),
    ]

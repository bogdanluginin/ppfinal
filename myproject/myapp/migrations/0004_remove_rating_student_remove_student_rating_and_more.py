# Generated by Django 4.2.7 on 2023-11-22 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_alter_rating_options_alter_student_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rating",
            name="student",
        ),
        migrations.RemoveField(
            model_name="student",
            name="rating",
        ),
        migrations.AddField(
            model_name="student",
            name="value",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_rating",
                to="myapp.rating",
            ),
        ),
    ]

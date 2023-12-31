# Generated by Django 4.2.7 on 2023-11-22 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_remove_rating_student_remove_student_rating_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="value",
        ),
        migrations.AddField(
            model_name="rating",
            name="student",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ratings",
                to="myapp.student",
            ),
        ),
    ]

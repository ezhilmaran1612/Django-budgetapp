# Generated by Django 2.1.7 on 2019-02-22 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='expense',
            name='category',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='project',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.AddField(
            model_name='expenses',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.Category'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='budget.Project'),
        ),
    ]

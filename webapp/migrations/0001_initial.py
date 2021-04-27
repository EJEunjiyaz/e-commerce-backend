# Generated by Django 2.2 on 2021-04-27 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField(max_length=512)),
                ('datetime_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('rating_person', models.PositiveIntegerField()),
                ('sold', models.PositiveIntegerField()),
                ('datetime_query', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Product')),
            ],
        ),
    ]

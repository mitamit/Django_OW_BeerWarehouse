# Generated by Django 3.0.5 on 2020-04-28 17:17

import beers.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('abv', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Alcohol by volume')),
                ('is_filtered', models.BooleanField(default=False, verbose_name='Is filtered')),
                ('color', models.PositiveIntegerField(choices=[(1, 'yellow'), (2, 'black'), (3, 'amber'), (4, 'brown')], default=1, verbose_name='Color')),
                ('image', models.ImageField(blank=True, null=True, upload_to=beers.utils.image_upload_location, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'beer',
                'verbose_name_plural': 'beers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EspecialIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('beers', models.ManyToManyField(blank=True, null=True, related_name='especial_ingredients', to='beers.Beer')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='beers_especialingredients_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='beers_especialingredients_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'verbose_name': 'Especial ingredient',
                'verbose_name_plural': 'Especial ingredients',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('tax_number', models.IntegerField(unique=True, verbose_name='Tax number')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='beers_company_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='beers_company_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='beer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='beers', to='beers.Company'),
        ),
        migrations.AddField(
            model_name='beer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='beers_beer_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='beer',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='beers_beer_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
    ]

# Generated by Django 3.2.9 on 2023-10-08 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'brand',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'flavor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'db_table': 'ingredient',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=45, null=True)),
                ('promotion', models.IntegerField()),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('brand', models.ForeignKey(db_column='brand', on_delete=django.db.models.deletion.CASCADE, to='back_app.brand')),
                ('category', models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, to='back_app.category')),
                ('flavor', models.ForeignKey(db_column='flavor', on_delete=django.db.models.deletion.CASCADE, to='back_app.flavor')),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'role',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StockDisponible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_disponible', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'stock_disponible',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TypeContenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_contenant', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'type_contenant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=500, null=True)),
                ('role', models.ForeignKey(db_column='role', on_delete=django.db.models.deletion.DO_NOTHING, to='back_app.role')),
            ],
            options={
                'db_table': 'user',
                'managed': True,
                'unique_together': {('id', 'role')},
            },
        ),
        migrations.CreateModel(
            name='ProductIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back_app.ingredient')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back_app.product')),
            ],
            options={
                'db_table': 'product_ingredient',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(related_name='products', through='back_app.ProductIngredient', to='back_app.Ingredient'),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_disponible',
            field=models.ForeignKey(db_column='stock_disponible', on_delete=django.db.models.deletion.CASCADE, to='back_app.stockdisponible'),
        ),
        migrations.AddField(
            model_name='product',
            name='type_contenant',
            field=models.ForeignKey(db_column='type_contenant', on_delete=django.db.models.deletion.CASCADE, to='back_app.typecontenant'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateTimeField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='back_app.user')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
                'unique_together': {('id', 'user')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('id', 'flavor', 'type_contenant', 'brand', 'stock_disponible', 'category')},
        ),
        migrations.CreateModel(
            name='LineOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('order', models.ForeignKey(db_column='order', on_delete=django.db.models.deletion.CASCADE, to='back_app.order')),
                ('product', models.ForeignKey(db_column='product', on_delete=django.db.models.deletion.CASCADE, to='back_app.product')),
            ],
            options={
                'db_table': 'line_order',
                'managed': True,
                'unique_together': {('id', 'product', 'order')},
            },
        ),
    ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed=True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "role"


class StockDisponible(models.Model):
    stock_disponible = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "stock_disponible"


class Flavor(models.Model):
    flavor = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = "flavor"


class Category(models.Model):
    category = models.CharField(max_length=400)

    class Meta:
        managed = True
        db_table = "category"


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "ingredient"


class Brand(models.Model):
    brand = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "brand"


class User(models.Model):
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column="role")

    class Meta:
        managed = True
        db_table = "user"
        unique_together = (("id", "role"),)


class TypeContenant(models.Model):
    type_contenant = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "type_contenant"


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)
    flavor = models.ForeignKey(Flavor, db_column="flavor", on_delete=models.CASCADE)
    type_contenant = models.ForeignKey(
        "TypeContenant", db_column="type_contenant", on_delete=models.CASCADE
    )
    brand = models.ForeignKey(Brand, db_column="brand", on_delete=models.CASCADE)
    promotion = models.IntegerField()
    stock_disponible = models.ForeignKey(
        StockDisponible, db_column="stock_disponible", on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category, db_column="category", on_delete=models.CASCADE
    )
    quantity = models.FloatField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, through="ProductIngredient")

    class Meta:
        managed = True
        db_table = "product"
        unique_together = (
            ("id", "flavor", "type_contenant", "brand", "stock_disponible", "category"),
        )


class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "product_ingredient"


class Order(models.Model):
    date_order = models.DateTimeField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "order"
        unique_together = (("id", "user"),)


class LineOrder(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    product = models.ForeignKey(Product, db_column="product", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, db_column="order", on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "line_order"
        unique_together = (("id", "product", "order"),)

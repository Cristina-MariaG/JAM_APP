# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    role = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "role"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    role = models.ForeignKey("Role", models.DO_NOTHING, db_column="role")

    class Meta:
        managed = True
        db_table = "User"
        unique_together = (("id", "role"),)


class Brand(models.Model):
    id_brand = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "brand"


class Category(models.Model):
    id_category = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=400)

    class Meta:
        managed = True
        db_table = "category"


class Flavor(models.Model):
    id_flavor = models.AutoField(primary_key=True)
    flavor = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = "flavor"
        unique_together = (("id_flavor", "flavor"),)


class Ingredient(models.Model):
    id_ingredient = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "ingredient"


class StockDisponible(models.Model):
    id_stock_disponible = models.AutoField(primary_key=True)
    stock_disponible = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "stock_disponible"


class TypeContenant(models.Model):
    id_type_contenant = models.AutoField(primary_key=True)
    type_contenant = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "type_contenant"


class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)
    flavor = models.ForeignKey(Flavor, models.DO_NOTHING, db_column="flavor")
    type_contenant = models.ForeignKey(
        "TypeContenant", models.DO_NOTHING, db_column="type_contenant"
    )
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    promotion = models.IntegerField()
    stock_disponible = models.ForeignKey(
        "StockDisponible", models.DO_NOTHING, db_column="stock_disponible"
    )
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column="category")

    class Meta:
        managed = True
        db_table = "product"


class ProductHasIngredient(models.Model):
    product = models.OneToOneField(
        Product, models.DO_NOTHING, db_column="product", primary_key=True
    )
    ingredient = models.ForeignKey(
        Ingredient, models.DO_NOTHING, db_column="ingredient"
    )

    class Meta:
        managed = True
        db_table = "product_has_ingredient"


class LineOrder(models.Model):
    id_line_order = models.AutoField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    product = models.ForeignKey("Product", models.DO_NOTHING, db_column="product")
    order = models.ForeignKey("Order", models.DO_NOTHING, db_column="order")

    class Meta:
        managed = True
        db_table = "line_order"
        unique_together = (("id_line_order", "product", "order"),)


class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    date_order = models.DateTimeField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column="user")

    class Meta:
        managed = True
        db_table = "order"
        unique_together = (("id_order", "user"),)

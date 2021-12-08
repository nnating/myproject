# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Companys(models.Model):
    # company_id = models.IntegerField(primary_key=True)
    #自增
    company_id = models.AutoField(primary_key=True)
    company_name = models.TextField(blank=True, null=True)
    company_logo = models.TextField(blank=True, null=True)
    system_name = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companys'
        ordering = ['company_id']


class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_no = models.TextField(blank=True, null=True)
    department_name = models.TextField(blank=True, null=True)
    is_storage = models.BigIntegerField(blank=True, null=True)
    level = models.BigIntegerField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Galleries(models.Model):
    gallery_id = models.BigAutoField(primary_key=True)
    image = models.TextField(blank=True, null=True)
    image_no = models.TextField(blank=True, null=True)
    image_thumb = models.TextField(blank=True, null=True)
    modify_time = models.DateTimeField()
    sku = models.TextField(blank=True, null=True)
    user_info = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'galleries'
        unique_together = (('gallery_id', 'modify_time'),)


class Permissions(models.Model):
    permission_id = models.BigAutoField(primary_key=True)
    permission_name = models.TextField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    menu_type = models.BigIntegerField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    sort = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class Roles(models.Model):
    role_id = models.BigAutoField(primary_key=True)
    role_name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    permissions = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    role_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_no = models.TextField(blank=True, null=True)
    user_name = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    department_id = models.BigIntegerField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    mobile = models.TextField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    role_ids = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        ordering = ['user_id']


class WorkOrderDetails(models.Model):
    work_order_detail_id = models.BigAutoField(primary_key=True)
    work_order_id = models.BigIntegerField(blank=True, null=True)
    work_order_no = models.TextField(blank=True, null=True)
    customer_no = models.TextField(blank=True, null=True)
    department_id = models.BigIntegerField(blank=True, null=True)
    warehouse_no = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    import_time = models.DateTimeField()
    label = models.TextField(blank=True, null=True)
    new_sku = models.TextField(blank=True, null=True)
    old_sku = models.TextField(blank=True, null=True)
    number = models.BigIntegerField(blank=True, null=True)
    print_number = models.BigIntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    stock_no = models.TextField(blank=True, null=True)
    tag1 = models.TextField(blank=True, null=True)
    tag2 = models.TextField(blank=True, null=True)
    tag3 = models.TextField(blank=True, null=True)
    user_info = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_order_details'
        unique_together = (('work_order_detail_id', 'import_time'),)


class WorkOrderPrints(models.Model):
    work_order_print_id = models.BigAutoField(primary_key=True)
    work_order_detail_id = models.BigIntegerField(blank=True, null=True)
    work_order_id = models.BigIntegerField(blank=True, null=True)
    work_order_no = models.TextField(blank=True, null=True)
    department_id = models.BigIntegerField(blank=True, null=True)
    customer_no = models.TextField(blank=True, null=True)
    stock_no = models.TextField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    number = models.BigIntegerField(blank=True, null=True)
    print_number = models.BigIntegerField(blank=True, null=True)
    new_sku = models.TextField(blank=True, null=True)
    old_sku = models.TextField(blank=True, null=True)
    print_time = models.DateTimeField()
    label = models.TextField(blank=True, null=True)
    tag1 = models.TextField(blank=True, null=True)
    tag2 = models.TextField(blank=True, null=True)
    tag3 = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user_info = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_order_prints'
        unique_together = (('work_order_print_id', 'print_time'),)


class WorkOrders(models.Model):
    work_order_id = models.BigAutoField(primary_key=True)
    work_order_no = models.TextField(blank=True, null=True)
    department_id = models.BigIntegerField(blank=True, null=True)
    warehouse_no = models.TextField(blank=True, null=True)
    import_time = models.DateTimeField()
    level = models.TextField(blank=True, null=True)
    sku_kind = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    user_info = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_orders'
        unique_together = (('work_order_id', 'import_time'),)


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
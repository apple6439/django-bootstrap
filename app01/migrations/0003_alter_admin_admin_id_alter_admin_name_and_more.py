# Generated by Django 5.1.2 on 2024-11-24 05:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='admin_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='管理员ID'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='name',
            field=models.CharField(max_length=100, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=128, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='部门ID'),
        ),
        migrations.AlterField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_departments', to='app01.employee', verbose_name='部门负责人'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, verbose_name='部门名称'),
        ),
        migrations.AlterField(
            model_name='department',
            name='parent_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_departments', to='app01.department', verbose_name='上级部门'),
        ),
        migrations.AlterField(
            model_name='department',
            name='performance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='部门业绩'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='app01.department', verbose_name='所属部门'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='员工ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('male', '男性'), ('female', '女性')], max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='薪资'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=100, verbose_name='客户名称'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_image',
            field=models.ImageField(upload_to='product_images/', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.CharField(max_length=100, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='订单数量'),
        ),
    ]

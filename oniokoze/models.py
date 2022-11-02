from django.db import models

class Spot(models.Model):

    capital=models.TextField(verbose_name='都道府県',blank=True,null=False)
    city=models.TextField(verbose_name='市区町村',blank=True,null=False)
    address=models.TextField(verbose_name='番地以降',blank=True,null=False)
    place=models.TextField(verbose_name='場所',blank=True,null=False)
    location=models.TextField(verbose_name='ロケーション',blank=True,null=False)
    fish=models.TextField(verbose_name='釣れる魚',blank=True,null=True)
    spotURL=models.URLField(verbose_name='URL',blank=True,null=True)
    free=models.TextField(verbose_name='自由記入欄',blank=True,null=True)
    created_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    updated_at=models.DateTimeField(verbose_name='更新日時',auto_now=True)

class Catch(models.Model):

    name=models.TextField(verbose_name='魚種',blank=True,null=False)
    photo=models.ImageField(verbose_name='写真',blank=True,null=False)
    capital=models.TextField(verbose_name='都道府県',blank=True,null=True)
    city=models.TextField(verbose_name='市区町村',blank=True,null=True)
    address=models.TextField(verbose_name='番地以降',blank=True,null=True)
    size=models.IntegerField(verbose_name='番地以降',blank=True,null=True)
    place=models.TextField(verbose_name='場所',blank=True,null=True)
    location=models.TextField(verbose_name='ロケーション',blank=True,null=True)
    free = models.TextField(verbose_name='自由記入欄', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
# Create your models here.

class Recipe(models.Model):

    method=models.TextField(verbose_name='魚種',blank=True,null=False)
    title=models.TextField(verbose_name='魚種',blank=True,null=False)
    material=models.TextField(verbose_name='魚種',blank=True,null=False)
    procedure=models.TextField(verbose_name='魚種',blank=True,null=False)
    shopphoto=models.ImageField(verbose_name='魚種',blank=True,null=False)
    shopURL=models.URLField(verbose_name='魚種',blank=True,null=False)
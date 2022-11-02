from django.db import models

class Spot(models.Model):

    CAPITALS = (
        ('北海道','北海道'),
        ('青森県','青森県'),
        ('岩手県','岩手県'),
        ('宮城県','宮城県'),
        ('秋田県','秋田県'),
        ('山形県','山形県'),
        ('福島県','福島県'),
        ('茨城県','茨城県'),
        ('栃木県','栃木県'),
        ('群馬県','群馬県'),
        ('埼玉県','埼玉県'),
        ('千葉県','千葉県'),
        ('東京都','東京都'),
        ('神奈川県','神奈川県'),
        ('新潟県','新潟県'),
        ('富山県','富山県'),
        ('石川県','石川県'),
        ('福井県','福井県'),
        ('山梨県','山梨県'),
        ('長野県','長野県'),
        ('岐阜県','岐阜県'),
        ('静岡県','静岡県'),
        ('愛知県','愛知県'),
        ('三重県','三重県'),
        ('滋賀県','滋賀県'),
        ('京都府','京都府'),
        ('大阪府','大阪府'),
        ('兵庫県','兵庫県'),
        ('奈良県','奈良県'),
        ('和歌山県','和歌山県'),
        ('鳥取県','鳥取県'),
        ('島根県','島根県'),
        ('岡山県','岡山県'),
        ('広島県','広島県'),
        ('山口県','山口県'),
        ('徳島県','徳島県'),
        ('香川県','香川県'),
        ('愛媛県','愛媛県'),
        ('高知県','高知県'),
        ('福岡県','福岡県'),
        ('佐賀県','佐賀県'),
        ('長崎県','長崎県'),
        ('熊本県','熊本県'),
        ('大分県','大分県'),
        ('宮崎県','宮崎県'),
        ('鹿児島県','鹿児島県'),
        ('沖縄県','沖縄県')
    )

    capital=models.TextField(choices=CAPITALS,verbose_name='都道府県',blank=True,null=False)
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
    LOCATIONS=(
        ('海','海'),
        ('川','川'),
        ('管理釣り場','管理釣り場'),
        ('船','船'),
        ('湖','湖'),
        ('その他','その他')
    )
    name=models.TextField(verbose_name='魚種',blank=True)
    photo=models.ImageField(verbose_name='写真',blank=True)
    capital=models.TextField(verbose_name='都道府県',blank=True,null=True)
    city=models.TextField(verbose_name='市区町村',blank=True,null=True)
    address=models.TextField(verbose_name='番地以降',blank=True,null=True)
    size=models.IntegerField(verbose_name='番地以降',blank=True,null=True)
    place=models.TextField(verbose_name='場所',blank=True,null=True)
    location=models.TextField(choices=LOCATIONS,verbose_name='ロケーション',blank=True,null=True)
    free = models.TextField(verbose_name='自由記入欄', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
# Create your models here.

# class Recipe(models.Model):
#
#     method=models.TextField(verbose_name='分類',blank=True,null=False)
#     title=models.TextField(verbose_name='タイトル',blank=True,null=False)
#     material=models.TextField(verbose_name='',blank=True,null=False)
#     procedure=models.TextField(verbose_name='魚種',blank=True,null=False)
#     shopphoto=models.ImageField(verbose_name='魚種',blank=True,null=False)
#     shopURL=models.URLField(verbose_name='魚種',blank=True,null=False)
from accounts.models import CustomUser
from django.db import models

# Create your models here.
class Catch(models.Model):
    # """釣果テーブル"""
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
        ('沖縄県','沖縄県'),
    )
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    name1 = models.TextField(verbose_name='魚種1', blank=True, )
    name2 = models.TextField(verbose_name='魚種2', blank=True, null=True)
    name3 = models.TextField(verbose_name='魚種3', blank=True, null=True)
    name4 = models.TextField(verbose_name='魚種4', blank=True, null=True)
    name5 = models.TextField(verbose_name='魚種5', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    photo4 = models.ImageField(verbose_name='写真4', blank=True, null=True)
    photo5 = models.ImageField(verbose_name='写真5', blank=True, null=True)
    size1 = models.IntegerField(verbose_name='サイズ1', blank=True, )
    size2 = models.IntegerField(verbose_name='サイズ2', blank=True, null=True)
    size3 = models.IntegerField(verbose_name='サイズ3', blank=True, null=True)
    size4 = models.IntegerField(verbose_name='サイズ4', blank=True, null=True)
    size5 = models.IntegerField(verbose_name='サイズ5', blank=True, null=True)
    capital = models.CharField(choices=CAPITALS,verbose_name="都道府県",max_length=5)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    class Meta:
        verbose_name_plural = 'Catch'

    def __str__(self):
        return self.title

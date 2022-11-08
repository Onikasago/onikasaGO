from accounts.models import CustomUser
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

    capital=models.TextField(choices=CAPITALS,verbose_name='都道府県',blank=True)
    city=models.TextField(verbose_name='市区町村',blank=True)
    address=models.TextField(verbose_name='番地以降',blank=True)
    place=models.TextField(verbose_name='釣り場名',blank=True)
    location=models.TextField(verbose_name='ロケーション',blank=True)
    spotURL=models.URLField(verbose_name='URL',blank=True,null=True)
    URLcheck = models.IntegerField(verbose_name='URLチェック',blank=True,null=True)
    free=models.TextField(verbose_name='自由記入欄',blank=True,null=True)
    beginner = models.BooleanField(verbose_name='初心者おすすめチェック',default=False, help_text='初心者おすすめ',blank=True,null=True)
    created_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    updated_at=models.DateTimeField(verbose_name='更新日時',auto_now=True)
    class Meta:
        verbose_name_plural = 'Spot'

    def __str__(self):
        return self.title
class Catch(models.Model):
    LOCATIONS=(
        ('海','海'),
        ('川','川'),
        ('管理釣り場','管理釣り場'),
        ('船','船'),
        ('湖','湖'),
        ('その他','その他')
    )
    capital=models.TextField(verbose_name='都道府県',blank=True,null=True)
    city=models.TextField(verbose_name='市区町村',blank=True,null=True)
    address=models.TextField(verbose_name='番地以降',blank=True,null=True)
    place=models.TextField(verbose_name='場所',blank=True,null=True)
    location=models.TextField(choices=LOCATIONS,verbose_name='ロケーション',blank=True,null=True)
    free = models.TextField(verbose_name='自由記入欄', blank=True, null=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザーID', on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    class Meta:
        verbose_name_plural = 'Catch'

    def __str__(self):
        return self.title
class Recipe(models.Model):

     method=models.TextField(verbose_name='分類',blank=True,null=True)
     title=models.TextField(verbose_name='タイトル',blank=True,null=True)
     shopphoto=models.ImageField(verbose_name='お店の写真',blank=True,null=True)
     shopURL=models.URLField(verbose_name='お店のURL',blank=True,null=True)
     iinecount = models.TextField(verbose_name='いいね総数', blank=True, null=True)
     URLcheck = models.TextField(verbose_name='URL確認チェック', blank=True, null=True)
     titlephoto = models.ImageField(verbose_name='タイトル写真',blank=True,null=True)
     titlemovie = models.TextField(verbose_name='タイトル動画',blank=True,null=True)
     user = models.ForeignKey(CustomUser, verbose_name='ユーザーID', on_delete=models.PROTECT)
     created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
     updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
     class Meta:
        verbose_name_plural = 'Recipe'

     def __str__(self):
        return self.title
class Order(models.Model):
    recipeID = models.ForeignKey(Recipe, verbose_name='レシピID', on_delete=models.PROTECT)
    order = models.IntegerField(verbose_name='順番',blank=True)
    procedure = models.IntegerField(verbose_name='手順',blank=True)
    photo = models.IntegerField(verbose_name='写真',blank=True)
    material = models.IntegerField(verbose_name='材料',blank=True)
    amount = models.IntegerField(verbose_name='量',blank=True)
    unit = models.IntegerField(verbose_name='単位',blank=True)
    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.title


class Fishname(models.Model):
    catchID = models.ForeignKey(Catch,verbose_name='釣果ID', on_delete=models.PROTECT)
    name = models.TextField(verbose_name='魚種', blank=True)
    size = models.IntegerField(verbose_name='サイズ', blank=True)
    No = models.IntegerField(verbose_name='種類数', blank=True)

class Fish(models.Model):
    spotID = models.ForeignKey(Spot,verbose_name='釣り場ID',on_delete=models.PROTECT)
    fish = models.IntegerField(verbose_name='釣れる魚',blank=True)
    No = models.IntegerField(verbose_name='番号',blank=True)

class Iine(models.Model):
    userID = models.ForeignKey(CustomUser, verbose_name='ユーザーID', on_delete=models.PROTECT,blank=True,null=True)
    catchID = models.ForeignKey(Catch,verbose_name='釣果ID', on_delete=models.PROTECT,blank=True,null=True)
    recipeID = models.ForeignKey(Recipe, verbose_name='レシピID', on_delete=models.PROTECT,blank=True,null=True)
    spotID = models.ForeignKey(Spot,verbose_name='釣り場ID',on_delete=models.PROTECT,blank=True,null=True)


class Trivia(models.Model):
    trivia = models.TextField(verbose_name='豆知識',blank=True)
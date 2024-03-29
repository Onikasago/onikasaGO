from accounts.models import CustomUser
from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Catch(models.Model):
    CAPITALS = (
        ('北海道', '北海道'),
        ('青森県', '青森県'),
        ('岩手県', '岩手県'),
        ('宮城県', '宮城県'),
        ('秋田県', '秋田県'),
        ('山形県', '山形県'),
        ('福島県', '福島県'),
        ('茨城県', '茨城県'),
        ('栃木県', '栃木県'),
        ('群馬県', '群馬県'),
        ('埼玉県', '埼玉県'),
        ('千葉県', '千葉県'),
        ('東京都', '東京都'),
        ('神奈川県', '神奈川県'),
        ('新潟県', '新潟県'),
        ('富山県', '富山県'),
        ('石川県', '石川県'),
        ('福井県', '福井県'),
        ('山梨県', '山梨県'),
        ('長野県', '長野県'),
        ('岐阜県', '岐阜県'),
        ('静岡県', '静岡県'),
        ('愛知県', '愛知県'),
        ('三重県', '三重県'),
        ('滋賀県', '滋賀県'),
        ('京都府', '京都府'),
        ('大阪府', '大阪府'),
        ('兵庫県', '兵庫県'),
        ('奈良県', '奈良県'),
        ('和歌山県', '和歌山県'),
        ('鳥取県', '鳥取県'),
        ('島根県', '島根県'),
        ('岡山県', '岡山県'),
        ('広島県', '広島県'),
        ('山口県', '山口県'),
        ('徳島県', '徳島県'),
        ('香川県', '香川県'),
        ('愛媛県', '愛媛県'),
        ('高知県', '高知県'),
        ('福岡県', '福岡県'),
        ('佐賀県', '佐賀県'),
        ('長崎県', '長崎県'),
        ('熊本県', '熊本県'),
        ('大分県', '大分県'),
        ('宮崎県', '宮崎県'),
        ('鹿児島県', '鹿児島県'),
        ('沖縄県', '沖縄県')
    )

    LOCATIONS = (
        ('海', '海'),
        ('川', '川'),
        ('管理釣り場', '管理釣り場'),
        ('船', '船'),
        ('湖', '湖'),
        ('その他', 'その他')
    )


    nametitle = models.TextField(verbose_name='釣果タイトル')
    photo1 = models.ImageField(verbose_name='写真1')
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    photo4 = models.ImageField(verbose_name='写真4', blank=True, null=True)
    photo5 = models.ImageField(verbose_name='写真5', blank=True, null=True)
    capital = models.CharField(choices=CAPITALS, verbose_name='都道府県', blank=True,max_length=5)
    city = models.CharField(verbose_name='市区町村', max_length=10)
    address = models.CharField(verbose_name='番地以降', max_length=30)
    place = models.CharField(verbose_name='釣り場', max_length=50)
    location = models.CharField(choices=LOCATIONS,verbose_name='ロケーション', max_length=5)
    free = models.TextField(verbose_name='自由記入欄',blank=True,null=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザID', on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.nametitle
        # return str(self.nametitle)+self.capital

class Fishname(models.Model):
    name = models.CharField(verbose_name='魚種',max_length=50 ,blank=True, null=True)

    size = models.DecimalField(verbose_name='サイズ', max_digits=6, decimal_places=1, blank=True, null=True,validators=[MinValueValidator(0)])
    no = models.IntegerField(verbose_name='種類数', blank=True, null=True)
    catch = models.ForeignKey(Catch, on_delete = models.CASCADE, related_name='fishname')

class Spot(models.Model):
    CAPITALS = (
        ('北海道', '北海道'),
        ('青森県', '青森県'),
        ('岩手県', '岩手県'),
        ('宮城県', '宮城県'),
        ('秋田県', '秋田県'),
        ('山形県', '山形県'),
        ('福島県', '福島県'),
        ('茨城県', '茨城県'),
        ('栃木県', '栃木県'),
        ('群馬県', '群馬県'),
        ('埼玉県', '埼玉県'),
        ('千葉県', '千葉県'),
        ('東京都', '東京都'),
        ('神奈川県', '神奈川県'),
        ('新潟県', '新潟県'),
        ('富山県', '富山県'),
        ('石川県', '石川県'),
        ('福井県', '福井県'),
        ('山梨県', '山梨県'),
        ('長野県', '長野県'),
        ('岐阜県', '岐阜県'),
        ('静岡県', '静岡県'),
        ('愛知県', '愛知県'),
        ('三重県', '三重県'),
        ('滋賀県', '滋賀県'),
        ('京都府', '京都府'),
        ('大阪府', '大阪府'),
        ('兵庫県', '兵庫県'),
        ('奈良県', '奈良県'),
        ('和歌山県', '和歌山県'),
        ('鳥取県', '鳥取県'),
        ('島根県', '島根県'),
        ('岡山県', '岡山県'),
        ('広島県', '広島県'),
        ('山口県', '山口県'),
        ('徳島県', '徳島県'),
        ('香川県', '香川県'),
        ('愛媛県', '愛媛県'),
        ('高知県', '高知県'),
        ('福岡県', '福岡県'),
        ('佐賀県', '佐賀県'),
        ('長崎県', '長崎県'),
        ('熊本県', '熊本県'),
        ('大分県', '大分県'),
        ('宮崎県', '宮崎県'),
        ('鹿児島県', '鹿児島県'),
        ('沖縄県', '沖縄県')
    )

    LOCATIONS = (
        ('海', '海'),
        ('川', '川'),
        ('管理釣り場', '管理釣り場'),
        ('船', '船'),
        ('湖', '湖'),
        ('その他', 'その他')
    )

    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)
    capital = models.CharField(choices=CAPITALS, verbose_name='都道府県', blank=True,max_length=5)
    city = models.CharField(verbose_name='市区町村',max_length=50, blank=True)
    address = models.CharField(verbose_name='番地以降',max_length=50, blank=True)
    place = models.CharField(verbose_name='釣り場',max_length=50, blank=True)
    free = models.TextField(verbose_name='自由記入欄', blank=True, null=True)
    spotURL = models.URLField(verbose_name='URL記入欄', blank=True, null=True)
    location = models.CharField(choices=LOCATIONS, verbose_name='ロケーション',blank=True, null=True, max_length=5)
    beginner = models.BooleanField(verbose_name='初心者おすすめチェック',default=False, help_text='初心者おすすめ',blank=True,null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Spot'
    def __str__(self):
        return self.place

class Recipe(models.Model):

    CHOICE_TUPLE=(
        ("調理", "調理"),
        ("処理", "処理"),
        ("豆知識", "豆知識"),
    )

    method = models.TextField(choices=CHOICE_TUPLE,verbose_name='分類', blank=True)
    title = models.CharField(verbose_name='タイトル',max_length=100)
    shopphoto = models.ImageField(verbose_name='お店の写真', blank=True, null=True)
    shopURL = models.URLField(verbose_name='お店のURL', blank=True, null=True)
    titlephoto = models.ImageField(verbose_name='タイトル写真', blank=True, null=True)
    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Recipe'

    def __str__(self):
        return self.title



class Order(models.Model):
    order = models.IntegerField(verbose_name='順番')
    procedure = models.CharField(verbose_name='手順',max_length=100 , blank=True, null=True)
    material = models.CharField(verbose_name='材料',max_length=30 , blank=True, null=True)
    amount = models.DecimalField(verbose_name='量', max_digits=6,decimal_places=2, blank=True, null=True,validators=[MinValueValidator(0)])
    unit = models.CharField(verbose_name='単位',max_length=32 , blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE,related_name='order')

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.procedure




class Fish(models.Model):
    fish = models.CharField(verbose_name='釣れる魚',max_length=50, blank=True, null=True)
    no = models.IntegerField(verbose_name='番号', blank=True, null=True)
    spot = models.ForeignKey(Spot, on_delete = models.CASCADE,related_name='fish')

    class Meta:
        verbose_name_plural = 'Fish'

    def __str__(self):
        return self.fish

class Trivia(models.Model):
    trivia = models.TextField(verbose_name='豆知識', blank=True, null=True)
    kind = models.TextField(verbose_name='分類')

class LikeForSpot(models.Model):
    """投稿に対するいいね"""
    target = models.ForeignKey(Spot, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

class LikeForCatch(models.Model):
    """投稿に対するいいね"""
    target = models.ForeignKey(Catch, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

class LikeForRecipe(models.Model):
    """投稿に対するいいね"""
    target = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)



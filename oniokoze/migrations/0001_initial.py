# Generated by Django 3.2.7 on 2023-01-30 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nametitle', models.TextField(verbose_name='釣果タイトル')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真4')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真5')),
                ('capital', models.CharField(blank=True, choices=[('北海道', '北海道'), ('青森県', '青森県'), ('岩手県', '岩手県'), ('宮城県', '宮城県'), ('秋田県', '秋田県'), ('山形県', '山形県'), ('福島県', '福島県'), ('茨城県', '茨城県'), ('栃木県', '栃木県'), ('群馬県', '群馬県'), ('埼玉県', '埼玉県'), ('千葉県', '千葉県'), ('東京都', '東京都'), ('神奈川県', '神奈川県'), ('新潟県', '新潟県'), ('富山県', '富山県'), ('石川県', '石川県'), ('福井県', '福井県'), ('山梨県', '山梨県'), ('長野県', '長野県'), ('岐阜県', '岐阜県'), ('静岡県', '静岡県'), ('愛知県', '愛知県'), ('三重県', '三重県'), ('滋賀県', '滋賀県'), ('京都府', '京都府'), ('大阪府', '大阪府'), ('兵庫県', '兵庫県'), ('奈良県', '奈良県'), ('和歌山県', '和歌山県'), ('鳥取県', '鳥取県'), ('島根県', '島根県'), ('岡山県', '岡山県'), ('広島県', '広島県'), ('山口県', '山口県'), ('徳島県', '徳島県'), ('香川県', '香川県'), ('愛媛県', '愛媛県'), ('高知県', '高知県'), ('福岡県', '福岡県'), ('佐賀県', '佐賀県'), ('長崎県', '長崎県'), ('熊本県', '熊本県'), ('大分県', '大分県'), ('宮崎県', '宮崎県'), ('鹿児島県', '鹿児島県'), ('沖縄県', '沖縄県')], max_length=5, verbose_name='都道府県')),
                ('city', models.CharField(max_length=10, verbose_name='市区町村')),
                ('address', models.CharField(max_length=30, verbose_name='番地以降')),
                ('place', models.CharField(max_length=50, verbose_name='釣り場')),
                ('location', models.CharField(choices=[('海', '海'), ('川', '川'), ('管理釣り場', '管理釣り場'), ('船', '船'), ('湖', '湖'), ('その他', 'その他')], max_length=5, verbose_name='ロケーション')),
                ('free', models.TextField(blank=True, null=True, verbose_name='自由記入欄')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザID')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.TextField(blank=True, choices=[('調理', '調理'), ('処理', '処理'), ('豆知識', '豆知識')], verbose_name='分類')),
                ('title', models.TextField(verbose_name='タイトル')),
                ('shopphoto', models.ImageField(blank=True, null=True, upload_to='', verbose_name='お店の写真')),
                ('shopURL', models.URLField(blank=True, null=True, verbose_name='お店のURL')),
                ('titlephoto', models.ImageField(blank=True, null=True, upload_to='', verbose_name='タイトル写真')),
                ('titlemovie', models.URLField(blank=True, null=True, verbose_name='タイトル動画')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': 'Recipe',
            },
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trivia', models.TextField(blank=True, null=True, verbose_name='豆知識')),
                ('kind', models.TextField(verbose_name='分類')),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.CharField(blank=True, choices=[('北海道', '北海道'), ('青森県', '青森県'), ('岩手県', '岩手県'), ('宮城県', '宮城県'), ('秋田県', '秋田県'), ('山形県', '山形県'), ('福島県', '福島県'), ('茨城県', '茨城県'), ('栃木県', '栃木県'), ('群馬県', '群馬県'), ('埼玉県', '埼玉県'), ('千葉県', '千葉県'), ('東京都', '東京都'), ('神奈川県', '神奈川県'), ('新潟県', '新潟県'), ('富山県', '富山県'), ('石川県', '石川県'), ('福井県', '福井県'), ('山梨県', '山梨県'), ('長野県', '長野県'), ('岐阜県', '岐阜県'), ('静岡県', '静岡県'), ('愛知県', '愛知県'), ('三重県', '三重県'), ('滋賀県', '滋賀県'), ('京都府', '京都府'), ('大阪府', '大阪府'), ('兵庫県', '兵庫県'), ('奈良県', '奈良県'), ('和歌山県', '和歌山県'), ('鳥取県', '鳥取県'), ('島根県', '島根県'), ('岡山県', '岡山県'), ('広島県', '広島県'), ('山口県', '山口県'), ('徳島県', '徳島県'), ('香川県', '香川県'), ('愛媛県', '愛媛県'), ('高知県', '高知県'), ('福岡県', '福岡県'), ('佐賀県', '佐賀県'), ('長崎県', '長崎県'), ('熊本県', '熊本県'), ('大分県', '大分県'), ('宮崎県', '宮崎県'), ('鹿児島県', '鹿児島県'), ('沖縄県', '沖縄県')], max_length=5, verbose_name='都道府県')),
                ('city', models.TextField(blank=True, verbose_name='市区町村')),
                ('address', models.TextField(blank=True, verbose_name='番地以降')),
                ('place', models.TextField(blank=True, verbose_name='釣り場')),
                ('free', models.TextField(blank=True, null=True, verbose_name='自由記入欄')),
                ('URLcheck', models.CharField(blank=True, max_length=1, null=True, verbose_name='URLチェック')),
                ('spotURL', models.URLField(blank=True, null=True, verbose_name='URL記入欄')),
                ('location', models.CharField(blank=True, choices=[('海', '海'), ('川', '川'), ('管理釣り場', '管理釣り場'), ('船', '船'), ('湖', '湖'), ('その他', 'その他')], max_length=5, null=True, verbose_name='ロケーション')),
                ('beginner', models.BooleanField(blank=True, default=False, help_text='初心者おすすめ', null=True, verbose_name='初心者おすすめチェック')),
                ('spotfish', models.TextField(blank=True, verbose_name='釣れる魚')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Spot',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='順番')),
                ('procedure', models.TextField(blank=True, null=True, verbose_name='手順')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('material', models.TextField(blank=True, null=True, verbose_name='材料')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='量')),
                ('unit', models.TextField(blank=True, null=True, verbose_name='単位')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oniokoze.recipe')),
            ],
            options={
                'verbose_name_plural': 'Order',
            },
        ),
        migrations.CreateModel(
            name='LikeForSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oniokoze.spot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeForRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oniokoze.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeForCatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oniokoze.catch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.TextField(choices=[('北海道', '北海道'), ('青森県', '青森県'), ('岩手県', '岩手県'), ('宮城県', '宮城県'), ('秋田県', '秋田県'), ('山形県', '山形県'), ('福島県', '福島県'), ('茨城県', '茨城県'), ('栃木県', '栃木県'), ('群馬県', '群馬県'), ('埼玉県', '埼玉県'), ('千葉県', '千葉県'), ('東京都', '東京都'), ('神奈川県', '神奈川県'), ('新潟県', '新潟県'), ('富山県', '富山県'), ('石川県', '石川県'), ('福井県', '福井県'), ('山梨県', '山梨県'), ('長野県', '長野県'), ('岐阜県', '岐阜県'), ('静岡県', '静岡県'), ('愛知県', '愛知県'), ('三重県', '三重県'), ('滋賀県', '滋賀県'), ('京都府', '京都府'), ('大阪府', '大阪府'), ('兵庫県', '兵庫県'), ('奈良県', '奈良県'), ('和歌山県', '和歌山県'), ('鳥取県', '鳥取県'), ('島根県', '島根県'), ('岡山県', '岡山県'), ('広島県', '広島県'), ('山口県', '山口県'), ('徳島県', '徳島県'), ('香川県', '香川県'), ('愛媛県', '愛媛県'), ('高知県', '高知県'), ('福岡県', '福岡県'), ('佐賀県', '佐賀県'), ('長崎県', '長崎県'), ('熊本県', '熊本県'), ('大分県', '大分県'), ('宮崎県', '宮崎県'), ('鹿児島県', '鹿児島県'), ('沖縄県', '沖縄県')], verbose_name='都道府県')),
                ('city', models.TextField(blank=True, verbose_name='市区町村')),
                ('address', models.TextField(blank=True, verbose_name='番地以降')),
                ('place', models.TextField(blank=True, verbose_name='釣り場')),
                ('free', models.TextField(blank=True, null=True, verbose_name='自由記入欄')),
                ('spotURL', models.URLField(blank=True, null=True, verbose_name='URL記入欄')),
                ('location', models.CharField(blank=True, choices=[('海', '海'), ('川', '川'), ('管理釣り場', '管理釣り場'), ('船', '船'), ('湖', '湖'), ('その他', 'その他')], max_length=5, null=True)),
                ('beginner', models.BooleanField(blank=True, default=False, help_text='初心者おすすめ', null=True, verbose_name='初心者おすすめチェック')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザID')),
            ],
            options={
                'verbose_name_plural': 'Fishname',
            },
        ),
        migrations.CreateModel(
            name='Fishname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='魚種')),
                ('size', models.IntegerField(blank=True, null=True, verbose_name='サイズ')),
                ('no', models.IntegerField(blank=True, null=True, verbose_name='種類数')),
                ('catch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fishname', to='oniokoze.catch')),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish', models.TextField(blank=True, null=True, verbose_name='釣れる魚')),
                ('no', models.IntegerField(blank=True, null=True, verbose_name='番号')),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oniokoze.spot')),
            ],
            options={
                'verbose_name_plural': 'Fish',
            },
        ),
    ]

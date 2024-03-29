# Generated by Django 3.2.7 on 2023-02-10 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oniokoze', '0002_alter_recipe_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catch',
            name='address',
            field=models.CharField(max_length=30, verbose_name='番地以降'),
        ),
        migrations.AlterField(
            model_name='catch',
            name='capital',
            field=models.CharField(blank=True, choices=[('北海道', '北海道'), ('青森県', '青森県'), ('岩手県', '岩手県'), ('宮城県', '宮城県'), ('秋田県', '秋田県'), ('山形県', '山形県'), ('福島県', '福島県'), ('茨城県', '茨城県'), ('栃木県', '栃木県'), ('群馬県', '群馬県'), ('埼玉県', '埼玉県'), ('千葉県', '千葉県'), ('東京都', '東京都'), ('神奈川県', '神奈川県'), ('新潟県', '新潟県'), ('富山県', '富山県'), ('石川県', '石川県'), ('福井県', '福井県'), ('山梨県', '山梨県'), ('長野県', '長野県'), ('岐阜県', '岐阜県'), ('静岡県', '静岡県'), ('愛知県', '愛知県'), ('三重県', '三重県'), ('滋賀県', '滋賀県'), ('京都府', '京都府'), ('大阪府', '大阪府'), ('兵庫県', '兵庫県'), ('奈良県', '奈良県'), ('和歌山県', '和歌山県'), ('鳥取県', '鳥取県'), ('島根県', '島根県'), ('岡山県', '岡山県'), ('広島県', '広島県'), ('山口県', '山口県'), ('徳島県', '徳島県'), ('香川県', '香川県'), ('愛媛県', '愛媛県'), ('高知県', '高知県'), ('福岡県', '福岡県'), ('佐賀県', '佐賀県'), ('長崎県', '長崎県'), ('熊本県', '熊本県'), ('大分県', '大分県'), ('宮崎県', '宮崎県'), ('鹿児島県', '鹿児島県'), ('沖縄県', '沖縄県')], max_length=4, verbose_name='都道府県'),
        ),
        migrations.AlterField(
            model_name='catch',
            name='city',
            field=models.CharField(max_length=50, verbose_name='市区町村'),
        ),
        migrations.AlterField(
            model_name='catch',
            name='free',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='自由記入欄'),
        ),
        migrations.AlterField(
            model_name='catch',
            name='nametitle',
            field=models.CharField(max_length=50, verbose_name='釣果タイトル'),
        ),
        migrations.AlterField(
            model_name='catch',
            name='place',
            field=models.CharField(max_length=50, verbose_name='釣り場'),
        ),
        migrations.AlterField(
            model_name='fish',
            name='fish',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='釣れる魚'),
        ),
        migrations.AlterField(
            model_name='fishname',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='魚種'),
        ),
        migrations.AlterField(
            model_name='order',
            name='material',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='材料'),
        ),
        migrations.AlterField(
            model_name='order',
            name='procedure',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='手順'),
        ),
        migrations.AlterField(
            model_name='order',
            name='unit',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='単位'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='address',
            field=models.CharField(max_length=50, verbose_name='番地以降'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='capital',
            field=models.CharField(choices=[('北海道', '北海道'), ('青森県', '青森県'), ('岩手県', '岩手県'), ('宮城県', '宮城県'), ('秋田県', '秋田県'), ('山形県', '山形県'), ('福島県', '福島県'), ('茨城県', '茨城県'), ('栃木県', '栃木県'), ('群馬県', '群馬県'), ('埼玉県', '埼玉県'), ('千葉県', '千葉県'), ('東京都', '東京都'), ('神奈川県', '神奈川県'), ('新潟県', '新潟県'), ('富山県', '富山県'), ('石川県', '石川県'), ('福井県', '福井県'), ('山梨県', '山梨県'), ('長野県', '長野県'), ('岐阜県', '岐阜県'), ('静岡県', '静岡県'), ('愛知県', '愛知県'), ('三重県', '三重県'), ('滋賀県', '滋賀県'), ('京都府', '京都府'), ('大阪府', '大阪府'), ('兵庫県', '兵庫県'), ('奈良県', '奈良県'), ('和歌山県', '和歌山県'), ('鳥取県', '鳥取県'), ('島根県', '島根県'), ('岡山県', '岡山県'), ('広島県', '広島県'), ('山口県', '山口県'), ('徳島県', '徳島県'), ('香川県', '香川県'), ('愛媛県', '愛媛県'), ('高知県', '高知県'), ('福岡県', '福岡県'), ('佐賀県', '佐賀県'), ('長崎県', '長崎県'), ('熊本県', '熊本県'), ('大分県', '大分県'), ('宮崎県', '宮崎県'), ('鹿児島県', '鹿児島県'), ('沖縄県', '沖縄県')], max_length=4, verbose_name='都道府県'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='city',
            field=models.CharField(max_length=30, verbose_name='市区町村'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='free',
            field=models.TextField(blank=True, null=True, verbose_name='自由記入欄'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='place',
            field=models.CharField(max_length=40, verbose_name='釣り場'),
        ),
    ]

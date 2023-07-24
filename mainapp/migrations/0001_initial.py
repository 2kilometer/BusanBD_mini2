from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('dis_rank', models.CharField(max_length=500)),
                ('dis_code', models.CharField(max_length=500)),
                ('dis_top', models.CharField(max_length=300)),
                ('dis_m_num', models.IntegerField(max_length=10)),
                ('dis_middle', models.CharField(max_length=300)),
                ('dis_id', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('dis_age1', models.CharField(max_length=50)),
                ('dis_age2', models.CharField(max_length=50)),
                ('dis_age3', models.CharField(max_length=50)),
                ('dis_gender', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'disease',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('prod_name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('prod_eff', models.CharField(max_length=1000)),
                ('prod_m_num', models.IntegerField(max_length=10)),
                ('prod_middle', models.CharField(max_length=300)),
                ('prod_min', models.CharField(max_length=300)),
                ('prod_max', models.CharField(max_length=300)),
                ('prod_unit', models.CharField(max_length=300)),
                ('prod_warn', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'prod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userdis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ud_id', models.CharField(max_length=50)),
                ('ud_dis', models.CharField(max_length=50)),
                ('ud_middle', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'userdis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(max_length=20)),
                ('user_age', models.CharField(max_length=15)),
                ('user_gender', models.CharField(max_length=15)),
                ('user_stress', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]

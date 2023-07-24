from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField
from django.db.models.fields import DateField 

# Create your models here.
class Users (models.Model) :
    user_id = CharField (primary_key=True, max_length=50, null=False)
    user_pw = CharField (max_length=20, null=False)
    user_age = CharField (max_length=15, null=False)
    user_gender = CharField (max_length=15, null=False)
    user_stress = CharField (max_length=30, null=False)
    
    class Meta :
        db_table = "users"
        app_label = "mainapp"
        managed = False
        
class Disease (models.Model) :
    dis_rank = CharField (max_length=500, null=False)
    dis_code = CharField (max_length=500, null=False)
    dis_top = CharField (max_length=300, null=False)
    dis_m_num = IntegerField (max_length=10 ,null=False)
    dis_middle = CharField (max_length=300, null=False)
    dis_id = CharField (primary_key=True, max_length=1000, null=False)
    dis_age1 = CharField (max_length=50, null=False)
    dis_age2 = CharField (max_length=50, null=False)
    dis_age3 = CharField (max_length=50, null=False)
    dis_gender = CharField (max_length=10)
    
    class Meta :
        db_table = "disease"
        app_label = "mainapp"
        managed = False
        
class Prod (models.Model) :
    prod_name = CharField (primary_key=True, max_length=1000, null=False)
    prod_eff = CharField (max_length=1000, null=False)
    prod_m_num = IntegerField (max_length=10 ,null=False)
    prod_middle = CharField (max_length=300, null=False)
    prod_min = CharField (max_length=300, null=False)
    prod_max = CharField (max_length=300, null=False)
    prod_unit = CharField (max_length=300, null=False)
    prod_warn = CharField (max_length=1000, null=False)
    
    class Meta :
        db_table = "prod"
        app_label = "mainapp"
        managed = False
        
class Userdis (models.Model) :
    ud_id = CharField (max_length=50, null=False)
    ud_dis = CharField (max_length=50, null=False)
    ud_middle = CharField (max_length=50, null=False)
    
    class Meta :
        db_table = "userdis"
        app_label = "mainapp"
        managed = False
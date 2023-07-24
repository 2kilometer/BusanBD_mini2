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
    prod_id = CharField (primary_key=True, max_length=10, null=False)
    prod_name = CharField (max_length=40, null=False)
    prod_lgu = CharField (max_length=4, null=False)
    prod_cost = IntegerField (null=False)
    prod_price = IntegerField (null=False)
    prod_sale = IntegerField (null=False)
    
    class Meta :
        db_table = "prod"
        app_label = "mainapp"
        managed = False
        
class Userdis (models.Model) :
    ud_id = CharField (primary_key=True, max_length=50, null=False)
    ud_dis = CharField (max_length=50, null=False)
    ud_middle = CharField (max_length=50, null=False)
    
    class Meta :
        db_table = "lprod"
        app_label = "mainapp"
        managed = False
        
class CartMember (models.Model) :
    # FK
    ### ForeignKey() : 부모클래스 (테이블)과 관계 (Join) 맺기 (연결하기)
    # - 첫번째 값 : 부모 클래스 (테이블) 이름
    # - 두번째 값 : 부모 클래스 (테이블)의 PK 변수 (컬럼)명 지정
    # - 세번째 값 : 자식 클래스 (테이블)의 FK 변수 (컬럼)명 지정
    # - 네번째 값 : on_delete -> 부모 클래스 (테이블)의 정보 삭제시 허락할 것인지 여부
    #           : PROTECT -> 자식이 있는 부모 클래스 (테이블)의 정보가 삭제될 수 없도록 함
    #           : CASCADE -> 자식이 있는 부모 클래스 (테이블)의 정보가 삭제될 수 있도록 함
    cart_member = models.ForeignKey(Member,
                                    to_field="mem_id",
                                    db_column="cart_member",
                                    on_delete=models.PROTECT)
   
    # PK
    cart_no = CharField (primary_key=True, max_length=13, null=False)
    
    # FK & PK
    cart_prod = CharField (max_length=10, null=False)
    cart_qty = IntegerField (null=False)
    
    class Meta :
        db_table = "cart"
        app_label = "oracleapp"
        managed = False

class CartMemberProd (models.Model) :

    cart_member = models.ForeignKey(Member,
                                    to_field="mem_id",
                                    db_column="cart_member",
                                    on_delete=models.PROTECT)

    cart_no = CharField (primary_key=True, max_length=13, null=False)
    
    cart_prod = models.ForeignKey(Prod,
                                  to_field="prod_id",
                                  db_column="cart_prod",
                                  on_delete=models.PROTECT)

    cart_qty = IntegerField (null=False)
    
    class Meta :
        db_table = "cart"
        app_label = "oracleapp"
        managed = False
        
class ProdLprod (models.Model) :
    prod_id = CharField (primary_key=True, max_length=10, null=False)
    prod_name = CharField (max_length=40, null=False)
    prod_lgu = models.ForeignKey (Lprod,
                                  to_field="lprod_gu",
                                  db_column="prod_lgu",
                                  on_delete=models.PROTECT)
    prod_cost = IntegerField (null=False)
    prod_price = IntegerField (null=False)
    prod_sale = IntegerField (null=False)
    
    class Meta :
        db_table = "prod"
        app_label = "oracleapp"
        managed = False
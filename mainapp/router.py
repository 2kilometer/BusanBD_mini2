### Database 추가시 아래 클래스를 APP에 router.py 추가해야함
# - return or db에는 : oracle 입력(settings.py에 설정하 DB 이름)
# - app_label에는 : oracleapp 이름 지정
class DBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label=='oracleapp':
            return'oracle'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label=='oracleapp':
            return'oracle'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label=='oracleapp'or\
            obj2._meta.app_label=='oracleapp':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label=='oracleapp':
            return db=='oracle'
        return None

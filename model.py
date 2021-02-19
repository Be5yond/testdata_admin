import configparser
from peewee import MySQLDatabase, Model 
from peewee import CharField, PrimaryKeyField, TextField, IntegerField
from playhouse.shortcuts import model_to_dict


config = configparser.ConfigParser()
config.read('config.ini')
db_cfg = dict(config.items('db'))

db=MySQLDatabase(db_cfg['db'], user=db_cfg['username'], password=db_cfg['password'], host=db_cfg['host'], port=3306)


class TestData(Model):
    id = PrimaryKeyField()
    title = CharField()
    description = CharField(default='')
    epic = CharField()
    method = CharField()
    precondition = TextField()
    step = TextField()
    schema = TextField()
    module = IntegerField()

    class Meta:
        database = db 
        table_name = 'tb_testdata'

    def to_dict(self):
        return model_to_dict(self)


if __name__ == "__main__":
    ret = TestData.select().limit(1)
    
    ret = TestData.select(TestData.module).group_by(TestData.module)
    breakpoint()
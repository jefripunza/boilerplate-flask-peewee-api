import datetime

from peewee import *
from src.utils.database import BaseModel

from src.models import Users

class ProductCategories(BaseModel):
    class Meta:
        db_table = 'product_categories'

    id = AutoField()
    name = CharField(null=False)
    created_by = ForeignKeyField(Users, column_name='created_by')
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(null=True)
    deleted_at = DateTimeField(null=True)
    is_show = BooleanField(default=True)

    def new(name, created_by):
        try:
            ProductCategories.create(
                name=name,
                created_by=created_by,
            )
            return True
        except Exception as e:
            print(e)
            return False

    def show_all():
        res = ProductCategories \
            .select(
                ProductCategories.id,
                ProductCategories.name,
            ) \
            .where(
                (ProductCategories.is_show == True) & ProductCategories.deleted_at == None
            ) \
            .dicts()
        return list(res)

    def is_exist(name):
        try:
            return ProductCategories.get(
                (ProductCategories.name == name)
            )
        except:
            return False

    def is_exist_by_id(id):
        try:
            return ProductCategories.get(
                (ProductCategories.id == id)
            )
        except:
            return False

    def update_by_id(id, name):
        try:
            ProductCategories.update(
                    name=name,
                ).where(
                    (ProductCategories.id == id)
                ).execute()
            return True
        except Exception as e:
            print(e)
            return False

    def show_by_id(id, is_show):
        try:
            ProductCategories.update(
                    is_show=is_show,
                ).where(
                    (ProductCategories.id == id)
                ).execute()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_by_id(id):
        try:
            ProductCategories.update(
                    deleted_at=datetime.datetime.now,
                ) \
                .where(
                    (ProductCategories.id == id)
                ).execute()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_by_name(name):
        try:
            ProductCategories.update(
                    deleted_at=datetime.datetime.now,
                ) \
                .where(
                    (ProductCategories.name == name)
                ).execute()
            return True
        except Exception as e:
            print(e)
            return False

import importlib
from decimal import Decimal

from sqlalchemy.orm import declarative_base
from tornado.options import options

sqlalchemy_orm = None
sqlalchemy_util_compat = None
try:
    sqlalchemy_orm = importlib.import_module("sqlalchemy.orm")
    sqlalchemy_util_compat = importlib.import_module("sqlalchemy.util.compat")
except ImportError as e:
    raise Exception(f"sqlalchemy is not exist,run:pip install sqlalchemy==1.4.36")


class SqlAlchemyHelper:
    def __init__(self, pool):
        """
        初始化sql工具
        :param pool: 连接池名称
        """
        if isinstance(pool, str):
            self.pool, self.conn_info = options.database[pool]
        else:
            self.pool = pool

    @sqlalchemy_util_compat.contextmanager
    def make_session(self, **kwargs):
        db_session = sqlalchemy_orm.scoped_session(sqlalchemy_orm.sessionmaker(bind=self.pool, **kwargs))
        session = db_session()
        yield session
        session.commit()
        session.close()


def alchemy_default_to_dict(params, data, repetition=False):
    data_list = []
    key_list = []
    if repetition:
        for arg in params:
            if arg.key:
                key_list.append(arg.key)
            else:
                key_list.append(arg.name)
    else:
        for arg in params:
            arg = str(arg)
            if "(" in arg and ")" in arg:
                key_list.append(arg.split(".")[-1][:-1])
            else:
                key_list.append(arg.split(".")[-1])
    if isinstance(data, list):
        for d in data:
            dict_data = dict(zip(key_list, d))
            data_list.append(dict_data)
        return data_list
    else:
        if data:
            return dict(zip(key_list, data))
        else:
            return {}


def sqlalchemy_paging(Query, limit_number, offset_number):
    data_list = Query.limit(limit_number).offset(offset_number).all()
    data_count = Query.count()
    return {"count": data_count, "dataSource": data_list}


def covert_relationship_property(attr, attr_value):
    if attr.__class__.__name__ == 'ColumnProperty':
        return attr_value
    elif attr.__class__.__name__ == 'RelationshipProperty':
        attrs = []
        for ar, ar_value in attr.mapper.attrs.items():
            if ar_value.__class__.__name__ == 'ColumnProperty' and ar not in attrs:
                attrs.append(ar)
        if attr_value.__class__.__name__ == 'InstrumentedList':
            new_data = []
            for item in attr_value:
                info = dict()
                for ar in attrs:
                    new_attr_value = getattr(item, ar)
                    if not item.__class__.__name__ == 'RelationshipProperty':
                        info[ar] = new_attr_value
                    else:
                        info = covert_relationship_property(ar, new_attr_value)
                new_data.append(info)
            return new_data
        else:
            new_data = dict()
            for column, value in attr.entity.attrs.items():
                if not value.__class__.__name__ == 'RelationshipProperty':
                    new_data[column] = getattr(attr_value, column)
            return new_data
    else:
        return attr_value


def query_set_to_dict(obj):
    if hasattr(obj, "__mapper__"):
        obj_dict = {}
        mapper = obj.__mapper__
        if hasattr(mapper, "attrs"):
            attrs = mapper.attrs
            for column, attr in attrs.items():
                attr_value = getattr(obj, column)
                value = covert_relationship_property(attr, attr_value)
                if not value.__class__.__name__ == 'RelationshipProperty':
                    obj_dict[column] = value

        return obj_dict
    elif hasattr(obj, "keys"):
        return {key: getattr(obj, key) for key in obj.keys()}
    else:
        return dict(obj)


def query_set_to_list(query_set):
    ret_list = []
    for obj in query_set:
        ret_dict = query_set_to_dict(obj)
        ret_list.append(ret_dict)
    return ret_list


def result_to_json(data):
    if isinstance(data, list):
        return query_set_to_list(data)
    else:
        return query_set_to_dict(data)


def result_page(query, page_num=1, page_size=10):
    offset_number = (page_num - 1) * page_size if page_num >= 1 else 0
    data_list = result_to_json(query.limit(page_size).offset(offset_number).all())
    data_count = query.count()
    return {"count": data_count, "dataSource": data_list}

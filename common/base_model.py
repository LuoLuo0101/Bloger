# -*- coding: utf-8 -*-
# @Time    : 18-1-15 上午11:28
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : base_model.py
# @Software: PyCharm

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models
from django.db.models import Manager

from common.exceptions import ObjectNotExistError, MultipleObjectsReturnedError


class BaseManager(Manager):

    def create_one_obj(self, db_select=None, create_info=None):
        """
        创建一个对象
        :param db_select: 读写分离
        :param create_info: 创建对象的信息
        :return: 返回一个obj对象
        """
        create_info = dict() if create_info is None or (not isinstance(create_info, dict)) else dict(create_info)
        obj = self.db_manager(using=db_select).model(**create_info)
        obj.save()
        return obj

    def delete_one_obj(self, db_select=None, f_args=None, f_kwargs=None,
                       e_args=None, e_kwargs=None):
        """
        逻辑删除单个数据
        :param db_select: 读写分离
        :param f_args: filter 中的 args 参数
        :param f_kwargs: filter 中的 kwargs 参数
        :param e_args: exclude 中的 args 参数
        :param e_kwargs: exclude 中的 kwargs 参数
        :return: 返回修改的行数
        """
        update_info = {
            "is_delete": 1
        }
        f_args = tuple() if f_args is None or (not isinstance(f_args, (tuple, set, list))) else tuple(f_args)
        e_args = tuple() if e_args is None or (not isinstance(e_args, (tuple, set, list))) else tuple(e_args)
        f_kwargs = dict() if f_kwargs is None or (not isinstance(f_kwargs, dict)) else dict(f_kwargs)
        e_kwargs = dict() if e_kwargs is None or (not isinstance(e_kwargs, dict)) else dict(e_kwargs)
        obj_list = self.db_manager(using=db_select) \
            .filter(*f_args, **f_kwargs) \
            .exclude(*e_args, **e_kwargs)
        objs_len = obj_list.count()
        if objs_len == 0:
            raise ObjectNotExistError("没有获取到对象")
        elif objs_len > 1:
            raise MultipleObjectsReturnedError("获取到多个对象")
        else:
            return obj_list.update(**update_info)

    def delete_obj_list(self, db_select=None, f_args=None, f_kwargs=None,
                        e_args=None, e_kwargs=None):
        """
        更新批量数据
        :param db_select: 读写分离
        :param f_args: filter 中的 args 参数
        :param f_kwargs: filter 中的 kwargs 参数
        :param e_args: exclude 中的 args 参数
        :param e_kwargs: exclude 中的 kwargs 参数
        :param updates:
        :return: 返回修改的行数
        """
        update_info = {
            "is_delete": 1
        }
        f_args = tuple() if f_args is None or (not isinstance(f_args, (tuple, set, list))) else tuple(f_args)
        e_args = tuple() if e_args is None or (not isinstance(e_args, (tuple, set, list))) else tuple(e_args)
        f_kwargs = dict() if f_kwargs is None or (not isinstance(f_kwargs, dict)) else dict(f_kwargs)
        e_kwargs = dict() if e_kwargs is None or (not isinstance(e_kwargs, dict)) else dict(e_kwargs)
        rows = self.db_manager(using=db_select) \
            .filter(*f_args, **f_kwargs) \
            .exclude(*e_args, **e_kwargs) \
            .update(**update_info)
        return rows

    def update_one_obj(self, db_select=None, f_args=None, f_kwargs=None,
                       e_args=None, e_kwargs=None, update_info=None):
        """
        更新单个数据
        :param db_select: 读写分离
        :param f_args: filter 中的 args 参数
        :param f_kwargs: filter 中的 kwargs 参数
        :param e_args: exclude 中的 args 参数
        :param e_kwargs: exclude 中的 kwargs 参数
        :param update_info: 修改的信息
        :return: 返回修改的行数
        """
        f_args = tuple() if f_args is None or (not isinstance(f_args, (tuple, set, list))) else tuple(f_args)
        e_args = tuple() if e_args is None or (not isinstance(e_args, (tuple, set, list))) else tuple(e_args)
        f_kwargs = dict() if f_kwargs is None or (not isinstance(f_kwargs, dict)) else dict(f_kwargs)
        e_kwargs = dict() if e_kwargs is None or (not isinstance(e_kwargs, dict)) else dict(e_kwargs)
        update_info = dict() if update_info is None or (not isinstance(update_info, dict)) else dict(update_info)
        obj_list = self.db_manager(using=db_select) \
            .filter(*f_args, **f_kwargs) \
            .exclude(*e_args, **e_kwargs)
        objs_len = obj_list.count()
        if objs_len == 0:
            raise ObjectNotExistError("没有获取到对象")
        elif objs_len > 1:
            raise MultipleObjectsReturnedError("获取到多个对象")
        else:
            return obj_list.update(**update_info)

    def update_obj_list(self, db_select=None, f_args=None, f_kwargs=None,
                        e_args=None, e_kwargs=None, update_info=None):
        """
        更新批量数据
        :param db_select: 读写分离
        :param f_args: filter 中的 args 参数
        :param f_kwargs: filter 中的 kwargs 参数
        :param e_args: exclude 中的 args 参数
        :param e_kwargs: exclude 中的 kwargs 参数
        :param update_info: 修改的信息
        :return: 返回修改的行数
        """
        f_args = tuple() if f_args is None or (not isinstance(f_args, (tuple, set, list))) else tuple(f_args)
        e_args = tuple() if e_args is None or (not isinstance(e_args, (tuple, set, list))) else tuple(e_args)
        f_kwargs = dict() if f_kwargs is None or (not isinstance(f_kwargs, dict)) else dict(f_kwargs)
        e_kwargs = dict() if e_kwargs is None or (not isinstance(e_kwargs, dict)) else dict(e_kwargs)
        update_info = dict() if update_info is None or (not isinstance(update_info, dict)) else dict(update_info)
        rows = self.db_manager(using=db_select) \
            .filter(*f_args, **f_kwargs) \
            .exclude(*e_args, **e_kwargs) \
            .update(**update_info)
        return rows

    def get_one_obj(self, db_select=None, *args, **kwargs):
        """
        获取一个对象
        :param db_select: 读写分离
        :param args: 查询参数
        :param kwargs: 查询参数
        :return: 返回一个obj对象
        """
        args = tuple() if args is None or (not isinstance(args, (tuple, set, list))) else tuple(args)
        kwargs = dict() if kwargs is None or (not isinstance(kwargs, dict)) else dict(kwargs)
        try:
            obj = self.db_manager(using=db_select).get(*args, **kwargs)
        except ObjectDoesNotExist as e:
            raise ObjectNotExistError("没有获取到对象")
        except MultipleObjectsReturned as e:
            raise MultipleObjectsReturnedError("获取到多个对象")
        return obj

    def get_obj_list(self, db_select=None, f_args=None, f_kwargs=None,
                     e_args=None, e_kwargs=None, s_fields=None,
                     o_fields=None, order_by=None):
        """
        批量获取数据
        :param db_select: 读写分离
        :param f_args: filter 中的 args 参数
        :param f_kwargs: filter 中的 kwargs 参数
        :param e_args: exclude 中的 args 参数
        :param e_kwargs: exclude 中的 kwargs 参数
        :param s_fields: 外键名，元组类型，控制只 INNER JOIN xxx ON
        :param o_fields: only只获取某些字段，元组类型，控制只获取某些字段
        :param order_by: 排序，元组类型
        :return: 返回批量数据
        """
        f_args = tuple() if f_args is None or (not isinstance(f_args, (tuple, set, list))) else tuple(f_args)
        e_args = tuple() if e_args is None or (not isinstance(e_args, (tuple, set, list))) else tuple(e_args)
        s_fields = tuple() if s_fields is None or (not isinstance(s_fields, (tuple, set, list))) else tuple(s_fields)
        o_fields = tuple() if o_fields is None or (not isinstance(o_fields, (tuple, set, list))) else tuple(o_fields)
        order_by = tuple() if order_by is None or (not isinstance(order_by, (tuple, set, list))) else tuple(order_by)
        f_kwargs = dict() if f_kwargs is None or (not isinstance(f_kwargs, dict)) else dict(f_kwargs)
        e_kwargs = dict() if e_kwargs is None or (not isinstance(e_kwargs, dict)) else dict(e_kwargs)
        obj_list = self.db_manager(using=db_select) \
            .filter(*f_args, **f_kwargs) \
            .exclude(*e_args, **e_kwargs) \
            .order_by(*order_by) \
            .select_related(*s_fields) \
            .only(*o_fields)
        return obj_list

    def __get_all_attr_list(self):
        """
        BaseManager 返回数据库当中的有效字段
        :return:
        """
        res_attr_list = []

        attr_list = self.model()._meta.get_fields()
        for attr in attr_list:
            if isinstance(attr, models.ForeignKey):
                res_attr_list.append(attr.name + '_id')
                continue
            res_attr_list.append(attr.name)

        return res_attr_list


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="主键id")
    is_delete = models.BooleanField(default=0, verbose_name="是否删除")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    objects = BaseManager()

    class Meta:
        abstract = True

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            value = f.value_from_object(self)
            if isinstance(value, datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            data[f.name] = value
        return data

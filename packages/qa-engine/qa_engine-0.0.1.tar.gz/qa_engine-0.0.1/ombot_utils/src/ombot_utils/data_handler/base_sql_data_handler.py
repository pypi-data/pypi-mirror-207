#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
from sqlmodel import create_engine, SQLModel
from ..schemas import *


class BaseSQLDataHandler:
    """
    数据库操作基础类
    """
    # 获取数据库相关环境变量
    MYSQL_DB = os.environ.get('MYSQL_DB', 'ombot_test')  # 数据库名
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')  # 数据库账号
    MYSQL_PASSWD = os.environ.get('MYSQL_PASSWD', '123123')  # 数据库登陆密码
    MYSQL_HOST = os.environ.get('MYSQL_HOST', '10.8.21.36')  # 数据库地址
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', '3306'))  # 端口
    basedir = os.path.abspath(os.path.dirname(__file__))  # 路径
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8" % (
        MYSQL_USER, MYSQL_PASSWD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)  # 数据库连接url
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    DELETED = 1
    NO_DELETED = 0

    def __init__(self, *args, **kwargs) -> None:
        """
        从环境变量，初始化数据库，创建数据库，创建表。
        """
        self.init_db_engine()

    def init_db_engine(self)->None:
        # 检查是否存在database，若没有则创建database
        self._init_database()
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URI)

        # 初始化表
        self._create_db_and_tables()

    def _create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def _init_database(self):
        conn = pymysql.connect(host=self.MYSQL_HOST,
                               port=self.MYSQL_PORT,
                               user=self.MYSQL_USER,
                               password=self.MYSQL_PASSWD,
                               charset="utf8mb4",
                               autocommit=True,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.cursor().execute('CREATE DATABASE IF NOT EXISTS %s;' % self.MYSQL_DB)
        del conn

    def get_data(self, *args, **kwargs):
        pass

    def set_data(self, *args, **kwargs):
        pass

    def add_data(self, *args, **kwargs):
        pass

    def delete_data(self, *args, **kwargs):
        pass

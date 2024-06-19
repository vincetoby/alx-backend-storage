#!/usr/bin/env python3
"""
This module contains a utility func that inserts documents
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert into school
    """
    return mongo_collection.insert_one(kwargs).inserted_id

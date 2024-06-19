#!/usr/bin/env python3
"""
This module cobtains a utility func that lists all document
"""
import pymongo


def list_all(mongo_collection):
    """
    list all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())

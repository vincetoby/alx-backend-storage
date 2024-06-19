#!/usr/bin/env python3
"""
changes school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    a funct that updates many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

#!/usr/bin/env python3
"""
a module with a func that finds by topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    it Finds by topic
    """
    return mongo_collection.find({"topics": topic})

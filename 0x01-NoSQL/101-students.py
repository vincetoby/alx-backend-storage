#!/usr/bin/env python3
"""
Module for processing student data from MongoDB
"""


def top_students(mongo_collection):
    """ Returns a list of students sorted by their average score in descending order.
    
    Args:
        mongo_collection: The MongoDB collection object containing student data.

    Returns:
        A MongoDB aggregation cursor with the sorted student documents.
    """
    return mongo_collection.aggregate([
        {
            # Project stage: Calculate the average score for each student
            "$project":
                {
                    "name": "$name", # Include the name field as is
                    "averageScore": {"$avg": "$topics.score"} # Calculate the average score from topics array
                }
        },
        {
            # Sort stage: Sort students by average score in descending order
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])

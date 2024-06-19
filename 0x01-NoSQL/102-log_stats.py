#!/usr/bin/env python3
""" this Log stats - new version """
from pymongo import MongoClient


def nginx_stats_check():
    """ this func provides some stats about Nginx logs stored in MongoDB:"""
    client = MongoClient()
    collection = client.logs.nginx

    num_docs = collection.count_documents({})
    print("{} logs".format(num_docs))
    print("Methods:")
    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods_list:
        method_count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))
    stat = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(stat))

    print("IPs:")

    top_IPs = collection.aggregate([
        {"$group":
         {
             "_id": "$ip",
             "count": {"$sum": 1}
         }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])
    for the_ip in top_IPs:
        count = the_ip.get("count")
        ip_addy = the_ip.get("ip")
        print("\t{}: {}".format(ip_addy, count))


if __name__ == "__main__":
    nginx_stats_check()

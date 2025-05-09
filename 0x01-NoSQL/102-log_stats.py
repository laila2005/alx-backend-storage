#!/usr/bin/env python3
'''Task 15's module.'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.'''
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    status_check_count = nginx_collection.count_documents({
        'method': 'GET', 'path': '/status'
    })
    print(f"{status_check_count} status check")


def print_top_ips(nginx_collection):
    '''Prints statistics about the top 10 IPs in the Nginx logs.'''
    print("IPs:")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for entry in top_ips:
        print(f"\t{entry['_id']}: {entry['count']}")


def run():
    '''Connects to MongoDB and prints Nginx log stats.'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print_nginx_request_logs(nginx_collection)
    print_top_ips(nginx_collection)


if __name__ == '__main__':
    run()

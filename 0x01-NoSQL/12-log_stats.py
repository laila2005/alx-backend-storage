#!/usr/bin/env python3
'''Task 12's module.'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.'''
    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")
    status_check_count = nginx_collection.count_documents({
        'method': 'GET',
        'path': '/status'
    })
    print(f"{status_check_count} status check")


def run():
    '''Connects to MongoDB and prints log stats.'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()

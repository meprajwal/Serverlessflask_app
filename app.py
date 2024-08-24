import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def send_notification(data):
    r.publish('notifications', data['message'])

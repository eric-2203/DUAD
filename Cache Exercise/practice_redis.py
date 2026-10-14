import redis

redis_client = redis.Redis(
    host= "voyage-golden-glove-68223.db.redis.io",
    port= "19408",
    password= "PLACEHOLDER",
)

try:
    connection_status = redis_client.ping()
    if connection_status:
        print("Connected to Redis!")
    else:
        print("Connection to Redis was unsuccessful!")
except redis.ConnectionError as ex:
    print("An error occurred while connecting to Redis.", ex)

redis_client.delete("full_name")
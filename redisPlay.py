import redis
import random
import pprint

r79 = redis.Redis(host="localhost", port=6379, db=0)
r80 = redis.Redis(host="localhost", port=6380, db=0, socket_timeout=10, socket_connect_timeout=10)
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(r79.echo("smt"))

def addData(r):
    random.seed(100)
    hats = {f"hat:{random.getrandbits(32)}": i for i in (
        {
            "color": "black",
            "price": 49.99,
            "style": "fitted",
            "quantity": 1000,
            "npurchased": 0,
        },
        {
            "color": "maroon",
            "price": 59.99,
            "style": "hipster",
            "quantity": 500,
            "npurchased": 0,
        },
        {
            "color": "green",
            "price": 99.99,
            "style": "baseball",
            "quantity": 200,
            "npurchased": 0,
        })
    }

    with r.pipeline() as pipe:
        for h_id, hat in hats.items():
            #print(f'{h_id}: {hat}')
            pipe.hmset(h_id, hat)
        pipe.execute()

    r.bgsave()

# addData(r79)
# addData(r80)
# pp.pprint(r79.keys())
# pp.pprint(r80.keys())

# key = r1.keys()[0]
# pp.pprint(key)
# pp.pprint(r1.hgetall(key))
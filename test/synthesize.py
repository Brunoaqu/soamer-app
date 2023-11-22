from faker  import Faker
            import json
            import random

# Setup
SIZE    = 30
fake    = Faker()
objs    = []

for i in range(SIZE):
    objs.append({
        "productionOrderId": random.randint(1000000000, 9999999999),
        "productId": random.randint(1000000000, 9999999999)
    })

import redis

N=1_000_000
# Connect to Redis server (assuming it's running locally on the default port)
r = redis.Redis(host='localhost', port=6379, db=0)

r.flushdb()

# Add 100 items (strings)
for i in range(0, int(N/2)):
    r.set(f'item:{i}', f'value_{i}')

r.flushdb()

for i in range(0, int(N/2)):
    r.set(f'item:{i}', f'value_{i}')

r.flushdb()

print(f"{N} items added to Redis.")

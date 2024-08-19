import time
import random
from concurrent.futures import ThreadPoolExecutor
import cProfile

def simulate_bid(advertiser):
    time.sleep(random.uniform(0.1, 0.5))  # Simulate network latency
    return random.uniform(1, 10)  # Return a random bid amount

advertisers = ['A', 'B', 'C', 'D', 'E']

def unoptimized_bidding():
    bids = [simulate_bid(adv) for adv in advertisers]
    return bids

def optimized_bidding():
    with ThreadPoolExecutor(max_workers=5) as executor:
        bids = list(executor.map(simulate_bid, advertisers))
    return bids

# Profiling the unoptimized version
print("Profiling the unoptimized version:")
cProfile.run('unoptimized_bidding()')

# Profiling the optimized version
print("\nProfiling the optimized version:")
cProfile.run('optimized_bidding()')
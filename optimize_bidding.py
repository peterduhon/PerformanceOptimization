import time
import random
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt

def simulate_bid(advertiser):
    time.sleep(random.uniform(0.1, 0.5))  # Simulate network latency
    return random.uniform(1, 10)  # Return a random bid amount

advertisers = ['A', 'B', 'C', 'D', 'E']

# Unoptimized version
start_time = time.time()
bids = [simulate_bid(adv) for adv in advertisers]
unoptimized_time = time.time() - start_time

# Optimized version using parallel processing
start_time = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    bids = list(executor.map(simulate_bid, advertisers))
optimized_time = time.time() - start_time

# Print execution times
print(f"Unoptimized execution time: {unoptimized_time:.2f} seconds")
print(f"Optimized execution time: {optimized_time:.2f} seconds")

# Visualization
times = [unoptimized_time, optimized_time]
labels = ['Unoptimized', 'Optimized']

plt.bar(labels, times, color=['red', 'green'])
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison: Unoptimized vs. Optimized')
plt.show()

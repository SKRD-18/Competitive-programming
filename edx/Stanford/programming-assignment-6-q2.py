import heapq
import time


def median_maintenance(filename):
    start_time = time.time()

    numbers = []
    try:
        with open(filename, "r") as f:
            for line in f:
                numbers.append(int(line.strip()))
    except FileNotFoundError:
        return 0

    low_max_heap = []
    high_min_heap = []
    median_sum = 0

    # Process the stream
    for x in numbers:
        # --- STEP A: INSERT ---
        # Logic: If x is smaller than the current median (max of low), it goes to low.
        # Otherwise, it goes to high.
        # (Handle edge case: if low is empty, just push there)
        if len(low_max_heap) == 0:
            heapq.heappush(low_max_heap, -x)
        else:
            current_median = -1 * low_max_heap[0]  # Peek!
            if x < current_median:
                heapq.heappush(high_min_heap, heapq.heappop(low_max_heap) * -1)
                heapq.heappush(low_max_heap, -1 * x)
            else:
                heapq.heappush(high_min_heap, x)

        # --- STEP B: BALANCE ---
        # Rule 1: low must be >= high (size diff 0 or 1)
        # Rule 2: low cannot be > high + 1

        # Case 1: High is bigger than Low (Illegal) -> Move Min(High) to Low
        if len(high_min_heap) > len(low_max_heap):
            val = heapq.heappop(high_min_heap)
            heapq.heappush(low_max_heap, -val)
        # Case 2: Low is too big (More than 1 bigger than High) -> Move Max(Low) to High
        elif len(low_max_heap) > len(high_min_heap) + 1:
            val = -heapq.heappop(low_max_heap)  # Remember to flip sign back!
            heapq.heappush(high_min_heap, val)

        # --- STEP C: RECORD ---
        # The median is ALWAYS the root of low_max_heap because of our balancing rules.
        # (If k is odd, low has 1 more element. If k is even, they are equal,
        #  and problem says take the k/2-th element, which is the max of the lower half).

        median = -1 * low_max_heap[0]
        median_sum += median

    # 3. Final Output
    # The problem asks for the sum modulo 10000
    print(f"Finished in {time.time() - start_time:.4f} seconds.")
    return median_sum % 10000


path = "/Users/shiva/Documents/Competitive-programming/edx/Stanford/data/Median.txt"
result = median_maintenance(path)
print(f"Sum of the 10000 medians: {result}")

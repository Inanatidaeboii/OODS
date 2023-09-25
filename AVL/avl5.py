class van:
    def __init__(self, k, time) -> None:
        self.k = int(k)
        self.time = int(time)
    
    def __lt__(self, other):
        if self.time == other.time:
            return self.k < other.k
        return self.time < other.time


inp = input("Enter Input : ").split("/")

k, queue_list = int(inp[0]), [int(i) for i in inp[1].split()]
queue = []

for i in range(k):
    queue.append(van(i+1, 0))
    
for i in range(len(queue_list)):
    ready = queue.pop(0)
    print(f"Customer {i+1} Booking Van {ready.k} | {queue_list[i]} day(s)")
    queue.append(van(ready.k , int(ready.time + queue_list[i]) ))
    queue.sort()
    
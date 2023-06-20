
#. BAEKJOON 11279. <Max Heap>
def push_heap(heap, value):
  heap.append(value)
  i = len(heap) - 1
  while i > 0:
    parent = (i - 1) // 2
    if heap[parent] >= heap[i]:
      break
    heap[parent], heap[i] = heap[i], heap[parent]
    i = parent

def pop_heap(heap):
  if not heap:
    return 0

  max_value = heap[0]
  heap[0] = heap[-1]
  heap.pop()

  i = 0
  while True:
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    max_child = left_child

    if right_child < len(heap) and heap[right_child] > heap[left_child]:
      max_child = right_child

    if max_child >= len(heap) or heap[i] >= heap[max_child]:
      break

    heap[i], heap[max_child] = heap[max_child], heap[i]
    i = max_child

  return max_value

N = int(input())
heap = []

for _ in range(N):
  x = int(input())
  if x == 0:
    print(pop_heap(heap))
  else:
    push_heap(heap, x)

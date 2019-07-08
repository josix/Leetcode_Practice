class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq as hq
        task_to_count = {}
        for task in tasks:
            if task not in task_to_count:
                task_to_count[task] = 1
            else:
                task_to_count[task] += 1
        tasks_heap = [ -1*count for task, count in task_to_count.items()]
        hq.heapify(tasks_heap)
        ans = 0
        while len(tasks_heap) != 0:
            # print(tasks_heap)
            next_tasks = []
            i = 0
            while i <= n:
                if len(tasks_heap) != 0:
                    task_num = hq.heappop(tasks_heap)
                    # print(task_num)
                    if -1*task_num > 1:
                        next_tasks.append(task_num + 1)
                        # print('done', ans)
                i += 1
                ans += 1
                if len(tasks_heap) == 0 and len(next_tasks) == 0:
                    break
            if len(tasks_heap) != 0:
                next_tasks += tasks_heap
            # print('after', next_tasks)
            tasks_heap = next_tasks
        return ans
            

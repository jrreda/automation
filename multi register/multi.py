from selenium import webdriver
import threading
import time
from test import register


N = 5   # Number of browsers to spawn
thread_list = list()

# Start test
for i in range(N):
    t = threading.Thread(name=f'Test {i}', target=register)
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print('Test completed!')

# from concurrent import futures

# # default number of threads is optimized for cpu cores 
# # but you can set with `max_workers` like `futures.ThreadPoolExecutor(max_workers=...)`
# with futures.ThreadPoolExecutor() as executor: 
#   future_test_results = [ 
#     executor.submit(register(), i) for i in range(N)
#     ] # running same test N=5 times
#   for future_test_result in future_test_results: 
#     try:        
#         test_result = future_test_result.result() # can use `timeout` to wait max seconds for each thread               
#         #... do something with the test_result
#         print(test_result)
#     except Exception as exc: # can give a exception in some thread, but 
#         # print(f'thread generated an exception: {exc:0}')
#         print(exc)
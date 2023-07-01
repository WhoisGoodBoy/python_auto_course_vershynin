import threading
import time
import  concurrent.futures



def function_thread_example(name):
    print(f'we are in {name} function')
    time.sleep(2)
    print(f'we exited from {name} function')


#threads = list()
#for index in range(30):
    #x = threading.Thread(target=function_thread_example, args=(index,))
    #threads.append(x)
    #x.start()
#    function_thread_example(index)

#for index, thread in enumerate(threads):
 #   thread.join()
with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
    executor.map(function_thread_example, range(30))




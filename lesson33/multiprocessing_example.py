import multiprocessing
import time

def function_thread_example(name):
    print(f'we are in {name} function')
    time.sleep(2)
    print(f'we exited from {name} function')

#multiprocessing.set_start_method('spawn')
process = multiprocessing.Process(target=function_thread_example, args=(1,))

process.start()
print('we`re in the middle of nowhere')
#process.join()
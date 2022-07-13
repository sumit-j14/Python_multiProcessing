import multiprocessing
from multiprocessing import Process


def print_func(current_name='default'):
    print('current name is : ',current_name )

def multiprocessfunc():
    print("Number of cpu : ", multiprocessing.cpu_count())
    names = [1,2,3,4,5,6,7,8,9,10]
    procs = []
    
    # for each value in list names, 
    # it allocates SEPARATE PROCESS
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # wait till complete ALL processes
    for proc in procs:
        proc.join()

    print("done")
multiprocessfunc()

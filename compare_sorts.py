import random
import time
import matplotlib.pyplot as plot
from Merge.merge_sort import merge_sort
from Quicksort.Quicksort import quicksort
from BubbleSort.BubbleSort import bubble_sort
from PriorityQ.HeapSort import heap_sort

def generate_testcase(N):
    rand_list = random.sample(range(-523000, 14252000), N)
    return rand_list


def calc_time(list, fn):
    start_time = time.time()
    fn(list)
    end_time = time.time()
    elapsed = end_time - start_time
    return elapsed


# TODO: ADD HEAPSORT TO LIST
def compare_sorts():
    function_list = [merge_sort, quicksort, bubble_sort, heap_sort]
    function_times = []
    for i in range(len(function_list)):
        function_times.append([])

    n_list = list(range(100, 5001, 200))  # 25 testcases

    for n in n_list:
        # generate n-size testcase
        testcase = generate_testcase(n)
        # run diff algos on same testcase
        for i in range(len(function_times)):
            time = calc_time(testcase, function_list[i])
            print("n = {} function = {} time = {}".format(n, function_list[i].__name__, time))
            function_times[i].append(time*1000)

    # plot the different runtimes for each algo
    plot_colors = ['r', 'b', 'g', 'y']
    for i in range(len(function_times)):
        plot.plot(n_list, function_times[i], plot_colors[i]+'-', label = function_list[i].__name__)
        plot.plot(n_list, function_times[i], plot_colors[i] + 'o')


    plot.axis([100, 4900, 0, 400])
    plot.xlabel('Sample size')
    plot.ylabel('Run time (ms)')
    plot.legend()
    plot.show()

compare_sorts()

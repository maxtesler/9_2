from typing import List
import timeit


# Task 1
#Let's start simple: write a function `mean` that calculates the average of the list.
#$$\mu = \frac{{\sum_{i=1}^n x_i}}{{n}}$$


def mean(li: List[float]) -> float:
   if not li: 
       raise ValueError('List is empty but should not')
   return sum(li) / len(li)


assert mean([1., 2., 3.]) == 2.
assert mean([1., 1., 2., 0.]) == 1.


# Task 2
#Now let's calculate variance (dispersion). You may use the `mean` function implemented before.
#$$V = \frac{{\sum_{i=1}^n (x_i - \mu)^2}}{{n}}$$


def variance(li: List[float]) -> float:
   if not li: 
       raise ValueError('List is empty but should not')
   y = mean(li)
   return sum((x - y) ** 2 for x in li) / len(li)


assert variance([1., 1., 1.]) == 0.
assert variance([1., 2., 3., 4.]) == 1.25


# Task 3
#The standard deviation is easy once you get the variance:
#$$\sigma = \sqrt{V}$$


def std(li: List[float]) -> float:
   if not li: 
       raise ValueError('List is empty but should not')
   variance_value = variance(li) 
   return variance_value ** 0.5

assert std([1., 1., 1.]) == 0.
assert std([1., 2., 3., 4.]) == 1.25**0.5


# Task 4
#**Median**
#The median is the middle value in a sorted dataset. If the dataset has an odd number of values, the median is the value at the center. If the dataset has an even number of values, the median is the average of the two middle values.

def median(li: List[float]) -> float:
   if not li: 
       raise ValueError('List is empty but should not')
   sorted_li = sorted(li)
   n = len(sorted_li)
   mid = n // 2 


   if n % 2 == 1: 
       return sorted_li[mid]
   else: 
       return (sorted_li[mid - 1] + sorted_li[mid]) / 2


assert median([1., 1., 1.]) == 1.
assert median([1., 4., 3., 2.]) == 2.5


# Measure performance
#Sometimes, apart from theoretical, algorithmic complexity, it's a good idea to compare the runtime of two algorithms empirically, i.e., run the code many times and time it.
#In Python's standard library, we have [timeit](https://docs.python.org/3/library/timeit.html) module that does exactly that.
#Let's compare the runtime of your implementations and numpy. Use the provided setup code:

# generate data for tests
setup = '''
import random
import numpy as np


arr = np.random.rand(10_000) * 100
li = [random.random() * 100 for _ in range(10_000)]
'''


# pass your function to timeit module
funcs = {
   'mean': mean,
   'variance': variance,
   'std': std,
   'median': median,
}


# Task 5
#Complete Python statements to compare your functions to numpy. Use `li` for your function and `arr` for numpy functions.

stmt_mean_custom = 'mean(li)'
stmt_mean_np = 'np.mean(arr)'


stmt_var_custom = 'variance(li)'
stmt_var_np = 'np.var(arr)'


stmt_std_custom = 'std(li)'
stmt_std_np = 'np.std(arr)'


stmt_median_custom = 'median(li)'
stmt_median_np = 'np.median(arr)'


# Task 6
#Measure average exec time of your statements with `timeit` module. As your submission, fill out the table with results (rounded to 2 decimal places)

time_mean_custom = timeit.timeit(stmt=stmt_mean_custom, setup=setup, globals=globals(), number=10_000)
time_mean_np = timeit.timeit(stmt=stmt_mean_np, setup=setup, globals=globals(), number=10_000)


time_var_custom = timeit.timeit(stmt=stmt_var_custom, setup=setup, globals=globals(), number=10_000)
time_var_np = timeit.timeit(stmt=stmt_var_np, setup=setup, globals=globals(), number=10_000)


time_std_custom = timeit.timeit(stmt=stmt_std_custom, setup=setup, globals=globals(), number=10_000)
time_std_np = timeit.timeit(stmt=stmt_std_np, setup=setup, globals=globals(), number=10_000)


time_median_custom = timeit.timeit(stmt=stmt_median_custom, setup=setup, globals=globals(), number=10_000)
time_median_np = timeit.timeit(stmt=stmt_median_np, setup=setup, globals=globals(), number=10_000)


print(f"{'Func':<10} {'Custom':<10} {'NumPy'}")
print(f"{'mean':<10} {round(time_mean_custom, 2):<10} {round(time_mean_np, 2)}")
print(f"{'variance':<10} {round(time_var_custom, 2):<10} {round(time_var_np, 2)}")
print(f"{'std':<10} {round(time_std_custom, 2):<10} {round(time_std_np, 2)}")
print(f"{'median':<10} {round(time_median_custom, 2):<10} {round(time_median_np, 2)}")






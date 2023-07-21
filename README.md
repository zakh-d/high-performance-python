# high-performance-python
This repo consist some code from High Performance Python Book and my own modification to it


## Julia Set

Julia Set is a CPU-bound problem

To calculate julia set use function ```calc_pure_python```

```python
  from julia_set.julia import calc_pure_python
  
  zs, output = calc_pure_python(desired_width=1000, max_iterations=300)
```

## Timing

To find how long it takes for function to finish ```timefn``` decorator can be used

```python
  from utils.timing import timefn


  @timefn
  def some_function():
    # some complex calculations

```

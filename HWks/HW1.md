# Prerequisites



```python
import numpy as np
```

#### Question 1 - Dot and Cross


```python
u = np.array([2, 4, -1])
v = np.array([1, -3, 5])
np.dot(u, v)
```




    -15



#### Question 2 - Matrix Multiplications


```python
A = np.array([[3, -1],
              [2, 4]])
B = np.array([[5, 2], 
              [-1, 0]])
print(np.matmul(A, B))
print(f'{np.linalg.det(A):.0f}')

```

    [[16  6]
     [ 6  4]]
    14
    

#### Question 3 - Probability


```python
print("3 / 6")
```

    3 / 6
    

#### Question 4 - Probability 


```python
print("26 / 26")
```

    26 / 26
    

#### Question 5 - Prime Numbers



```python
first_five_primes = [2, 3, 5, 7, 11]
first_five_primes
```




    [2, 3, 5, 7, 11]



#### Question 6 - Even / Odd


```python
def is_even(num: int) -> str:
    return "Odd" if num % 2 else "Even"
```

#### Question 7 - NumPy Matrices


```python
randarray = np.random.rand(3, 3)
print(randarray)
transposed = randarray.T
print(transposed)

```

    [[0.75467759 0.83340783 0.08002645]
     [0.92724008 0.76722221 0.39658964]
     [0.09296492 0.78547947 0.63544528]]
    [[0.75467759 0.92724008 0.09296492]
     [0.83340783 0.76722221 0.78547947]
     [0.08002645 0.39658964 0.63544528]]
    

#### Question 8 - Simulation


```python
theoretical = 1 / 6
monte = [0 for _ in range(6)]
for inx in range(100):
    carlo = np.random.randint(1, 6)
    monte[carlo] += 1

print(f"The simulated value is {monte[3] / 100:.4f}")
print(f"The theoretical value is {theoretical:.4f}")

```

    The simulated value is 0.2000
    The theoretical value is 0.1667
    
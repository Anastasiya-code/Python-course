import sympy
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from sympy import solveset
from sympy.abc import x
from sympy import sin, cos, pi
import pylab

x = sympy.symbols('x')
f = -12*(x**4)*sin(cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
ans = solveset(f)
ans
x = np.arange(-5, 5, 0.01)
f = f = -12*(x**4)*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
plt.plot(x, f)
plt.grid(color='g')
plt.show()

# Рассмотрен проммежуток (-6; 6)
# Функция возрастает на промежутках f (-6;-4,2), (1,4;3,8)
# Функция убывает на промежутках f (-4,2;-1,6), (3,8;5)
# x = -4,2 max (вершина)
# x = 5 min (вершина)
# Функция больше нуля на промежутке (-6; -1,7), (2,3;4,8)
# Функция меньше нуля на промежутке (-1,7;2,3), (4,8;5,3)
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Крок 1: Визначення функції та меж інтегрування
def f(x):
    return x ** 2

a = 0  # нижня межа
b = 2  # верхня межа

# Крок 2: Метод Монте-Карло для обчислення інтеграла
N = 100000  # кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
f_rand = f(x_rand)
monte_carlo_result = (b - a) * np.mean(f_rand)

# Крок 3: Аналітичний розрахунок через scipy.quad
quad_result, quad_error = spi.quad(f, a, b)

# Крок 4: Побудова графіка функції
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Крок 5: Виведення результатів
print("Результати обчислення інтеграла:")
print(f"Метод Монте-Карло:            {monte_carlo_result:.6f}")
print(f"Аналітичне значення (quad):   {quad_result:.6f}")
print(f"Оцінка похибки (quad):        {quad_error:.2e}")
print(f"Абсолютна різниця:            {abs(monte_carlo_result - quad_result):.6f}")

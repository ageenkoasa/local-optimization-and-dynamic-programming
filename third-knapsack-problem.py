import random
import matplotlib.pyplot as plt
import numpy as np

# Генерация случайных предметов
def generate_items(num_items):
    items = []
    for _ in range(num_items):
        length = random.randint(1, 3)
        width = random.randint(1, 3)
        value = random.randint(1, 3)
        weight = length * width
        items.append((weight, value, length, width))
    return items

# Задача о рюкзаке с использованием динамического программирования
def knapsack_dp(items, max_weight):
    num_items = len(items)
    dp = np.zeros((num_items + 1, max_weight + 1), dtype=int)

    for i in range(1, num_items + 1):
        weight, value, _, _ = items[i - 1]
        for w in range(max_weight + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    # Восстановление решения
    w = max_weight
    packed_items = []
    for i in range(num_items, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            packed_items.append(items[i - 1])
            w -= items[i - 1][0]
    
    packed_items.reverse()
    return dp[num_items][max_weight], packed_items

# Визуализация рюкзака
def visualize_knapsack(packed_items, max_weight):
    fig, ax = plt.subplots()
    x_offset = 0
    y_offset = 0
    for weight, value, length, width in packed_items:
        rect = plt.Rectangle((x_offset, y_offset), width, length, edgecolor='black', facecolor='lightgreen')
        ax.add_patch(rect)
        plt.text(x_offset + width/2, y_offset + length/2, f'V{value}\nW{weight}', 
                 horizontalalignment='center', verticalalignment='center')
        y_offset += length  # Stack items vertically
        if y_offset > max_weight:
            x_offset += width  # Move to the next column
            y_offset = 0

    plt.xlim(0, max_weight)
    plt.ylim(0, max_weight)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Параметры задачи
num_items = 10
max_weight = 9

# Генерация случайных предметов
items = generate_items(num_items)

# Решение задачи о рюкзаке
max_value, packed_items = knapsack_dp(items, max_weight)

# Вывод результата
print(f"Максимальная ценность: {max_value}")
print("Упакованные предметы (вес, ценность, длина, ширина):")
for item in packed_items:
    print(item)

# Визуализация рюкзака
visualize_knapsack(packed_items, max_weight)

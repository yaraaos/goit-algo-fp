import random
import matplotlib.pyplot as plt
import pandas as pd

# Функція для симуляції кидків кубиків
def roll_dice(num_rolls):
    sums = [0] * 13
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sum_of_dice = die1 + die2
        sums[sum_of_dice] += 1
    return sums

# Функція для обчислення ймовірностей
def calculate_probabilities(sums, num_rolls):
    probabilities = [0] * 13
    for i in range(2, 13):
        probabilities[i] = sums[i] / num_rolls * 100
    return probabilities

# Функція для створення таблиці ймовірностей
def create_probability_table(probabilities):
    table = []
    for i in range(2, 13):
        table.append({'Сума': i, 'Імовірність': f"{probabilities[i]:.2f}% ({sums[i]}/{num_rolls})"})
    return table

# Функція для візуалізації результатів
def plot_probabilities(probabilities):
    sums = list(range(2, 13))
    plt.bar(sums, probabilities[2:], color='#4CAF50')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.show()

# Основна частина програми
num_rolls = 100000
sums = roll_dice(num_rolls)
probabilities = calculate_probabilities(sums, num_rolls)
table = create_probability_table(probabilities)

# Виведення таблиці ймовірностей
df = pd.DataFrame(table)
print(df)

# Збереження таблиці у файл
df.to_csv('probability_table.csv', index=False)

# Побудова графіка
plot_probabilities(probabilities)


import numpy as np

# Матриця прибутків
F = np.array([
    [45, 32, 16],
    [15, 8, 10],
    [20, 18, 14],
    [30, 23, 7]
])

# Функція для обчислення компромісного значення за критерієм Ходжеса-Лемана
def hodges_lehmann_criterion(F, lambda_val):
    strategies_values = []
    for i in range(F.shape[0]):
        # Обчислення очікуваного (середнього) значення та мінімального значення для кожної стратегії
        expected_value = np.mean(F[i])
        min_value = np.min(F[i])
        # Критерій Ходжеса-Лемана
        hl_value = lambda_val * expected_value + (1 - lambda_val) * min_value
        strategies_values.append(hl_value)
    return strategies_values

# Вибір оптимальної стратегії
def find_optimal_strategy(F, lambda_val):
    strategies_values = hodges_lehmann_criterion(F, lambda_val)
    optimal_strategy = np.argmax(strategies_values)  # Індекс стратегії з максимальним значенням
    return optimal_strategy, strategies_values

# Заданий параметр λ (можна змінити для експериментів)
lambda_val = 0.5  # Наприклад, λ = 0.5 для компромісного підходу

# Знаходження оптимальної стратегії
optimal_strategy, strategies_values = find_optimal_strategy(F, lambda_val)

print(f"Оптимальна стратегія: {optimal_strategy + 1}")
print("Значення критерію Ходжеса-Лемана для кожної стратегії:", strategies_values)

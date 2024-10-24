import matplotlib.pyplot as plt

def get_input(prompt, default):
    user_input = input(prompt)
    return float(user_input) if user_input else default

lambda_1 = get_input("Лямбда 1 (по умолчанию 0.1. Просто нажмите Enter): ", 0.1)
lambda_2 = get_input("Лямбда 2 (по умолчанию 0.2): ", 0.2)
t_obsl_1 = get_input("tобсл.1 (по умолчанию 1): ", 1)
t_obsl_2 = get_input("tобсл.2 (по умолчанию 2.5): ", 2.5)

mu_1 = 1 / t_obsl_1
mu_2 = 1 / t_obsl_2

y1 = lambda_1 / mu_1
y2 = lambda_2 / mu_2
y = y1 + y2

t_och_1 = y1 / (mu_1 * (1 - y1))
t_sist_1 = t_och_1 + t_obsl_1

t_och_2 = (1 / mu_2) * (((mu_2 / mu_1) * (y1 / (1 - y)) + y) / (1 - y)) / (1 / mu_2)
t_sist_2 = t_och_2 + (1 / mu_2)

print(f"\ny1 = {y1:.1f}")
print(f"y = {y:.1f}")

print(f"\nСреднее время пребывания в очереди заявок, обладающих приоритетом составит tоч.1 = {t_och_1:.2f} ч.")
print(f"Среднее время пребывания в отключенном состоянии потребителей I категории составит tсист.1 = {t_sist_1:.2f} ч.")

print(f"\nСреднее время ожидания в очереди заявки, не обладающей приоритетом, составит tоч.2 = {t_och_2:.2f} ч.")
print(f"Среднее время пребывания в системе заявки, не обладающей приоритетом, составит tсист.2 = {t_sist_2:.2f} ч.")

# Создание столбчатой диаграммы
labels = ['tоч.1 (приоритет)', 'tсист.1 (приоритет)', 'tоч.2 (без приоритета)', 'tсист.2 (без приоритета)']
values = [t_och_1, t_sist_1, t_och_2, t_sist_2]

plt.bar(labels, values, color=['blue', 'lightblue', 'orange', 'lightcoral'])
plt.ylabel('Время (ч)')
plt.title('Сравнение средних времен ожидания и пребывания в системе')
plt.ylim(0, max(values) + 1)  # Увеличиваем верхнюю границу для лучшей визуализации
plt.grid(axis='y')
plt.show()

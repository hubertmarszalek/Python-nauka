import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generujemy przykładowe dane (symulacja 1000 zamówień w Krakowie)
np.random.seed(42)
dni_tygodnia = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']

# Tworzymy wagi - w weekendy (szczególnie piątek i sobota) zamawiamy więcej!
wagi = [0.10, 0.08, 0.09, 0.12, 0.22, 0.25, 0.14]

dane_zamowien = np.random.choice(dni_tygodnia, size=1000, p=wagi)
df = pd.DataFrame(dane_zamowien, columns=['Dzień'])

# 2. Ustawiamy styl wykresu
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 3. Tworzymy wykres słupkowy
ax = sns.countplot(
    x='Dzień',
    data=df,
    order=dni_tygodnia,
    palette='viridis'
)

# 4. Dodajemy tytuły i etykiety
plt.title('Kiedy Kraków zamawia najwięcej jedzenia?', fontsize=16, fontweight='bold')
plt.xlabel('Dzień tygodnia', fontsize=12)
plt.ylabel('Liczba zamówień', fontsize=12)

# Dodanie wartości nad słupkami dla lepszej czytelności
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                textcoords='offset points')

plt.show()
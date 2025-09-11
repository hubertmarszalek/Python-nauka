import time

# ===============================
# PODSTAWY
# ===============================
print("=== Podstawowe informacje o czasie ===")

# Aktualny czas w sekundach od 01.01.1970 (Unix epoch)
ticks = time.time()
print("Sekundy od 01.01.1970:", ticks)

# Pobranie aktualnej daty i czasu jako struktury
timeData = time.localtime()
print("Struktura czasu:", timeData)

# Poszczególne elementy struktury
print("Rok:", timeData.tm_year)
print("Miesiąc:", timeData.tm_mon)
print("Dzień miesiąca:", timeData.tm_mday)
print("Godzina:", timeData.tm_hour)
print("Minuta:", timeData.tm_min)
print("Sekunda:", timeData.tm_sec)
print("Dzień tygodnia (0=poniedziałek):", timeData.tm_wday)
print("Dzień roku:", timeData.tm_yday)
print("Czas letni (DST):", timeData.tm_isdst)  # # -1: Python sam zarządza, 0: brak DST, 1: aktywne DST

# ===============================
# FORMATOWANIE DATY
# ===============================
print("\n=== Formatowanie daty i czasu ===")
print("asctime:", time.asctime(time.localtime()))
print("strftime:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# Konwersja string -> struktura czasu
timeStr1 = "08 March, 2025"
timeData1 = time.strptime(timeStr1, "%d %B, %Y")
print("strptime (string na datę):", timeData1)

# ===============================
# PĘTLA CZASOWA
# ===============================
print("\n=== Aktualny czas przez 5 sekund ===")
for i in range(5):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(1)


# ===============================
# POMIAR CZASU DZIAŁANIA KODU
# ===============================
print("\n=== Pomiar czasu działania ===")
start = time.time()
total = 0
for i in range(1_000_000):
    total += i
end = time.time()
print("Czas wykonania pętli:", round(end - start, 3), "sekundy")

# ===============================
# ODLICZANIE (TIMER)
# ===============================
print("\n=== Odliczanie ===")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("START!")

# ===============================
# DOKŁADNY POMIAR CZASU
# ===============================
print("\n=== Dokładny pomiar czasu (perf_counter) ===")
start = time.perf_counter()
time.sleep(1.234)  # symulacja działania programu
end = time.perf_counter()
print("Dokładny pomiar:", round(end - start, 6), "sekundy")

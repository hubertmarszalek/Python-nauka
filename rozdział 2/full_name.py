first_name = "jan"
last_name = "kowal"
full_name = first_name + " " + last_name
print(full_name)

first_name = "jan"
last_name = "kowal"
full_name = f"{first_name} {last_name}"  #f - szybsze łączenie bez potrzeby "+"
print(full_name)



first_name = "jan"
last_name = "kowal"
full_name = f"{first_name} {last_name}"
print(f"Witaj {full_name.title()}!")      #połaczenie oraz uzycie .title


#nowy wiersz i tab
print("\tPython")
# t - tabulator-wcięcie
print("Jezyki:\nPython\nJava\nC#")
# n - nowy wiersz


#usuwanie znakow
# .lstrip - po lewej
# .rstrip po prawej

ulubiony_jezyk = 'pythonxd'
ulubiony_jezyk = ulubiony_jezyk.rstrip('xd')
print(ulubiony_jezyk)


first_name = "jan"
last_name = "kowal"
middle_name = "aleks"
full_name = f"{first_name} {middle_name} {last_name} "
print(full_name)
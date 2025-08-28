def increaseSalary(money,bonus):
    money = money + (money*0.2)
    return money + bonus

salary = 5000

newsalary = increaseSalary(salary,1000)
print(newsalary)

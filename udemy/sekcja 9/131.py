class Pizza:
    def __init__(self):
        self.ingredients = []

    def addIngredient(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredients.append(ingredient)

    def showIngredients(self):
        for ingredient in self.ingredients:
            print(ingredient)

capricossa = Pizza()
capricossa.addIngredient("ser")
capricossa.addIngredient("pieczarki")
capricossa.showIngredients()

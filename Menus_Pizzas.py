class Pizza:
    def __init__(self, name, price, ingredient, vegetarians=False):
        self.name = name
        self.price = price
        self.ingredient = ingredient
        self.vegetarians = vegetarians

    def ViewingMenus(self):
        v = ""
        if self.vegetarians == True:
            v = " | VEGETARIAN"
        print()
        print(f"PIZZA {self.name} : {self.price}€" + v)
        print(", ".join(self.ingredient))
        print()


class PersonalisedPizza(Pizza):
    ORIGINAL_PRICE = 7
    PRICE_FOR_ONE_INGREDIENT = 1.20
    unit = 0
    def __init__(self):
        PersonalisedPizza.unit += 1
        self.number = PersonalisedPizza.unit
        super().__init__(f"Personalised n°{self.number}", 0, [])
        self.Ask_user_ingredients()
        self.calculate_the_price()

    def Ask_user_ingredients(self):
        print()
        print(f"Ingredient for the pizza number {self.number}:")
        while True:
            ingredients = input("Add an ingredient (or ENTER to finish): ")
            if ingredients == "":
                return
            self.ingredient.append(ingredients)
            print(f"You have {len(self.ingredient)} ingredient(s): {', '.join(self.ingredient)}")

    def calculate_the_price(self):
        self.price = self.ORIGINAL_PRICE + len(self.ingredient) * self.PRICE_FOR_ONE_INGREDIENT


pizzasmenus = [
    Pizza("Margherita", 10.5, ("tomato sauce", "fiordilatte mozzarella", "parmesan", "fresh basil", "EVO oil 8.5")),

    Pizza("Napoletana", 10.5, ("tomato sauce", "fiordilatte mozzarella", "anchovies", "Kalamata olives", "wild capers & oregano", "EVO oil 12.5")),

    Pizza("Bufalina", 10.5, ("tomato sauce", "buffalo mozzarella", "parmesan", "resh basil", "EVO oil 14")),

    Pizza("Calzone", 10.5, ("folded pizza with salame Napoli", "ham", "fresh buffalo ricotta", "parmesan", "fiordilatte mozzarella", "tomato sauce", "EVO oil 15.25")),

    Pizza("Marinara", 8.5, ("tomato sauce", "fresh garlic", "basil", "wild oregano", "EVO oil 7"), vegetarians=True),

    Pizza("Margherita Vegana", 8.5, ("tomato sauce", "Mozzarisella vegan", "fresh basil", "EVO oil 9.5"), vegetarians=True),
    PersonalisedPizza(),
    PersonalisedPizza()
]

"""
print("Displaying the menus of my pizzas")
for i in pizzasmenus:
    i.ViewingMenus()

print()

print("Displaying the prices of my pizzas")
for i in pizzasmenus:
    if i.price > 8.50:
        i.ViewingMenus

print()

print("Display a pizza that has the ingredient i chose")
for i in pizzasmenus:
    if "Mozzarisella vegan" in i.ingredient:
        i.ViewingMenus()

print()

print("From the smallest to the largest (price)")


def tri(e):
    return e.price


pizzasmenus.sort(key=tri) # We can do the reverse order of this result with add "reverse=True"

for i in pizzasmenus:
    i.ViewingMenus()

print()

print("From the smallest to the largest (ingredients)")


def tri(e):
    return len(e.ingredient)


pizzasmenus.sort(key=tri)

for i in pizzasmenus:
    i.ViewingMenus()

print()

print("From the largest to the smallest (ingredients)")
pizzasmenus.sort(key=tri) # We can do the reverse order of this result with add "reverse=True"

for i in pizzasmenus:
    i.ViewingMenus()
"""

for i in pizzasmenus:
    i.ViewingMenus()

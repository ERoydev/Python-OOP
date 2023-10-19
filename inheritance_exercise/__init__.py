
from Lab.drink import Drink
from Lab.food import Food
from Lab.product import Product
from Lab.product_repository import ProductRepository


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(str(repo))

from products import Product
from store import Store

product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)

def start(store):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            all_products = store.get_all_products()
            print("----------")
            for number, product in enumerate(all_products, start = 1):
                print(f"{number}. {product.show()}")
            print("----------")

        elif choice == "2":
            print(f"Total of {store.get_total_quantity()} items in store")

        elif choice == "3":
            all_products = store.get_all_products()
            shopping_list = []
            for number, product in enumerate(all_products, start = 1):
                print(f"{number}. {product.show()}")
            print("----------")
            print("When you want to finish order, enter empty text.")
            while True:
                product_number = input("Which product # do you want?: ")
                amount = input("What amount do you want?: ")

                if product_number == "" or amount == "":
                    break

                product = all_products[int(product_number) - 1]
                shopping_list.append((product, int(amount)))
                print("Product added to list!\n")

            if shopping_list:
                total_price = store.order(shopping_list)
                print("********")
                print(f"Order made! Total payment: ${total_price}")


        elif choice == "4":
            break

        else:
            print("Error with your choice! Try again!")

start(best_buy)

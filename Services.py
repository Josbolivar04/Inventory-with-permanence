import csv
def save_csv(inventory,route,include_header=True):
    columnas = ["name", "price", "quantity"]

    with open(route, mode="w", newline="", encoding="utf-8") as archive:
        writer = csv.DictWriter(archive, fieldnames=columnas)
        if include_header:
            writer.writeheader()
        writer.writerows(inventory)
        print(f"Archived save at the route: {route}")

def upload_csv(route,inventory):
    skipped_rows = 0
    try:
        with open(route, mode="r", encoding="utf-8") as uploaded_archive:

            reader = csv.DictReader(uploaded_archive)
            init = uploaded_archive.tell()
            first_row = uploaded_archive.readline()
            if not first_row.startswith('sep='):
                uploaded_archive.seek(init)

            if not reader.fieldnames:
                print("Error, archive empty or doesn't have header")
                return
            
            for row in reader:  
                try:
                    raw_price = row.get("price")
                    raw_quantity = row.get("quantity")

                    if raw_price is None or raw_quantity is None:
                        raise KeyError("Column missing")

                    row["price"] = float(raw_price)
                    row["quantity"] = int(raw_quantity)
                    inventory.append(dict(row))

                except ValueError:
                    print(f"Skipping row. Values from {row.get('name','unknown')} aren't valid")
                    skipped_rows += 1
                except KeyError:
                    print(f"Skipping row. There are columns missing")
                    skipped_rows +=1
                    continue
        print(f"Uploaded successfully! \n Invalid skipped rows: {skipped_rows} ")
    except FileNotFoundError:
        print(f"No results were found on the route: {route} ")
    except UnicodeDecodeError:
        print("The format of the file isn't UTF-8")
    except Exception as general:
        print(f"An Unspecified error has occurred {general}")

def value_filter(message, type, positive):

    #Filter code line, dedicate to detect incorrect valued like strings or negative numbers.
    while True:
        try:
            value = type(input(message))
            if positive and value < 0:
                print("Please, use a positive number")
                continue
            return value
        except ValueError:
            print("Invalid value, try again")

def print_menu():
    """
    Displays the main menu in a cleaner format.
    """
    menu_options = [
        "Add product",
        "Show inventory",
        "Search product",
        "Update product",
        "Remove product",
        "Statistics",
        "Save CSV",
        "Upload CSV",
        "Exit"
    ]

    print("\n" + "="*40)
    print("        INVENTORY SYSTEM")
    print("="*40)

    for i, option in enumerate(menu_options, start=1):
        print(f"{i}. {option}")

    print("="*40)


def add_product(inventory):
    print(" - - - - - - - ADD PRODUCT - - - - - -")
    product_name = input("Product name: ")
    product_price = value_filter("Product price: ", float, positive=True)
    product_quantity = value_filter("Quantity: ", int, positive=True)

    inventory.append({
        "name": product_name,
        "price": product_price,
        "quantity": product_quantity
    })

    print(" - - - - - - - - - - - - - - - - - - -")
    print("Product added successfully!")
    print(" - - - - - - - - - - - - - - - - - - -")


def show_inventory(inventory):
    if len(inventory) == 0:
        print("Error, the inventory is empty")
        return

    print("- - - - - - - INVENTORY LOG - - - - - -")

    for product in inventory:
        print(f"| Name: {product['name']:<20} | Price: {product['price']:>10,.2f} | Quantity: {product['quantity']:>5} |")

    print("- - - - - - - - - - - - - - - - - - -")


def search_product(inventory):
    name = input("Please, write the product name: ").lower()
    searched = next((product for product in inventory if product["name"].lower() == name), None)

    if searched:
        print(" - - - - - - - - RESULTS - - - - - - -")
        print(searched)
        print(" - - - - - - - - - - - - - - - - - - -")
    else:
        print(" - - - - - - - - - - - - - - - - - - -")
        print("Product not found!")
        print(" - - - - - - - - - - - - - - - - - - -")


def update_product(inventory):
    target_name = input("Write the product's name:  ")

    index, up_search = next(
        ((i, p) for i, p in enumerate(inventory) if p["name"].lower() == target_name.lower()),
        (None, None)
    )

    if up_search:
        print(target_name)
        print(" - - - - - - - - - - - - - - - - - - -")

        while True:
            menu_update = {
                1: "Change product name",
                2: "Change product price",
                3: "Change product quantity",
                4: "Go back to the menu"
            }

            for number, action in menu_update.items():
                print(f"[{number}] {action}")

            option = value_filter("Choose an option: ", int, positive=True)

            if option == 1:
                new_name = input("Product's name: ")
                up_search["name"] = new_name

            elif option == 2:
                new_price = value_filter("Product's price: ", float, positive=True)
                up_search["price"] = new_price

            elif option == 3:
                new_quantity = value_filter("Product's quantity: ", int, positive=True)
                up_search["quantity"] = new_quantity

            elif option == 4:
                break
    else:
        print(" - - - - - - - - - - - - - - - - - - -")
        print("Product not found!")
        print(" - - - - - - - - - - - - - - - - - - -")


def remove_product(inventory):
    target_id = value_filter("Write the product's ID: ", int, positive=True)
    product_remover = next((product for product in inventory if product.get("id") == target_id), None)

    if product_remover:
        inventory.remove(product_remover)
        print("Product removed successfully!")
    else:
        print("ID not found, try again")


def total_units(inventory):
    for product in inventory:
        print(f"Product | {product['name']:>15} | Quantity | {product['quantity']:>5} |")

    summation = sum(product["quantity"] for product in inventory)
    print(f"The total of products:  {summation}")
    print("✄ - - - - - - - - - - - - - - - - - - -")


def total_value(inventory):
    subtotal = lambda p: p["price"] * p["quantity"]

    for product in inventory:
        result = subtotal(product)
        print(f"Product | {product['name']:>15} | Quantity | {product['quantity']:>5} | Subtotal | {result:>10}")

    summation = sum((product["price"] * product["quantity"]) for product in inventory)
    print(f"Total value: {summation:,}")


def most_expensive(inventory):
    most_expensive = max(inventory, key=lambda p: p["price"])
    print(most_expensive)


def most_stock(inventory):
    most_stock = max(inventory, key=lambda p: p["quantity"])
    print(most_stock)


def statistics(inventory):
    if len(inventory) == 0:
        print("No products to calculate!")
        return

    menu_statistics = True

    while menu_statistics:
        menu_options = {
            1: "Total units",
            2: "Total value",
            3: "Most expensive product",
            4: "Most stock product",
            5: "Exit"
        }

        for key, value in menu_options.items():
            print(f"[{key}] {value}")

        option = value_filter("Please, Choose an option: ", int, positive=True)

        if option == 1:
            total_units(inventory)

        elif option == 2:
            total_value(inventory)

        elif option == 3:
            most_expensive(inventory)

        elif option == 4:
            most_stock(inventory)

        elif option == 5:
            menu_statistics = False
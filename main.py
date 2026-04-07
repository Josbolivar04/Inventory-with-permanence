from Services import *
inventory = []
program_running = True

while program_running:
    
    print_menu()
    
    option = value_filter("Choose an option: ", int, positive=any)

    if   option == 1:
        add_product(inventory)
    elif option == 2:
        show_inventory(inventory)
    elif option == 3:
        search_product(inventory)
    elif option == 4:
        update_product(inventory)
    elif option == 5:
        remove_product(inventory)
    elif option == 6:
        statistics(inventory)
    elif option == 7:
        route = input("Please, choose a route: ")
        save_csv(inventory, route, include_header=True)
    elif option == 8:
        route = input("Please, choose a route: ")
        upload_csv(route, inventory)
    elif option == 9:
        program_running = False


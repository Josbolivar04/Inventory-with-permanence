# Inventory-with-permanence

## Project Overview

This project is a console-based inventory management system developed in Python. It allows users to manage products using a modular structure and supports data persistence through CSV files.

The system follows good programming practices such as modular design, input validation, error handling, and proper documentation using docstrings.

## Project Structure

project/
│
├── main.py          # Main application (menu and user interaction)
├── services.py    # Core inventory logic (CRUD operations and statistics) and CSV file handling (save and load)
└── README.md       # Project documentation

---

## Data Structure

The inventory is stored in memory as a list of dictionaries. Each product has the following structure:

```
{
    "nombre": str,
    "precio": float,
    "cantidad": int
}
```

---

## Core Functionalities (servicios.py)

### agregar_producto(inventario, nombre, precio, cantidad)

Adds a new product to the inventory.

Parameters:

* inventario (list): Inventory list
* nombre (str): Product name
* precio (float): Product price
* cantidad (int): Product quantity

Returns:

* None

---

### mostrar_inventario(inventario)

Displays all products in a formatted way.

Parameters:

* inventario (list)

Returns:

* None

---

### buscar_producto(inventario, nombre)

Searches for a product by name.

Parameters:

* inventario (list)
* nombre (str)

Returns:

* dict or None

---

### actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)

Updates an existing product.

Parameters:

* inventario (list)
* nombre (str)
* nuevo_precio (float, optional)
* nueva_cantidad (int, optional)

Returns:

* None

---

### eliminar_producto(inventario, nombre)

Removes a product from the inventory.

Parameters:

* inventario (list)
* nombre (str)

Returns:

* None

---

## Inventory Statistics

### calcular_estadisticas(inventario)

Calculates the following metrics:

* unidades_totales: sum of all quantities
* valor_total: sum of (precio * cantidad)
* producto_mas_caro: product with highest price
* producto_mayor_stock: product with highest quantity

Returns:

* Dictionary or tuple with all calculated metrics

Optional lambda function:

```
subtotal = (lambda p: p["precio"] * p["cantidad"])
```

---

## CSV File Handling (archivos.py)

### guardar_csv(inventario, ruta, incluir_header=True)

Saves the inventory into a CSV file.

Rules:

* Format: nombre,precio,cantidad
* Validate that the inventory is not empty before saving
* Use try/except to handle errors

Handled errors:

* Permission errors
* File writing errors

Success message:

* "Inventory saved at: {ruta}"

---

### cargar_csv(ruta)

Loads inventory data from a CSV file.

Validations:

* File must include header: nombre,precio,cantidad
* Each row must have exactly three columns
* precio must be a non-negative float
* cantidad must be a non-negative integer

Error handling:

* FileNotFoundError
* UnicodeDecodeError
* ValueError
* Generic exceptions

Invalid rows:

* Skipped automatically
* Counted and reported at the end

---

## Load Behavior

The user is prompted with:
"Overwrite current inventory? (Y/N)"

* If Y: Replace the current inventory
* If N: Merge inventories:

  * If a product already exists:

    * Quantity is added
    * Price is updated if different

Final summary includes:

* Number of products loaded
* Number of invalid rows
* Action performed (merge or replace)

---

## User Interface (app.py)

The application uses a menu-driven interface with the following options:

1. Add product
2. Show inventory
3. Search product
4. Update product
5. Remove product
6. Statistics
7. Save CSV
8. Load CSV
9. Exit

---

## Input Validations

* Menu option must be between 1 and 9
* Price must be a non-negative number
* Quantity must be a non-negative integer

---

## Program Flow

* The application runs inside a while loop
* It continues until the user selects "Exit"
* All input errors are handled without crashing the program
* The user is always returned to the menu after each operation

---

## Error Handling

The system ensures:

* No unexpected crashes
* Clear and informative error messages
* Safe and continuous user experience

---

## How to Run

1. Open Visual Studio Code
2. Open the project folder
3. Open a terminal
4. Run the following command:

```
python app.py
```

---

## Summary

This project demonstrates:

* Modular programming
* Use of lists and dictionaries
* File handling with CSV
* Input validation and error handling

It is suitable for practicing Python fundamentals and building structured console applications.

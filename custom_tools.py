import sqlite3

# Function to connect to the database
def connect_db():
    """Establishes a connection to the SQLite database and returns the connection object."""
    conn = sqlite3.connect('ecommerce.db')
    return conn


# Function to retrieve all products
def get_all_products() -> list:
    """Fetches and returns all products from the products table."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

# Function to retrieve products by category
def get_products_by_category(category: str) -> list:
    """
    Retrieves all products from the products table that belong to a specific category.

    Args:
        category (str): The category of products to retrieve.

    Returns:
        list: A list of tuples, each representing a product in the specified category.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
    products = cursor.fetchall()
    conn.close()
    return products

# Function to retrieve products within a price range
def get_products_by_price_range(min_price: float, max_price: float) -> list:
    """
    Fetches products whose prices fall within a specified range.

    Args:
        min_price (float): The minimum price of products to retrieve.
        max_price (float): The maximum price of products to retrieve.

    Returns:
        list: A list of tuples, each representing a product within the specified price range.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price BETWEEN ? AND ?", (min_price, max_price))
    products = cursor.fetchall()
    conn.close()
    return products

# Function to retrieve products based on stock availability
def get_products_by_stock(min_stock: int) -> list:
    """
    Retrieves products that have at least a specified quantity in stock.

    Args:
        min_stock (int): The minimum stock level of products to retrieve.

    Returns:
        list: A list of tuples, each representing a product with sufficient stock.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE stock >= ?", (min_stock,))
    products = cursor.fetchall()
    conn.close()
    return products

# Function to retrieve a product by ID
def get_product_by_id(product_id: int) -> tuple:
    """
    Fetches a specific product based on its ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        tuple: A tuple representing the product with the specified ID, or None if not found.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product
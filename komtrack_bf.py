# =============================================================
#  KOMTRACK BF — Inventory Management System
#  Simplified platform for small merchants in Ouagadougou
#  Burkina Institute of Technology — CS27 Advanced Programming
#  Group Assignment 1 | Parts 1 & 2
# =============================================================


# =============================================================
# PART 2 — INHERITANCE
# =============================================================

class Product:
    """
    PARENT class representing a generic product in stock.
    Contains attributes and methods common to all products.
    """

    def __init__(self, name: str, category: str, purchase_price: float,
                 selling_price: float, quantity: int, alert_threshold: int,
                 active: bool):
        # str — product name and category
        self.name = name
        self.category = category
        # float — prices in FCFA
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        # int — whole quantities
        self.quantity = quantity
        self.alert_threshold = alert_threshold
        # bool — product available for sale or not
        self.active = active

    def calculate_margin(self) -> float:
        """Calculates the profit margin as a percentage. [Arithmetic expression 1]"""
        return ((self.selling_price - self.purchase_price) / self.purchase_price) * 100

    def is_low_stock(self) -> bool:
        """Returns True if the stock is below the alert threshold."""
        return self.quantity <= self.alert_threshold

    def record_sale(self, qty_sold: int) -> float:
        """
        Records a sale, updates the stock.
        Returns the profit generated. [Arithmetic expression 2]
        """
        if qty_sold > self.quantity:
            print(f"  Insufficient stock — available: {self.quantity} unit(s).")
            return 0.0
        self.quantity -= qty_sold
        profit = (self.selling_price - self.purchase_price) * qty_sold
        return profit

    def display(self):
        """Displays the product information using f-strings."""
        status = "Active" if self.active else "Inactive"
        alert = " LOW STOCK" if self.is_low_stock() else ""
        print(f"  [{status}] {self.name} | Category: {self.category}")
        print(f"    Purchase: {self.purchase_price:.0f} FCFA | "
              f"Selling: {self.selling_price:.0f} FCFA | "
              f"Quantity: {self.quantity}{alert}")


class FoodProduct(Product):
    """
    CHILD class — inherits from Product.
    Adds a specific attribute: the unit of measure (kg, liter, bag...).
    A FoodProduct IS A Product — valid IS-A relationship.
    """

    def __init__(self, name: str, category: str, purchase_price: float,
                 selling_price: float, quantity: int, alert_threshold: int,
                 active: bool, unit: str):
        # Call the parent constructor
        super().__init__(name, category, purchase_price, selling_price,
                         quantity, alert_threshold, active)
        # Attribute UNIQUE to the child — unit of measure
        self.unit = unit

    def display(self):
        """Enhanced version of display() — includes the unit of measure."""
        status = "Active" if self.active else "Inactive"
        alert = " LOW STOCK" if self.is_low_stock() else ""
        print(f"  [{status}] {self.name} ({self.unit}) | Category: {self.category}")
        print(f"    Purchase: {self.purchase_price:.0f} FCFA | "
              f"Selling: {self.selling_price:.0f} FCFA | "
              f"Quantity: {self.quantity} {self.unit}{alert}")


# =============================================================
# PART 1 — FOUNDATIONS
# =============================================================

# --- Validated input functions (while + try/except) ---

def input_float(message: str) -> float:
    """
    Prompts for a decimal number with validation.
    Uses while + try/except — never crashes on bad input.
    """
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("  Enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("  Invalid input — a number is expected (e.g. 250.5).")


def input_int(message: str, min_val: int = 0) -> int:
    """
    Prompts for an integer with validation.
    Uses while + try/except — no possible crash.
    """
    while True:
        try:
            value = int(input(message))
            if value < min_val:
                print(f"  Enter an integer >= {min_val}.")
                continue
            return value
        except ValueError:
            print("  Invalid input — a whole number is expected (e.g. 10).")


# --- Add product function ---

def add_product() -> Product:
    """
    Collects information for a new product.
    Covers all data types and correct booleans.
    """
    print("\n" + "-" * 50)
    print("  NEW PRODUCT")
    print("-" * 50)

    # input() 1 — str
    name = input("Product name: ").strip()

    # input() 2 — str
    category = input("Category (e.g. Food, Hygiene, Beverage): ").strip()

    # input() 3 — correct bool (not bool(input(...)))
    is_food: bool = input("Is this a food product? (yes/no): ").lower() == "yes"

    # input() 4 — float via validated input
    purchase_price: float = input_float("Purchase price (FCFA): ")

    # input() 5 — float via validated input
    selling_price: float = input_float("Selling price (FCFA): ")

    # input() 6 — int via validated input
    quantity: int = input_int("Initial stock quantity: ", min_val=1)

    # input() 7 — int via validated input
    alert_threshold: int = input_int("Alert threshold (minimum quantity): ", min_val=1)

    # input() 8 — correct bool
    active: bool = input("Product available for sale right now? (yes/no): ").lower() == "yes"

    if is_food:
        # input() 9 — str (food branch)
        unit: str = input("Unit of measure (kg, liter, bag, box...): ").strip()
        return FoodProduct(name, category, purchase_price, selling_price,
                           quantity, alert_threshold, active, unit)
    else:
        return Product(name, category, purchase_price, selling_price,
                       quantity, alert_threshold, active)


# --- Record sale function ---

def record_sale(stock: list) -> float:
    """
    Allows the user to select a product and enter the quantity sold.
    Returns the profit from the transaction.
    """
    active_products = [p for p in stock if p.active and p.quantity > 0]

    if not active_products:
        print("  No products currently available for sale.")
        return 0.0

    print("\n" + "-" * 50)
    print("  RECORD A SALE")
    print("-" * 50)

    for i, p in enumerate(active_products):
        print(f"  {i + 1}. {p.name} — {p.quantity} available @ {p.selling_price:.0f} FCFA")

    # input() 10 — int with validation
    while True:
        try:
            choice: int = int(input("Product number sold: ")) - 1
            if 0 <= choice < len(active_products):
                break
            print(f"  Choose between 1 and {len(active_products)}.")
        except ValueError:
            print("  Enter the number shown in the list.")

    # input() 11 — int with validation
    qty_sold: int = input_int("Quantity sold: ", min_val=1)

    product = active_products[choice]
    profit: float = product.record_sale(qty_sold)

    if profit > 0:
        # Arithmetic expression 3 — total revenue from the transaction
        revenue: float = product.selling_price * qty_sold
        margin_pct: float = product.calculate_margin()
        print(f"  ✓ Sale recorded!")
        print(f"    Revenue  : {revenue:.0f} FCFA")
        print(f"    Profit   : {profit:.0f} FCFA")
        print(f"    Margin   : {margin_pct:.1f}%")

    return profit


# --- Final summary screen ---

def show_dashboard(store_name: str, stock: list,
                   total_profit: float, num_sales: int):
    """
    Displays the complete dashboard with all statistics.
    Uses exclusively f-strings for display.
    """
    print("\n" + "=" * 55)
    print(f"  KOMTRACK BF — {store_name.upper()}")
    print(f"  DASHBOARD")
    print("=" * 55)

    if not stock:
        print("  No products registered yet.")
        print("=" * 55)
        return

    # Arithmetic expression 4 — total stock value (purchase cost)
    stock_value: float = sum(p.purchase_price * p.quantity for p in stock)

    # Arithmetic expression 5 — potential revenue if everything is sold
    potential_revenue: float = sum(p.selling_price * p.quantity for p in stock)

    # Counts using implicit bool
    num_products: int = len(stock)
    num_active: int = sum(1 for p in stock if p.active)
    num_alerts: int = sum(1 for p in stock if p.is_low_stock())

    print(f"\n  STOCK")
    print(f"    Registered products       : {num_products}")
    print(f"    Active products           : {num_active}")
    print(f"    Low stock alerts          : {num_alerts}")
    print(f"\n  FINANCES")
    print(f"    Stock value               : {stock_value:,.0f} FCFA")
    print(f"    Remaining potential revenue: {potential_revenue:,.0f} FCFA")
    print(f"    Number of sales           : {num_sales}")
    print(f"    Total profit              : {total_profit:,.0f} FCFA")

    if num_alerts > 0:
        print(f"\n   LOW STOCK PRODUCTS:")
        for p in stock:
            if p.is_low_stock():
                print(f"    → {p.name}: {p.quantity} unit(s) remaining "
                      f"(threshold: {p.alert_threshold})")

    print(f"\n  STOCK DETAIL:")
    for p in stock:
        p.display()

    print("\n" + "=" * 55)
    print("  KomTrack BF — Manage your business simply")
    print("=" * 55)


# --- Main program loop ---

def start():
    """
    Main entry point.
    Manages the menu and main application loop.
    """
    print("=" * 55)
    print("   KOMTRACK BF")
    print("   Inventory management for merchants — Ouagadougou")
    print("=" * 55)

    # input() 12 — str
    store_name: str = input("\nYour store name: ").strip()
    if not store_name:
        store_name = "My Store"

    print(f"\nWelcome, {store_name}!")
    print("Your inventory management system is ready.\n")

    stock: list = []
    total_profit: float = 0.0
    num_sales: int = 0
    running: bool = True

    while running:
        print("\n--- MAIN MENU ---")
        print("  1. Add a product")
        print("  2. Record a sale")
        print("  3. View dashboard")
        print("  4. Quit")

        # input() 13 — int with validation
        while True:
            try:
                choice: int = int(input("Your choice (1-4): "))
                if 1 <= choice <= 4:
                    break
                print("  Enter a number between 1 and 4.")
            except ValueError:
                print("  Enter a digit (1, 2, 3 or 4).")

        if choice == 1:
            product = add_product()
            stock.append(product)
            margin = product.calculate_margin()
            print(f"\n  ✓ '{product.name}' added to stock.")
            print(f"    Profit margin: {margin:.1f}%")

        elif choice == 2:
            p = record_sale(stock)
            if p > 0:
                total_profit += p
                num_sales += 1

        elif choice == 3:
            show_dashboard(store_name, stock, total_profit, num_sales)

        elif choice == 4:
            # Mandatory final summary before quitting
            show_dashboard(store_name, stock, total_profit, num_sales)
            print(f"\nGoodbye, {store_name}! See you on KomTrack BF.")
            running = False


# =============================================================
# ENTRY POINT
# =============================================================
if __name__ == "__main__":
    start()

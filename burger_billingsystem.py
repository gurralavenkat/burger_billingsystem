class BurgerBillingSystem:
    def __init__(self):
        self.menu = {
            1: {"name": "aloo tikki", "price": 5},
            2: {"name": "maharaja", "price": 10},
            3: {"name": "mac special", "price": 15}
        }
        self.orders = []

    def display_menu(self):
        print("Menu:")
        for key, item in self.menu.items():
            print(f"{key}. {item['name']} - ${item['price']}")
        print("")

    def take_orders(self):
        self.display_menu()
        while True:
            order_input = input("Enter item number and quantity (e.g., '1 2' or '0' to finish): ")
            if order_input.strip().lower() == '0':
                break
            
            try:
                item_number, quantity = map(int, order_input.split())
                if item_number not in self.menu:
                    print("Invalid item number. Please try again.")
                    continue
                
                self.orders.append((item_number, quantity))
            except ValueError:
                print("Invalid input. Please enter item number and quantity.")
                print("----------------------------------")
    def calculate_bill(self):
        student_discount_rate = 0.20  # 20% student discount
        delivery_charge_rate = 0.05    # 5% delivery charge
        total_discount = 0
        total_delivery_charge = 0
        subtotal = 0

        print("\nFinal Bill:")
        item_totals = []
        for item_number, quantity in self.orders:
            item = self.menu[item_number]
            item_total = item['price'] * quantity
            item_totals.append(item_total)
            print(f"{item['name']} x {quantity}: ${item_total:.2f}")
        
        subtotal = sum(item_totals)
        print(f"Total Price of Items: ${subtotal:.2f}")
        print("----------------------------------")

        is_student = int(input("Are you a student? (0 for no, 1 for yes): "))
        has_delivery = int(input("Do you want delivery? (0 for no, 1 for yes): "))

        if is_student == 1:
            student_discount = subtotal * student_discount_rate
            total_discount += student_discount
            print(f"   - Total Student Discount: ${student_discount:.2f} ({student_discount_rate * 100}%)")

        if has_delivery == 1:
            delivery_charge = subtotal * delivery_charge_rate
            total_delivery_charge += delivery_charge
            print(f"   - Total Delivery Charge: ${delivery_charge:.2f} ({delivery_charge_rate * 100}%)")

        final_amount = subtotal - total_discount + total_delivery_charge
        print("----------------------------------")
        print(f"Final Amount to Pay: ${final_amount:.2f}")
        print("Thank you and come again!")

    def start(self):
        self.take_orders()
        self.calculate_bill()

 if __name__ == "__main__":
    billing_system = BurgerBillingSystem()
    billing_system.start()

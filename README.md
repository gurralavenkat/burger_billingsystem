# burger_billingsystem
Burger Billing System This project is a simple burger billing system implemented in Python. The system allows users to select different types of burgers along with optional add-ons, calculates the total cost based on the selections, and generates a receipt for the transaction. 

Features
Menu Display: Displays a list of available burgers with corresponding prices.
Order Taking: Allows users to select items from the menu and specify quantities.


Billing Calculation: Calculates the total cost of the order including any applicable discounts or delivery charges.



Setup
Requirements : Python 3.x

Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/venkatgurrala/burger_billingsystem.git


Navigate to the project directory:
bash
Copy code
cd burger_billingsystem
Running the Program
Ensure you have Python installed.


Run the following command to start the program:
bash
Copy code
python burger_billingsystem.py
Follow the on-screen prompts to place your order:
Enter the item number and quantity (e.g., 1 2 to order 2 units of the first item).
Enter 0 to finish and calculate the bill.
After entering your order details, the program will display the total cost, any discounts (for students), and delivery charges 




sample output :
Menu:
1. aloo tikki - $5
2. maharaja - $10
3. mac special - $15

Enter item number and quantity (e.g., '1 2' or '0' to finish): 1 2
Enter item number and quantity (e.g., '1 2' or '0' to finish): 2 1
Enter item number and quantity (e.g., '1 2' or '0' to finish): 0

Final Bill:
aloo tikki x 2: $10.00
maharaja x 1: $10.00
Total Price of Items: $20.00
----------------------------------
Are you a student? (0 for no, 1 for yes): 1
   - Total Student Discount: $4.00 (20.0%)
Do you want delivery? (0 for no, 1 for yes): 1
   - Total Delivery Charge: $1.00 (5.0%)
----------------------------------
Final Amount to Pay: $17.00
Thank you and come again!

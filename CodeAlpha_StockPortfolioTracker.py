stocks ={}


      
           
while True:

    print("\n===== Stock Portfolio Tracker =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Remove Stock")
    print("4. Exit")
    print("5.Save Portfolio")

    choice = input("Enter your choice: ")

    if choice == "1":
           name = input("Enter stock name: ")
           quantity = int(input("Enter quantity: "))
           price = float(input("Enter purchase price per share: "))

           stocks[name] = {
              "quantity": quantity,
              "price": price
          }

           print("Stock added successfully!")

       
    elif choice == "2":
           total_investment =0

           print("\nYour Portfolio:")

           for stock, details in stocks.items():
               print("Stock:", stock)
               print("Quantity:", details["quantity"])
               print("Purchase Price:", details["price"])
               print("Total Investment:", details["quantity"] * details["price"])

               total_investment+= details["quantity"] * details["price"]

           print("\nTotal Portfolio Value:", total_investment)

    elif choice =="3":

          remove_stock = input("\nEnter the stock name you want to remove: ")

          if remove_stock in stocks:
             del stocks[remove_stock]
             print("Stock removed successfully!")
          else:
             print("Stock not found!")

    elif choice == "4":
            print("Thank you for using Stock Portfolio Tracker!")
            break
    elif choice =="5":
        with open("portfolio.txt","w") as file:
            file.write("stock portfolio\n")
            file.write("===============\n")

            for stock, details in stocks.items():
                total =details["quantity"]* details["price"]
                file.write("stock: " + stock + "\n")

                file.write("Quantity:" + str(details["quantity"]) +"\n")
                file.write("Purchase price: " + str(details["price"]) + "\n")
                file.write("total Investment: " + str(total) + "\n")

                file.write("--------------\n")

                print("Portfolio saved successfully!")
 
    else:
        print("Invalid choice!")
        break
        
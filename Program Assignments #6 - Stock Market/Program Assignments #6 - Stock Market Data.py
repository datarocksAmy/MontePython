####################################################################################################################################################
##
## CS 101
## Program #6 Stock Market Data
##
## Name: CHIA-HUI,AMY,LIN
## Email: clthf@mail.umkc.edu
##
## Creaetion Date: 04/01/2016
## Due Date:       04/10/2016
##
## PROBLEM : Read csv file to get stock prices on specific dates.
##           Output the buy and sell results of the chosen stock with calculated profit/loss.
##
##
## ALGORITHM :
##      1. Create function chosen_stock to ask the user for purchased stock ticker & check if it's in the list.
##      2. Create function buy_date_check to ask for stock purchased date and check if it's valid.
##      3. Create function sell_date_check to ask for stock sold date and check if it's valid.
##      4. Create function sell_buy_date to check if sell date is later than buy date.
##      5. Create function stock_numbers_to_buy to ask for numbers of stock purchased on start date, catch any error occurs & ask for prompt again.
##      6. Create function file_valid_date_check to check buy & sell date are in the file or not.
##      7. Create function portfolio_header to print the header for the portfolio.
##      8. Create function fetch_share_price to get the share price.
##      9. Create function stock_split to calculate sold stock numbers if there's stock split in between buy & sell date.
##      10.Call function created in Step 1 to get stock ticker.
##      11.Call functions in Step 2 & 3 to check sell & buy dates.
##      12.Call function in Step 5 to get the number of shares of buy stock.
##      13.Call function created Step 6 to check if sell & buy dates are in the file.
##      14.Call function in Step 8 to get buy and sell stock price.
##      15.Calculate sold stock numbers if there's a stock split by calling function in Step 9. If no split, sold number will be the same as purchased number.
##      16.Calculate buy and sell total price by multiplying stock price in Step 14 with stock numbers in Step 15.
##      17.Calculate profit/loss by subtracting sell to buy total price.
##      18.Print Portfolio header by using function in Step 7.
##      19.Output results.
##      
##
## ERROR HANDLING:
##      Read csv file to fetch the right data and use the datetime module for valid date.
##
##
## OTHER COMMENTS:
##      The most humongous number of functions created so far!
##
####################################################################################################################################################
import datetime
import csv
import os

def chosen_stock():
    """ Ask the user for stock ticker. """
    error = True
    while error:
        error = False
        choice = input("Enter the ticker of the stock purchased / Enter 'quit' to exit: =====>")
        stocklist = []
        with open("stocklist.csv", newline='') as file:
            readstock = csv.DictReader(file)
            for row in readstock:
                stocklist.append(row["Stock"])

        if choice in stocklist:
            return choice.upper()
            break

        elif choice.lower() == "quit":
            print("\n Exiting Program. See you later! ")
            os._exit(0)
            break

        else:
            error = True
            print("\n Ticker not found in the list. Please try another one. \n ")


def buy_date_check():
    """ Ask the user for stock purchase date. """
    #import datetime
    while True:
         try:
              enter_buy_date = input("Enter the stock PURCHASED date: [ MM/DD/YYYY ] =====> ")
              buy_date = datetime.datetime.strptime(enter_buy_date, "%m/%d/%Y")
              return buy_date
              break

         except ValueError:
              print(" Invalid date. Please re-enter in the format [ MM/DD/YYYY ] \n")

def sell_date_check():
    """ Ask the user for stock sold date. """
    #import datetime
    while True:
         try:
              enter_sell_date = input("Enter the stock SELL date: [ MM/DD/YYYY ] =====> ")
              sell_date = datetime.datetime.strptime(enter_sell_date, "%m/%d/%Y")
              return sell_date
              break

         except ValueError:
              print(" Invalid date. Please re-enter in the format [ MM/DD/YYYY ] \n")


def sell_buy_date(buy_date, sell_date):
    """ Check if sell date is later than buy date. """
    #import datetime
    if buy_date > sell_date:
        print(" Warning. Buy date can't be later than Sell date. Please Enter buy/sell date again. ")
        return True


def stock_numbers_to_buy():
    """ Ask the user for the number of stocks purchased on the start date. """
    while True:
        try:
            stock_numbers = int(input(" Enter the number of stocks purchased on start date:  =====> "))
            if stock_numbers >= 0:
                return stock_numbers
                break

            else:
                print(" Please enter a positive number. ")
        except ValueError:
            print(" Please enter an interger number. ")


def file_valid_date_check(chosen_stock_ticker, buy_date, sell_date):
    """ Check buy & sell date can be located in the file. """
    date_output = []
    file = open(chosen_stock_ticker+".csv", "rU")
    for column in file:
        cells = column.split(",")
        date_output.append(cells[0])
    file.close()

    if buy_date.strftime("%m/%d/%Y") not in date_output:
        check = True
        print("Counld not locate the start date of ",buy_date)
        return check

    if sell_date.strftime("%m/%d/%Y") not in date_output:
        check = True
        print("Counld not locate the end date of ",sell_date)
        return check

def portfolio_header(chosen_stock_ticker):
    """ Print Out Portfolio Header from the file. """
    #import csv
    with open("stocklist.csv", newline='') as file:
         readstock = csv.DictReader(file)
         for row in readstock:
              if chosen_stock_ticker == row["Stock"]:
                   return print("\n{:<} ({:<}) Portfolio\n".format(row["Name"], chosen_stock_ticker))


def fetch_share_price(chosen_stock_ticker, date):
    """ Fetch the close price for a specific date. """
    #import csv
    if date == buy_date:
        format_date = buy_date.strftime("%m/%d/%Y")
    if date == sell_date:
        format_date = sell_date.strftime("%m/%d/%Y")

    with open(chosen_stock_ticker+".csv", newline='') as file:
         readprice = csv.DictReader(file)
         for row in readprice:
              if format_date == row["Date"]:
                  close_price = row["Close"]
                  return(close_price)

def stock_split(chosen_stock_ticker, buy_date, sell_date, stock_purchase_number):
    """ Calculate sold stock numbers if there's stock split in between buy & sell date. """
    #import csv
    #import datetime
    sold_stock_numbers = stock_purchase_number
    with open(chosen_stock_ticker+".csv", newline='') as file:
        split_check = csv.DictReader(file)
        for row in split_check:
            if buy_date <= datetime.datetime.strptime(row["Date"], "%m/%d/%Y") <= sell_date:
                if row["Split Ratio"] > "1.0":
                    sold_stock_numbers *= float(row["Split Ratio"])

        return sold_stock_numbers

#-------------------------------------------------------Main Code-------------------------------------------------------#
run = True
while run:
    #Input of stock ticker, number of purchased stock
    validated = False
    while not validated:
        chosen_stock_ticker = chosen_stock()
        date = True
        while date:
            date = False
            buy_date = buy_date_check()
            sell_date = sell_date_check()
            warning_date_order = sell_buy_date(buy_date, sell_date)

            if warning_date_order == True:
                date = True

            else:
                date = True
                break
        stock_purchase_number = stock_numbers_to_buy()

        #Check validity of buy and sell dates

        date_check = file_valid_date_check(chosen_stock_ticker, buy_date, sell_date)
        run = False
        while True:
            if date_check == True:
                run = True
                break

            else:
                
                validated = True
                break

    #Fetch Buy and Sold Stock Price
    buy_stock_price = fetch_share_price(chosen_stock_ticker, buy_date)
    sell_stock_price = fetch_share_price(chosen_stock_ticker, sell_date)

    #Sold stock numbers, check if split or not
    sold_stock_split = stock_split(chosen_stock_ticker, buy_date, sell_date, stock_purchase_number)
    if sold_stock_split != stock_purchase_number:
        sold_stock_numbers = sold_stock_split
    else:
        sold_stock_numbers = stock_purchase_number

    #Calculate Buy & Sold Total Stock Price
    buy_total_price = float(buy_stock_price) * stock_purchase_number
    sell_total_price = float(sell_stock_price) * sold_stock_numbers

    #Calculate Profit/Loss
    profit_loss = sell_total_price - buy_total_price

    #Output Result
    portfolio_header_print = portfolio_header(chosen_stock_ticker)
    print("{:<10s}{:<15s}{:^15s}{:>10s}{:>20s}".format("Action", "Date", "Shares", "Price", "Total Price"))
    print("======================================================================")
    print("{:<10s}{:<15s}{:^15.1f}{:>10.2f}{:>20.2f}".format("Buy", buy_date.strftime("%m/%d/%Y"), stock_purchase_number, float(buy_stock_price), buy_total_price))
    print("{:<10s}{:<15s}{:^15.1f}{:>10.2f}{:>20.2f}".format("Sell", sell_date.strftime("%m/%d/%Y"), sold_stock_numbers, float(sell_stock_price), sell_total_price))
    print("______________________________________________________________________")
    print("{:<10s}{:>53.2f}".format("Profit(+)/Loss(-)",profit_loss))
    print("======================================================================\n")


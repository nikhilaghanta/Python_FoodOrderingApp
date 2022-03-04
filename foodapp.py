# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:21:04 2022

@author: Admin
"""
import re, random, csv, os
from tabulate import tabulate
from datetime import datetime 


list_foods = []
list_users = []
list_user_fields = []

def default():
    global list_foods, list_users, list_user_fields

default()


def read_admin_details():
    admin_file = open('files/admin_details.txt', 'r') 
    admin_details = admin_file.readlines()
    adminId = admin_details[0].strip()
    adminPwd = admin_details[1].strip()
    return adminId, adminPwd

adminId, adminPwd = read_admin_details()

def read_user_details():
    global list_users, list_user_fields
    user_file = open('files/user_details.csv','r')
    csvreader = csv.reader(user_file)
    list_user_fields = next(csvreader)
    for row in csvreader:
        list_users.append(row)
    user_file.close()

read_user_details()

def write_new_user_details(user):
    global list_users, list_user_fields
    user_file = open('files/user_details.csv', 'a')
    csvwriter = csv.writer(user_file)
    csvwriter.writerow(user)
    user_file.close()

def write_users_details():
    global list_users, list_user_fields
    os.remove('files/user_details.csv')
    user_file = open('files/user_details.csv', 'w', newline='')
    csvwriter = csv.writer(user_file)
    csvwriter.writerow(list_user_fields)
    csvwriter.writerows(list_users)
    user_file.close()


def main():
    while True:
        print("*" * 28 + "FOOD ORDERING APP" + "*" * 24 + "\n")
        print("*" * 31 + "CHOOSE ROLE" + "*" * 32 + "\n"     
              "\t(A) ADMIN\n"                              
              "\t(U) USER\n"
              "\t(E) EXIT\n" +
              "_" * 72)
        role = str(input("Please Select Your Role: ")).upper()
        if (len(role) == 1):
            if (role == 'A'):                                          
                print("\n" * 10)                                        
                admin()                                          
                break                                                     
            elif (role == 'U'):                                        
                print("\n" * 10)                                        
                user()                                              
                break
            elif (role == 'E'):                                        
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")           
                break               
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(role) + "). Try again!")
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(role) + "). Try again!")
            
def admin():
    while True:
        print("*" * 28 + "ADMIN OPTIONS" + "*" * 24 + "\n")
        print("*" * 31 + "CHOOSE OPTION" + "*" * 32 + "\n"     
              "\t(L) LOGIN\n"                             
              "\t(E) EXIT\n" +
              "_" * 72)
        option = str(input("Please Select Your Option: ")).upper()
        if (len(option) == 1):
            if (option == 'L'):                                          
                admin_login()
                break
            elif (option =='E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")

def admin_login(): 
    while True:       
        adminIdInput = str(input("PLEASE ENTER ADMIN ID : "))
        if (adminIdInput == adminId):
            adminPwdInput = str(input("PLEASE ENTER ADMIN PASSWORD : "))
            if (adminPwdInput == adminPwd):
                admin_options()
                break
            else:
                print("\n" * 10 + "ERROR: INVALID ADMIN PASSWORD. Try again!")
        else:
            print("\n" * 10 + "ERROR: INVALID ADMIN ID (" + str(adminIdInput) + "). Try again!")

def user():
    while True:
        print("*" * 28 + "USER OPTIONS" + "*" * 24 + "\n")
        print("*" * 31 + "CHOOSE OPTION" + "*" * 32 + "\n"     
              "\t(L) LOGIN\n"                             
              "\t(R) REGISTER (SIGN-UP)\n"
              "\t(E) EXIT\n" +
              "_" * 72)
        option = str(input("Please Select Your Option: ")).upper()
        if (len(option) == 1):
            if (option == 'L'):                                          
                user_login()
                break
            elif (option == 'R'):
                user_registration()
                break
            elif (option =='E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")

def user_login():
     while True:       
        userId = str(input("PLEASE ENTER USER ID : "))
        filtered_user = list(filter(lambda user: user[0]==userId, list_users))
        if (len(filtered_user) < 1):
            print("\n USER ID NOT FOUND. PLEASE ENTER CORRECT USER ID or REGISTER IF NEW USER \n")
            user_login()
            break
        else:
            filtered_user = filtered_user[0]
            userPassword = str(input("PLEASE ENTER PASSWORD FOR USER ID " + str(userId) + " : "))
            if userPassword == filtered_user[5] :
                print("\n\n WELCOME TO FOOD ORDERING APP " + str(filtered_user[1]) + "\n\n")
                user_options(filtered_user)
                break
            else:
                print("\n" * 10 + "ERROR: INVALID USER PASSWORD. Try again! \n")
                user_login()
    

def user_registration():
    global list_users
    while True:       
        userId = str(input("PLEASE ENTER NEW USER ID: "))
        if userId in [user[0] for user in list_users]:
            print("ENTERED USER ID " + str(userId) + " ALREADY EXISTS. Please Try Again !!")
            user_registration()
        else:
            userName = str(input("PLEASE ENTER FULL NAME: "))
            userNumber = str(input("PLEASE ENTER VALID CONTACT NUMBER : "))
            userEmail = str(input("PLEASE ENTER VALID EMAIL ID : "))
            userAddress = str(input("PLEASE ENTER FULL ADDRESS : "))
            userPassword = str(input("PLEASE CREATE PASSWORD : "))
            print("\n USER " + userName + " CREATED SUCCESSFULLY \n")
            newUser = [userId, userName, userNumber, userEmail, userAddress, userPassword]
            list_users.append(newUser)
            write_new_user_details(newUser)
            user()
            break

def user_options(user):
    while True:
        print("*" * 28 + "HELLO " + str(user[1]).upper() + "*" * 24 + "\n")
        print("*" * 31 + "CHOOSE OPTION" + "*" * 32 + "\n"     
              "\t(N) PLACE NEW ORDER\n"                             
              "\t(H) VIEW ORDER HISTORY\n"
              "\t(U) UPDATE PROFILE\n" 
              "\t(E) EXIT\n" +
              "_" * 72)
        option = str(input("Please Select Your Option: ")).upper()
        if (len(option) == 1):
            if (option == 'N'):
                place_new_order(user)
                break
            elif (option == 'H'):
                view_order_history(user)
                break
            elif (option == 'U'):
                update_user_profile(user)
                break
            elif (option =='E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")

def update_user_profile(user):
    while True:
        print("\n")
        print("*" * 31 + "CHOOSE USER INFORMATION TO UPDATE" + "*" * 32 + "\n"     
              "\t(N) NAME\n"                             
              "\t(C) CONTACT NUMBER\n"
              "\t(I) EMAIL ID\n"
              "\t(A) ADDRESS\n"              
              "\t(P) PASSWORD\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)
        option = str(input("Please Select Your Option: ")).upper()
        if (len(option) == 1):
            if (option == 'N'):
                userName = str(input("PLEASE ENTER NEW FULL NAME : "))
                option = str(input("DO YOU WANT TO EDIT ANY OTHER INFO IN PROFILE " + str(userName) + " (Y/N) : ").upper())
                user[1] = userName
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_users_details()
                        user_options(user)
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
            elif (option == 'C'):
                userNumber = str(input("PLEASE ENTER NEW CONTACT NUMBER : "))
                option = str(input("DO YOU WANT TO EDIT ANY OTHER INFO IN PROFILE " + str(user[1]) + " (Y/N) : ").upper())
                user[2] = userNumber
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_users_details()
                        user_options(user)
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
            elif (option == 'I'):
                userEmail = str(input("PLEASE ENTER NEW EMAIL ID : "))
                option = str(input("DO YOU WANT TO EDIT ANY OTHER INFO IN PROFILE " + str(user[1]) + " (Y/N) : ").upper())
                user[3] = userEmail
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_users_details()
                        user_options(user)
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
            elif (option == 'A'):
                userAddr = str(input("PLEASE ENTER NEW ADDRESS : "))
                option = str(input("DO YOU WANT TO EDIT ANY OTHER INFO IN PROFILE " + str(user[1]) + " (Y/N) : ").upper())
                user[4] = userAddr
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_users_details()
                        user_options(user)
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
            elif (option == 'P'):
                userPwd = str(input("PLEASE ENTER NEW PASSWORD : "))
                option = str(input("DO YOU WANT TO EDIT ANY OTHER INFO IN PROFILE " + str(user[1]) + " (Y/N) : ").upper())
                user[5] = userPwd
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_users_details()
                        user_options(user)
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
            elif (option =='M'):
                user_options(user)
                break
            elif (option =='E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
            
def place_new_order(user):
    global list_foods
    while True:
        tabulate_food_items()
        print('\nPLEASE PLACE AN ORDER FROM ABOVE MENU')
        print('FOR SINGLE FOOD ITEM ENTER FOOD ID IN THE FORMAT [ID]')
        print('FOR MULTIPLE FOOD ITEMS ENTER FOOD IDs IN FORMAT [ID1, ID2]\n')
        order = input("PLEASE ENTER YOUR ORDER : ")
        order = order.lstrip('[')
        order = order.rstrip(']')
        food_ids = order.split(',')
        for i in range(0,len(food_ids)):
            food_ids[i] = int(food_ids[i].strip())
        print('\n')
        for i in range(0,len(food_ids)):
            if food_ids[i] in [food[0] for food in list_foods]:
                filtered_food_item = list(filter(lambda food: food[0]==food_ids[i], list_foods))
                food_item = filtered_food_item[0]
                food_item[6] = food_item[6] - 1
        write_food_items() #Update food items file
        ordered_food_items = list(filter(lambda food: food[0] in food_ids, list_foods))
        ordered_food_items = [sublist[:6] for sublist in ordered_food_items]
        print("*" * 26 + "ORDERED ITEMS" + "*" * 26)
        print('\n')
        print(tabulate(ordered_food_items, headers=['ID', 'FOOD NAME', 'PRICE','CURRENCY','QUANTITY','DISCOUNT %']))
        update_order_history(user,ordered_food_items)
        print("\n (M) MAIN MENU         (E) EXIT\n" + "_" * 72)
        option = input("Please Select Your Operation: ").upper() 
        if (len(option) == 1):
            if (option == 'M'):                                          
                print("\n" * 10)                                        
                user_options(user)
                break
            elif (option =='E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
        

def update_order_history(user,ordered_food_items):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file = open('files/order_history/'+str(user[0])+'.txt','a')
    file.write('*' * 70 + '\n')
    file.write('DATE : ' + dt_string + '\n')
    file.write('-' * 70 + '\n')
    file.write(tabulate(ordered_food_items, headers=['ID', 'FOOD NAME', 'PRICE','CURRENCY','QUANTITY','DISCOUNT %']))
    file.write('\n')
    file.close()
    
def view_order_history(user):
    if os.path.exists('files/order_history/'+str(user[0])+'.txt'):
        file = file = open('files/order_history/'+str(user[0])+'.txt','r')
        for line in file.readlines():
            line = line.rstrip('\n')
            print(line)
    else:
        print(" ---------- NO ORDER HISTORY ----------")
    print("\n (M) MAIN MENU         (E) EXIT\n" + "_" * 72)
    option = input("Please Select Your Operation: ").upper() 
    if (len(option) == 1):
        if (option == 'M'):                                          
            print("\n" * 10)                                        
            user_options(user)
        elif (option =='E'):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
    else:
        print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
    
    
        

def admin_options():
    while True:
        print("*" * 28 + "ADMIN OPTIONS" + "*" * 24 + "\n")
        print("*" * 31 + "CHOOSE OPTION" + "*" * 32 + "\n"     
              "\t(A) ADD FOOD ITEM TO MENU\n"                             
              "\t(U) EDIT FOOD ITEM IN MENU\n"
              "\t(V) VIEW FOOD ITEMS IN MENU\n" 
              "\t(R) REMOVE FOOD ITEM IN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)
        option = str(input("Please Select Your Option: ")).upper()
        if (len(option) == 1):
            if (option == 'A'):                                          
                print("\n" * 10)                                        
                add_food_item()                                          
                break
            elif (option == 'U'):                                        
                print("\n" * 10)                                        
                edit_food_item()                                              
                break
            elif (option == 'V'):                                        
                print("\n" * 10)                                        
                view_food_items()                                              
                break
            elif (option == 'R'):                                        
                print("\n" * 10)                                        
                remove_food_item()                                              
                break
            elif (option =='E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")


        
def file_reader():
    file_foods = open('files/food_items.txt', 'r')
    for i in file_foods:
        list_foods.append(str(i.strip())) 
    file_foods.close()
    i = 0
    while i <= (len(list_foods) - 1):
        pattern = '(\d+)\s([a-zA-Z\s]+)([\d.]+)\s(Rs)\s([0-9a-zA-Z]+)\s([\d.]+)\s(\d+)'
        result = re.findall(pattern,list_foods[i])
        result[0] = list(result[0]) #convert to list
        result[0][0] = int(result[0][0]) #food id
        result[0][1] = result[0][1].strip() #food name
        result[0][2] = float(result[0][2]) #price
        result[0][3] = result[0][3].strip() #Rs
        result[0][4] = result[0][4].strip() #quantity
        result[0][5] = float(result[0][5]) #discount
        result[0][6] = int(result[0][6]) #stock
        list_foods[i] = result[0]
        i+=1
file_reader()   

def food_sorter(): 
    global list_foods
    list_foods = sorted(list_foods, key = lambda food:food[0])
food_sorter()

def tabulate_food_items():
    global list_foods
    print("*" * 26 + "FOOD MENU" + "*" * 26)
    print(tabulate(list_foods, headers=['ID', 'FOOD NAME', 'PRICE','CURRENCY','QUANTITY','DISCOUNT %','STOCK']))

def write_food_items():
    global list_foods
    with open('files/food_items.txt','w') as file_foods:
        for list_food in list_foods:
            for entry in list_food:
                file_foods.write(str(entry)+' ')
            file_foods.write('\n')
        file_foods.close()

def add_food_item():
    global list_foods
    print("*" * 26 + "ADD NEW FOOD ITEM" + "*" * 26)
    while True:
        while True:
            food_id = random. randint(1,200)
            existing_food_ids = [food[0] for food in list_foods]
            if food_id not in existing_food_ids:
                break
        food_id = str(food_id)
        food_name = str(input("ENTER FOOD NAME : "))
        food_price = str(input("ENTER FOOD PRICE :"))
        food_quantity = str(input("ENTER FOOD QUANTITY :"))
        food_discount = str(input("ENTER FOOD DISCOUNT :"))
        food_stock = str(input("ENTER FOOD STOCK :"))
        food_item = [food_id,food_name,food_price,'Rs',food_quantity,food_discount,food_stock]
        with open('files/food_items.txt','a') as file_foods:
            file_foods.write('\n')
            for entry in food_item:
                file_foods.write(entry +' ')
            file_foods.close()
        food_item =[int(food_id),food_name,float(food_price),'Rs',food_quantity,float(food_discount),int(food_stock)]
        list_foods.append(food_item)
        print("\n" + "_" * 72)
        print("\n (M) MAIN MENU         (E) EXIT\n" + "_" * 72)
        option = input("Please Select Your Operation: ").upper() 
        if (len(option) == 1):
            if (option == 'M'):                                          
                print("\n" * 10)                                        
                admin_options()
                break
            elif (option =='E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
            
    
def edit_food_item():
    global list_foods
    tabulate_food_items()
    food_id = int(input("ENTER THE ID OF FOOD ITEM TO EDIT : "))
    if food_id in [food[0] for food in list_foods]:
        filtered_food_item = list(filter(lambda food: food[0]==food_id, list_foods))
        food_item = filtered_food_item[0]
    else:
        print("\n INVALID FOOD ID ENTERED. Please Try Again !! \n")
        edit_food_item()
    
    while True:
        print(tabulate(filtered_food_item, headers=['ID', 'FOOD NAME', 'PRICE','CURRENCY','QUANTITY','DISCOUNT %','STOCK']))
        print("\n")
        print("*" * 31 + "CHOOSE OPTION OF FOOD ITEM TO EDIT" + "*" * 32 + "\n"     
              "\t(N) NAME\n"                             
              "\t(P) PRICE\n"
              "\t(Q) QUANTITY\n" 
              "\t(D) DISCOUNT\n"
              "\t(S) STOCK\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)
        option = str(input("Please Select Your Option: ")).upper()
        if (len(option) == 1):
            if (option == 'N'):                                          
                food_name = str(input("ENTER THE NEW FOOD NAME : "))  
                option = str(input("DO YOU WANT TO EDIT ANY OTHER ENTRY FOR FOOD WITH ID " + str(food_id) + " (Y/N) : ").upper())
                food_item[1] = food_name
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_food_items()
                        admin_options()
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
            elif (option == 'P'):                                        
                food_price = float(input("ENTER THE NEW FOOD PRICE : "))
                food_item[2] = food_price 
                option = str(input("DO YOU WANT TO EDIT ANY OTHER ENTRY FOR FOOD WITH ID " + str(food_id) + " (Y/N) : ").upper())
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_food_items()
                        admin_options()
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")                                            
            elif (option == 'Q'):                                        
                food_quantity = float(input("ENTER THE NEW FOOD QUANTITY : "))
                food_item[4] = food_quantity 
                option = str(input("DO YOU WANT TO EDIT ANY OTHER ENTRY FOR FOOD WITH ID " + str(food_id) + " (Y/N) : ").upper())
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_food_items()
                        admin_options()
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")                                            
            elif (option == 'D'):                                        
                food_discount = float(input("ENTER THE NEW FOOD DISCOUNT % : "))
                food_item[5] = food_discount 
                option = str(input("DO YOU WANT TO EDIT ANY OTHER ENTRY FOR FOOD WITH ID " + str(food_id) + " (Y/N) : ").upper())
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_food_items()
                        admin_options()
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")                                            
            elif (option == 'S'):
                food_stock = float(input("ENTER THE NEW FOOD STOCK : "))
                food_item[6] = food_stock 
                option = str(input("DO YOU WANT TO EDIT ANY OTHER ENTRY FOR FOOD WITH ID " + str(food_id) + " (Y/N) : ").upper())
                if (len(option) == 1):
                    if (option == 'N'):
                        print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                        write_food_items()
                        admin_options()
                        break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!") 
            elif (option =='M'):
                admin_options()
                break
            elif (option =='E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
    

def view_food_items():
    while(True):
        tabulate_food_items()
        print("\n (M) MAIN MENU         (E) EXIT\n" + "_" * 72)
        option = input("Please Select Your Operation: ").upper() 
        if (len(option) == 1):
            if (option == 'M'):                                          
                print("\n" * 10)                                        
                admin_options()
                break
            elif (option =='E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(option) + "). Try again!")
                     
def remove_food_item():
    global list_foods
    tabulate_food_items()
    food_id = int(input("ENTER THE ID OF FOOD ITEM TO REMOVE : "))
    if food_id in [food[0] for food in list_foods]:
        filtered_food_item = list(filter(lambda food: food[0]==food_id, list_foods))
        food_item = filtered_food_item[0]
        for item in list_foods:
            if item[0] == food_item[0]:
                list_foods.remove(item)
        write_food_items()
        print("REMOVED FOOD ITEM WITH ID " + str(food_id) + " FROM THE MENU SUCCESSFULLY")
        admin_options()
    else:
        print("\n INVALID FOOD ID ENTERED. Please Try Again !! \n")
        remove_food_item()


main()
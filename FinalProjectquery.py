#MohammedRangwala

from FinalProjectInventorystore import ElectronicsStoreInventory as store
import csv
class App:
    def __init__(self):
        self.displayMenu()
    #Function to display menu
    def displayMenu(self):
        print("-----------------------------------------------------------Welcome to Electronics Store Inventory-----------------------------------------------")
        print("Select an option from the available options: ")
        print("------------------------------------------")
        print("------------------------------------------")
        print("1- Show Full Inventory \n2- Show Damaged Inventory\n3- Show Past Service Date Inventory\n4- Show Laptop Inventory\n5- Show Phone Inventory\n6- Show tower inventory")
        print("7- Query the user of an item \n8: Quit")
        print("------------------------------------------")
        try:
            option = int(input("Enter your option: "))      #user input
            if(option > 0 and option < 9):
                if (option == 1):
                    self.Inventory("Full Inventory")
                if (option == 2):
                    self.Inventory("Damaged Inventory")
                if (option == 3):
                    self.Inventory("Service Date Inventory")
                if (option == 4):
                    self.Inventory("Laptop Inventory")
                if (option == 5):
                    self.Inventory("Phone Inventory")
                if (option == 6):
                    self.Inventory("Tower Inventory")
                if (option == 7):
                    self.Menu()                                    #user query
                if (option == 8):
                    exit(1)
            else:
                print("Invalid option. Enter a valid option\n")
            try:
                print("\n")
                useroption  = input("Do you want to again display the menu? Enter y for yes and n for no\n")
                if (useroption == "y" or useroption == "Y"):
                    self.displayMenu()
                elif(useroption == "n" or useroption == "N"):
                    print("------------------------------------------Thank you!---------------------------------------------------")
                else:
                    print("Invalid option. Enter a valid option\n")
                    self.displayMenu()
            except Exception as e:
                print(e)
                print("Enter a valid option\n")
                self.displayMenu()

        except Exception as e:
            print(e)
            print("Enter a valid option\n")
            self.displayMenu()
    #Function to show user query menu   
    def Menu(self):
        manufacturer = input("Enter manufacturer name and item type: ")     #take manufacturer name and item type input from user
        items = store.getItem("Your item is: ",manufacturer)                #calling get item method from Electronics Store Inventory class to get items of specific manufacturer and item type
        if(items != None):                                                  #items found
            self.displayItems(items)                                        #calling displayItems method to display found items
        else:
            print("No such item in inventory ")                             #no items found
            print("\n")
        print("Select an option from these three available options: ")
        print("------------------------------------------")
        option = int(input("1- Show Main menu \n 2- Continue\n 3- Quit\n "))    #user input
        if(option == 1):
            self.displayMenu()                                                  #display main menu
        if (option == 2):
            self.Menu()                                                         #display current menu
        if(option == 3):
            exit(1)
        
    #Function prints inventory according to the inventory type entered by the user from main menu
    def Inventory(self, selectedtype):
        file = ""                                                   #stores file name 
        if(selectedtype == "Full Inventory"):
            file = 'FullInventory.csv'
        if(selectedtype == "Laptop Inventory"):
            file = 'LaptopInventory.csv'
        if(selectedtype == "Tower Inventory"):
            file = 'TowerInventory.csv'
        if(selectedtype == "Phone Inventory"):
            file = 'PhoneInventory.csv'
        if(selectedtype == "Damaged Inventory"):
            file = 'DamagedInventory.csv'
        if(selectedtype == "Service Date Inventory"):
            file = 'PastServiceDateInventory.csv'
        # opens the required file based on user's choice
        requiredfile = "Output/" + file                       # required file path
        itemlist = []                                               #list to display items
        with open(requiredfile, newline='') as csvfile:             #reads the items from the required file row wise
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                itemlist.append(row)                                #stores row wise extracted items from required in itemlist
        print("--------------------------------------------------------------------------------")
        print("%-12s %-17s %-13s %-10s %-15s %-10s" %
              ("Item ID","Manufacturer Name","Item Type","Price","Service Date","Condition"))
        print("--------------------------------------------------------------------------------")

        for item in itemlist:
            Itemstr = "".join(item)                                   #concatenates list items in a string
            iteminfo = Itemstr.split(",")                               #splitting item strings and stores in iteminfo list
            print("%-12s %-17s %-13s %-10s %-15s %-10s"
                  % (iteminfo[0],iteminfo[1],iteminfo[2],iteminfo[3],iteminfo[4],iteminfo[5]))      #display required items details
    #Function to show the data requested by user query
    def displayItems(self, items):
        print("Your item is: \n")
        print("%-12s %-14s %-13s %-10s" % ("Item ID","Manufacturer Name","Item Type","Price"))
        print("---------------------------------------------------")
        iteminfo = items[0].values()            #stores items data based on user selected item type
        iteminfo = list(iteminfo)               #list contaiins required items
        print("%-12s %-17s %-13s %-10s" % (iteminfo[0],iteminfo[1],iteminfo[2],iteminfo[3]))      #display required items details
        print("\nYou may also consider:\n" )
        print("%-12s %-17s %-13s %-10s" % ("Item ID","Manufacturer Name","Item Type","Price"))
        print("---------------------------------------------------")
        iteminfo = items[1].values()         #stores items data based on user selected manufacturer
        iteminfo = list(iteminfo)           #list contaiins required items
        print("%-12s %-17s %-13s %-10s" % (iteminfo[0],iteminfo[1],iteminfo[2],iteminfo[3]))    #display required items details
        print()
if __name__ == "__main__":
    App()

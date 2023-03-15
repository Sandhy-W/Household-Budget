import os
# from sys import argv

class Biils:

    def __init__(self):
        os.system('cls')
        self.tot_elecbill = float (input ("How much is the total bill of Electricity? \n> "))
        self.tot_gasbill = float (input("How much is the total bill of the gas? \n> "))
        self.tot_tenants = int(input ("How many tenent for Holder house? \n> "))
        os.system ('pause')
        self.elecbill()

    def elecbill (self):
        os.system ('cls')
        print ("\nThe Electricity Bill?")
        self.Edaily_usage = self.tot_elecbill / 90 #90 days represent the 90 days that consist of three months
        self.Eusage_perTent = self.Edaily_usage / self.tot_tenants
        print ("* Base on the input before, the daily electricity usage is $", '{:.2f}'.format(self.Edaily_usage))
        print ("* The daily usages per a tenant is $", '{:.2f}'.format(self.Eusage_perTent))
        self.gasbill()

    def gasbill(self):
        print ("\nThe Gas Bill?")
        self.Gdaily_usage = self.tot_gasbill / 90 #90 days above consist the three months
        self.Gusage_perTenant = self.Gdaily_usage / self.tot_tenants
        print ("* Base on the input above, the daily gas usage is $", '{:.2f}'.format(self.Gdaily_usage))
        print ("* The daily gas usage per a tenent is $", '{:.2f}'.format(self.Gusage_perTenant))
        os.system('pause')
        self.individual_calculation()

    # def list_tanants(self):
    #     tenants_name = []
    #
    #     while True:
    #         name = input ("\nEnter the tenant's name : ")
    #         tenants_name.append (name)
    #
    #         choice = input ("Do you want enter another name ? ( y / n) : ")
    #         if choice == 'n':
    #             break
    #
    #     print ("\n")
    #     for element in tenants_name:
    #          print ('*', element)



    def individual_calculation(self):
        indi_name = input ("\nEnter your name? \n> ")
        self.indi_days = int(input("How long is your staying period? \n> "))
        self.indi_elecbill = self.indi_days / self.Edaily_usage
        self.indi_gasbill = self.indi_days / self.Gdaily_usage
        print (f"\n* {indi_name}'s individu electric bill is $", '{:.2f}'.format(self.indi_elecbill))
        print (f"\n* And {indi_name}'s' individu gas bill is $", '{:.2f}'.format(self.indi_gasbill))
        print (f"\n* Total bill that need to be paid based on both Gas and electricity is $", '{:.2f}'.format(self.indi_gasbill + self.indi_elecbill))
        os.system('pause')
        self.continue_caculate()

    def continue_caculate (self):
        os.system('cls')
        choise = input ("do you want to calculate the next tenant (Yes or No)?  ")
        if choise == 'Yes':
            self.individual_calculation()
        elif choise == 'No':
            exit
        
        else:
            print ("Type the Yes or No for the option")



    # def assign (self):
    #     indi_name = input ("\nEnter your name? \n> ")
    #     txt = open(filename)
    #     i = 0
    #     line [i] = input (f"How much is {indi_name}'s total bill? ")
    #     for i in range (5):
    #         if i > 5:
    #             break
    #         else:
    #             line [i]



    #     target.write(line [i])
    #     target.close()
Biils()

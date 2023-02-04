message = ""

coffee = input("Do you only want coffee? ")

if coffee == "yes" or coffee == "no":
    meal = input("Do you want a meal? ")

    if meal == "yes" or meal == "no":
        snack = input("Do you want a snack? ")

        if snack == "yes" or snack == "no":
            message = "\nHere are your choices:\n"

            if coffee == "yes":
                
                if meal == "yes":

                    if snack == "yes" or snack == "no":
                        message += "Toast Bakery\n" + \
                                   "Dialog Cafe\n"
                else: 
                    if snack == "yes": #if coffee and snack only are yes
                        message += "Starbucks\n" + \
                                   "Alfred Coffee\n" + \
                                   "Joe and The Juice\n"
                    else: #if only coffee is yes
                        message += "Starbucks\n" + \
                                   "Alfred Coffee\n" + \
                                   "Joe and The Juice\n" + \
                                   "WFM Coffee and Juice Bar\n"
            else: # if coffee is no

                if meal == "yes":

                    if snack == "yes" or snack == "no":
                        message += "Toast Bakery/Dialog Cafe\n"

                else: # meal == "no"

                    if snack == "yes":
                        message += "Starbucks\n" + \
                                   "Alfred Coffee\n" + \
                                   "Joe and The Juice\n"                               
        else:
            message = "Enter yes or no and try again."
    
    else:
        message = "Enter yes or no and try again."

else:
    message = "Enter yes or no and try again"


print(message)

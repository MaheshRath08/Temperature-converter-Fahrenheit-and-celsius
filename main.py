def convert_to_F(c):            #define function for conversion to Fahrenheit
    F = (1.8 * c) + 32
    print(str(F)+"°")
  
def convert_to_C(f):            #define function for conversion to Celsius
    C = (f - 32) / 1.8
    print(str(C)+"°")
    
while(True):                    #Run the operation into a loop for contious inputs and value error 
    try:                        
        tempInput = float(input("Write the temperature:\n"))            #user input for tempertaure
        convertTo = input("Convert to what ? 'f' or 'c' ? \n")          #user input for choosing inbetween f or c for converion
        if (convertTo == "f" or convertTo =="F"):
            convert_to_F(tempInput) 
        elif (convertTo == "c" or convertTo == "C"):
            convert_to_C(tempInput)
        else:
            print("!!!!!!!------select either 'f' or 'c'!!!!!")
        continue
    except ValueError:                        #error handling for valueError
        print("!!!!!!!!!!!   Make sure to type in numerical value   !!!!!!!!!!!")
        continue
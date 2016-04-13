global variable_holder 
global registers
global text_array
global arr_values
global arr_used

arr_used = 0
arr_values = {}
text_array = []
variable_holder = {}
registers = {"R1": 1,"R2":10, "R3":0, "R4":0,"R5":0,"R6":0,"R7":0,"R8":0, "R9":0, "R10":0,
         "R11": 0, "R12":0, "R13":0, "R14":0,"R15":0,"R16":0,"R17":0,"R18":0, "R19":0, "R20":0,
         "R21": 0, "R22":0, "R23":0, "R24":0,"R25":0, "R26":0,"R27":0,"R28":0, "R29":0, "R30":0,
         "R31": 1, "R32":0, "R33":0, "R34":0,"R35":0, "R36":0,"R37":0,"R38":0, "R39":0, "R40":0,
         "R41": 1, "R42":0, "R43":0, "R44":0,"R45":0, "R46":0,"R47":0,"R48":0, "R49":0, "R50":0,
         "R51": 1, "R52":0, "R53":0, "R54":0,"R55":0, "R56":0,"R57":0,"R58":0, "R59":0, "R60":0,
         "R61": 1, "R62":0, "R63":0, "R64":0}

def readFile():
    text = open ('Benchmark2.txt', 'r')
    global arr_used
    for file_line in text.readlines():
        line = file_line.split()
        text_array.append(file_line)
        arr_used = arr_used + 1
        if (len(line) >= 2):
                if line[0]  == 'PLUS':
                     plus(line)
                elif line[0] == 'MINU':
                    subt(line)
                elif line[0] == 'MULT':
                    mult(line)
                elif line[0] == 'DIVI':
                    divi(line)
                elif line[0] == 'DISP':
                    disp(line)
                elif line[0] == 'MODU':
                    modu(line)
                elif line[0] == 'JUMP':
                    jump(line)
                elif line[0] == 'LOOP':
                    loop(line)
                elif line[0] == 'ARRA':
                    arr_name = line[1]
                    arr_values[arr_name] = []
                elif line[0] == 'INCR':
                    incr(line)
                elif line[0] == 'DECR':
                    decr(line)
                elif line[0] == 'FIND':
                    find(line)
                elif line[0]== "SAVE":
                    save(line)
                else:
                    initvar(line)
        elif len(line) == 1: 
                if(line[0]== 'QUIT'):
                        quit(line)
                elif(line[0]== 'CLRR'):
                       clrr()
                elif(line[0] == 'TAKE'):
                    take(line)
                else:
                    arr_values[arr_name].append(int(line[0]))
    text.close()
    return

def plus(argument):
    temp = 0
    first_var = argument[1]
    second_var = argument[2]

    #register to Register 
    if(first_var[0] == 'R' ):
        if(second_var[0] == 'R'):
            for word in argument: 
                for key,value in registers.items(): 
                    if(word == key):
                        temp = temp + value 
            registers[argument[1]] = temp
#Add a number to a register 
        elif(second_var.isdigit()):
            registers[first_var] += int(second_var)
#memory to register
        elif (first_var[0] == 'R'):
            for key, value in registers.items():
                if( first_var == key):
                    temp = value
            for key, value in variable_holder.items():
                if(second_var == key):    
                	temp = temp + int(value)
            registers[first_var] = temp         
                
    else:
        for word in argument: 
            if(word != "PLUS"):
                for k, v in variable_holder.items():
                    if( word == k):
                        temp = temp + v
        variable_holder[argument[1]] = temp
    return

def subt(argument):
    temp = 0
    first_var = argument[1]
    second_var = argument[2]

    #register to Register 
    if(first_var[0] == 'R' ):
        if(second_var[0] == 'R'):
            for word in argument: 
                for key,value in registers.items(): 
                    if(word == key):
                        temp = temp +value 
            registers[argument[1]] = temp
#Add a number to a register 
        elif(second_var.isdigit()):
             registers[first_var] -= int(second_var)
             #resgisters and varibles 
        elif (second_var[0] != 'R'):
            for key, value in registers.items():
                if( first_var == key):
                    temp = value
            for key, value in variable_holder.items():
                if(second_var == key):    
                    temp = temp - value 
        registers[first_var] = temp
    else:
                 
        for word in argument: 
            if(word != "PLUS"):
                for k, v in variable_holder.items():
                    if( word == k):
                        temp = temp - v
        variable_holder[argument[1]] = temp
        
    return

def mult(argument):
    temp = 1
    first_var = argument[1]
    second_var = argument[2]

    #register to Register 
    if(first_var[0] == 'R' ):
        if(second_var[0] == 'R'):
            for word in argument: 
                for key,value in registers.items(): 
                    if(word == key):
                        temp = temp * value 
            registers[argument[1]] = temp
#Add a number to a register 
        elif(second_var.isdigit()):
            registers[first_var] *= int(second_var)
#resgisters and varibles 
        elif (second_var[0] != 'R'):
            for key, value in registers.items():
                if( first_var == key):
                    temp = value
            for key, value in variable_holder.items():
                if(second_var == key):    
                    temp *= value 
        registers[first_var] = temp         
    else:
    #memory to memory                  
        for word in argument: 
            if(word != "PLUS"):
                for k, v in variable_holder.items():
                    if( word == k):
                        temp = temp * v
        variable_holder[argument[1]] = temp
    return

def divi(argument):
    temp = 0
    temp2= 0
    result = 0
    first_var = argument[1]
    second_var = argument[2]

    if(first_var[0] == 'R'):
        if(second_var[0] == 'R'):
            temp = registers[argument[1]]
            temp = registers[argument[2]]
            result = temp/temp2
            registers[argument[1]] = result
        elif(second_var.isdigit()):
            temp = registers[argument[1]]
            temp2 = int(second_var)
            result = temp/temp2
            registers[argument[1]] = result
        elif(second_var[0] != 'R'):
            temp = registers[argument[1]]
            temp2 = variable_holder[second_var]
            result = temp/temp2
            registers[first_var] = result

    temp = variable_holder[argument[1]]
    temp2= variable_holder[argument[2]]
    result = temp/temp2
    variable_holder[argument[1]] = result 
    return

def take(argument):
     num = 0
     variable = raw_input("Enter name of Variable")
     num = raw_input("Enter the value of the")
     variable_holder[variable] = num
     return 
    

def initvar(argument):

    var_name = argument[0]
    var_int = int(argument[1]) 
    variable_holder[var_name] = var_int
    return 

def disp(argument):
    
    variable = argument[1]
    if(variable[0] != 'R'):
        for key, value in variable_holder.items():
            if(argument[1] == key):
                print(value)
    else:
        for key, value in registers.items():
            if(variable == key):
                print value
             
def modu(argument):

    if(variable_holder[argument[1]] > variable_holder[argument[2]]):
         variable_holder[argument[1]] = variable_holder[argument[1]] % variable_holder[argument[2]]
    return 

def incr(argument): 
    #add code for registers 
    for key, value in variable_holder.items():
        if(argument[1] == key):
            variable_holder[argument[1]] = value + 1
    return 
def decr(argument):
    #add code for registers
    for key, value in variable_holder.items():
        if(argument[1] == key):
            variable_holder[argument[1]] = value - 1
    return 
def save(argument):
    for name,val in registers.items():
        if(argument[1] == name):
            for key, value in variable_holder.items():
                    if(argument[2] == key ):
                        registers[argument[1]] = value
    return 
    #add code for registers
def jump(argument):

    index = int(argument[1])
    text_line = text_array[index-1] #inserts at zero
    line = text_line.split()
    if line[0]  == 'PLUS' :
        plus(line)
    elif line[0] == 'MINU':
        subt(line)
    elif line[0] == 'MULT':
        mult(line)
    elif line[0] == 'DIVI':
        divi(line)
    elif line[0] == 'TAKE':
        take(line)
    elif line[0] == 'DISP':
        disp(line)
    elif line[0] == 'MODU':
        modu(line)
    elif line[0] == 'QUIT':
        quit(line)    
    return     
def clrr():

    for key,value in registers.items():
        registers[key] = 0 
    return
def loop(argument):

    counter = 1
    index = int(argument[1])

    while(index < arr_used-1):
        start = text_array[index]
        line = start.split()
        counter = int(argument[2])
        while(counter != 0):
            counter = counter -1
            if line[0]  == 'PLUS' :
                plus(line)
            elif line[0] == 'MINU':
                subt(line)
            elif line[0] == 'MULT':
                mult(line)
            elif line[0] == 'DIVI':
                divi(line)
            elif line[0] == 'TAKE':
                take(line)
            elif line[0] == 'DISP':
                disp(line)
            elif line[0] == 'MODU':
                modu(line)
            
        index = index + 1
    return    
def arra(argument):
    return 
def find (argument):
    found = False
    for key,values in arr_values.items():
        if(argument[1]==key):
            for i in values:
                if(int(argument[2]) == i):
                    found = True 
    if(found):
        print "Item Found"
    else:
        print "Item NOT found"
    return
def quit(argument):
    exit(0)
    return 

def main():
    readFile()
    return
main()

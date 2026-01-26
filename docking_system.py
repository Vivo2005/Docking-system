#part 1 assign value and name 
def Value(a):
    A=(a).strip('£$')
    return (float(A))


ship_name= (input("Ship Name?")).strip().replace(" ","_").upper()
cargo_value= Value(input("Estimated cargo value?"))
print(cargo_value,"|", ship_name)

#part2 assign a docking bay
Reg_number=int(input("What is your ships registration number?"))

def assign_bay(a):
    if (a%2)==0:
        return ("starboard bay")
    else:
        return ("port bay")


print(ship_name,"please go to",assign_bay(Reg_number))

#part 3 clearance level
sheild_integrity=int(input("sheild integrity?").strip("%"))
def clearance (a):
    if a >= 90:
        return("priority clearance")
    elif a >= 50:
        return("standard clearance")
    elif a >= 20:
        return("restricted clearance")
    else:
        return("Docking denied-unsafe")
print (clearance(sheild_integrity))

#part 4 crew routing




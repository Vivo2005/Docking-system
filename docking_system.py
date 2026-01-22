
ship_name= (input("Ship Name?")).replace(" ","_").upper()
cargo_value= value(input("Estimated cargo value?"))

def value(a):
    A=(a).strip('£$')
    return (float(A))
print(cargo_value)

"""docstring module"""
def seperate_unit(unit):
    """Seperate unit function"""
    # 1-10
    units = []
    unitget1 = unit - max(unit-10,0)
    units.append(unitget1)
    left1 = unit - unitget1
    # 11-50
    unitget2 = left1 - max(left1-40,0)
    units.append(unitget2)
    left2 = left1 - unitget2
    # 51-100
    unitget3 = left2 - max(left2-50,0)
    units.append(unitget3)
    left3 = left2 - unitget3
    # 101-200
    unitget4 = left3 - max(left3-100,0)
    units.append(unitget4)
    left4 = left3 - unitget4
    # 201++
    unitget5 = left4
    units.append(unitget5)
    return units
def calculate_ft(units):
    """calculate FT"""
    ft = 0
    for i in units:
        ft += i*0.5
    return ft
def calculate_price_per_unit(units):
    """calculate unit to price baht (NO VAT)"""
    total = 0
    for i,v in enumerate(units):
        if not i:
            total += v*5
        elif i == 1:
            total += v*7
        elif i == 2:
            total += v*10
        elif i == 3:
            total += v*12
        elif i == 4:
            total += v*15
    return total
def main():
    """main function"""
    unit_input = float(input())
    units = seperate_unit(unit_input)
    # FT
    ft = calculate_ft(units)
    # calculate Unit With Vat
    unit_cal = calculate_price_per_unit(units)
    # Result
    result = (unit_cal*1.07)+ft
    print(f"{result:.1f}")
main()

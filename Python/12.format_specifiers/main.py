price1 = 3234.14156
price2 = -345234.235
price3 = 12234234.23

# upto 2 decimals
print(f"price2: ${price2:.2f}")
print(f"price3: ${price3:.1f}")
print(f"price1: ${price1:.2f}")
#spacing
print(f"price2: ${price2:10}")
print(f"price3: ${price3:10}")
print(f"price1: ${price1:10}")
#padding
print(f"price2: ${price2:010}")
print(f"price3: ${price3:010}")
print(f"price1: ${price1:010}")
#justify right
print(f"price2: ${price2:>10}")
print(f"price3: ${price3:>10}")
print(f"price1: ${price1:>10}")
#justify left
print(f"price2: ${price2:<10}")
print(f"price3: ${price3:<10}")
print(f"price1: ${price1:<10}")
#center
print(f"price2: ${price2:^10}")
print(f"price3: ${price3:^10}")
print(f"price1: ${price1:^10}")
#number signs
print(f"price2: ${price2:+10}")
print(f"price3: ${price3:+10}")
print(f"price1: ${price1:+10}")
#commas in numbers
print(f"price2: ${price2:,}")
print(f"price3: ${price3:,}")
print(f"price1: ${price1:,}")
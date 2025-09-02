#args

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(add(1,2,3,4,5,6,7,8,9,10))


#kwargs

def print_address(**address):
    print(f"i live in {address['street']}, {address['city']}, {address['state']},and my zipcode is {address['pincode']}")

print_address(street="Karwar",city="Jodhpur",state="Rajasthan",pincode=342304)
def get_age():
    age = int(input("Enter your age in years: "))
    if age > 60:
        raise Exception('Too old')
    else:
        return age


age = get_age()
max_heart_rate = 206.9 - (0.67 * age)  # as per Med Sci Sports Exerc.
print(f"Max heart rate is {max_heart_rate}")
target = 0.65 * max_heart_rate
print("Your target fat-burning heart rate is ", target)

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

#BMI form is weight/(height * height)
float_height = float(height)
int_weight = int(weight)

bmi = int_weight / (float_height * float_height)

int_bmi = int(bmi)

print(int_bmi)
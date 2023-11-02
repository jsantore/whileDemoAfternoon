
all_done = False
while not all_done:
    answer = float(input("Please enter a GPA from 0.0 to 4.0:"))
    #if answer >=0.0 <=4.0:
    if 0.0<= answer <=4.0:
        all_done = True
print(f"The gpa was {answer}")
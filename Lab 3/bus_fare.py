# The following function is provided to you.
# Do not modify the function definition!
def get_personal_info():
    """
    This function prompts the user for his/her name, gender, age and whether
    or not he/she is a student.
    The function returns a tuple that contains all the information entered
    by the user.
    """
    name = input("What's your name? ")
    gender = input("What's your gender? [M|F] ")
    age = int(input("What's your age? "))
    is_student = input("Are you a student? [yes|no] ")
    return (name, gender, age, is_student == 'yes')

# Write your code below:
name, gender, age, is_student = get_personal_info()

if age == "M":  
    title = "Mr."
else: 
    title = "Ms." 

if age >= 60: 
    print (title, name + ",", "you can get concessionary fare for senior citizens.")

elif age > 6: 
    if is_student == "yes": 
        print (title, name + ",","you can get concessionary fare for students.")
    else: 
        print (title, name + ",","you need to pay full fare.")
    
else:
    print (str(name) +  ",","you can travel for free.")

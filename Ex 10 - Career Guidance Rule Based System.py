RollNo : 92600584051
Name   : Dwarkesh Parmar

# CAREER GUIDENCE SYSTEM
"""

do you like coding?yes
do you like mathematics?yes
do you like biology?no
do you like drawing?yes

====== career suggestion ======

suggested career : software engineer / computer scientist
thankyou for using the career guidance expert system!

"""
print("==============================")
print("    CAREER GUIDENCE SYSTEM    ")
print("==============================")

Coding = str(input("Do You Like Coding ? yes / no : "))
Mathematics = str(input("Do You Like Mathematics ? yes / no : "))
Biology = str(input("Do You Like Biology ? yes / no : "))
Drawing = str(input("Do You Like Drawing ? yes / no : "))

if(Coding == "no" and Mathematics == "no" and Biology == "no" and Drawing == "no"):

    print("Explore Your Interests and Career Option Further.")

elif(Coding == "no" and Mathematics == "no" and Biology == "no" and Drawing == "yes"):

    print("Graphic Designer / Animator.")

elif(Coding == "no" and Mathematics == "no" and Biology == "yes" and Drawing == "no"):

    print("Pharmacist / Nurse")

elif(Coding == "no" and Mathematics == "no" and Biology == "yes" and Drawing == "yes"):

    print("Medical Illustrator / Healthcare Educator")

elif(Coding == "no" and Mathematics == "yes" and Biology == "no" and Drawing == "no"):

    print("Engineer / Data Analyst")

elif(Coding == "no" and Mathematics == "yes" and Biology == "no" and Drawing == "yes"):

    print("Architect")

elif(Coding == "no" and Mathematics == "yes" and Biology == "yes" and Drawing == "no"):

    print("Doctor")

elif(Coding == "no" and Mathematics == "yes" and Biology == "yes" and Drawing == "yes"):

    print("Medical illustrator / Biomedical Designer")

elif(Coding == "yes" and Mathematics == "no" and Biology == "no" and Drawing == "no"):

    print("Programmer / Web Developer")

elif(Coding == "yes" and Mathematics == "no" and Biology == "no" and Drawing == "yes"):

    print("Web Designer / UIUX Designer")

elif(Coding == "yes" and Mathematics == "no" and Biology == "yes" and Drawing == "no"):

    print("Health App Developer")

elif(Coding == "yes" and Mathematics == "no" and Biology == "yes" and Drawing == "yes"):

    print("Medical Illustrator")

elif(Coding == "yes" and Mathematics == "yes" and Biology == "no" and Drawing == "no"):

    print("Software Engineer / Computer Scientist")

elif(Coding == "yes" and Mathematics == "yes" and Biology == "no" and Drawing == "yes"):

    print("Game Developer / UI Engineer")
    
elif(Coding == "yes" and Mathematics == "yes" and Biology == "yes" and Drawing == "no"):

    print("Bioinformatics Scientist")

elif(Coding == "yes" and Mathematics == "yes" and Biology == "yes" and Drawing == "yes"):

    print("Biomedical Software Engineer / Medical Technology Specialist")

else:

    print("Wrong Input")


print("\n")
print("Thankyou For Using The Career Guidance Expert System!")

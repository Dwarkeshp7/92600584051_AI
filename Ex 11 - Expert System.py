RollNo : 92600584051
Name   : Dwarkesh Parmar

#Expert System
#Answer the following qustions with yes or no.
# Like this :
    # Do you have fever ? : yes / no
    # Do you have cough ? : yes / no
    # Do you have headache ? : yes / no

print("========== Expert System ==========")

Fever = input("Do you have fever ? : ").lower()
Cough = input("Do you have cough ? : ").lower()
Headache = input("Do you have headache ? : ").lower()


if Fever == "no" and Cough == "no" and Headache == "no":
    print("You seem to be Healthy.")

elif Fever == "Yes" and Cough == "no" and Headache == "no":
    print("You may have a Mild infection.")

elif Fever == "no" and Cough == "yes" and Headache == "no":
    print("You may have a Throat infection or Mild Cold.")

elif Fever == "no" and Cough == "no" and Headache == "yes":
    print("You may have Stress , Migraine , or Fatigue.")

elif Fever == "yes" and Cough == "yes" and Headache == "no":
    print("You may have Flu.")

elif Fever == "yes" and Cough == "no" and Headache == "yes":
    print("You may have Viral Fever.")

elif Fever == "no" and Cough == "yes" and Headache == "yes":
    print("You may have Common Cold.")

elif Fever == "yes" and Cough == "yes" and Headache == "yes":
    print("You may have Flu or a Viral infection.")

else:
    print("Invlid Input")

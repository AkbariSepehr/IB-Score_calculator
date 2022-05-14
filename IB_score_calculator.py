import time

print('''

██╗██████╗░  ░██████╗░█████╗░░█████╗░██████╗░███████╗
██║██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║██████╦╝  ╚█████╗░██║░░╚═╝██║░░██║██████╔╝█████╗░░
██║██╔══██╗  ░╚═══██╗██║░░██╗██║░░██║██╔══██╗██╔══╝░░
██║██████╦╝  ██████╔╝╚█████╔╝╚█████╔╝██║░░██║███████╗
╚═╝╚═════╝░  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝

''')
print("program by Sepehr")

subjects = ["Language & Literature (G1)", "Language Acquisition (G2)", "Individuals and Societies (G3)",
            "Experimental Sciences (G4)", "Mathematics (G5)", "The Arts (G6)"]

s1_score = 0
s2_score = 0
s3_score = 0
s4_score = 0
s5_score = 0
s6_score = 0
core_score = 0

flag = True

while flag:

    q1 = input("\n\nWould you like to add your own subjects? \n respond with [Y/N]: ").upper()

    time.sleep(0.5)

    if q1 == "Y":
        for i in range(0, 6):
            subjects[i] = str(input("\nWhat subject do you take in " + subjects[i] + "? ")).upper()
        flag = False

        time.sleep(0.5)
    if q1 == "N":
        flag = False

        time.sleep(0.5)

################################################################################

#first subject
print("\n\nlets begin with "+subjects[0]+" :)")
print("\nTo calculate your IB score, we need subject specific grade boundries.")
print("This is the default grade boundry: ")
print("seven = 85% \nsix = 70% \nfive = 55% \nfour = 48% \nthree = 30% \ntwo = 20% \none = 5%")
gb_in = input("If you like to continue with this default grade boundry respond with [Y], if you wish to edit, respond with [N]: ").upper()
if gb_in == "N":
    s1_seven = float((input("\nWhat is the grade boundry for a seven? \n do NOT add precenatage sign(%): ")))
    s1_six = float((input("What is the grade boundry for a six? \n do NOT add precenatage sign(%): ")))
    s1_five = float((input("What is the grade boundry for a five? \n do NOT add precenatage sign(%): ")))
    s1_four = float((input("What is the grade boundry for a four? \n do NOT add precenatage sign(%): ")))
    s1_three = float((input("What is the grade boundry for a three? \n do NOT add precenatage sign(%): ")))
    s1_two = float((input("What is the grade boundry for a two? \n do NOT add precenatage sign(%): ")))
    s1_one = float((input("What is the grade boundry for a one? \n do NOT add precenatage sign(%): ")))

    time.sleep(0.2)
if gb_in == "Y":
    print("\nGreat!")
    s1_seven = 1000.0
    s1_six = 1000.0
    s1_five = 1000.0
    s1_four = 1000.0
    s1_three = 1000.0
    s1_two = 1000.0
    s1_one = 1000.0
    time.sleep(0.2)

s1_tests = int(input("\nhow many summatives were conducted in "+subjects[0]+"? "))

s1_max_sum = 0
s1_grade_sum = 0

for i in range(0,s1_tests):
    s1_max = int(input(f"\nwhat was the maximum marks in test{ i+1 }? "))
    s1_max_sum = s1_max_sum + s1_max

    time.sleep(0.2)

for i in range(0,s1_tests):
    s1_grade = int(input(f"\nwhat was the marks awarded to you in test{ i+1 }? "))
    s1_grade_sum = s1_grade_sum + s1_grade
    continue

precentage = (s1_grade_sum / s1_max_sum) * 100
print(" ")
print(" ")
print(" ")
flag1 = True
while flag1:
    if (precentage >= s1_seven) or (precentage >= 85):
        s1_score = 7
        print("your score in this subject is 7")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s1_six) or (precentage >= 70):
        s1_score = 6
        print("your score in this subject is 6")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s1_five) or (precentage >= 55):
        s1_score = 5
        print("your score in this subject is 5")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s1_four) or (precentage >= 48):
        s1_score = 4
        print("your score in this subject is 4")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s1_three) or (precentage >= 30):
        s1_score = 3
        print("your score in this subject is 3")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s1_two) or (precentage >= 20):
        s1_score = 2
        print("your score in this subject is 2")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s1_one) or (precentage >= 5):
        s1_score = 1
        print("your score in this subject is 1")
        flag1 = False
        break
        time.sleep(0.5)
    else:
        s1_score = 0
        print("FAILED")
        flag1 = False
        break
        time.sleep(0.5)

################################################################################

#Second subject
print("\n\nlets move on to "+subjects[1]+" :)")
print("\nTo calculate your IB score, we need subject specific grade boundries.")
print("This is the default grade boundry: ")
print("seven = 85% \nsix = 70% \nfive = 55% \nfour = 48% \nthree = 30% \ntwo = 20% \none = 5%")
gb_in = input("If you like to continue with this default grade boundry respond with [Y], if you wish to edit, respond with [N]: ").upper()
if gb_in == "N":
    s2_seven = float((input("\nWhat is the grade boundry for a seven? \n do NOT add precenatage sign(%): ")))
    s2_six = float((input("What is the grade boundry for a six? \n do NOT add precenatage sign(%): ")))
    s2_five = float((input("What is the grade boundry for a five? \n do NOT add precenatage sign(%): ")))
    s2_four = float((input("What is the grade boundry for a four? \n do NOT add precenatage sign(%): ")))
    s2_three = float((input("What is the grade boundry for a three? \n do NOT add precenatage sign(%): ")))
    s2_two = float((input("What is the grade boundry for a two? \n do NOT add precenatage sign(%): ")))
    s2_one = float((input("What is the grade boundry for a one? \n do NOT add precenatage sign(%): ")))

    time.sleep(0.2)
if gb_in == "Y":
    print("\nGreat!")
    s2_seven = 1000.0
    s2_six = 1000.0
    s2_five = 1000.0
    s2_four = 1000.0
    s2_three = 1000.0
    s2_two = 1000.0
    s2_one = 1000.0
    time.sleep(0.2)

s2_tests = int(input("\nhow many summatives were conducted in "+subjects[1]+"? "))

s2_max_sum = 0
s2_grade_sum = 0

for i in range(0,s2_tests):
    s2_max = int(input(f"\nwhat was the maximum marks in test{ i+1 }? "))
    s2_max_sum = s2_max_sum + s2_max

    time.sleep(0.2)

for i in range(0,s2_tests):
    s2_grade = int(input(f"\nwhat was the marks awarded to you in test{ i+1 }? "))
    s2_grade_sum = s2_grade_sum + s2_grade
    continue

precentage = (s2_grade_sum / s2_max_sum) * 100
print(" ")
print(" ")
print(" ")
flag1 = True
while flag1:
    if (precentage >= s2_seven) or (precentage >= 85):
        s2_score = 7
        print("your score in this subject is 7")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s2_six) or (precentage >= 70):
        s2_score = 6
        print("your score in this subject is 6")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s2_five) or (precentage >= 55):
        s2_score = 5
        print("your score in this subject is 5")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s2_four) or (precentage >= 48):
        s2_score = 4
        print("your score in this subject is 4")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s2_three) or (precentage >= 30):
        s2_score = 3
        print("your score in this subject is 3")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s2_two) or (precentage >= 20):
        s2_score = 2
        print("your score in this subject is 2")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s2_one) or (precentage >= 5):
        s2_score = 1
        print("your score in this subject is 1")
        flag1 = False
        break
        time.sleep(0.5)
    else:
        s2_score = 0
        print("FAILED")
        flag1 = False
        break
        time.sleep(0.5)

################################################################################

#Third subject
print("\n\nlets move on to "+subjects[2]+" :)")
print("\nTo calculate your IB score, we need subject specific grade boundries.")
print("This is the default grade boundry: ")
print("seven = 85% \nsix = 70% \nfive = 55% \nfour = 48% \nthree = 30% \ntwo = 20% \none = 5%")
gb_in = input("If you like to continue with this default grade boundry respond with [Y], if you wish to edit, respond with [N]: ").upper()
if gb_in == "N":
    s3_seven = float((input("\nWhat is the grade boundry for a seven? \n do NOT add precenatage sign(%): ")))
    s3_six = float((input("What is the grade boundry for a six? \n do NOT add precenatage sign(%): ")))
    s3_five = float((input("What is the grade boundry for a five? \n do NOT add precenatage sign(%): ")))
    s3_four = float((input("What is the grade boundry for a four? \n do NOT add precenatage sign(%): ")))
    s3_three = float((input("What is the grade boundry for a three? \n do NOT add precenatage sign(%): ")))
    s3_two = float((input("What is the grade boundry for a two? \n do NOT add precenatage sign(%): ")))
    s3_one = float((input("What is the grade boundry for a one? \n do NOT add precenatage sign(%): ")))

    time.sleep(0.2)
if gb_in == "Y":
    print("\nGreat!")
    s3_seven = 1000.0
    s3_six = 1000.0
    s3_five = 1000.0
    s3_four = 1000.0
    s3_three = 1000.0
    s3_two = 1000.0
    s3_one = 1000.0
    time.sleep(0.2)

s3_tests = int(input("\nhow many summatives were conducted in "+subjects[2]+"? "))

s3_max_sum = 0
s3_grade_sum = 0

for i in range(0,s3_tests):
    s3_max = int(input(f"\nwhat was the maximum marks in test{ i+1 }? "))
    s3_max_sum = s3_max_sum + s3_max

    time.sleep(0.2)

for i in range(0,s3_tests):
    s3_grade = int(input(f"\nwhat was the marks awarded to you in test{ i+1 }? "))
    s3_grade_sum = s3_grade_sum + s3_grade
    continue

precentage = (s3_grade_sum / s3_max_sum) * 100
print(" ")
print(" ")
print(" ")
flag1 = True
while flag1:
    if (precentage >= s3_seven) or (precentage >= 85):
        s3_score = 7
        print("your score in this subject is 7")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s3_six) or (precentage >= 70):
        s3_score = 6
        print("your score in this subject is 6")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s3_five) or (precentage >= 55):
        s3_score = 5
        print("your score in this subject is 5")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s3_four) or (precentage >= 48):
        s3_score = 4
        print("your score in this subject is 4")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s3_three) or (precentage >= 30):
        s3_score = 3
        print("your score in this subject is 3")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s3_two) or (precentage >= 20):
        s3_score = 2
        print("your score in this subject is 2")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s3_one) or (precentage >= 5):
        s3_score = 1
        print("your score in this subject is 1")
        flag1 = False
        break
        time.sleep(0.5)
    else:
        s3_score = 0
        print("FAILED")
        flag1 = False
        break
        time.sleep(0.5)

################################################################################

#Fourth subject
print("\n\nlets begin with "+subjects[3]+" :)")
print("\nTo calculate your IB score, we need subject specific grade boundries.")
print("This is the default grade boundry: ")
print("seven = 85% \nsix = 70% \nfive = 55% \nfour = 48% \nthree = 30% \ntwo = 20% \none = 5%")
gb_in = input("If you like to continue with this default grade boundry respond with [Y], if you wish to edit, respond with [N]: ").upper()
if gb_in == "N":
    s4_seven = float((input("\nWhat is the grade boundry for a seven? \n do NOT add precenatage sign(%): ")))
    s4_six = float((input("What is the grade boundry for a six? \n do NOT add precenatage sign(%): ")))
    s4_five = float((input("What is the grade boundry for a five? \n do NOT add precenatage sign(%): ")))
    s4_four = float((input("What is the grade boundry for a four? \n do NOT add precenatage sign(%): ")))
    s4_three = float((input("What is the grade boundry for a three? \n do NOT add precenatage sign(%): ")))
    s4_two = float((input("What is the grade boundry for a two? \n do NOT add precenatage sign(%): ")))
    s4_one = float((input("What is the grade boundry for a one? \n do NOT add precenatage sign(%): ")))

    time.sleep(0.2)
if gb_in == "Y":
    print("\nGreat!")
    s4_seven = 1000.0
    s4_six = 1000.0
    s4_five = 1000.0
    s4_four = 1000.0
    s4_three = 1000.0
    s4_two = 1000.0
    s4_one = 1000.0
    time.sleep(0.2)

s4_tests = int(input("\nhow many summatives were conducted in "+subjects[3]+"? "))

s4_max_sum = 0
s4_grade_sum = 0

for i in range(0,s4_tests):
    s4_max = int(input(f"\nwhat was the maximum marks in test{ i+1 }? "))
    s4_max_sum = s4_max_sum + s4_max

    time.sleep(0.2)

for i in range(0,s4_tests):
    s4_grade = int(input(f"\nwhat was the marks awarded to you in test{ i+1 }? "))
    s4_grade_sum = s4_grade_sum + s4_grade
    continue

precentage = (s4_grade_sum / s4_max_sum) * 100
print(" ")
print(" ")
print(" ")
flag1 = True
while flag1:
    if (precentage >= s4_seven) or (precentage >= 85):
        s4_score = 7
        print("your score in this subject is 7")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s4_six) or (precentage >= 70):
        s4_score = 6
        print("your score in this subject is 6")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s4_five) or (precentage >= 55):
        s4_score = 5
        print("your score in this subject is 5")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s4_four) or (precentage >= 48):
        s4_score = 4
        print("your score in this subject is 4")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s4_three) or (precentage >= 30):
        s4_score = 3
        print("your score in this subject is 3")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s4_two) or (precentage >= 20):
        s4_score = 2
        print("your score in this subject is 2")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s4_one) or (precentage >= 5):
        s4_score = 1
        print("your score in this subject is 1")
        flag1 = False
        break
        time.sleep(0.5)
    else:
        s4_score = 0
        print("FAILED")
        flag1 = False
        break
        time.sleep(0.5)

################################################################################

#Fifth subject
print("\n\nlets begin with "+subjects[4]+" :)")
print("\nTo calculate your IB score, we need subject specific grade boundries.")
print("This is the default grade boundry: ")
print("seven = 85% \nsix = 70% \nfive = 55% \nfour = 48% \nthree = 30% \ntwo = 20% \none = 5%")
gb_in = input("If you like to continue with this default grade boundry respond with [Y], if you wish to edit, respond with [N]: ").upper()
if gb_in == "N":
    s5_seven = float((input("\nWhat is the grade boundry for a seven? \n do NOT add precenatage sign(%): ")))
    s5_six = float((input("What is the grade boundry for a six? \n do NOT add precenatage sign(%): ")))
    s5_five = float((input("What is the grade boundry for a five? \n do NOT add precenatage sign(%): ")))
    s5_four = float((input("What is the grade boundry for a four? \n do NOT add precenatage sign(%): ")))
    s5_three = float((input("What is the grade boundry for a three? \n do NOT add precenatage sign(%): ")))
    s5_two = float((input("What is the grade boundry for a two? \n do NOT add precenatage sign(%): ")))
    s5_one = float((input("What is the grade boundry for a one? \n do NOT add precenatage sign(%): ")))

    time.sleep(0.2)
if gb_in == "Y":
    print("\nGreat!")
    s5_seven = 1000.0
    s5_six = 1000.0
    s5_five = 1000.0
    s5_four = 1000.0
    s5_three = 1000.0
    s5_two = 1000.0
    s5_one = 1000.0
    time.sleep(0.2)

s5_tests = int(input("\nhow many summatives were conducted in "+subjects[4]+"? "))

s5_max_sum = 0
s5_grade_sum = 0

for i in range(0,s5_tests):
    s5_max = int(input(f"\nwhat was the maximum marks in test{ i+1 }? "))
    s5_max_sum = s5_max_sum + s5_max

    time.sleep(0.2)

for i in range(0,s5_tests):
    s5_grade = int(input(f"\nwhat was the marks awarded to you in test{ i+1 }? "))
    s5_grade_sum = s5_grade_sum + s5_grade
    continue

precentage = (s5_grade_sum / s5_max_sum) * 100
print(" ")
print(" ")
print(" ")
flag1 = True
while flag1:
    if (precentage >= s5_seven) or (precentage >= 85):
        s5_score = 7
        print("your score in this subject is 7")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s5_six) or (precentage >= 70):
        s5_score = 6
        print("your score in this subject is 6")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s5_five) or (precentage >= 55):
        s5_score = 5
        print("your score in this subject is 5")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s5_four) or (precentage >= 48):
        s5_score = 4
        print("your score in this subject is 4")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s5_three) or (precentage >= 30):
        s5_score = 3
        print("your score in this subject is 3")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s5_two) or (precentage >= 20):
        s5_score = 2
        print("your score in this subject is 2")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s5_one) or (precentage >= 5):
        s5_score = 1
        print("your score in this subject is 1")
        flag1 = False
        break
        time.sleep(0.5)
    else:
        s5_score = 0
        print("FAILED")
        flag1 = False
        break
        time.sleep(0.5)

################################################################################

#Sixth subject
print("\n\nlets begin with "+subjects[5]+" :)")
print("\nTo calculate your IB score, we need subject specific grade boundries.")
print("This is the default grade boundry: ")
print("seven = 85% \nsix = 70% \nfive = 55% \nfour = 48% \nthree = 30% \ntwo = 20% \none = 5%")
gb_in = input("If you like to continue with this default grade boundry respond with [Y], if you wish to edit, respond with [N]: ").upper()
if gb_in == "N":
    s6_seven = float((input("\nWhat is the grade boundry for a seven? \n do NOT add precenatage sign(%): ")))
    s6_six = float((input("What is the grade boundry for a six? \n do NOT add precenatage sign(%): ")))
    s6_five = float((input("What is the grade boundry for a five? \n do NOT add precenatage sign(%): ")))
    s6_four = float((input("What is the grade boundry for a four? \n do NOT add precenatage sign(%): ")))
    s6_three = float((input("What is the grade boundry for a three? \n do NOT add precenatage sign(%): ")))
    s6_two = float((input("What is the grade boundry for a two? \n do NOT add precenatage sign(%): ")))
    s6_one = float((input("What is the grade boundry for a one? \n do NOT add precenatage sign(%): ")))

    time.sleep(0.2)
if gb_in == "Y":
    print("\nGreat!")
    s6_seven = 1000.0
    s6_six = 1000.0
    s6_five = 1000.0
    s6_four = 1000.0
    s6_three = 1000.0
    s6_two = 1000.0
    s6_one = 1000.0
    time.sleep(0.2)

s6_tests = int(input("\nhow many summatives were conducted in "+subjects[5]+"? "))

s6_max_sum = 0
s6_grade_sum = 0

for i in range(0,s6_tests):
    s6_max = int(input(f"\nwhat was the maximum marks in test{ i+1 }? "))
    s6_max_sum = s6_max_sum + s6_max

    time.sleep(0.2)

for i in range(0,s6_tests):
    s6_grade = int(input(f"\nwhat was the marks awarded to you in test{ i+1 }? "))
    s6_grade_sum = s6_grade_sum + s6_grade
    continue

precentage = (s6_grade_sum / s6_max_sum) * 100
print(" ")
print(" ")
print(" ")
flag1 = True
while flag1:
    if (precentage >= s6_seven) or (precentage >= 85):
        s6_score = 7
        print("your score in this subject is 7")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s6_six) or (precentage >= 70):
        s6_score = 6
        print("your score in this subject is 6")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s6_five) or (precentage >= 55):
        s6_score = 5
        print("your score in this subject is 5")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s6_four) or (precentage >= 48):
        s6_score = 4
        print("your score in this subject is 4")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s6_three) or (precentage >= 30):
        s6_score = 3
        print("your score in this subject is 3")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s6_two) or (precentage >= 20):
        s6_score = 2
        print("your score in this subject is 2")
        flag1 = False
        break
        time.sleep(0.5)
    if (precentage >= s6_one) or (precentage >= 5):
        s6_score = 1
        print("your score in this subject is 1")
        flag1 = False
        break
        time.sleep(0.5)
    else:
        s6_score = 0
        print("FAILED")
        flag1 = False
        break
        time.sleep(0.5)

################################################################################

#TOK & EE
wocore_score = s1_score + s2_score + s3_score + s4_score + s5_score + s6_score
converted_score = str(wocore_score)
print("\n\nYour IB score, without the core elements is "+converted_score+"/42. \nhowever IB score is out of 45")
x = input("If you wish to see your total IB score, respond with [Y]; If not, respond with [N]: ").upper()

if x == "N":
    print("\n\nGoodbye :)")
    time.sleep(1)
    exit()

if x == "Y":
    pass
    time.sleep(0.5)

print("\n\nTo calculate your total Ib score out of 45, we need to calculate your ToK and EE score.")
tok = input("\nWhat grade did you get for ToK? (Theory of Knowledge) \nrespond with [A],[B],[C],[D] or [E]: ").upper()
ee = input("\nWhat grade did you get for EE? (Extended Essay) \nrespond with [A],[B],[C],[D] or [E]: ").upper()

if (tok == "A") and (ee == "A"):
    core_score = 3
    print("your core score is 3")
    time.sleep(0.5)
if (tok == "A") and (ee == "B"):
    core_score = 3
    print("your core score is 3")
    time.sleep(0.5)
if (tok == "A") and (ee == "C"):
    core_score = 2
    print("your core score is 2")
    time.sleep(0.5)
if (tok == "A") and (ee == "D"):
    core_score = 2
    print("your core score is 2")
    time.sleep(0.5)
if (tok == "A") and (ee == "E"):
    core_score = 1
    print("your core score is 1")
    time.sleep(0.5)

if (tok == "B") and (ee == "A"):
    core_score = 3
    print("your core score is 3")
    time.sleep(0.5)
if (tok == "B") and (ee == "B"):
    core_score = 2
    print("your core score is 2")
    time.sleep(0.5)
if (tok == "B") and (ee == "C"):
    core_score = 1
    print("your core score is 1")
    time.sleep(0.5)
if (tok == "B") and (ee == "D"):
    core_score = 1
    print("your core score is 1")
    time.sleep(0.5)
if (tok == "B") and (ee == "E"):
    core_score = 0
    print("your core score is 0")
    time.sleep(0.5)

if (tok == "C") and (ee == "A"):
    core_score = 2
    print("your core score is 2")
    time.sleep(0.5)
if (tok == "C") and (ee == "B"):
    core_score = 1
    print("your core score is 1")
    time.sleep(0.5)
if (tok == "C") and (ee == "C"):
    core_score = 1
    print("your core score is 1")
    time.sleep(0.5)
if (tok == "C") and (ee == "D"):
    core_score = 0
    print("your core score is 0")
    time.sleep(0.5)
if (tok == "C") and (ee == "E"):
    core_score = 0
    print("your core score is 0")
    time.sleep(0.5)

if (tok == "D") and (ee == "A"):
    core_score = 2
    print("your core score is 2")
    time.sleep(0.5)
if (tok == "D") and (ee == "B"):
    core_score = 1
    print("your core score is 1")
    time.sleep(0.5)
if (tok == "D") and (ee == "C"):
    core_score = 0
    print("your core score is 0")
    time.sleep(0.5)
if (tok == "D") and (ee == "D"):
    core_score = 0
    print("your core score is 0")
    time.sleep(0.5)
if (tok == "D") and (ee == "E"):
    core_score = 0
    print("your core score is 0")
    time.sleep(0.5)

if (tok == "E") and (ee == "A"):
    core_score = 1
    print("your core score is 1")
    time.sleep(0.5)
if (tok == "E") and (ee == "B"):
    core_score = 0
    print("your core score is 0")
    time.sleep(0.5)
if (tok == "E") and (ee == "C"):
    core_score = 0
    print("your core score is 0")
    time.sleep(0.5)
if (tok == "E") and (ee == "D"):
    core_score = 0
    print("your core score is 0")
    time.sleep(0.5)
if (tok == "E") and (ee == "E"):
    core_score = 0
    print("you will not be awarded an IB diploma :(")
    time.sleep(0.5)

################################################################################

total_IB = wocore_score + core_score
total_converted = str(total_IB)
print("\n\n\nyour total IB score is "+total_converted+"/45 :)")

print("\n\n\nProgram was created by SepehrAkbari")

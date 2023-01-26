#birth_year = input('Birth year: ')
#print(type(birth_year))
#age = 2019 - int(birth_year)
#print(age)

#name = input('what is your name?')
#weight_lbs = input('Weight (lbs): ')
#weight_kg = int(weight_lbs) * (0.45)
#print('your weight in kg is ' + str(weight_kg) + 'kg')

#Formatted Strings
#first = 'john'
#last = 'Smith'
#message = first + ' [' + last +  '] is a coder'
#msg = f'{first} {last} is a coder'
#print(message)

#String Methods
#course = 'Python is for beginners'
#print(len(course))
#print(course.upper())
#print(course.lower())
#print(course.find('P'))
#print(course.find('Beginners'))
#print(course.replace('P',  'J'))
#print(course.replace ('beginners',  'Absolute Beginners'))
#print('Python' in course)
#print(course.title())

#Arithmetic Operations
#print(10/3)
#print(10%3)
#x = 10
#x = x - 4
#x -= 4
#print(x)

#Operator Precedence
#x = 10 + 3 * 2
#print(x)
#parenthesis
#exponentiation 2**3 power
#multiplication or division
#addition or subtraction

#Math Functions
#import math
#math.ceil(2.9)
#x = 2.9
#print(round((x)))
#print(abs(-2.9))

#if Statements
#is_hot = False
#is_cold = True
#if is_hot:
   # print('its a hot day')
   # print('Drink some water')
#elif is_cold:
 #   print("It's a cold day")
  #  print('Wear warm clothes')
#else:
 #   print('Have a lovely day')
#print('Enjoy your day')

#Exercise
#price = 1000000
#has_goodcredit = False

#if has_goodcredit:
#    down_payment = 0.1 * price
#else:
#    down_payment = 0.2 * price
#print(f'down_payment: ${down_payment}')

#Logical operators
#has_high_income = False
#has_good_credit = True
#has_criminal_record = False
#if has_good_credit and not has_criminal_record:
 #   print('Eligible for loan')

#Comparison Operators
#temparature = 35
#if temparature > 30:
 #   print("It's a hot day")
#else:
 #   print("It's not a hot day")

#exercise(mine)
#min_name = 3
#max_name = 50
#if min_name < 3:
#    print('name must be at least 3 characters long')
#elif max_name > 50:
 #   print('name must be a maximum of 50 characters long')
#else:
 #   print('name looks good')

#exercise(mosh)

#name = 'Johny Jon'


#if len(name) < 3:
   # print('Name must be atleast 3 characters long')
#elif len(name) > 50:
   # print('Name must be a maximum of 50 caharacters')
#else:
 #   print('Name looks good!')

#Project: Weight Converter
#weight = int(input('Weight: '))
#unit = input('(L)bs or (K)gs:')

#if unit.upper() == 'L':
 #   converted = weight * 0.45
  #  print(f'You are {converted} kilos')
#else:
#    converted = weight // 0.45
 #   print(f'You are {converted} pounds')


#***While Loops**#

#i= 1
#while i <= 5:
 #   print('*' * i)
  #  i = i + 1
#print("Done")

#secret_number = 9
#guess_count = 0
#guess_limit = 3
#while guess_count < guess_limit:
 #     guess = int(input('Guess:'))
  #    guess_count += 1
   #   if guess == secret_number:
    #      print('You won!')
     #     break
#else:
 #         print('Sorry you failed!')

#Car Game

#help = input('>')
 #       if help = help:
  #      print(  'start -  to start the car')

#***Mosh Car game:(here lower() is placed on user input instead of every  "if" command statement!!***#
##command = ""
##started = False
#while True:
    #command = input("> ").lower()
    #if command == "start":
      #  if started:
#            print("car already started!!")
     #   else:
      #      started = True
     #       print(" car started")

    #elif command == "stop":
      #  if not started:
     #       print("car already stopped")

    #    else:
   #         started = False
  #          print("Car stopped...")
 #   elif command == "help":
#        print("""
#start -to start the car
#stop - to stop the car
#quit - to quit
 #       """)
    #elif command == "quit":
   #     print("You quit the game..thank you;)")
  #      break
 #   else:
#        print("invalid command")




for number in range (0, 100):
    number = int(input('Enter number: '))
    if number % 2 == 0:
      print(f"Even")
    else:
      if number % 2 != 0:
       print(f"Odd")







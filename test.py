                                          #exersie one 
a = 1998
b = 2023

c = a-b
print(c)

a = "babar"
b =  "Aziz"
c  = "khan"
print("my full name is:" + a + ""+ b + "" +c)

                                           #exercise two
num = 17
print(format(num,"b"))
          
                                           #exercise 3
city = "karachi"
Street = 18
country = "pakistan"
 Adress = ( +city+""+ Street +"" + country)
 print(f' this is my adress:\n{city}\n{Street}\n{country}')
                                        
                                            #exercise 4
a = "Earth Resolve around the sun"
print(a[0:4])
print(a[-4:])

slice = "many 10 banaan khye"  
slice=slice.replace("banana","samosa").replace("200", "300")
print(slice)
s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)
                                       # exersize no 5 len
a = input("this is first number")
b = input("this is my second number")  
print(a,b)

#                          #exerxcise = number 6 list in python 

name = ['hamza','bilal','babar','awias','habib','moiz','khan',]
        # print(type(metaia)
name.append("Raja") # append ka matlb hai value ko list k akhri ma add kerna
print(name)
name.insert(4, 'dada') # inert ka matlb hai list ma value khi bi insert kerdena
print(name)

mitai = ['samsa','kheer','gulab jaman','barfi','rabri']
food = name+mitai
print(food) # do alag list k0 mila sikty ham + -> concitination ki madad sy 

['hamza','bilal','babar','awias','habib','moiz','khan',]
print(name)
name[3:4]=[1,2,3,4,5] # in pthon we have add nubers and string only in python not any another laguage
print(name)
print(dir(name))
                         #exercise solution
  
# monthly_expense = [2200,2350,2600,2130,2190] 
# 1. In Feb, how many dollars you spent extra compare to January
print(monthly_expense[1]-monthly_expense[0])
# Find out if you spent exactly 2000 dollars in any month
print("can i spend 2000$ in any month:" , 2000 in monthly_expense)
#4.June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expense.append("1990")
print(monthly_expense)
# #Find out your total expense in first quarter (first three months) of the year.
monthly_expense=2200+2350+2600
print(monthly_expense)
#1. Length of the listprint
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
#  Add 'black panther' at the end of this list
heros.append("black_panter")
print(heros)
# so remove it from the list first and then add it after 'hulk
heros.remove("black_panter")
print(heros)
#3. You realize that you need to add 'black panther' after 'hulk',
heros.insert(3,"balck_panter")
print(heros)
#4.Now you don't like thor and hulk because they get angry easily :)
# #    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# #    Do that with one line of cod
heros[1:3]=["doctor_strange"]
print(heros)
heros.sort()
print(heros)
                               #exerxcise = number 7 condition if and else in python
  
pakistani= ["biryani","samosa","nihari","gajarkajoss"]
indian = ["dal","samosa","dal","dalchawal"]
bangladesh = ["pantabaht","fuchka","chorchori",]

dish =input("enter your food + "" ")
if dish in indian:
  print(f"{dish} is indian")
elif dish in pakistani:
  print(f"{dish} is pakistani")
elif dish in bangladesh:
    print(f"{dish} is bangladeshi")
else:
  print("enter no food")

                                      #exercise no 8

a = [1200, 1500, 1700, 1300]

total = a[0]+a[1]+a[2]+a[3]
print(total)

total = 0

for expense in a:
  total = total+a
print(total)

for i in range(1,11):
  if i % 2 == 0:
    continue
  print[i*i]

month_list = ["janwary","febrary","march", "aprail"]
expense_list = [1200, 1300, 1400, 1500]

e = input("enter expense amount")
e = int("e")

month =  -1
for i in range(len(expense_list)):
    if e  == expense_list[i]:
        month = i 


    if  month != -1:
        print(f"you spent{e}")

    else:
        print(f"you dint sped{e}")

for i in range(5):

  print(f"you ran {i+1} miles")
  tired = input("are you tired? ")

  if tired == 'yes':
    
   break

  if i==4:
    print("you achieved the miles")

  else:
    print("you did'nt the achieve the miles try again next time")
  

for i in range(1,6):
  
  s = ''
for j in range (i):
      
      s += '3'
      print(s)

import math
print(math.sqrt(18))
print(math.log10(500))

               # exercise no 12  DICTIONERISES                   

 captain ={
     'china' : 143,
     'india ' : '136',
     'pakistam' : '22',
     'afghnistan' : '20'
}

print(captain)
print(captain['pakistan'])

print(captain.keys())
print(captain.values())

                                 # add the value in dictionary
captain['england']='root'
print(captain)
 
                                     # used "get" method 
print(captain.get('india'))

             # method of empty intialize the dictionary and add the value 
e = {}
e['ndia']= 'rohit'
e['pakistan']= 'babar azam'
e['sri lanka']= 'demuth'
e['afghnistan']='nabi'
print(e)
                      # tuple is not immutable meas once sighn the value then cant change the value
tuple = (1,2,4,5)
print(tuple)

 population = {
 'china' : 140,
'india' : 136,
'pakistam' : 22,
'afghnistan' : 20
}


for item in captain:
print(item,"==>",captain[item])

def add():
  country = input("enter the country")
  country == country.lower()
  if country in  population:
    print("country is  already exit")

    return
    p =input(f"enter the population {country}")
    p=float(p)
    population["shrlanka", 20]=p
    print_ll()

             #   You are given following list of stocks and their prices in last 3 days,

                                # import statistics
stock = {
    'ifo': [600,630,620],
    'ril': [1430,1490,1567],
     'mtl': [234,180,160]
}
def   print_all():
  for stock,price_list in stock.item():
      avg= statistics.mean(price_list)
      print(f'{stock} ==> {price_list} ==> avg:', round(avg,2))

def add():
  s = ('enter the stock to sriker to add')
  p = ('enter the price of this stock')

  p(float)(p)

  if s in stock:
    stock[s].append(p)
  else:
    stock[s] = [p]
    print_all()
    
def main():
    op=input("Enter operation (print, add or amend):")
    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add()
    else:
        print("Unsupported operation:",op)

# if __name__ == '__main__':
#     main()


    # Machine Learning Assignment     Jyothi Sai Rajesh Kunapareddy - 700742325

# Sir, I just commented code to all questions except the first one

 #Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() #  sorting the given list
print(ages)
print(min(ages),max(ages))# minimum and maximum values
ages.extend([min(ages),max(ages)]) # adding min,max values to list
print(ages)
middle_position = len(ages)//2
median_value = (ages[middle_position] + ages[middle_position]) //2
print("median:", median_value)# median value
print("average : ",sum(ages)/ len(ages)) # average value
print("range : ", max(ages)-min(ages)) # range value

#Question 2
dog = {}
dog['name'] = 'Jessy'
dog['color'] = 'GoldenWhite'
dog['breed'] = 'Lab'
dog['legs'] = 4
dog['age'] = 1
#print(dog)
Student = {}
Student['first_name'] = 'Rajesh'
Student['last_name'] = 'Kunapareddy'
Student['gender'] = 'Male'
Student['age'] = '23'
Student['marital_status'] = 'Single'
ValuesOfSkill = ['python','html','css']
Student['skills'] = ValuesOfSkill
Student['country'] = 'India'
Student['city'] = 'Machilipatnam'
Student['address'] = '404 Zella Street,Warrensberg'
#print(len(Student))# length of dictionery
#print(Student['skills'], type(ValuesOfSkill))#datatype of skill value
#print(Student)
ValuesOfSkill.extend(['java','ruby'])
#print(Student['skills'])
keys = Student.keys()
#print(keys)
values = Student.values()
#print(values)

# Question 3

brothers = ('luffy','Zoro')
sisters = ('Nami','Robin')
siblings = brothers + sisters # joining the tuples
#print(siblings)

#print("how many siblings do you have ?..", len(siblings))

family_members = siblings + ('Monkey D Dragon','Monkey D Tiger')
#print(family_members) # family tuple

# Question 4

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#print(len(it_companies))
it_companies.add('twitter')
it_companies.update({'Tiktok','Netflix','Uber','Ola'}) # mutiple values added
#print(it_companies)
it_companies.remove('Microsoft') # microsoft removed

#print(it_companies)
# it_companies.remove('Zoro') # remove() throws an error if element to
# it_companies.discard('Zoro') # be deleted does not exist  while discard() doesn't

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#print("A union B :",A.union(B)) # joined  a and b
#print("A intersection B :",A.intersection(B)) # a interscet b
#print("Is A subset of B ?..", A.issubset(B))
#print('Are A and B disjoint sets ?..', A.isdisjoint(B))
#print("A with B and B with A ",A.union(B) and B.union(A))
#print("Symmetric Difference : ",B.symmetric_difference(A)) # symmetric difference b/w A and B
del A,B # deleted set completely
age = [22, 19, 24, 25, 26, 24, 25, 24]
age2 = set(age)
#print("list age converted to set age2 :",age2)
#print('length of List Vs set :' ,len(age),"|",len(age2))

# Question 5

#print("area 1 :", 3.14*30*30)
area_of_circle = 2826.0
#print("circum:", 2*3.14*30)
circum_of_circle = 188.4
#r = int(input("enter radius :"))
#print("area 2 : ", 3.14*r*r)

# Question 6

str = "I am a teacher and I love to inspire and teach people"
str = str.split() # splitting words and storing in list
unique_set = set(str) # list to set conversion
#print("Unique words : ",unique_set)

#Question 7

text = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
#print(text)

# Question 8

radius =10
#print("radius = 10")
#print(f"area = 3.14*{radius} **2" )# f string formatting
area = '314 meters square.'
#print("area :",3.14*100)
result = f"\"The area of a circle with radius 10 is {area}\""
#print(result)

#Question 9
l=[]
l2=[]
#N = int(input("Enter Num of students : ")) # user input
#for i in range(0,N): # iterates until i = N - 1
    #pounds = float(input())
    #l.append(pounds)
    #l2.append(pounds*0.453592) # coverts pounds to kilograms
#print("Weights in Pounds :",l)
#print("Weights in Kilograms :",l2)

# Question 10

"I uploaded a screenshot for this answer in word document."


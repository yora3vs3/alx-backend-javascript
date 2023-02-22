

1. print("Hello World") 
2. x = 5 
3. y = 10 
4. z = x + y 
5. print(z) 
6. a = "Hello" 
7. b = "World" 
8. c = a + b 
9. print(c) 
10. list1 = [1,2,3] 
11. list2 = [4,5,6] 
12. list3 = list1 + list2  
13. print(list3)  
14. for i in range(10):  
15     print(i)  
16. def add_two_numbers(x,y):  
17     return x+y  
18. result = add_two_numbers(5,10)  
19. print(result)  
20. my_dict = {'name': 'John', 'age': 25}  
21. print(my_dict['name'])   
22. my_list = [1,2,3]   
23. my_list[0] = 0    #change the first element of the list to 0    24 .print (my_list[0])    25 .if 5 > 3:    26     print("Five is greater than three")    27 .else:    28     print("Five is not greater than three")    29 .while True:    30     userInput=input("Please enter your name: ")    31     if userInput == 'quit': break;    32 .print('Welcome', userInput)    33 .import math #import math module to use its functions 34 .x=math.cos(math.pi/4) #calculate cosine of pi/4 35 .print (x) 36 .class Person: 37      def __init__ (self, name): 38          self._name=name 39      def getName (self): 40          return self._name 41      def setName (self, name): 42          self._name=name 43 44 p=Person('John') 45 46 print (p._name) 47 48 p._name='David' 49 50 print (p._name) 51 52 p=Person('John') 53 54 psetName('David') 55 56
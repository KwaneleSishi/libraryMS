""" Task 2: Comprehensions (lists and sets). 
The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books: 
§	Create a normal and comprehensive list that will display the codes. 
§	Create a normal and comprehensive list that will add the codes together for auditing purpose. 
§	Create a normal and comprehensive list that will display only codes that are tracked by odd numbers. 
§	Create a set to display the list of codes. 
 """ 
#Create a normal and comprehensive list that will display the codes. 
codes = [14, 15, 16, 17, 18, 19, 20]
# Normal list
codesN = []
for c in codes:
    codesN.append(c)
print("A normal list that display the codes:", codesN)
# List comprehension
codes_list = [code for code in codes]
print("Normal List:")
print("A comprehensive list to display codes:",codes_list)

#§	Create a normal and comprehensive list that will add the codes together for auditing purpose
# Normal list
sumCodes =[]
sumN = 0
for cc in codes:
    sumN=sumN + cc
print("\nThe normal list that add the codes together for auditing purpose", sumCodes)


# List comprehension
sumC = 0
sumCodes = [sumC := sumC + Comp for Comp in codes]
print("Sum of Codes (List Comprehension):",sumCodes )

#Create a normal and comprehensive list that will display only codes that are tracked by odd numbers. 
# Normal list
odd_codes = []
for co in codes:
         if co % 2 != 0:
           odd_codes.append(co)    
print("Normal list of Odd Codes", odd_codes)
# List comprehension
odd_codes_comprehensive = [code for code in codes if code % 2 != 0]
print("List Comprehension of Odd Codes:", odd_codes_comprehensive)

#Create a set to display the list of codes
codes_set = set(codes)

print("\Sets of Codes:", codes_set)

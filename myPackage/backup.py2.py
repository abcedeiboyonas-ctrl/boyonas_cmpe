strFullName = "Sean Boyonas"
intLength = len(strFullName)
print(strFullName)
print(intLength)
print(strFullName[0])
print(strFullName[1])
print(strFullName[11])
print(strFullName[-2])
print(strFullName[intLength-5])
print(strFullName[intLength-2])

mySubString = strFullName[1:6:2]
print(mySubString)

strFullName = strFullName + "a"
print(strFullName)

#String Method
StringMethod = strFullName.upper()
print(StringMethod)
StringMethod = strFullName.lower()
print(StringMethod)
StringMethod = strFullName.capitalize()
print(StringMethod)

StringMethod = strFullName.split(" ")
print(StringMethod)
StringMethod = strFullName.split("ea")
print(StringMethod)

StringMethod = strFullName.replace("Sean", "Seanny")
print(StringMethod)

FirstName = "Seyan"
MiddleName = "Nguyen"
LastName = "FatChoi"

MyFullNameList= [FirstName, MiddleName, LastName]
print("Fine".join(MyFullNameList))

StringMethod = strFullName.count("e")
print(StringMethod)

myChar = strFullName[2]
print(myChar)
intIndex = strFullName.index("B")
print(intIndex)

#String
#NumericType
#Integer -10, 0, 2000
#Float 2.333
#Complex imagnary number

intA = 25
intB = 15
intC = 5
#arithmetic operations
intSum = intA + intB + intC
print(intSum)
intDiff = intA - intB
print(intDiff)
intProd = intA * intB
print(intProd)
intQu = intA / intB
print(intQu)
intResult = intA ** intB
print(intResult)

#PMDAS
import math
intAngle = 90
result = round(math.cos(math.radians(intAngle)), 1)
print(result)
result = round(math.sin(math.radians(intAngle)), 1)
print(result)
result = round(math.tan(math.radians(intAngle)), 1)
print(result)
result = round(math.atan(math.radians(intAngle)), 1)
print(result)

intAngle = 45
result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intX = 5
facResult = math.factorial(intX)
print(facResult)

myComA = 25 + 5j
myComB = 10 - 10j
comProd = myComA * myComB
print(comProd)

#Comparison Operator
# ==, >, <, >=, <=, !=
#Boolean Data Type : True or False
#"True" 'True' - String
#1 or 0 - Integer

IntA = 5
intB = 6

isResult = intA == intB
print(isResult)

isResult = intA <= intB
print(isResult)

isResult = intA >= intB
print(isResult)

isResult = intA > intB
print(isResult)

isResult = intA < intB
print(isResult)

#membership operator in, not in
isResult = "e" in "madagascar"
print(isResult) #False
isResult = "e" in "medegescer"
print(isResult) #True

myList = ["bearbrand", "juice", "coffee"]
isResult = "biscuit" in myList
print(isResult) #False
myList = ["coffee", "juice", "cup", "matcha", "biscuit"]
isResult = "biscuit" in myList
print(isResult)

#identity operator is, is not
isResult = "dege" is "medegescer"
print(isResult)

myInput = "121312hello 233wo2323rld33"
myOutput = " "

for char in myInput:
    if not char.isnumeric(): #pag letter ka nasa output ka, pag number wala ka
        myOutput = myOutput + char

print(myOutput)

myInput = "a34a3433alam3434mo3434 344sah"

myOutput = ""
for char in myInput:
    if not char.isnumeric():
        myOutput = myOutput + char

print(myOutput)

#LOGICAL OPERATOR
#LOGIC CIRCUITS AND SWITCH THEORY
isGroupPassed = False
passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade = 86

isMarkPassed = markGrade >= passingGrade
print(isMarkPassed)
isJennyPassed = jennyGrade >= passingGrade
print(isJennyPassed)
isArthurPassed = arthurGrade >= passingGrade
print(isArthurPassed)
isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed)
isGroupPassed = isJennyPassed or isArthurPassed or isMarkPassed
print(isGroupPassed)

#Remainder
#modulus

intA = 555
intB = 4
intC = 5

isDivisible = False
remainder = intA % intB
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

isDivisible = False
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

# LIST
# CRUD - CREATE READ UPDATE DELETE
fruitsA = [ "apple", "banana", "cherry" ]
print(fruitsA)
fruitsA.append("orange")
print(fruitsA)

print(fruitsA.index("orange"))

fruitsA[3] = "pineapple"
print(fruitsA)

print(len(fruitsA))

print(fruitsA.count("apple"))

fruitsA.insert(2, "apple")
print(fruitsA)

print(len(fruitsA))
print(fruitsA.remove("banana"))
print(fruitsA.remove("apple"))

# LIST
# CRUD - CREATE READ UPDATE DELETE
fruitsA = [ "apple", "banana", "orange", "banana", "grapes"]
fruitsB = [ "banana", "mango", "lychee", "orange", "mango",]
fruitsC = [ "mango", "grapes", "apple", "mango", "lychee"]

fruitbasket = [fruitsA, fruitsB, fruitsC] #list of list
print(fruitbasket)
print(fruitbasket[2][3])

fruitbasketadd = fruitsA + fruitsB + fruitsC #single list / wrong
print(fruitbasketadd)

fruitsA.extend(fruitsB) #single list / wrong
fruitsA.extend(fruitsC)
print(fruitsA)

#List of a different data types and list
myInfoList = ["sean", "18", "male", "sigma"]
print(myInfoList)
print(myInfoList[0])
print(myInfoList[1])
print(myInfoList[2][3])
print(len(myInfoList))
myInfoList.append("auramaxxing")
print(myInfoList)

#TUPLE
# list is have a square bracket and tuple is have bracket

fruitsA = ("apple", "banana", "orange", "banana", "grapes")
print(fruitsA[3])
#fruitsA[3] = "pine apple" - not supported, immutable
print(fruitsA.count("apple"))

fruitsB = [ "banana", "mango", "lychee", "orange", "mango",]
fruitsC = [ "mango", "grapes", "apple", "mango", "lychee"]
fruitBasket = (fruitsA, fruitsB, fruitsC)
print(fruitBasket[2][4])

#SET { } curly brace
fruitsA = {"apple", "banana", "orange", "banana", "grapes"}
fruitsB = {"grapes", "apple", "mango", "lychee"}
print(fruitsA)
fruitsUnion = fruitsA | fruitsB #union
print(fruitsUnion)
fruitsIntersection = fruitsA & fruitsB #intersection
print(fruitsIntersection)

fruitsDifference = fruitsA - fruitsB # difference
print(fruitsDifference)

# SUBSET
print(fruitsC.issubset(fruitsB))
print(fruitsC.issubset(fruitsA))

#DICTIONARY - dict - CURLY BRACES, KEY-VALUE PAIR

myInfo = {"Names" : "Sean Boyonas", "Age": 18, "Citizenship" : "Filipino"}
print(myInfo)

print(myInfo["Names"])
print(myInfo["Age"])
print(myInfo["Citizenship"])
print(myInfo.get("Citizenship"))

myInfo.update({"Age": 19})
print(myInfo)

myInfo.update({"Citizenship": "American"})
print(myInfo)

myInfo["Age"] = 55 #assigned value
print(myInfo)

print(myInfo.values())

#DICTIONARY - dict - CURLY BRACES, KEY-VALUE PAIR

myInfo = {"Names" : "Sean Boyonas", "Age" : 18, "Citizenship" : "Filipino"}
print(myInfo)

myInfo = {
   "Names": {
       "FirstName" : "Sean",
       "LastName" : "Boyonas"
   },
   "Age": 18,
   "Citizenship":"Filipino"
   "Hobbies"
}
print(myInfo)
print(myInfo["Names"]["FirstName"])
print(myInfo["Names"]["LastName"])
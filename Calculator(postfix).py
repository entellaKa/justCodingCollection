"""
*******후위 표기식 계산기*******
1. 입력된 식을 괄호로 묶어 계산 순서를 알기 쉽게 정리한다.
1-1) 괄호를 묶는 우선 순위는 계산 순서와 마찬가지로 "(,)" > "*,/,%" > "+,-" 으로 내림차순이다.
1-2) 괄호 바로 전후로 숫자가 있다면 중간에 곱하기를 추가한다
1-3) 음수 입력을 주의한다 (아직 미구현)
2. 정리된 식을 후위 표기식으로 바꿔준다
3. 바뀐 식을 계산한다.

축약어 :  p - plus or minus, m - multiply or division, b - bracket, n - number
"""
#temp = "1+2-6+6-5+4-8+9-7+1-5+8-7"
#temp = "1*2*3*4*8*9"
#temp = "1+2-6*5+4-8*2*3+4*9+7+1-5*8-7"
#temp = "3+4*(1+4/2+2*3)" #(3+(4*(1+(4/2)+(2*3))))
temp = "3+4*(1+4*(2+6*18)*2)"
#temp = "123456+345678*567890"


storageNumber = []

def checkOperator(c): #check this character is operator
	if c == "+" or c == "-" or c == "*" or c == "/" or c == "%":
		return True
	else:
		return False
    
def standardization(formula):
    formula = formula.replace(" ", "")
    fixedFormula = ""
    num = ""

    for i in range(len(formula)):
        if formula[i].isnumeric():
            num+=formula[i]
        elif formula[i] == "(":
            if not num == "":
                storageNumber.append(num) #extract a number from formula 식에서 숫자를 추출한다
                fixedFormula += "n*"
                num == ""
            fixedFormula += "("
        elif formula[i] == ")":
            if not num == "":
                fixedFormula += "n"
                storageNumber.append(num) #extract a number from formula 식에서 숫자를 추출한다
                num = ""
            fixedFormula += ")"
            if i+1 < len(formula):
                if formula[i+1].isnumeric():
                    fixedFormula += "*"
        elif checkOperator(formula[i]):
            if not num == "":
                fixedFormula += "n"
                storageNumber.append(num) #extract a number from formula 식에서 숫자를 추출한다
                num = ""
            else:
                #음수 입력 구현
                pass
            fixedFormula += formula[i]
    if num == "":
        return fixedFormula
    else:
        storageNumber.append(num) #extract a number from formula 식에서 숫자를 추출한다
        num = ""
        return fixedFormula + "n"
            
def refactoring(formula, stack, char):
    while len(stack) > 0:
        n = formula.rfind(char)
        formula = formula[:n] + stack.pop() + formula[n+1:]
    return formula

def abbreviatePlus(formula): #더하기 빼기는 줄일필요 없이 바로 괄호로 묶어 줘도 상관 없음
    n = int((len(formula)-3)/2)
    returnFormula = "(" * (n+1) + formula[:3] + ")"
    for i in range(2, n+2):
        returnFormula += formula[2*i-1:2*i+1] + ")"
    return returnFormula 

def abbreviateMultiply(formula):
    stack = []
    i = 0

    while i < len(formula):
        if formula[i] == "*" or formula[i] == "/" or formula[i] == "%":
            stack.append("("+formula[i-1:i+2]+")")
            formula = formula[:i-1] + "m" + formula[i+2:]
        else:
            i+=1
    return refactoring(abbreviatePlus(formula), stack, "m")

def abbreviateBracket(formula):
    count = 1
    returnFormula = ""
    stack = []
    i = 0
    
    while count > 0:
        if formula[i] == "(":
            count += 1
        elif formula[i] == ")":
            count -= 1
            if count == 0:
                return i
        i+=1
    return -1  

def function(formula):
    stack = []
    i = formula.find("(")
    while i >= 0:
        n = abbreviateBracket(formula[i+1:])
        innerBracket = formula[i+1:i+n+1]
        
        formula = formula[:i] + "b" + formula[i+n+2:]
        
        b = function(innerBracket)
        stack.append(b)
        i = formula.find("(")
    
    formula = abbreviateMultiply(formula)
    return refactoring(formula, stack, "b")

def restore(formula, storage):
    while "n" in formula:
        formula = formula.replace("n", storage.pop(0), 1)
    return formula

def postfix(formula):
	postfixedFormula = ""
	opStack = []
	for i in range(len(formula)):
		if formula[i].isnumeric():
			postfixedFormula += formula[i]
		elif formula[i] == "(":
			pass
		elif formula[i] == ")":
			postfixedFormula += " " + opStack.pop()
		else:
			opStack.append(formula[i])
			postfixedFormula += " "
	return postfixedFormula
	
def calculate(formula):
	stack = []
	num = ""
	
	for i in range(len(formula)):
		if formula[i] == " ":
			stack.append(int(num))
			num = ""
		elif formula[i].isnumeric():
			num += formula[i]
		else:
			if formula[i] == "+":
				num = stack.pop() + stack.pop()
			elif formula[i] == "-":
				n = stack.pop()
				num = stack.pop() - n
			elif formula[i] == "*":
				num = stack.pop() * stack.pop()
			elif formula[i] == "/":
				n = stack.pop()
				num = stack.pop() / n
			elif formula[i] == "%":
				n = stack.pop()
				num = stack.pop() % n
	return num

#f = abbreviateBracket(f)
formula = "("+temp+")"
f = standardization(temp)
f = function(f)
print("입력 값 : "+temp)
print("식 정리 : "+str(f))
f = restore(f, storageNumber)
print("식 복구 : "+f)
g = postfix(f)
print("식 재구성 : "+g)
h = calculate(g)
print("식 계산값 : "+str(h))

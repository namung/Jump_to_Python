# 1
def is_odd(a):
    if a % 2 == 0:
        return "입력한 숫자 %d : 짝수입니다." % a
    else:
        return "입력한 숫자 %d : 홀수입니다." % a

a = is_odd(2)
print(a)

b = is_odd(11)
print(b)

# 2. 모르겠다 확인!!
def add(*args): # "*" 은 인수를 튜플형태에 저장하여 반환함.
    sum = 0
    for i in args: # 매개변수로 작성한 "*args"를 쓸 때는 "*"을 제거하여 작성.
        sum += i
    result = sum / len(args)
    return result

b = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(b)

# 3
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2) # input으로 받은 값은 문자열로 저장됨. int()로 바꿔줘야함.
print("두 수의 합은 %s 입니다" % total)

# 4
# 3번. "," : 문자열을 연결할 때 띄어쓰기 해줌.

# 5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

# 5 - with 사용. -> 공부하기!!!
with open("test.txt", 'w') as f1:
    f1.write("Life is too short")
with open("test.txt", "r") as f2:
    print(f2.read())

# 6. 내가 한 것.
f1 = open("test.txt", "a")
f1.write(input("추가할 내용을 입력하세요: "))
f1.close()

# 6 답안코드
user_input = input("저장할 내용을 입력하세요: ")
with open("test.txt", "a") as f:
    f.write(user_input)   
    f.write("\n")

# 7. 수정 어떻게??? 모르겠다 확인.
# 파일 작성
f1 = open("test.txt", "w")
f1.write("Life is too short\nyou need java")
f1.close()

# 작성한 파일 내용 가져오기.
with open("test.txt", "r") as f2:
    text = f2.read()

text = text.replace("java", "python") # replace() 는 특정 단어만 지정해서 바꾸는 것. 전체적인 내용은 text 변수 안에 다 가지고 있음.

# 수정한 내용으로 새롭게 저장
with open("test.txt", "w") as f3:
    f3.write(text)

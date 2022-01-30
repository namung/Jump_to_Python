# 1
scores = {"국어":80, "영어":75, "수학":55}
sum1 = sum(list(scores.values()))
len1 = len(scores)
print(sum1/len1)

# 2
print(13 % 2) # 0이면 짝수, 1이면 홀수

# 3
jumin_number =  "881120-1068234"
jumin_number2 = jumin_number.split("-")
print("연월일:", jumin_number2[0], "나머지:", jumin_number2[1])

# 4
pin = "881120-1068234"
pin2 = pin.split("-")
print(pin2[1][0])

# 5
a = "a:b:c:d"
a = a.replace(":", "#")
print(a)

# 6. 체크하기!!!!!!
a = [1, 3, 5, 4, 2]
a.sort()
a = a[::-1] # a[::-1] 은 곧, a.reverse()
print(a)

# 7.
text = ['Life', 'is', 'too', 'short']
a = " ".join(text)
print(a)

# 8. 체크!!
a = (1, 2, 3)
a = (1, 2, 3, 4)
print(a)
# 오답! 튜플에 더하기 값 "하나"를 추가하려면 a + (4, ) 이렇게 하면 된다. 
# 단, 이 때 만들어지는 a + (4,)의 결과는 a의 값이 변경되는 것이 아니라 새로운 튜블이 생성되고 그 값이 a 변수에 대입되는 것이다.

# 8 답
a = (1,2,3)
print(id(a))
a = a + (4,)
print(a, id(a))

# 9. 체크!!
# key 값에는 변하지 않는 값만 들어갈 수 있다. 그래서 답은 list인 3번.

# 10. 
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))
print(a)

# 11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a2 = set(a)
print(list(a2))

# 12
# b의 값은 변경되지 않는다. 왜냐하면 a와 b는 각기 다른 메모리 주소를 참조하고 있기 때문이다. -> 오답!!!!
# 위 내용은 오답. 놀랍게도 같은 값을 참조한다... 그래서 a 값이 변경되면 b 값도 변경된다.

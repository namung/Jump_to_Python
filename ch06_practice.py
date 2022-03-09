# 06-1
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result

print(GuGu(2))

# 06-2
result = 0

for i in range(1, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        result += i

print(result)

# 06-3. 페이징
def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))

# 06-4. 간단한 메모장 만들기
import sys

option = sys.argv[1]

if option == "-a":
    memo = sys.argv[2]
    f = open("memo.txt", "a")
    f.write(memo)
    f.write("\n")
    f.close()
elif option == "-v":
    f = open("memo.txt")
    memo = f.read()
    f.close()
    print(memo)

# 06-5. tab 4개를 공백으로 바꾸기
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, "w")
f.write(space_content)
f.close

# 06-6.1 하위 디렉토리 검색하기
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname) # os.listdir: 해당 디렉터리에 있는 파일들의 리스트(파일 이름만 있음)를 구할 수 있음.
        for filename in filenames:
            full_filename = os.path.join(dirname, filename) # os.path.join: 디렉터리와 파일 이름을 이어 줌. 파일 경로를 포함하기 위해서는 dirname을 파일 앞에 앞에 덧붙여줘야함.
            if os.path.isdir(full_filename): # os.path.isdir : filename 안에 들어온 변수가 디렉토리인지 파일인지 확인함.
                search(full_filename) # 디렉토리인 경우, 다시 search 함수를 호출해 해당 디렉토리의 하위 파일들을 검색함(재귀호출)
                # 재귀 호출: 자기 자신을 다시 호출하는 프로그래밍 기법.
            else:
                ext = os.path.splitext(full_filename)[-1] # os.path.splitext : 파일 이름을 확장자 기준으로 두 부분으로 나누어줌.
                if ext == ".py":
                    print(full_filename)
    except PermissionError:
        pass

search("c:/")

# 06-6.2 하위 디렉토리 검색하기 - os.walk 이용
# os.walk : 시작 디렉토리부터 그 하위 모든 디렉토리를 차례로 방문하게 하는 함수
import os

for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".py":
            print("%s/%s" % (path, filename))

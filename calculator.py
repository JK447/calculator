import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0で割ることはできません！"
    return x / y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def ln(x):
    if x <= 0:
        return "自然対数は正の数にのみ適用可能です"
    return math.log(x)

def log10(x):
    if x <= 0:
        return "対数は正の数にのみ適用可能です"
    return math.log10(x)

def factorial(x):
    if x < 0:
        return "負の数の階乗は定義されていません"
    return math.factorial(x)

def to_binary(x):
    return bin(int(x))

def to_octal(x):
    return oct(int(x))

def to_hexadecimal(x):
    return hex(int(x))

def simple_interest(p, r, t):
    return p * r * t / 100

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def absolute_value(x):
    return abs(x)

def circle_area(radius):
    return math.pi * radius * radius

def triangle_area(base, height):
    return 0.5 * base * height

def cube_root(x):
    return x ** (1/3)

def exponential(x):
    return math.exp(x)

def gcd(x, y):
    return math.gcd(int(x), int(y))

def lcm(x, y):
    # LCM (a, b) = |a * b| / GCD(a, b)
    return abs(x * y) // gcd(x, y)

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while True:
    print("選択してください:")
    print("1.加算")
    print("2.減算")
    print("3.乗算")
    print("4.除算")
    print("11.サイン")
    print("12.コサイン")
    print("13.タンジェント")
    print("14.自然対数")
    print("15.10を基とする対数")
    print("16.階乗")
    print("17.2進数変換")
    print("18.8進数変換")
    print("19.16進数変換")
    print("20.単利計算")
    print("22.平方根")
    print("23.累乗")
    print("24.絶対値")
    print("25.円の面積")
    print("26.三角形の面積")
    print("27.立方根")
    print("28.指数関数")
    print("29.最大公約数 (GCD)")
    print("30.最小公倍数 (LCM)")
    print("31.素数チェック")
    print(":q.終了")

    choice = input("選択 (1~31):")

    if choice == ':q':
        print("終了します。")
        break

    try:
        num1 = float(input("最初の数字を入力してください: "))
    except ValueError:
        print("無効な入力です")
        continue


    if choice not in ['11', '12', '13', '14', '15', '16', '17', '18', '19','22','24']:
        try:
            num2 = float(input("次の数字を入力してください: "))
        except ValueError:
            print("無効な入力です")
            continue
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(num1, "/", num2, "=", result)
    elif choice == '11':
        print("sin(", num1, ") =", sine(num1))
    elif choice == '12':
        print("cos(", num1, ") =", cosine(num1))
    elif choice == '13':
        print("tan(", num1, ") =", tangent(num1))
    elif choice == '14':
        print("ln(", num1, ") =", ln(num1))
    elif choice == '15':
        print("log10(", num1, ") =", log10(num1))
    elif choice == '16':
        print(num1, "の階乗 =", factorial(num1))
    elif choice == '17':
        print(num1, "の2進数 =", to_binary(num1))
    elif choice == '18':
        print(num1, "の8進数 =", to_octal(num1))
    elif choice == '19':
        print(num1, "の16進数 =", to_hexadecimal(num1))
    elif choice == '20':
        t = float(input("時間 (年) を入力してください: "))
        print("単利 =", simple_interest(num1, num2, t))
    elif choice == '22':
        print("√", num1, "=", square_root(num1))
    elif choice == '23':
        print(num1, "^", num2, "=", power(num1, num2))
    elif choice == '24':
        print("|", num1, "| =", absolute_value(num1))
    elif choice == '25':
        print("円の面積 =", circle_area(num1))
    elif choice == '26':
        print("三角形の面積 =", triangle_area(num1, num2))
    elif choice == '27':
        print("∛", num1, "=", cube_root(num1))
    elif choice == '28':
        print("e^", num1, "=", exponential(num1))
    elif choice == '29':
        print("GCD(", num1, ",", num2, ") =", gcd(num1, num2))
    elif choice == '30':
        print("LCM(", num1, ",", num2, ") =", lcm(num1, num2))
    elif choice == '31':
        print(num1, "は素数です" if is_prime(num1) else num1, "は素数ではありません")
    else:
        print("無効な入力です")

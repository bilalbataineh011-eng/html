import os



while True:


    choice = input("""
اختر رقم المثال:

--- أنواع الأرقام ---
1  - type(1)
2  - type(-10)
3  - type(0)
4  - type(0.0)
5  - type(2.2)
6  - type(4E2)

--- العمليات الحسابية ---
7  - 10 + 3
8  - 10 - 3
9  - 10 * 3
10 - 10 ** 3
11 - 10 / 3
12 - 10 // 3
13 - 10 % 3

--- الدوال الأساسية ---
14 - pow(5, 2)
15 - abs(-50)
16 - round(5.46)
17 - round(5.468, 2)
18 - bin(512)
19 - hex(512)

0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=================================")

    if choice == "1":
        print("الأمر: type(1)")
        print("النتيجة:", type(1))

    elif choice == "2":
        print("الأمر: type(-10)")
        print("النتيجة:", type(-10))

    elif choice == "3":
        print("الأمر: type(0)")
        print("النتيجة:", type(0))

    elif choice == "4":
        print("الأمر: type(0.0)")
        print("النتيجة:", type(0.0))

    elif choice == "5":
        print("الأمر: type(2.2)")
        print("النتيجة:", type(2.2))

    elif choice == "6":
        print("الأمر: type(4E2)")
        print("النتيجة:", type(4E2))

    elif choice == "7":
        print("الأمر: 10 + 3")
        print("النتيجة:", 10 + 3)

    elif choice == "8":
        print("الأمر: 10 - 3")
        print("النتيجة:", 10 - 3)

    elif choice == "9":
        print("الأمر: 10 * 3")
        print("النتيجة:", 10 * 3)

    elif choice == "10":
        print("الأمر: 10 ** 3")
        print("النتيجة:", 10 ** 3)

    elif choice == "11":
        print("الأمر: 10 / 3")
        print("النتيجة:", 10 / 3)

    elif choice == "12":
        print("الأمر: 10 // 3")
        print("النتيجة:", 10 // 3)

    elif choice == "13":
        print("الأمر: 10 % 3")
        print("النتيجة:", 10 % 3)

    elif choice == "14":
        print("الأمر: pow(5, 2)")
        print("النتيجة:", pow(5, 2))

    elif choice == "15":
        print("الأمر: abs(-50)")
        print("النتيجة:", abs(-50))

    elif choice == "16":
        print("الأمر: round(5.46)")
        print("النتيجة:", round(5.46))

    elif choice == "17":
        print("الأمر: round(5.468, 2)")
        print("النتيجة:", round(5.468, 2))

    elif choice == "18":
        print("الأمر: bin(512)")
        print("النتيجة:", bin(512))

    elif choice == "19":
        print("الأمر: hex(512)")
        print("النتيجة:", hex(512))

    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=================================")
    input("\nاضغط Enter للمتابعة...")

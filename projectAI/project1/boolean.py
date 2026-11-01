import os

while True:
    choice = input("""
اختر رقم المثال (Boolean):

--- القيم المنطقية الأساسية ---
1  - bool(True)
2  - bool(False)

--- قيم تُعتبر False في بايثون ---
3  - bool(None)
4  - bool(False)
5  - bool(0)
6  - bool(0.0)
7  - bool([])
8  - bool({})
9  - bool(())
10 - bool('')
11 - bool(range(0))
12 - bool(set())

0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=================================")

    # -------- القيم المنطقية --------
    if choice == "1":
        print("الأمر: bool(True)  # تحويل True إلى Boolean")
        print("النتيجة:", bool(True))

    elif choice == "2":
        print("الأمر: bool(False)  # تحويل False إلى Boolean")
        print("النتيجة:", bool(False))

    # -------- القيم التي تقيّم False --------
    elif choice == "3":
        print("الأمر: bool(None)  # None تعني لا شيء")
        print("النتيجة:", bool(None))

    elif choice == "4":
        print("الأمر: bool(False)  # القيمة المنطقية False")
        print("النتيجة:", bool(False))

    elif choice == "5":
        print("الأمر: bool(0)  # الصفر يُعتبر False")
        print("النتيجة:", bool(0))

    elif choice == "6":
        print("الأمر: bool(0.0)  # صفر عشري يُعتبر False")
        print("النتيجة:", bool(0.0))

    elif choice == "7":
        print("الأمر: bool([])  # قائمة فارغة")
        print("النتيجة:", bool([]))

    elif choice == "8":
        print("الأمر: bool({})  # قاموس فارغ")
        print("النتيجة:", bool({}))

    elif choice == "9":
        print("الأمر: bool(())  # tuple فارغ")
        print("النتيجة:", bool(()))

    elif choice == "10":
        print("الأمر: bool('')  # نص فارغ")
        print("النتيجة:", bool(""))

    elif choice == "11":
        print("الأمر: bool(range(0))  # range بدون عناصر")
        print("النتيجة:", bool(range(0)))

    elif choice == "12":
        print("الأمر: bool(set())  # set فارغ")
        print("النتيجة:", bool(set()))

    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=================================")
    input("\nاضغط Enter للمتابعة...")

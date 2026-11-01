import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    choice = input("""
اختر رقم المثال (Loops):

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list2 = [(1, 2), (3, 4), (5, 6)]
my_dict = {'a': 1, 'b': 2, 'c': 3}

--- for loop ---
1  - for مع list
2  - for مع tuple
3  - for مع list of tuples
4  - for مع string
5  - for مع dictionary (unpacking)

--- while loop ---
6  - while مع break
7  - while مع continue
8  - while مع input (quit)

0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 50)

    # البيانات المستخدمة
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    my_list2 = [(1, 2), (3, 4), (5, 6)]
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # ---------- for مع list ----------
    if choice == "1":
        print("🧠 الأمر:")
        print(">>> for num in my_list")
        print("\n📝 الشرح: المرور على كل عنصر داخل القائمة.")
        print("\n✅ النتيجة:")
        for num in my_list:
            print("العنصر:", num)

    # ---------- for مع tuple ----------
    elif choice == "2":
        print("🧠 الأمر:")
        print(">>> for num in my_tuple")
        print("\n📝 الشرح: المرور على عناصر الـ tuple.")
        print("\n✅ النتيجة:")
        for num in my_tuple:
            print("العنصر:", num)

    # ---------- for مع list of tuples ----------
    elif choice == "3":
        print("🧠 الأمر:")
        print(">>> for pair in my_list2")
        print("\n📝 الشرح: كل عنصر هو tuple.")
        print("\n✅ النتيجة:")
        for pair in my_list2:
            print("العنصر:", pair)

    # ---------- for مع string ----------
    elif choice == "4":
        print("🧠 الأمر:")
        print(">>> for ch in '123'")
        print("\n📝 الشرح: المرور على كل حرف في النص.")
        print("\n✅ النتيجة:")
        for ch in "123":
            print("الحرف:", ch)

    # ---------- for مع dictionary ----------
    elif choice == "5":
        print("🧠 الأمر:")
        print(">>> for k, v in my_dict.items()")
        print("\n📝 الشرح: تفكيك القاموس (key, value).")
        print("\n✅ النتيجة:")
        for k, v in my_dict.items():
            print("المفتاح:", k, "| القيمة:", v)

    # ---------- while + break ----------
    elif choice == "6":
        print("🧠 الأمر:")
        print(">>> while True (مع break)")
        print("\n📝 الشرح: الخروج من الحلقة عند تحقق شرط.")
        print("\n✅ النتيجة:")
        x = 0
        while True:
            print("x =", x)
            if x == 3:
                print("break → الخروج من الحلقة")
                break
            x +=1

    # ---------- while + continue ----------
    elif choice == "7":
        print("🧠 الأمر:")
        print(">>> while x < 5 (مع continue)")
        print("\n📝 الشرح: تخطي دورة واحدة عند شرط معين.")
        print("\n✅ النتيجة:")
        x = 0
        while x < 5:
            x += 1
            if x == 3:
                print("continue → تخطي الرقم 3")
                continue
            print("x =", x)

    # ---------- while + input ----------
    elif choice == "8":
        print("🧠 الأمر:")
        print(">>> while msg != 'quit'")
        print("\n📝 الشرح: الحلقة تستمر حتى كتابة quit.")
        print("\n✅ النتيجة:")
        msg = ""
        while msg != "quit":
            msg = input("What should I do? ")
            print("المدخل:", msg)

    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=" * 50)
    input("\nاضغط Enter للمتابعة...")

import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    choice = input("""
اختر رقم المثال (range):

1  - range(10)
2  - range(1, 10)
3  - list(range(0, 10, 2))
4  - range + for loop

0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 50)

    # ---------- range(10) ----------
    if choice == "1":
        print("🧠 الأمر:")
        print(">>> range(10)")
        print("\n📝 الشرح: إنشاء أرقام من 0 إلى 9 (10 غير مشمول).")
        print("\n✅ النتيجة:")
        print("كائن range:", range(10))
        print("بعد التحويل لقائمة:", list(range(10)))

    # ---------- range(1, 10) ----------
    elif choice == "2":
        print("🧠 الأمر:")
        print(">>> range(1, 10)")
        print("\n📝 الشرح: إنشاء أرقام من 1 إلى 9 (10 غير مشمول).")
        print("\n✅ النتيجة:")
        print("كائن range:", range(1, 10))
        print("بعد التحويل لقائمة:", list(range(1, 10)))

    # ---------- list(range(...)) ----------
    elif choice == "3":
        print("🧠 الأمر:")
        print(">>> list(range(0, 10, 2))")
        print("\n📝 الشرح: من 0 إلى 8 بخطوة 2 (أرقام زوجية).")
        print("\n✅ النتيجة:")
        print(list(range(0, 10, 2)))

    # ---------- range + for ----------
    elif choice == "4":
        print("🧠 الأمر:")
        print(">>> for i in range(5)")
        print("\n📝 الشرح: استخدام range داخل حلقة for.")
        print("\n✅ النتيجة:")
        for i in range(5):
            print("i =", i)

    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=" * 50)
    input("\nاضغط Enter للمتابعة...")

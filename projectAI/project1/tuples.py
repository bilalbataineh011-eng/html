import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    choice = input("""
اختر رقم المثال (Tuple):

my_tuple = ('apple', 'grapes', 'mango', 'grapes')

--- إنشاء واستخدام Tuple ---
1  - Tuple unpacking
2  - len(my_tuple)
3  - my_tuple[2]
4  - my_tuple[-1]

--- عدم قابلية التغيير (Immutability) ---
5  - محاولة تعديل عنصر
6  - محاولة append

--- دوال Tuple ---
7  - index()
8  - count()


0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 45)

    my_tuple = ('apple', 'grapes', 'mango', 'grapes')

    # -------- Tuple basics --------
    if choice == "1":
        print("🧠 الأمر:")
        print(">>> apple, grapes1, mango, grapes2 = my_tuple")
        print("\n📝 الشرح: تفكيك (unpacking) عناصر الـ tuple في متغيرات.")
        print("\n✅ النتيجة:")
        apple, grapes1, mango, grapes2 = my_tuple
        print("apple :", apple)
        print("grapes:", grapes1)
        print("mango :", mango)
        print("grapes :", grapes2)

    elif choice == "2":
        print("🧠 الأمر:")
        print(">>> len(my_tuple)")
        print("\n📝 الشرح: عدد العناصر داخل الـ tuple.")
        print("\n✅ النتيجة:")
        print(len(my_tuple))

    elif choice == "3":
        print("🧠 الأمر:")
        print(">>> my_tuple[2]")
        print("\n📝 الشرح: الوصول لعنصر باستخدام index (يبدأ من 0).")
        print("\n✅ النتيجة:")
        print(my_tuple[2])

    elif choice == "4":
        print("🧠 الأمر:")
        print(">>> my_tuple[-1]")
        print("\n📝 الشرح: الوصول لآخر عنصر باستخدام index سالب.")
        print("\n✅ النتيجة:")
        print(my_tuple[-1])

    # -------- Immutability --------
    elif choice == "5":
        print("🧠 الأمر:")
        print(">>> my_tuple[1] = 'donuts'")
        print("\n📝 الشرح: الـ tuple غير قابلة للتغيير (immutable).")
        print("\n✅ النتيجة:")
        try:
            my_tuple[1] = 'donuts'
        except Exception as e:
            print("❌ الخطأ:", type(e).__name__)

    elif choice == "6":
        print("🧠 الأمر:")
        print(">>> my_tuple.append('candy')")
        print("\n📝 الشرح: لا يوجد append لأن tuple غير قابلة للتعديل.")
        print("\n✅ النتيجة:")
        try:
            my_tuple.append('candy')
        except Exception as e:
            print("❌ الخطأ:", type(e).__name__)

    # -------- Methods --------
    elif choice == "7":
        print("🧠 الأمر:")
        print(">>> my_tuple.index('grapes')")
        print("\n📝 الشرح: إرجاع أول موقع للكلمة grapes.")
        print("\n✅ النتيجة:")
        print(my_tuple.index('grapes'))

    elif choice == "8":
        print("🧠 الأمر:")
        print(">>> my_tuple.count('grapes')")
        print("\n📝 الشرح: حساب عدد مرات تكرار grapes.")
        print("\n✅ النتيجة:")
        print(my_tuple.count('grapes'))




    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=" * 45)
    input("\nاضغط Enter للمتابعة...")

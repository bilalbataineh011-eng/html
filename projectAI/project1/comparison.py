import os

# بيانات الطالب
name = "sofyan tarawneh"
age = 20
score = 50
passed_score = 60
banned_students = ["ali", "omar"]
is_verified = True

while True:
    os.system("cls" if os.name == "nt" else "clear")

    choice = input("""
اختر رقم المثال (Operators & Conditions):

name = "sofyan tarawneh"
age = 20
score = 78
passed_score = 60
banned_students = ["ali", "omar"]
is_verified = True

--- Comparison Operators ---
1  - ==
2  - !=
3  - >
4  - <
5  - >=
6  - <=

--- is / is not ---
7  - ==
8  - is
9  - is not

--- Logical Operators ---
10 - and
11 - or
12 - not
13 - in / not in

--- if / elif / else ---
14 - قرار نجاح الطالب

0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 50)

    # ---------- Comparison Operators ----------
    if choice == "1":
        print("🧠 الأمر:")
        print(">>> score == passed_score")
        print("\n📝 الشرح: هل القيمتان متساويتان؟")
        print("\n✅ النتيجة:")
        print(score == passed_score)

    elif choice == "2":
        print("🧠 الأمر:")
        print(">>> score != passed_score")
        print("\n📝 الشرح: هل القيمتان غير متساويتين؟")
        print("\n✅ النتيجة:")
        print(score != passed_score)

    elif choice == "3":
        print("🧠 الأمر:")
        print(">>> score > passed_score")
        print("\n📝 الشرح: هل score أكبر من passed_score؟")
        print("\n✅ النتيجة:")
        print(score > passed_score)

    elif choice == "4":
        print("🧠 الأمر:")
        print(">>> score < passed_score")
        print("\n📝 الشرح: هل score أصغر من passed_score؟")
        print("\n✅ النتيجة:")
        print(score < passed_score)

    elif choice == "5":
        print("🧠 الأمر:")
        print(">>> score >= passed_score")
        print("\n📝 الشرح: هل score أكبر أو يساوي passed_score؟")
        print("\n✅ النتيجة:")
        print(score >= passed_score)

    elif choice == "6":
        print("🧠 الأمر:")
        print(">>> score <= passed_score")
        print("\n📝 الشرح: هل score أصغر أو يساوي passed_score؟")
        print("\n✅ النتيجة:")
        print(score <= passed_score)

    # ---------- is / is not ----------
    elif choice == "7":
        a = [1, 2, 3]
        b = [1, 2, 3]
        print("🧠 الأمر:")
        print(">>> a == b")
        print("\n📝 الشرح: مقارنة القيم وليس المكان في الذاكرة.")
        print("\n✅ النتيجة:")
        print(a == b)

    elif choice == "8":
        a = [1, 2, 3]
        b = [1, 2, 3]
        print("🧠 الأمر:")
        print(">>> a is b")
        print("\n📝 الشرح: هل المتغيران يشيران لنفس المكان في الذاكرة؟")
        print("\n✅ النتيجة:")
        print(a is b)

    elif choice == "9":
        a = [1, 2, 3]
        b = [1, 2, 3]
        print("🧠 الأمر:")
        print(">>> a is not b")
        print("\n📝 الشرح: هل المتغيران لا يشيران لنفس المرجع؟")
        print("\n✅ النتيجة:")
        print(a is not b)

    # ---------- Logical Operators ----------
    elif choice == "10":
        print("🧠 الأمر:")
        print(">>> 1 < 2 and 4 > 1")
        print("\n📝 الشرح: and تعيد True إذا كل الشروط صحيحة.")
        print("\n✅ النتيجة:")
        print(1 < 2 and 4 > 1)

    elif choice == "11":
        print("🧠 الأمر:")
        print(">>> 1 > 3 or 4 > 1")
        print("\n📝 الشرح: or تعيد True إذا شرط واحد صحيح.")
        print("\n✅ النتيجة:")
        print(1 > 3 or 4 > 1)

    elif choice == "12":
        print("🧠 الأمر:")
        print(">>> not True")
        print("\n📝 الشرح: not تعكس القيمة المنطقية.")
        print("\n✅ النتيجة:")
        print(not True)

    elif choice == "13":
        print("🧠 الأمر:")
        print(">>> name not in banned_students")
        print("\n📝 الشرح: التحقق إذا الاسم غير موجود في القائمة.")
        print("\n✅ النتيجة:")
        print(name not in banned_students)

    # ---------- if / elif / else ----------
    elif choice == "14":
        print("🧠 الأمر:")
        print(">>> if score >= passed_score and is_verified and name not in banned_students")
        print("\n📝 الشرح: اتخاذ قرار بناءً على عدة شروط.")
        print("\n✅ النتيجة:")
        if score >= passed_score and is_verified and name not in banned_students:
            print("✅ الطالب ناجح ومسموح له بالدخول")
        elif score < passed_score and is_verified:
            print("❌ الطالب راسب")
        else:
            print("⛔ لا يُسمح بالدخول")

    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=" * 50)
    input("\nاضغط Enter للمتابعة...")

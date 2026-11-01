import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    choice = input("""
اختر رقم المثال (عمليات متقدمة على القوائم):
basket = ['apples', 'pears', 'oranges']
--- نسخ القوائم ---
1  - copy()
2  - slicing copy [:]

--- الحذف من القائمة ---
3  - pop()
4  - pop(index)
5  - remove(value)
6  - clear()
7  - del index

--- ترتيب القوائم ---
8  - sort()
9  - sort(reverse=True)
10 - reverse()
11 - sorted()
12 - reversed()

--- عمليات مفيدة ---
13 - in
14 - min()
15 - max()
16 - sum()

--- أول وآخر عنصر ---
17 - استخراج أول وآخر عنصر

0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 45)

    # -------- نسخ القوائم --------
    if choice == "1":
        basket = ['apples', 'pears', 'oranges']
        print("🧠 الأمر:")
        print(">>> new_basket = basket.copy()")
        print("\n📝 الشرح: إنشاء نسخة مستقلة من القائمة.")
        print("\n✅ النتيجة:")
        print("الأصل:", basket)
        new_basket = basket.copy()
        print("النسخة:", new_basket)

    elif choice == "2":
        basket = ['apples', 'pears', 'oranges']
        print("🧠 الأمر:")
        print(">>> new_basket = basket[:1]")
        print("\n📝 الشرح: نسخ القائمة باستخدام slicing.")
        print("\n✅ النتيجة:")
        print("الأصل:", basket)
        new_basket = basket[:1]
        print("النسخة:", new_basket)

    # -------- الحذف من القائمة --------
    elif choice == "3":
        lst = [1, 2, 3]
        print("🧠 الأمر:")
        print(">>> lst.pop()")
        print("\n📝 الشرح: حذف آخر عنصر من القائمة.")
        print("\n✅ النتيجة:")
        print("قبل:", lst)
        removed = lst.pop()
        print("العنصر المحذوف:", removed)
        print("بعد :", lst)

    elif choice == "4":
        lst = [1, 2, 3]
        print("🧠 الأمر:")
        print(">>> lst.pop(1)")
        print("\n📝 الشرح: حذف عنصر باستخدام index.")
        print("\n✅ النتيجة:")
        print("قبل:", lst)
        removed = lst.pop(1)
        print("العنصر المحذوف:", removed)
        print("بعد :", lst)

    elif choice == "5":
        lst = [1, 2, 3]
        print("🧠 الأمر:")
        print(">>> lst.remove(2)")
        print("\n📝 الشرح: حذف أول ظهور للقيمة 2.")
        print("\n✅ النتيجة:")
        print("قبل:", lst)
        lst.remove(2)
        print("بعد :", lst)

    elif choice == "6":
        lst = [1, 2, 3]
        print("🧠 الأمر:")
        print(">>> lst.clear()")
        print("\n📝 الشرح: حذف جميع عناصر القائمة.")
        print("\n✅ النتيجة:")
        print("قبل:", lst)
        lst.clear()
        print("بعد :", lst)

    elif choice == "7":
        lst = [1, 2, 3]
        print("🧠 الأمر:")
        print(">>> del lst[0]")
        print("\n📝 الشرح: حذف عنصر باستخدام del.")
        print("\n✅ النتيجة:")
        print("قبل:", lst)
        del lst[0]
        print("بعد :", lst)

    # -------- ترتيب القوائم --------
    elif choice == "8":
        lst = [1, 2, 5, 3]
        print("🧠 الأمر:")
        print(">>> lst.sort()")
        print("\n📝 الشرح: ترتيب تصاعدي (يعدّل القائمة الأصلية).")
        print("\n✅ النتيجة:")
        print("قبل:", lst)
        lst.sort()
        print("بعد :", lst)

    elif choice == "9":
        lst = [1, 2, 5, 3]
        print("🧠 الأمر:")
        print(">>> lst.sort(reverse=True)")
        print("\n📝 الشرح: ترتيب تنازلي.")
        print("\n✅ النتيجة:")
        print("قبل:", lst)
        lst.sort(reverse=True)
        print("بعد :", lst)

    elif choice == "10":
        lst = [1, 2, 5, 3]
        print("🧠 الأمر:")
        print(">>> lst.reverse()")
        print("\n📝 الشرح: عكس ترتيب العناصر.")
        print("\n✅ النتيجة:")
        print("قبل:", lst)
        lst.reverse()
        print("بعد :", lst)

    elif choice == "11":
        lst = [1, 2, 5, 3]
        print("🧠 الأمر:")
        print(">>> sorted(lst)")
        print("\n📝 الشرح: إنشاء قائمة جديدة مرتبة بدون تعديل الأصل.")
        print("\n✅ النتيجة:")
        print("الأصل :", lst)
        print("الجديد :", sorted(lst))

    elif choice == "12":
        lst = [1, 2, 5, 3]
        print("🧠 الأمر:")
        print(">>> list(reversed(lst))")
        print("\n📝 الشرح: reversed ترجع iterator لذلك نحولها لقائمة.")
        print("\n✅ النتيجة:")
        print(list(reversed(lst)))

    # -------- عمليات مفيدة --------
    elif choice == "13":
        print("🧠 الأمر:")
        print(">>> 1 in [1, 2, 5, 3]")
        print("\n📝 الشرح: التحقق من وجود عنصر.")
        print("\n✅ النتيجة:")
        print(1 in [1, 2, 5, 3])

    elif choice == "14":
        print("🧠 الأمر:")
        print(">>> min([1, 2, 3, 4, 5])")
        print("\n📝 الشرح: إيجاد أصغر قيمة.")
        print("\n✅ النتيجة:")
        print(min([1, 2, 3, 4, 5]))

    elif choice == "15":
        print("🧠 الأمر:")
        print(">>> max([1, 2, 3, 4, 5])")
        print("\n📝 الشرح: إيجاد أكبر قيمة.")
        print("\n✅ النتيجة:")
        print(max([1, 2, 3, 4, 5]))

    elif choice == "16":
        print("🧠 الأمر:")
        print(">>> sum([1, 2, 3, 4, 5])")
        print("\n📝 الشرح: حساب مجموع القيم.")
        print("\n✅ النتيجة:")
        print(sum([1, 2, 3, 4, 5]))

    # -------- أول وآخر عنصر --------
    elif choice == "17":
        mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
        print("🧠 الأمر:")
        print(">>> first, *x, last = mList")
        print("\n📝 الشرح: unpacking لاستخراج أول وآخر عنصر.")
        print("\n✅ النتيجة:")
        print("القائمة:", mList)
        first, *x, last = mList
        print("أول عنصر:", first)
        print("آخر عنصر:", last)

    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=" * 45)
    input("\nاضغط Enter للمتابعة...")

import os

while True:
    choice = input("""
اختر رقم المثال (List Basics):
my_list = [1, 2, '3', True]
--- معلومات عن القائمة ---
1  - len(my_list)
2  - my_list.index('3')
3  - my_list.count(2)

--- الوصول والتقطيع ---
4  - my_list[3]
5  - my_list[1:]
6  - my_list[:1]
7  - my_list[-1]
8  - my_list[::1]
9  - my_list[::-1]
10 - my_list[0:3:2]

--- الإضافة ---
11 - my_list * 2
12 - my_list + [100]
13 - my_list.append(100)
14 - my_list.extend([100, 200])
15 - my_list.insert(2, '!!!')

--- نصوص ---
16 - ' '.join(['Hello','There'])

0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=================================")

    # القائمة الأساسية (لا نغيرها مباشرة)
    my_list = [1, 2, '3', True]

    if choice == "1":
        print("الأمر: len(my_list)  # حساب عدد العناصر")
        print("القائمة:", my_list)
        print("النتيجة:", len(my_list))

    elif choice == "2":
        print("الأمر: my_list.index('3')  # معرفة موقع العنصر '3'")
        print("النتيجة:", my_list.index('3'))

    elif choice == "3":
        print("الأمر: my_list.count(2)  # عدّ عدد مرات ظهور 2")
        print("النتيجة:", my_list.count(2))

    elif choice == "4":
        print("الأمر: my_list[3]  # جلب عنصر باستخدام index")
        print("النتيجة:", my_list[3])

    elif choice == "5":
        print("الأمر: my_list[1:]  # من العنصر الثاني للنهاية")
        print("النتيجة:", my_list[1:])

    elif choice == "6":
        print("الأمر: my_list[:1]  # أول عنصر فقط")
        print("النتيجة:", my_list[:1])

    elif choice == "7":
        print("الأمر: my_list[-1]  # آخر عنصر")
        print("النتيجة:", my_list[-1])

    elif choice == "8":
        print("الأمر: my_list[::1]  # نفس القائمة بدون تغيير")
        print( my_list[::1])

    elif choice == "9":
        print("الأمر: my_list[::-1]  # عكس ترتيب القائمة")
        print(my_list[::-1])

    elif choice == "10":
        print("الأمر: my_list[0:3:2]  # slicing (بداية، نهاية، خطوة)")
        print("النتيجة:", my_list[0:3:2])

    elif choice == "11":
        print("الأمر: my_list * 2  # تكرار القائمة")
        print("النتيجة:", my_list * 2)

    elif choice == "12":
        print("الأمر: my_list + [100]  # إنشاء قائمة جديدة (بدون تعديل الأصل)")
        print("النتيجة:", my_list + [100])

    elif choice == "13":
        print("الأمر: my_list.append(100)  # إضافة عنصر (تعديل القائمة)")
        temp = my_list.copy()
        temp.append(100)
        print("النتيجة:", temp)

    elif choice == "14":
        print("الأمر: my_list.extend([100, 200])  # إضافة أكثر من عنصر")
        temp = my_list.copy()
        temp.extend([100, 200])
        print("النتيجة:", temp)

    elif choice == "15":
        print("الأمر: my_list.insert(2, '!!!')  # إدخال عنصر بمكان محدد")
        temp = my_list.copy()
        temp.insert(2, '!!!')
        print("النتيجة:", temp)

    elif choice == "16":
        print("الأمر: ' '.join(['Hello','There'])  # دمج عناصر نصية بفاصل")
        print("النتيجة:", ' '.join(['Hello', 'There']))

    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=================================")
    input("\nاضغط Enter للمتابعة...")

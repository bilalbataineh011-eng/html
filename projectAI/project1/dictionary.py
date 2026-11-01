import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    choice = input("""
اختر رقم المثال (Dictionary):

my_dict = {
    'name': 'sofyan tarawneh',
    'age': 80,
    'magic_power': False
}

--- معلومات أساسية ---
1  - عرض قيمة باستخدام المفتاح
2  - len(my_dict)
3  - keys()
4  - values()
5  - items()

--- الإضافة والوصول ---
6  - إضافة عنصر جديد
7  - get(key)
8  - get(key, default)

--- الحذف ---
9  - del key
10 - pop(key, default)

--- التحديث والدمج ---
11 - update()
12 - دمج باستخدام **

--- إنشاء قاموس ---
13 - dict من list
14 - dict من zip

--- الحذف مع الإرجاع ---
15 - pop() مع إرجاع القيمة


0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 45)

    # القاموس الأساسي
    my_dict = {
        'name': 'sofyan tarawneh',
        'age': 80,
        'magic_power': False
    }

    # -------- معلومات أساسية --------
    if choice == "1":
        print("🧠 الأمر:")
        print(">>> my_dict['name']")
        print("\n📝 الشرح: الوصول للقيمة باستخدام المفتاح.")
        print("\n✅ النتيجة:")
        print(my_dict['name'])

    elif choice == "2":
        print("🧠 الأمر:")
        print(">>> len(my_dict)")
        print("\n📝 الشرح: عدد العناصر داخل القاموس.")
        print("\n✅ النتيجة:")
        print(len(my_dict))

    elif choice == "3":
        print("🧠 الأمر:")
        print(">>> my_dict.keys()")
        print("\n📝 الشرح: إرجاع جميع المفاتيح.")
        print("\n✅ النتيجة:")
        print(list(my_dict.keys()))

    elif choice == "4":
        print("🧠 الأمر:")
        print(">>> my_dict.values()")
        print("\n📝 الشرح: إرجاع جميع القيم.")
        print("\n✅ النتيجة:")
        print(list(my_dict.values()))

    elif choice == "5":
        print("🧠 الأمر:")
        print(">>> my_dict.items()")
        print("\n📝 الشرح: إرجاع أزواج (مفتاح، قيمة).")
        print("\n✅ النتيجة:")
        print(list(my_dict.items()))

    # -------- الإضافة والوصول --------
    elif choice == "6":
        print("🧠 الأمر:")
        print(">>> my_dict['favourite_snack'] = 'Grapes'")
        print("\n📝 الشرح: إضافة عنصر جديد للقاموس.")
        print("\n✅ النتيجة:")
        print("قبل:", my_dict)
        my_dict['favourite_snack'] = 'Grapes'
        print("بعد :", my_dict)

    elif choice == "7":
        print("🧠 الأمر:")
        print(">>> my_dict.get('age')")
        print("\n📝 الشرح: جلب قيمة المفتاح بدون حدوث خطأ.")
        print("\n✅ النتيجة:")
        print(my_dict.get('age'))

    elif choice == "8":
        print("🧠 الأمر:")
        print(">>> my_dict.get('ages', 0)")
        print("\n📝 الشرح: إرجاع قيمة افتراضية إذا المفتاح غير موجود.")
        print("\n✅ النتيجة:")
        print(my_dict.get('ages', 0))

    # -------- الحذف --------
    elif choice == "9":
        print("🧠 الأمر:")
        print(">>> del my_dict['name']")
        print("\n📝 الشرح: حذف عنصر باستخدام del.")
        print("\n✅ النتيجة:")
        print("قبل:", my_dict)
        del my_dict['name']
        print("بعد :", my_dict)

    elif choice == "10":
        print("🧠 الأمر:")
        print(">>> my_dict.pop('name', None)")
        print("\n📝 الشرح: حذف عنصر مع حماية من الخطأ.")
        print("\n✅ النتيجة:")
        print("قبل:", my_dict)
        my_dict.pop('name', None)
        print("بعد :", my_dict)

    # -------- التحديث والدمج --------
    elif choice == "11":
        print("🧠 الأمر:")
        print(">>> my_dict.update({'cool': True})")
        print("\n📝 الشرح: إضافة أو تعديل عدة قيم دفعة واحدة.")
        print("\n✅ النتيجة:")
        print("قبل:", my_dict)
        my_dict.update({'cool': True})
        print("بعد :", my_dict)

    elif choice == "12":
        print("🧠 الأمر:")
        print(">>> {**my_dict, **{'cool': True}}")
        print("\n📝 الشرح: دمج قاموسين بدون تعديل الأصل.")
        print("\n✅ النتيجة:")
        new_dict = {**my_dict, **{'cool': True}}
        print(new_dict)

    # -------- إنشاء قاموس --------
    elif choice == "13":
        print("🧠 الأمر:")
        print(">>> dict([['name','sofyan tarawneh'],['age',32],['magic_power',False]])")
        print("\n📝 الشرح: إنشاء قاموس من list تحتوي أزواج.")
        print("\n✅ النتيجة:")
        new_dict = dict([
            ['name', 'sofyan tarawneh'],
            ['age', 32],
            ['magic_power', False]
        ])
        print(new_dict)

    elif choice == "14":
        print("🧠 الأمر:")
        print(">>> dict(zip(['name', 'age', 'magic_power'],['sofyan tarawneh', 32, False]))")
        print("\n📝 الشرح: إنشاء قاموس من قائمتين.")
        print("\n✅ النتيجة:")
        new_dict = dict(zip(
            ['name', 'age', 'magic_power'],
            ['sofyan tarawneh', 32, False]
        ))
        print(new_dict)

    # -------- الحذف مع الإرجاع --------
    elif choice == "15":
        print("🧠 الأمر:")
        print(">>> my_dict.pop('favourite_snack')")
        print("\n📝 الشرح: حذف عنصر وإرجاع قيمته.")
        print("\n✅ النتيجة:")
        my_dict['favourite_snack'] = 'Grapes'
        print("قبل:", my_dict)
        removed = my_dict.pop('favourite_snack')
        print("القيمة المحذوفة:", removed)
        print("بعد :", my_dict)



    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=" * 45)
    input("\nاضغط Enter للمتابعة...")

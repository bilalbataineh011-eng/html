import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    choice = input("""
اختر رقم المثال (Strings):

--- النوع وكتابة النص ---
1  - type('Hellloooooo')
2  - 'I\\'m thirsty'
3  - "I'm thirsty"
4  - "\\n" (سطر جديد)
5  - "\\t" (تاب)
'Hello'

name = "sofyan tarawneh"
name1 = "sofyan"
name2 = "tarawneh"

--- الفهرسة والتقطيع ---
6  - 'Hey you!'[4]
7  - name[4]
8  - name[:]
9  - name[1:]
10 - name[:1]
11 - name[-1]
12 - name[::1]
13 - name[::-1]
14 - name[0:10:2]

--- عمليات على النص ---
15 - 'Hi there ' + 'Timmy'
16 - '*' * 10
17 - len('turtle')

--- الدوال (Methods) ---
18 - strip()
19 - strip('d')
20 - split()
21 - replace()
22 - startswith()
23 - endswith()
24 - index()
25 - upper()
26 - lower()
27 - capitalize()
28 - find()
29 - count()

--- تنسيق النص ---
30 - f-string
31 - format()
32 - % formatting

--- Palindrome ---
33 - فحص كلمة palindrome

0  - خروج

أدخل الرقم: """)

    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 45)

    # الاسم المستخدم في الأمثلة
    name = "sofyan tarawneh"
    name1 = "sofyan"
    name2 = "tarawneh"

    # ---------- النوع ----------
    if choice == "1":
        print("🧠 الأمر:")
        print(">>> type('Hellloooooo')")
        print("\n📝 الشرح: معرفة نوع البيانات (String).")
        print("\n✅ النتيجة:")
        print(type('Hellloooooo'))

    elif choice == "2":
        print("🧠 الأمر:")
        print(r">>> 'I\'m thirsty'")
        print("\n📝 الشرح: استخدام \\ للهروب من ' داخل النص.")
        print("\n✅ النتيجة:")
        print('I\'m thirsty')

    elif choice == "3":
        print("🧠 الأمر:")
        print('>>> "I\'m thirsty"')
        print("\n📝 الشرح: استخدام double quotes لكتابة ' بدون هروب.")
        print("\n✅ النتيجة:")
        print("I'm thirsty")

    elif choice == "4":
        print("🧠 الأمر:")
        print(r">>> print('\n')")
        print("\n📝 الشرح: طباعة سطر جديد (النتيجة سطر فاضي).")
        print("\n✅ النتيجة:")
        print("(قبل السطر الجديد)")
        print("\n")
        print("(بعد السطر الجديد)")

    elif choice == "5":
        print("🧠 الأمر:")
        print(r">>> print('\tنص بعد التاب')")
        print("\n📝 الشرح: طباعة tab قبل النص.")
        print("\n✅ النتيجة:")
        print("\tنص بعد التاب")

    # ---------- Indexing / Slicing ----------
    elif choice == "6":
        print("🧠 الأمر:")
        print(">>> 'Hey you!'[4]")
        print("\n📝 الشرح: جلب حرف باستخدام index (العد يبدأ من 0).")
        print("\n✅ النتيجة:")
        print('Hey you!'[4])

    elif choice == "7":
        print("🧠 الأمر:")
        print(">>> name[4]")
        print(f"\n📝 الشرح: name = '{name}' ثم نجيب الحرف رقم 4.")
        print("\n✅ النتيجة:")
        print(name[4])

    elif choice == "8":
        print("🧠 الأمر:")
        print(">>> name[:]")
        print("\n📝 الشرح: إرجاع النص كامل.")
        print("\n✅ النتيجة:")
        print(name[:])

    elif choice == "9":
        print("🧠 الأمر:")
        print(">>> name[1:]")
        print("\n📝 الشرح: حذف أول حرف (من index 1 للنهاية).")
        print("\n✅ النتيجة:")
        print(name[1:])

    elif choice == "10":
        print("🧠 الأمر:")
        print(">>> name[:1]")
        print("\n📝 الشرح: أول حرف فقط (من البداية لقبل 1).")
        print("\n✅ النتيجة:")
        print(name[:1])

    elif choice == "11":
        print("🧠 الأمر:")
        print(">>> name[-1]")
        print("\n📝 الشرح: آخر حرف باستخدام index سالب.")
        print("\n✅ النتيجة:")
        print(name[-1])

    elif choice == "12":
        print("🧠 الأمر:")
        print(">>> name[::]")
        print("\n📝 الشرح: نفس النص (خطوة 1 يعني طبيعي).")
        print("\n✅ النتيجة:")
        print(name[::1])

    elif choice == "13":
        print("🧠 الأمر:")
        print(">>> name[::-1]")
        print("\n📝 الشرح: عكس النص (خطوة -1).")
        print("\n✅ النتيجة:")
        print(name[::-1])

    elif choice == "14":
        print("🧠 الأمر:")
        print(">>> name[0:10:2]")
        print("\n📝 الشرح: من 0 لقبل 10 وبخطوة 2 (كل حرفين حرف).")
        print("\n✅ النتيجة:")
        print(name[0:10:2])

    # ---------- عمليات ----------
    elif choice == "15":
        print("🧠 الأمر:")
        print(">>> 'Hi there ' + 'Timmy'")
        print("\n📝 الشرح: دمج نصين باستخدام +.")
        print("\n✅ النتيجة:")
        print('Hi there ' + 'Timmy')

    elif choice == "16":
        print("🧠 الأمر:")
        print(">>> '*' * 10")
        print("\n📝 الشرح: تكرار النص 10 مرات.")
        print("\n✅ النتيجة:")
        print('*' * 10)

    elif choice == "17":
        print("🧠 الأمر:")
        print(">>> len('turtle')")
        print("\n📝 الشرح: حساب عدد الأحرف داخل النص.")
        print("\n✅ النتيجة:")
        print(len('turtle'))

    # ---------- Methods ----------
    elif choice == "18":
        print("🧠 الأمر:")
        print(">>> '  I am alone '.strip()")
        print("\n📝 الشرح: إزالة الفراغات من الطرفين.")
        print("\n✅ النتيجة:")
        print("قبل:", repr('  I am alone '))
        print("بعد :", repr('  I am alone '.strip()))

    elif choice == "19":
        print("🧠 الأمر:")
        print(">>> 'On an island'.strip('d')")
        print("\n📝 الشرح: إزالة الحرف 'd' من أطراف النص فقط (إذا موجود).")
        print("\n✅ النتيجة:")
        print("قبل:", repr('On an island'))
        print("بعد :", repr('On an island'.strip('d')))

    elif choice == "20":
        print("🧠 الأمر:")
        print(">>> 'but life is good!'.split()")
        print("\n📝 الشرح: تقسيم النص لكلمات حسب الفراغ.")
        print("\n✅ النتيجة:")
        print('but life is good!'.split())

    elif choice == "21":
        print("🧠 الأمر:")
        print(">>> 'Help me'.replace('me','you')")
        print("\n📝 الشرح: استبدال جزء من النص.")
        print("\n✅ النتيجة:")
        print("قبل:", 'Help me')
        print("بعد :", 'Help me'.replace('me', 'you'))

    elif choice == "22":
        print("🧠 الأمر:")
        print(">>> 'Need to make fire'.startswith('Need')")
        print("\n📝 الشرح: هل النص يبدأ بكلمة Need؟")
        print("\n✅ النتيجة:")
        print('Need to make fire'.startswith('Need'))

    elif choice == "23":
        print("🧠 الأمر:")
        print(">>> 'and cook rice'.endswith('rice')")
        print("\n📝 الشرح: هل النص ينتهي بـ rice؟")
        print("\n✅ النتيجة:")
        print('and cook rice'.endswith('rice'))

    elif choice == "24":
        print("🧠 الأمر:")
        print(">>> 'bye bye'.index('e')")
        print("\n📝 الشرح: يرجع أول موقع للحرف e (إذا مش موجود يعطي خطأ).")
        print("\n✅ النتيجة:")
        print('bye bye'.index('e'))

    elif choice == "25":
        print("🧠 الأمر:")
        print(">>> 'still there?'.upper()")
        print("\n📝 الشرح: تحويل النص لأحرف كبيرة.")
        print("\n✅ النتيجة:")
        print('still there?'.upper())

    elif choice == "26":
        print("🧠 الأمر:")
        print(">>> 'HELLO?!'.lower()")
        print("\n📝 الشرح: تحويل النص لأحرف صغيرة.")
        print("\n✅ النتيجة:")
        print('HELLO?!'.lower())

    elif choice == "27":
        print("🧠 الأمر:")
        print(">>> 'ok, I am done.'.capitalize()")
        print("\n📝 الشرح: أول حرف كبير والباقي صغير.")
        print("\n✅ النتيجة:")
        print('ok, I am done.'.capitalize())

    elif choice == "28":
        print("🧠 الأمر:")
        print(">>> 'oh hi there'.find('i')")
        print("\n📝 الشرح: يرجع موقع أول ظهور لـ i، وإذا مش موجود يرجع -1.")
        print("\n✅ النتيجة:")
        print('oh hi there'.find('i'))

    elif choice == "29":
        print("🧠 الأمر:")
        print(">>> 'oh hi there'.count('e')")
        print("\n📝 الشرح: عدّ كم مرة ظهر الحرف e.")
        print("\n✅ النتيجة:")
        print('oh hi there'.count('e'))

    # ---------- Formatting ----------
    elif choice == "30":
        print("🧠 الأمر:")
        print(">>> f'Hello {name1} {name2}'")
        print("\n📝 الشرح: تنسيق حديث (f-string).")
        print("\n✅ النتيجة:")
        print(f'Hello {name1} {name2}')

    elif choice == "31":
        print("🧠 الأمر:")
        print(">>> 'Hello {} {}'.format(name1, name2)")
        print("\n📝 الشرح: تنسيق باستخدام format().")
        print("\n✅ النتيجة:")
        print('Hello {} {}'.format(name1, name2))

    elif choice == "32":
        print("🧠 الأمر:")
        print(">>> 'Hello %s %s' % (name1, name2)")
        print("\n📝 الشرح: تنسيق قديم باستخدام %.")
        print("\n✅ النتيجة:")
        print('Hello %s %s' % (name1, name2))

    # ---------- Palindrome ----------
    elif choice == "33":
        word = "reviver"
        print("🧠 الأمر:")
        print(">>> word == word[::-1]")
        print("\n📝 الشرح: هل الكلمة تقرأ نفسها بالعكس؟")
        print("\n✅ النتيجة:")
        print("الكلمة:", word)
        print("عكسها :", word[::-1])
        print("Palindrome؟", word == word[::-1])

    elif choice == "0":
        print("انتهى الشرح 👋")
        break

    else:
        print("❌ اختيار غير صحيح")

    print("=" * 45)
    input("\nاضغط Enter للمتابعة...")

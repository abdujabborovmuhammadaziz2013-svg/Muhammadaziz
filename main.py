# a=int(input("Yoshingizni kiriting: "))
# if a<7:
#     print("Siz bog'chaga borasiz")
# elif a>=7 and a<=18:
#     print("Siz maktabda o'qiysiz")
# elif a>=19 and a<=40:
#     print("Siz ishlaysiz")
# elif a>40:
#     print("Siz nafaqadasiz")

# s=input()
# print(len(s))
# print(s.upper())
# print(s.lower())

# x=int(input())
# y=float(input())
# print(x+y)
# print(x*y)
# print(x/y)
# print(x**2)
# print(math.sqrt(x))
# print(math.sqrt(y))

# d={"apple":2,"banana":5,"orange":3}
# print(d)
# print(d.keys())
# print(d.values())
# print(d["apple"])

# s={1,2,3,4,5}
# s.add(6)        
# s.remove(3)
# print(s)
# print(len(s))

# a=0
# for i in range(10):
#     print(i)

# qadam = 0
# while qadam < 10:
#     print(qadam) 
#     qadam +=1
# else:
#     print(qadam, "Loop tugadi")

# ishora = True
# while ishora:
#     son = input("Son kiriting: ")
#     if son == 'stop':
#         ishora = False
#         print("Loop tugadi")
#     else:
#         son=int(son)
#         print(son**2)

# k=["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]
# n=int(input())
# print(k[(n-1)%7])

# k=["Shahriyor","Shohjahon","Diyorbek","Shukurullo","Husanboy","Muhammadaziz","Fayozbek"]
# n=int(input())
# print(k[(n-1)%7])

# m=int(input())
# i=int(input())
# f=int(input())

# if not(0<=m<=100 and 0<=i<=100 and 0<=f<=100):
#     print("Xato ball")
# elif m>85 and i>85 and f>85:
#     print("Mukofot oladi")
# elif m>60 and i>60 and f>60:
#     print("O'quvchi kursni muvaffaqiyatli tugatdi")
# elif m<50 or i<50 or f<50:
#     print("Qayta topshirish kerak")

# matem = int(input("Matematika fani bahosi (0-100): "))
# english = int(input("Ingliz fani bahosi (0-100): "))
# info = int(input("Informatika fani bahosi (0-100): "))

# if 0 < matem <= 100 and 0 < english <= 100 and 0 < info <= 100:
#     average = (matem + english + info) / 3
#     average = round(average)

#     if average > 60 and average < 85:
#         print(f"O'quvchi kursni muvaffaqiyatli tugatdi {average} ball")
#     elif average < 50:
#         print(f"Qayta topshirish kerak {average} ball")
#     else:
#         print(f"Mukofot oladi {average} ball")
# else:
#     print("Siz noto'g'ri baho kiritdingiz")

# a=5
# b=7
# print(a+b)

# a=4
# b=6
# c=8
# print((a+b+c)/3)

# birth_year=int(input())
# current_year=int(input())
# print(current_year-birth_year)

# meva=input()
# match meva:
#     case "olma":
#         print(5000)
#     case "banan":
#         print(7000)
#     case "apelsin":
#         print(6000)
#     case "nok":
#         print(8000)
#     case _:
#         print("Bu meva mavjud emas")

# valyuta=input()
# match valyuta:
#     case "usd":
#         print(11500)
#     case "eur":
#         print(12500)
#     case "rub":
#         print(150)
#     case "jpy":
#         print(85)
#     case _:
#         print("Bunday valyuta mavjud emas")

# rang=input()
# match rang:
#     case "qizil":
#         print("To'xtang")
#     case "sariq":
#         print("Ehtiyot bo'ling")
#     case "yashil":
#         print("Harakatlaning")
#     case _:
#         print("Noma'lum rang")

# l=["Xayrullo","Difuza","Shaxrizoda","Muhammadaziz","Parizoda"]
# k=0
# if k==0:
#     print("Xayrullo")
# if k==1:
#     print("Dilfuza")
# if k==2:
#     print("Shaxrizoda")
# if k==3:
#     print("Muhammadaziz")
# if k==4:
#     print("Parizoda")
# else:
#     print("Oila a'zolar soni bundan kam!!!")

# names = []

# n = int(input("Nechta oila a'zosi bor: "))

# for i in range(n):
#     name = input(f"{i+1}-ismni kiriting: ")
#     names.append(name)

# for name in names:
#     print(name)

# words = input("Vergul bilan ajratib so'zlar kiriting: ").split(",")

# words.reverse()

# for word in words:
#     print(word.strip(), end=", ")

# words = input("Vergul bilan ajratib so'zlar kiriting: ").split(",")

# words = [w.strip() for w in words]
# words.sort()

# for word in words:
#     print(word, end=", ")

# words=input("Vergul bilan ajratib so'zlar kiriting: ").split(",")
# target=input("Qaysi so'zni qidiryapsiz: ")
# words=[w.strip() for w in words]
# if target in words:
#     print(words.index(target))
# else:
#     print("Topilmadi")

# words=input("Vergul bilan ajratib so'zlar kiriting: ").split(",")
# target=input("Qaysi so'zni sanamoqchisiz: ")
# words=[w.strip() for w in words]
# count=words.count(target)
# print(count)

# a=input("Ismingizni kiriting: ")
# print("Salom, " + a)

# yil = 2020
# yosh = 18
# kun = 7
# oy = 12
# talaba_soni = 30

# print(yil, yosh, kun, oy, talaba_soni)

# harorat=36.6
# boy=1.75 
# vazn=65.5 
# foiz=12.5 

# print("Harorat: "harorat,
#       "Boy: "boy,
#       "Vazn: "vazn,
#       "Foiz: "foiz)

# a=int(input("1-son: "))
# b=int(input("2-son: "))



# while b!=0:
#     a,b=b,a%b

# print("EKUB:", a)

# son=float(input("Son kiriting: "))
# print(f"{son:.1e}")

# ota={'ismi':'Mavlutdin','yil':1954,'shahar':'Namangan'}
# ona={'ismi':'Gulchehra','yil':1960,'shahar':'Farg\'ona'}
# aka={'ismi':'Farhod','yil':1985,'shahar':'Toshkent'}
# family={'ota':ota,'ona':ona,'aka':aka}
# o=family['ota']
# print(f"Otamning ismi {o['ismi']}, {o['yil']}-yilda, {o['shahar']} viloyatida tug'ilgan")

# taomlar={'Ali':'osh','Vali':'shashlik','Olim':'somsa','Nodira':'manti','Zuhra':'lag\'mon'}
# print(f"Alining sevimli taomi {taomlar['Ali']}")
# print(f"Valining sevimli taomi {taomlar['Vali']}")
# print(f"Olimning sevimli taomi {taomlar['Olim']}")

# kalit=input("Kalit so'z kiriting:").lower()
# tarjima=python_words.get(kalit)
# if tarjima==None:
#     print("Bunda so'z mavjud emas")
# else:
#     print(tarjima)

# while True:
#     a = int(input("birinchi son: "))
#     b = int(input("ikkinchi son: "))
#     c = input('Operator (+ - * /): ')
#     if c == "+":
#         print(f"{a} + {b} = {a+b}")
#     elif c == "-":
#         print(f"{a} - {b} = {a-b}")
#     elif c == "*":
#         print(f"{a} * {b} = {a*b}")
#     elif c == "/":
#         print(f"{a} / {b} = {a/b}")

# fayllar bilan ishlash
# o'qish - r
# yozish - w
# qo'shib yozish -a
# sonlar = []
# file = open('sonlar,txt', 'r')
# print(file.read())
# print(file.readline())
# print(file.readlines())

# for i in file.readlines():
#     sonlar.append(int(i))
#     file.close()

#     print(sonlar)


# file = open('hujjatlar/ismlar.txt', 'w')
# file.write('Ikromjon')
# file.close()

# file = open('hujjatlar/ismlar.txt', 'a')
# file.write('\nIkromjon')
# file.close()

# a = open('dars4,py', 'w')
# a.write('print("salom dunyo!")')
# a.close()

# with open('hujjatlar/sonlar.txt', 'w') as file:
#     n = int(input('Nechta son kiritasiz?'))
#     for i in range(n):
#         son=input(f'{i+1}-sonni kiriting: ')
#         file.write(f"{son}\n")

# programming = {'Alice','Bob','Karimjon','Salimjon','Alijon','Bob'}
# maths = {'Alice','Salimjon','Hoshimjon','Ilyos','Feya','Guli','Dilshoda','Bob'}
# numbers = {1,2,3,4,5,6,1,1,1,1,1,1,1}
# print(programming, type(programming), len(programming))
# print(numbers , type(numbers), len(numbers))

# programming.add('Doniyor')
# print(programming)
# programming.pop()
# print(maths)
# maths.remove('Guli')
# print(maths)

# print(programming - maths) print(programming.difference(maths))
# print(maths - programming) print(maths.difference(programming))
# print(programming & maths) print(programming.intersection(maths))
# print(programming | maths) print(programming.union(maths))

son1,son2 = 1110, 1110
# > kattami
# < kichikmi
# == tengmi

# != teng emasmi
# >= kattami yoki tengmi
# <=kichikmi yoki tengmi

# in - ichida mavjudmi

# print(1 >= 1)

# print('mu' in 'Mustafo')

# and, or, not

# print(1 > 0 and 2 < 5)
# print(not 1 < 0 or 2 > 5)

# if son1 > son2:
#     print(f'son1 - Katta {son1} > {son2}')

# elif son2 == son1:
      # print(f'Ikki son ham teng {son1} = {son2}')

# else:
      # print(f'son2 - katta {son1} < {son2}')

# s=input()
# n=s.split(',')
# u=set(n)
# print(len(u))

# s=input().split()
# a=sorted(s[0])
# b=sorted(s[1])
# print(a==b)

# a = [1,2,3,4,5]
# b = int(input('B: '))
# c = int(input('C: '))

# try:
#     print(b/c)
#     print(a[1])
#     print(5 + 'ikki')
# except ZeroDivisionError:
      # print(`Nolga bo'lish mumkin emas`)

# except IndexError:
      # print('bu indexda data yoq')

# except (IndexError, ZeroDivisionError, TypeError) as e:
      # print(e)

# except BaseException:
      # print()

# mevalar = ["olma", "banan"]
# print(mevalar[5])


# lugat = {"ism": "Ali"}
# print(lugat["yosh"])


# son = 10
# matn = "5"
# print(son + matn)


# try:
#     mevalar = ["olma", "banan"]
#     print(mevalar[5])
# except IndexError as e:
#     print(f"Xatolik yuz berdi: {e}")

# try:
#     lugat = {"ism": "Ali"}
#     print(lugat["yosh"])
# except KeyError as e:
#     print(f"Xatolik yuz berdi: Kalit topilmadi - {e}")


# try:
#     print(10 + "5")
# except TypeError as e:
#     print(f"Xatolik yuz berdi: {e}")

# pupils = ('Ilyos','Asilbek','Mohinur','Nilufar', 'Kamronbek', "Alijon")
# xabar1 = f"Xurmatli {pupils[0]}, siz bilan bugun loop mavzusini boshladik"
# xabar2 = f"Xurmatli {pupils[1]}, siz bilan bugun loop mavzusini boshladik"
# xabar3 = f"Xurmatli {pupils[2]}, siz bilan bugun loop mavzusini boshladik"
# xabar4 = f"Xurmatli {pupils[3]}, siz bilan bugun loop mavzusini boshladik"
# print(xabar1)
# print(xabar2)
# print(xabar3)
# print(xabar4)

# for pupil in pupils:
#     print(f"Xurmatli {pupil}, siz bilan bugun loop mavzusini boshladik")
#     print('deb: Ikromjon')

# sonlar = [1,8,9,4,5,6]
# for son in sonlar:
#     text = f"{son} ^ 2 = {son*son}"
#     print(text)
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
# numbers = list(range(1, 11, 2))
# numbers = list(range(7,100,7))
# print(numbers)

# for i in range(1,10):
#     text = f"{i} ^ 2 = {i*i}"
#     print(text)

# n = int(input('Nechchi karra kerak: '))

# for i in range(1,11):
#     karra = f"{n} x {i} = {n*i}"
#     print(karra)

# a=int(input())
# if a%2==1:
#     print("Toq son")
# if a%2==0:
#     print("Juft son")

# a=int(input())
# if a%3==0 and a%5==0:
#     print("FizBiz")
# elif a%3==0:
#     print("Fiz")
# elif a%5==0:
#     print("Biz")
# else:
#     print(a)

# baho = int(input("Bahoyingiz: "))
# if baho == 5:
#     print("A'lo")
# elif baho == 4:
#     print("Yaxshi")
# elif baho == 3:
#     print("Qoniqarli")
# elif baho == 2 or baho == 1:
#     print("Qoniqarsiz")
# else:
#     print("Bunday baho mavjud emas")

# match baho:
#     case 5:
#         print("A'lo")
#     case 4:
#         print("Yaxshi")
#     case 3:
#         print("Qoniqarli")
#     case 2 | 1:
#         print("Qoniqarsiz")

# human = "Ikromjon","Abdurahmon","Anvarjon","Azimjon"
# match human:
#       case "Ikromjon":
#         print("Backend dastrulash ustozi")
#       case "Abdurahmon":
#         print("Computer science ustozi")
#       case "Anvarjon":
#         print("Frontend dasturlash ustozi")
#       case "Azimjon":
#         print("Grafik dizayn ustozi")
#       case _:
#         print("Biz bu insonni tanimaymiz")

# for i in "Python":
#     print(i*50)

# for i in range(1, 100, 2):
#     a = f"{"*" * i}".center(101)
#     print(a)

# print("| |".center(101))

# qadam = 1

# while qadam <5:
#       print(f"{qadam}=qadam")
#       qadam +=1

# print("Loop yakunlandi")

# flag = True
# while flag:
#       son = input("son kriting (stop): ")
#       if son == "stop":
#             flag= False
#             print("Loop yakunlandi")
#       else:
#             son = int(son)
#             print(f"{son}^2={son**2}")

# matematika=int(input("Matematika fanidan ballni kiritiring:"))
# ingliz_tili=int(input("Ingliz tili fanidan ballni kiritiring:"))
# informatika=int(input("Informatika fanidan ballni kiritiring:"))
# if 0<=matematika<=100 and 0<=ingliz_tili<=100 and 0<=informatika<=100:
#     if matematika>85 and ingliz_tili>85 and informatika>85:
#         print("Mukofot oladi")
#     elif matematika>60 and ingliz_tili>60 and informatika>60:
#         print("O'quvchi kursni muvaffaqiyatli tugatdi")
#     elif matematika<50 or ingliz_tili<50 or informatika<50:
#         print("Qayta topshirish kerak")
# else:
#     print("Xato: Ballar 0 va 100 oralig'ida bo'lishi kerak!")

# meva = input("Meva nomini kiriting: ").lower()
# match meva:
#     case "olma":
#         print("Narxi: 12 000 so'm")
#     case "banan":
#         print("Narxi: 20 000 so'm")
#     case "apelsin":
#         print("Narxi: 25 000 so'm")
#     case "nok":
#         print("Narxi: 18 000 so'm")
#     case _:
#         print("Bu meva mavjud emas")

# valyuta = input("Valyuta kodini kiriting (usd, eur, rub, jpy): ").lower()
# match valyuta:
#     case "usd":
#         print("1 USD = 12 800 so'm")
#     case "eur":
#         print("1 EUR = 13 500 so'm")
#     case "rub":
#         print("1 RUB = 140 so'm")
#     case "jpy":
#         print("1 JPY = 85 so'm")
#     case _:
#         print("Bunday valyuta mavjud emas")

# rang = input("Svetofor rangini kiriting: ").lower()
# match rang:
#     case "qizil":
#         print("To'xtang! Harakatlanish taqiqlanadi.")
#     case "sariq":
#         print("Tayyorlaning!")
#     case "yashil":
#         print("Harakatlaning!")
#     case _:
#         print("Noma'lum rang yoki svetofor ishlamayapti.")

# o'yin
# kompyuter bir son tanlaydi 1-10 gacha, foydalanuvchi shu sonni topishi zarur
# 9 - 5
# men tanlagan son kattaroq
# 9 - 10
# men tanlagan son kichikroq
# 9 - 9
# Ofarin topdingiz

# comp_num = random.randint(1, 10)
# print(f'Men bir son tanladim, 1-10, shu sonni topoliysizmi? ')

# while True:
#     user_num = int(input('Taxminingiz: '))
    
#     if comp_num > user_num:
#         print('Men tanlagan son kattaroq')
#     elif comp_num < user_num:
#         print('Men tanlagan son kichikroq')
#     else:
#         print('Ofarin topdingiz! ')
#         break

# def salomlash():
#     print('Assalomu aleykum!')

# def salomlash2(ism):
#     print(f'Assalomu aleykum {ism} aka!')

# def add(a,b,c):
#     qiymat=a+b+c
#     return qiymat

# def summ(*sonlar):
#     yigindi=0
#     for i in sonlar:
#         yigindi+=i
#     return yigindi


# def salomlash():
#     print('Assalomu aleykum')

# # salomlash()

# def salomlash2(name):
#     print(f'Assalomu aleykum {name} aka!')

# salomlash2('Alijon')
# salomlash2('Valijon')
# salomlash2('Bakzod')
# salomlash2('Salahiddin')
# salomlash2('Muhammadaziz')

# def juft_toq(son):
#     if son % 2 == 0:
#         return f'{son} - Juft son'
#     else:
#         return f'{son} - Toq son'

# son = int(input('Son: '))
# print(juft_toq(son))
# print(len('salom'))


# eni = int(input("Xona eni: "))
# boyi = int(input("Xona boyi: "))
# print(primetr(eni, boyi))

# def miin(a, b, c):
#     if a > b and b < c:
#         return b
#     elif a > c and c < b:
#         return c
#     else:
#         return a

# def minu(*a):
#     if len(a) > 1:
#         engkichik = a[0]
#         for i in a:
#             if i < engkichik:
#                 engkichik = i
#         return engkichik
#     else:
#         return '2 va undan ortiq son kiriting'

# print(a)
# print(type(a))
# print(len(a))

# print(min(1500, 4))
# print(miin(1500, 1550))
# print(minu(1500, 47, 6))

# def salomlash():
#     print('Assalomu aleykum')

# salomlash()

# def salomlash2(name):
#     print(f'Assalomu aleykum {name} aka!')

# salomlash2('Alijon')
# salomlash2('Valijon')
# salomlash2('Bakzod')
# salomlash2('Salahiddin')
# salomlash2('Muhammadaziz')

# def juft_toq(son):
#     if son % 2 == 0:
#         return f'{son} - Juft son'
#     else:
#         return f'{son} - Toq son'

# son = int(input('Son: '))
# print(juft_toq(son))
# print(len('salom'))

# def primetr(eni, boyi):
#     pri = (eni + boyi) * 2
#     return pri

# eni = int(input("Xona eni: "))
# boyi = int(input("Xona boyi: "))
# print(primetr(eni, boyi))

# def miin(a, b, c):
#     if a > b and b < c:
#         return b
#     elif a > c and c < b:
#         return c
#     else:
#         return a

# def minu(*a):
#     if len(a) > 1:
#         engkichik = a[0]
#         for i in a:
#             if i < engkichik:
#                 engkichik = i
#         return engkichik
#     else:
#         return '2 va undan ortiq son kiriting'

# print(a)
# print(type(a))
# print(len(a))

# print(min(1500, 4))
# print(miin(1500, 1550))
# print(minu(1500, 47, 6))

# friends = ['Bob','Alijon','Hakimjon','Alice','Ikromjon','Doniyor',"Jo'rabek"]
# a_xarf=list(filter(lambda ism: ism.startwith('I'),friends))
# length6=list(filter(lambda ism: len(ism)<6, friends))
# print(a_xarf)
# print(length6)
# kichik_harf=[]
# for i in friends:
#     kichik_xarf.append(i.lower())

# print(friends)
# print(kichik_xarf)
# kichik=list(map(lambda ism: ism.lower(), friends))
# kichik_tuple=list(map(tuple, friends))
# print(kichik)
# print(kichik_tuple)

# sonlar_map=list(map(int,input('Sonlar kiriting: ').split()))
# print(sonlar_map)
# print(type(sonlar_map))
# print(len(sonlar_map))
# print(max(sonlar_map))

# print(list(map(lambda x: x**2, sonlar_map)))

# name=input("What is your name?: ")
# print(f"Hello, {name}!")
# surname=input("What is your surname?: ")
# full_name=f"{name} {surname}"
# gender - ''
# if surname[-1] == "a"
#       gender = 'female'
# else:
#       gender = 'male'
# print(gender)

# gender = 'female' if surname[-1] == 'a' else 'male'
# if gender == 'male'
#       pass
# else:
#       print(f'Hello, {full_name} sister!')
# age = input("What is your age?: ")
# by = 2026 - int(age)
# print(f'Your birth year is {by}')
# print(f"Hello, {full_name} brother!")
# auto_number = "50Z777ZZ"


# programmers = ['Bob', 'Ali', 'Behruz', 'Mustafo', 'Guli', 'Salim', 'Alice', 'Hero']
# print(f'Janob {programmers[0]} python dasturlash tilini o\'rganmoqda')
# print(f'Janob {programmers[1]} python dasturlash tilini o\'rganmoqda')
# print(f'Janob {programmers[2]} python dasturlash tilini o\'rganmoqda')
# print(f'Janob {programmers[3]} python dasturlash tilini o\'rganmoqda')
# print(f'Janob {programmers[4]} python dasturlash tilini o\'rganmoqda')
# print(f'Janob {programmers[5]} python dasturlash tilini o\'rganmoqda')

# for dasturchi in programmers:
#     print(f'Janob {dasturchi} python dasturlash tilini o\'rganmoqda')

# numbers = (5,9,7,4,6,3,2,1,59)
# for i in numbers:
#     natija = f"{i} ^ 3 = {i**3}"
#     print(natija)
# print('Hisobladi Alijon')

# uch_xonali = list(range(100, 1000, 100))
# print(uch_xonali)
# print(len(uch_xonali))

# ikki_xona = tuple(range(14, 100, 7))
# ikki_xona = tuple(range(2, 100, 2))
# print(ikki_xona)

# n = int(input("Nechta do'stingiz bor: "))
# friends = []
# for i in range(n):
#     a = input(f"{i+1} - do'stingiz: ")
#     friends.append(a)

# print(f"sizning eng yaqin {len(friends)} ta do'stingiz {friends}")

# import telebot

# API_TOKEN = '8492048481:AAHXbnpWdNcK7oCuxjtLJ2hRavnmR0YpScs'
# bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     full_name = message.from_user.first_name
#     username = message.from_user.username
#     print(message)
#     bot.reply_to(message, f"""Salom {full_name}, bizning botimizga hush kelibsiz (@{username})""")

# @bot.message_handler(commands=['help'])
# def help_funk(xabar):
#     bot.reply_to(xabar, '''Bu yordam menyusi, botdan foydalanish yo'riqnomasi''')

# Handle all other messages with content_type 'text'
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     try:
#         data = message.text
#         calc = eval(data)
#         bot.reply_to(message, f"{data}={calc}")
#     except:
#         bot.reply_to(message, 'Normalniy misol jonating ')

# bot.infinity_polling()


# def user(ism, fam, age, address, **data):
#     info = f"Foydalanuvchi ismi: {ism}\n"
#     info += f"Foydalanuvchi familiyasi: {fam}\n"
#     info += f"Foydalanuvchi yoshi: {age}\n"
#     info += f"Foydalanuvchi manzili: {address}\n"
#     return info, data

# user1 = user('Alijon', 'Valiyev', 15, 'Namangan / Uchqorgon')
# user2 = user(age = 19, ism='Karimjon', address='Andijon / Izboskan', fam='Keldiboyev',
#              subject=['math', 'english'], parents='Hoshimjon, Halimaxon', phone = 998995641234)

# print(user1)
# print(user2)

# def my_lang(full_name, lang='English'):
#     '''bu funksiya foydalanuvchini qaysi tilni o'rganayotganini ko'rsatadi'''
#     info = f"{full_name} is learning {lang} language"
#     return info

# print(my_lang('Alijon', 'Russian'))
# print(my_lang('Valijon'))
# print(my_lang.__doc__)
# print(max.__doc__)
# print(max(5,9))

# def kv(son):
#     return son**2

# kv2 = lambda son: son**2
# juftmi = lambda number: True if number % 2 == 0 else False
# v = lambda leng, weight, height: leng * weight * height

# # print(v(6,4,2.5))
# # print(juftmi(10))
# # print(kv(8))
# # print(kv2(8))

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))

# num = 10
# print("The factorial of", num, "is", factorial(num))

#o'zgaruvchilar, comment va errors
# import keyword
# # ma'lumot turlari
# matnli ma'lumotlar turi = string(str)
# butun sonlar = integer(int)
# o'nli kasr sonlar = float
# mantiq amali = bool(True, False)

# ism = 'Alijon'
# print("Salom, ", ism)
# name = 'Valijon'
# print("salom,", name)
# age = 18
# print("Salom", name, "uning yoshi", age)
# name2 = "Hakimjon"
# _full_name = "Alijon Hakimov"
# class_ = "5A"
# print(keyword.kwlist)

# print = 'Salom dunyo'
# print(print)

# print(ism)

# son1 = 15
# son2 = 20
# yig = son1 + son2
# print(yig)

# eni,boyi = 8,12
# S = eni * boyi
# P = (eni+boyi)*2
# print("Yuzi: ", S)
# print("Perimetri: ", P)

# Pythonda string va uning metodlari

# index 0123456789
# name = "Aijon"
# full_name = "O'ktamov Alijon"
# about='''
# O'zbekiston poytaxti
# "Toshkent" shahri'''

# number = "15"
# number2 = '''2'''
# print(int(number)+ int(number2))
# print(number, type(number))
# print(name, type( name), len(name))
# print(full_name, type(full_name), len(full_name))
# print(about, type(about), len(about))

# a = 5
# b = 6
# print(a+b)

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[100])

# print(full_name[-2]+full_name[-1])
# print(name[0]+name[2])
# print(name[0:3])
# print(name[:3])
# print(name[3:])

# print(full_name)
# print(full_name[::-1])

# name = input('Ismingiz nima? ')
# print(name, type(name), len(name))
# print("Assalomu aleykum " + name + 'aka')
# print("Assalomu aleykum {name.capitalize()} aka")
# print("Assalomu aleykum {name.title()}aka")
# print("Assalomu aleykum {name.lower()} aka")
# print("Assalomu aleykum {name.upper()} aka" )


# import telebot
# import wikipedia

# API_TOKEN ='8382228104:AAHi0p15r9oal6NLPD7IJRzWHml8OPLaFLY'

# wikipedia.set_lang("uz")
# bot = telebot.TeleBot(API_TOKEN)


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     user_id = str(message.from_user.id)
    
    
#     with open('users.txt', 'r') as file:
#         users = file.read().splitlines())
#     with open('users.txt', 'a') as f:
#         if user_id not in users:
#             f.write(f'{user_id}\n')
            
#     full_name = message.from_user.first_name
#     bot.reply_to(message, text=f"""Salom {full_name}, bizning botga xush kelibsiz!""")

# @bot.message_handler(commands=['help'])
# def send_help(message):
#     bot.reply_to(message, text="""Yordam berolmaymiz!""")

# @bot.message_handler(commands=['ads'])
# def send_ads(message):
#     with open('users.txt', 'r') as file:
#         users = file.read().splitlines()
#         users_ids = list(map(int, users))
        
#         for user_id in users_ids:
#             try:
#                 bot.send_message(user_id, text='Salom bu botdan sizga xabarnoma')
#             except:
#                 continue
                
#     bot.reply_to(message, text=f'Xabarnoma {len(users_ids)} ta userga yuborildi')


# @bot.message_handler(commands=['users'])
# def count_users(message):
#     with open('users.txt', 'r') as file:
#         users = file.read().splitlines()
        
#     bot.reply_to(message, text=f"Sizning botingiz foydalanuvchilari soni {len(users)} ga yetdi")


# @bot.message_handler()
# def wiki(message):
#     try:
#         text = message.text
#         wiki_natija = wikipedia.summary(text)
#         bot.reply_to(message, wiki_natija)
#     except:
#         bot.reply_to(message, text="Ma'lumot topilmadi!")

# bot.infinity_polling()

# # 1. BMI (Tana Massa Indeksi)
# vazn = 55         # kg
# bo_y = 1.65       # metr
# bmi = vazn / (bo_y ** 2)
# print(f"BMI: {bmi:.2f}")   # BMI: 22.9
# print(f"BMI: {round(bmi, 2)}")   # BMI: 22.9


# # # 2. Kredit hisoblash
# kredit = 10_000_000  # 10 mln so'm (Python'da _ ishlating)
# foiz = 0.18          # 18% yillik
# muddat = 24          # oy
# oylik_foiz = foiz / 12
# oylik_tolov = kredit * (oylik_foiz * (1 + oylik_foiz)**muddat) / ((1 + oylik_foiz)**muddat - 1)

# print(f"Oylik to'lov: {oylik_tolov:,.0f} so'm")


# # # 3. Pifagor teoremasi
# a = 3
# b = 4
# import math
# c = math.sqrt(a**2 + b**2)
# print(f"Gipotenuza: {c}")  # 5.0


# a = float(input("Birinchi son: "))
# b = float(input("Ikkinchi son: "))

# print(f"\n{a} + {b} = {a + b}")
# print(f"{a} - {b} = {a - b}")
# print(f"{a} * {b} = {a * b}")
# # i...
# print(f"{a} / {b} = {a / b:.4f}")
# print(f"{a} // {b} = {a // b}")
# print(f"{a} % {b} = {a % b}")
# print(f"{a} ** 2 = {a ** 2}")


# misol = '(5+9)*2**3'
# print(eval(misol))

#1)
# a=5
# print(5**4)

# 2)
# print(22 % 4)

# 3)
# yuzi:
# print(125**2)
#perimetri:
# print(125*4)

# 4)
#d=2R
#S=2ПRR
#П=3.14
# d=12
# R=6
# П=3.14
# R**2==36
# print((2*П)*(R**2))

# 5)
# print((6*7):2)

# 6)
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# friends = ['ali', 'valijon', 'salimjon','karimjon', 'bob', 'alice', 'xasanboy','xusanboy']

# katta_xarf = []
# for dost in friends:
#     katta_xarf.append(dost.title())

# print(katta_xarf)

# for i in friends:
#     print(f"Do'stim {i.title()}, Seni Qurbon Hayit bayrami bilan tabriklayman!")

# numbers = [45,68,9,41,4,2,4,7,6,1,5,4]
# juft = []
# toq = []

# for i in numbers:
#     if i % 2 == 0:
#         juft.append(i)
#     else:
#         toq.append(i)

# print("Toq sonlar:", toq)
# print("Juft sonlar:", juft)

# for i in numbers:
#     print(f"{i} ** 2 = {i**2}")

# for i in range(10):
#     print(i * "*")


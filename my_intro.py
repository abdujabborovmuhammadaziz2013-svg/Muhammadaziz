print("Salom! Men Python o'rganmoqdaman!")
print("Mening ismim: Muhammadaziz")
print("Men dasturlashni o'rganmoqchiman, chunki bu juda qiziqarli")
print("Mening birinchi loyiham:", )

print("=== Mening Kalkulyatorim ===")
a = 25
b = 7
print("a =", a)
print("b =", b)
print("Yig'indi:    a + b =", a + b)
print("Ayirma:     a - b =", a - b)
print("Ko'paytma:  a * b =", a * b)
print("Bo'linma:   a / b =", a / b)
print("Qoldiq:     a % b =", a % b)
print("Daraja:     a ** 2 =", a ** 2)

ism = input("Ismingizni kiriting: ")

print("Asl:", ism)
print("Katta harf:", ism.upper())
print("Kichik harf:", ism.lower())
print("Uzunlik:", len(ism))
print("Birinchi harf:", ism[0])
print("Oxirgi harf:", ism[-1])
print(f"Salom, {ism.title()}!")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
    print(f"{a} > {b}")
elif a == b:
    print(f"{a} == {b}")
else:
    print(f"{a} < {b}")
birthday = int(input("Tug'ilgan yilingiz (2000): "))
hy = 2026
age = hy - birthday
if 7 <= age < 18:
    print('Maktabga boradi!')
    if age == 7:
        print('1-sinf')
    elif age == 8:
        print('2-sinf')
elif 18 < age <= 25:
    print("Unversitetga boradi")
elif 25 <= age < 60:
    print("ishga boradi")
elif 60 <= age:
    print("Nafaqadalar")
else:
    print('Bog\'chaga boradi!')
age = input('Yoshingiz: ')
if age.isdigit():
    age = int(age)
    if 7 <= age < 18:
        print('Maktabga boradi!')
        if age == 7:
            print('1-sinf')
        elif age == 8:
            print('2-sinf')
    elif 18 < age <= 25:
        print("Unversitetga boradi")
    elif 25 <= age < 60:
        print("ishga boradi")
    elif 60 <= age:
        print("Nafaqadalar")
    else:
        print('Bog\'chaga boradi!')
else:
    print('Faqat son kiriting!')

    age = input('Yoshiniz: ')
if age.isdigit():
    age = int(age)
    if 7 <= age < 18:
        print('Maktabga boradi!')
        sinf = age - 6
        print(f'{sinf} - sinf')
    elif 18 <= age <= 25:
        print("Unversitetga boradi")
    elif 25 <= age < 60:
        print("ishga boradi")
    elif 60 <= age:
        print("Nafaqadalar")
    else:
        print('Bog\'chaga boradi!')
else:
    print('Faqat son kiriting!')
teacher = input("Enter your name: ").capitalize()
match teacher:
    case 'Ikromjon':
        print('Python Backend')
    case 'Abdurahmon':
        print('CS')
    case _:
        print('Notanish Teacher')
if teacher == 'Ikromjon':
    print('Python Backend')
elif teacher == 'Abdurahmon':
    print('CS')
else:
    print('Notanish Teacher')
age = int(input("Your age: "))
if age <= 7 or age >= 60:
    print('Siz uchun kirish bepul')
elif age <= 16:
    print("Siz uchun kirish 5 000 so'm")
elif 16 < age < 60:
    print("Siz uchun kirish 10 000 so'm")
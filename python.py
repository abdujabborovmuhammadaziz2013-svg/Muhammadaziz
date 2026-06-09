# # # # a = 12
# # # # print(a, type(a))
# # # from typing import reveal_type


# # # class Pupil:
# # #     def __init__(self, ism, fam, sinf, phone):
# # #         self.first_name = ism
# # #         self.last_name = fam
# # #         self.clas = sinf
# # #         self.phone = phone
# # #         self.fan = []

# # #     def get_info(self):
# # #         text = (f"O'quvchi ismi {self.first_name}\nFamiliyasi {self.last_name}\n"
# # #                 f"sinfi {self.clas}")
# # #         return text

# # #     def phone_update(self, new_phone):
# # #         self.phone = new_phone
# # #         print( f"{self.first_name} telefon raqami yangilandi, yangi raqam: {self.phone}")

# # #     def add_subject(self, subject):
# # #         self.fan.append(subject)

# # #     def class_up(self):
# # #         sinf = self.clas[:-1]
# # #         harf = self.clas[-1]
# # #         self.clas = f"{int(sinf) + 1}{harf}"

# # #     def subjects(self):
# # #         return [i.title for i in self.fan]

# # #     def full_name(self):
# # #         first = self.first_name
# # #         last = self.last_name
# # #         return f"{first} {last}"


# # # class Subject:
# # #     def __init__(self, nomi):
# # #         self.title = nomi
# # #         self.pupils = []
# # #         self.pupil_count = 0

# # #     def get_info(self):
# # #         return f"{self.title} - fanida hozir o'qiyotgan jami o'quvchilar {self.pupil_count} nafar"

# # #     def add_pupil(self, pupil):
# # #         if pupil not in self.pupils and isinstance(pupil, Pupil):
# # #             self.pupils.append(pupil)
# # #             pupil.add_subject(self)
# # #             self.pupil_count += 1
# # #         else:
# # #             raise Exception(f"Pupil {pupil} already exists or Something went wrong" )

# # #     def count_pupils(self):
# # #         return self.pupil_count

# # #     def get_pupils(self):
# # #         return [ i.full_name() for i in self.pupils]

# # #     def remove_pupil(self, pupil):
# # #         self.pupils.remove(pupil)
# # #         self.pupil_count -= 1
# # #         print(f"Pupil {pupil.full_name()} is removed")

# # # sub1 = Subject('Matematika')
# # # sub2 = Subject('Fizika')
# # # sub3 = Subject('Programming')

# # # print(sub1.get_info())

# # # pupil1 = Pupil('Alijon', 'Valiyev', '6A', '998998765432')
# # # pupil2 = Pupil('Alice', 'George', '7B', '99875645662')
# # # pupil3 = Pupil('Bob', 'Ture', '5B', '99875645662')
# # # pupil4 = Pupil('Hakim', 'Turan', '7A', '99875645662')


# # # sub1.add_pupil(pupil1)
# # # sub1.add_pupil(pupil2)
# # # sub1.add_pupil(pupil3)
# # # # print(sub1.get_info())
# # # # sub1.add_pupil("Alijon")

# # # sub2.add_pupil(pupil1)
# # # sub3.add_pupil(pupil1)


# # # print(sub1.count_pupils())
# # # print(sub1.get_pupils())
# # # sub1.remove_pupil(pupil3)
# # # print(sub1.get_info())
# # # print(sub1.get_pupils())

# # # print(sub2.get_pupils())
# # # print(sub3.get_pupils())
# # # print(pupil1.subjects())
# # # # print(pupil1.first_name)
# # # # print(pupil1.last_name)
# # # # print(pupil1.clas)
# # # # print(pupil1.phone)

# # # # print(pupil1.get_info())
# # # # print(pupil2.get_info())
# # # # print(pupil1.phone)
# # # # pupil1.phone_update('997776655')
# # # # print(pupil1.get_info())
# # # # pupil1.class_up()
# # # # pupil1.class_up()
# # # # pupil1.class_up()
# # # # pupil1.class_up()
# # # # print(pupil1.get_info())


# # class Human:
# #     def __init__(self, first_name, last_name, by, address):
# #         self.first_name = first_name
# #         self.last_name = last_name
# #         self.by = by
# #         self.address = address

# #     def get_info(self):
# #         return f"{self.first_name} {self.last_name} {self.by} {self.address}"

# #     def get_age(self):
# #         c_year = 2025
# #         age = c_year - self.by
# #         return age

# #     def full_name(self):
# #         return f"{self.first_name} {self.last_name}"


# # class Doctor(Human):
# #     def __init__(self, first_name, last_name, by, address, mutaxassisligi, tajriba, lavozim):
# #         super().__init__(first_name, last_name, by, address)
# #         self.mutaxassisligi = mutaxassisligi
# #         self.tajriba = tajriba
# #         self.lavozim = lavozim

# #     def get_info(self):
# #         text = (f"Doctor {self.full_name()}\n"
# #                 f"Species: {self.mutaxassisligi}\n"
# #                 f"Experience: {self.tajriba}\n"
# #                 f"Level: {self.lavozim}\n")
# #         return text



# # human1 = Human('Bob','George', 2010, 'Namangan/Uchkurgan')
# # doctor = Doctor('Lee', 'Chan', 2000, 'Guanjou', 'Stamatolog', 4, 'Bo\'lim boshlig\'i')

# # # print(human1.full_name())
# # # print(human1.get_age())
# # print(human1.get_info())

# # # print(doctor.full_name())
# # # print(doctor.get_age())
# # print(doctor.get_info())


# class Human:
#     __human_count = 0
#     def __init__(self, first_name, last_name, passport, by, address):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.by = by
#         self.address = address
#         self.__passport = passport
#         Human.__human_count += 1

#     @classmethod
#     def count(cls):
#         return cls.__human_count

#     def get_info(self):
#         return f"{self.first_name} {self.last_name} {self.by} {self.address}"

#     def get_age(self):
#         c_year = 2025
#         age = c_year - self.by
#         return age

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def get_passport(self):
#         return self.__passport


# class Doctor(Human):
#     def __init__(self, first_name, last_name,passport, by, address, mutaxassisligi, tajriba, lavozim):
#         super().__init__(first_name, last_name, passport, by, address)
#         self.mutaxassisligi = mutaxassisligi
#         self.tajriba = tajriba
#         self.lavozim = lavozim
#         self.__passport = passport

#     def get_info(self):
#         text = (f"Doctor {self.full_name()}\n"
#                 f"Species: {self.mutaxassisligi}\n"
#                 f"Experience: {self.tajriba}\n"
#                 f"Level: {self.lavozim}\n")
#         return text



# human1 = Human('Bob','George', 'AA1234567',2010, 'Namangan/Uchkurgan')
# human2 = Human('Bob','George', 'AA1234567',2010, 'Namangan/Uchkurgan')
# human3 = Human('Bob','George', 'AA1234567',2010, 'Namangan/Uchkurgan')
# human4 = Human('Bob','George', 'AA1234567',2010, 'Namangan/Uchkurgan')
# doctor = Doctor('Lee', 'Chan', 'AA1234567',2000, 'Guanjou', 'Stamatolog', 4, 'Bo\'lim boshlig\'i')

# # print(human1.full_name())
# # print(human1.get_age())
# # print(human1.get_info())

# # print(doctor.full_name())
# # print(doctor.get_age())
# # print(doctor.get_info())

# # print(human1.get_passport())
# print(Human.count())



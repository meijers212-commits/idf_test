# import csv
# from io import StringIO
# from modolos import User
#
# class UserCSV:
#     def __init__(self, file):
#         self.file = file
#         self.users = []
#
#     def load(self):
#         decoded = self.file.read().decode('utf-8')
#         reader = csv.DictReader(StringIO(decoded))
#         for row in reader:
#             user = User(name=row['name'], email=row['email'], age=int(row['age']))
#             self.users.append(user)
#
#     def get_users(self):
#         return self.users
#
#     def find_by_email(self, email: str):
#         return next((u for u in self.users if u.email == email), None)
#
#     def average_age(self):
#         if not self.users:
#             return 0
#         return sum(u.age for u in self.users) / len(self.users)
#
#     def adults(self):
#         return [u for u in self.users if u.is_adult()]

# # book_dict = {
# #     "title": "Кобзар",
# #     "author": "Тарас Шевченко",
# #     "copies": 15
# # }
# #
# # print(book_dict["title"])
#
#
# # class Book:
# #     def __init__(self, title,price, copies):
# #         self.title = title
# #         self.price = price
# #         self.copies = copies
# # # init для запуску класу обовязково self перший параметр
# #     def available(self):
# #         return self.copies > 0
# #
# #
# # book1 = Book("Кобзар", 450,15)
# # book2 = Book("Лісова пісня", 500,0)
# # # print(book1.title)
# # # print("Перша книга вартість", book1.price)
# # # print(book2.title, book2.price)
# #
# # print(f'Кобзар доступний {book1.available()}')
# # print(f'Лісова пісня доступна {book1.available()}')
#
#
# class Rectangle:
#     def __init__(self,width, height):
#         self.width = width
#         self.height = height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def area(self):
#         return self.width * self.height
#     def info(self):
#         print(f'Розміри прямокутника {self.width}x{self.height}')
#         print(f'S={self.area()}')
#         print(f'P= {self.perimeter()}')
#
#
# a = int(input("введіть вистоту"))
# b = int(input("введіть ширину"))
# rectangle = Rectangle(a,b)
# rectangle.info()
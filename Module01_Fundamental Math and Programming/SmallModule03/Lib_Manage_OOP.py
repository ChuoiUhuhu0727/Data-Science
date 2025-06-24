class Library:
  # Load database
  def __init__(self, books_data, members_data, user_index):
    self.books_data = books_data
    self.members_data = members_data
    self.user_index = user_index

  def check_role(self, input_role, input_name):
    if input_role == "Librarian": 
      pass
    elif input_role in ("Regular", "Premium"): 
      if type(Library.check_name(self, input_name)) == dict: pass
      else: raise ValueError("Your name doesnt exist")
    else: raise ValueError("Your role doesnt exist")
    return

  def check_name(self, input_name):
    user_index = 0
    for mem in self.members_data:
      if input_name == mem["name"]:
        return mem
    raise ValueError("Your name doesn't exist")

  def check_action(self, input_role, input_action):
    if (input_role in ("Regular", "Premium")) \
      and (input_action in ("borrow", "return")):
        pass
    elif input_role == "Librarian" and input_action in ("add", "remove"):
      pass
    else: 
      raise ValueError("Your book doesnt exist")
    return

  def check_book(self, input_role, input_name, input_action, input_book):
    if (input_role == "Librarian" and input_action == "add"):
      Librarian.add_book(input_book)
    else:
      for book in self.books_data:
        print("this is self.books_data: ", self.books_data)
        if (input_book == book["title"]) and (input_role == "Librarian"):
          Librarian.remove_book(input_book)
        elif (input_book == book["title"]) and (input_role in ("Regular", "Premium")):
          Member.borrow_book(self, input_role, input_name, input_action, input_book)
          return # TÍ VỀ FIX LỖI Ở CHỖ NÀY
      raise ValueError("Your book doesnt exist")

  def main(self):
    # Check role & name
    input_role = input("Enter your role: ").strip()
    input_name = input("Enter your name: ").strip()
    Library.check_role(self, input_role, input_name)
    self.user_index = self.check_name(input_name)

    # Check action
    input_action = input("Enter action: ").strip().lower()
    Library.check_action(self, input_role, input_action)

    # Check book
    input_book = input("Enter book name: ")
    Library.check_book(self, input_role, input_name, input_action, input_book)

    # Finally, do i need to print the message of successfully done? 

if __name__ == "__main__":
  books_data = [
    {"title": "1984", "author": "George Orwell", "isbn": "12345"},
    {"title": "Python OOP", "author": "Jane Smith", "isbn": "54321"},
    {"title": "Clean Code", "author": "Robert C. Martin", "isbn": "11122"}
  ]

  members_data = [
    {"name": "Alice", "member_type": "Regular"},
    {"name": "Bob", "member_type": "Premium"}
  ]

  # if user borrow books
  for mem in members_data:
    mem.update({'books': []})

  user_index = {}
  Library(books_data, members_data, user_index).main()

class Member(Library):
  def __init__(self, user_index, input_role, input_name, input_action, input_book, books_data, members_data):
    self.input_role = input_role
    self.input_name = input_name
    self.input_action = input_action
    self.input_book = input_book
    self.books_data = books_data
    self.members_data = members_data 
    self.user_index = user_index

  def borrow_book(self, input_role, input_name, input_action, input_book):
    count_books = Member.count_books(self, input_role)
    # for mem in self.members_data:
    #   if self.input_name == mem["name"]:
    self.user_index["books"].append(input_book)
    count_books += 1

    return f"{input_name} successfully borrows {input_book}"
    
  def count_books(self, input_role):
    count_books = len(self.user_index["books"])
    print("This is self user index books: ", self.user_index["books"])
    if input_role == "regular" and count_books >= 3:
      raise Error("You cant borrow more than 3")
    elif input_role == "premium" and count_books >= 5:
      raise Error("You cant borrow more than 5")
    else:
      return count_books

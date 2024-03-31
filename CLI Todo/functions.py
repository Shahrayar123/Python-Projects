FILEPATH = './todo.txt'
def read_todos(filePath=FILEPATH):
     """"Read a text  file and return the list of todo's items"""
     with open(filePath, 'r') as db:
          read = db.readlines()
     return read


def write_todos(to_write, filePath=FILEPATH):
     """Write the to-do items list in the text file"""
     with open(filePath, 'w') as db:
          db.writelines(to_write)

if __name__ == '__main__':
     print('Hello World')
     print(read_todos())
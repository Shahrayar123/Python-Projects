from functions import write_todos, read_todos
import time

time = time.strftime('%b %d %Y %H:%M:%S')

while True:
     try: 
          user_input = input('Enter Add, Show, Exit, Edit and Complete: ').lower()

          if 'add' in user_input:
               text = user_input[4:]
               db = read_todos()
               db.append(text + '\n')
               write_todos(db)

          elif 'show' in user_input:
               db = read_todos()
               for index, item in enumerate(db):
                    item = item.replace('\n', '')
                    print(f"{index+1}. {item}")

          elif 'edit' in user_input:
               try:
                    number = int(user_input[4:])
                    number = number - 1
                    db_read = read_todos()
                    new_todo = input('Enter The New Todo: ')
                    db_read[number] = new_todo + '\n'
                    write_todos(db_read)

               except IndexError:
                    print('Enter a Valid Number!')
                    continue

          elif 'complete' in user_input:
               number = int(user_input[9:]) - 1
               db_read = read_todos()
               db_read.pop(number)
               write_todos(db_read)

          elif 'exit' in user_input:
               print('Bye :)')
               break
          else:
               print('Enter a Valid Command')
     except (EOFError, KeyboardInterrupt):
          print()
          print('Bye :)')
          break
class Node:
  def __init__(self, value, link_node = None):
    self.value = value
    self.link_node = link_node
    
  def set_next_node(self, link_node):
    self.link_node = link_node
    
  def get_next_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))
    
class TowersOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.left_stack = Stack("Left")
        self.middle_stack = Stack("Middle")
        self.right_stack = Stack("Right")
        self.stacks = [self.left_stack, self.middle_stack, self.right_stack]
        self.num_optimal_moves = (2 ** num_disks) - 1
        self.num_user_moves = 0

    def setup_game(self):
        for i in range(self.num_disks, 0, -1):
            self.left_stack.push(i)

    def print_stacks(self):
        print("\n...Current Stacks...")
        for stack in self.stacks:
            stack.print_items()

    def move_disk(self, from_stack, to_stack):
        if from_stack.is_empty():
            print("\nInvalid Move. Try Again")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            self.num_user_moves += 1
        else:
            print("\nInvalid Move. Try Again")

    def play(self):
        print("\nLet's play Towers of Hanoi!!")
        self.setup_game()

        while self.right_stack.get_size() != self.num_disks:
            self.print_stacks()

            while True:
                print("\nWhich stack do you want to move from?")
                from_stack = self.get_input()
                print("\nWhich stack do you want to move to?")
                to_stack = self.get_input()

                self.move_disk(from_stack, to_stack)
                break

        print(
            "\n\nYou completed the game in {use} moves, and the optimal number of moves is {opt}".format(
                use=self.num_user_moves, opt=self.num_optimal_moves
            )
        )

    def get_input(self):
        choices = [stack.get_name()[0] for stack in self.stacks]
        while True:
            for i in range(len(self.stacks)):
                name = self.stacks[i].get_name()
                letter = choices[i]
                print("Enter {let} for {nam}".format(let=letter, nam=name))
            user_input = input("")
            if user_input in choices:
                for i in range(len(self.stacks)):
                    if user_input == choices[i]:
                        return self.stacks[i]
            else:
                print("Invalid choice. Please enter a valid option.")

# Run the game
if __name__ == "__main__":
    num_disks = int(input("\nHow many disks do you want to play with?\n"))
    while num_disks < 3:
        num_disks = int(input("Enter a number greater than or equal to 3\n"))

    game = TowersOfHanoi(num_disks)
    game.play()

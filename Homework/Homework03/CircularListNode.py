class Link:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.current = None

    def insert(self, data):
        new_link = Link(data)
        if self.current is None:
            self.current = new_link
            self.current.next = self.current
        else:
            new_link.next = self.current.next
            self.current.next = new_link

    def search(self, data):
        if self.current is None:
            return None
        current_link = self.current
        while current_link.data != data:
            current_link = current_link.next
            if current_link == self.current:
                return None
        return current_link

    def delete(self, data):
        if self.current is None:
            return
        prev_link = self.current
        current_link = self.current.next
        while current_link.data != data:
            if current_link == self.current:
                return
            prev_link = current_link
            current_link = current_link.next
        prev_link.next = current_link.next
        if current_link == self.current:
            self.current = prev_link

    def display(self):
        if self.current is None:
            return
        current_link = self.current
        while True:
            print(current_link.data, end=" -> ")
            current_link = current_link.next
            if current_link == self.current:
                break
        print()

    def step(self):
        if self.current is not None:
            self.current = self.current.next
def main():
        # Example usage:
    circular_list = CircularList()

    # Insertion
    circular_list.insert(1)
    circular_list.insert(2)
    circular_list.insert(3)

    # Display
    circular_list.display()  # Output: 1 -> 2 -> 3 ->

    # Searching
    print(circular_list.search(2).data)  # Output: 2

    # Deletion
    circular_list.delete(2)

    # Display after deletion
    circular_list.display()  # Output: 1 -> 3 ->

# I inserted this to get it to run.  You probably used the VSCode
#  terminal pane to run it, but don't forget I stressed early on
#  this semester that I won't be running your code that way, that
#  I use the "real" command line.  So, YOU NEED THIS LINE....  :D
main()

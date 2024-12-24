class Impression:
    def __init__(self, name, pages, colored = False):
        self.name = name
        self.pages = pages
        self.colored = colored
        self.next = None
        self.previous = None
    
    def __str__(self):
        return f'Impression: {self.name} - Pages: {self.pages}'

class ImpressionList:
    def __init__(self, name):
        self.name = name
        self.head = None

    def queue(self, impression):
        if not self.head:
            self.head = impression
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = impression            
        current.next.previous = current

    def print_impressions(self):
        current = self.head
        while current:
            print(f'{current} - Next: {current.next} - Previous: {current.previous}')
            current = current.next

# Create an impression list for curriculums
curriculum_list = ImpressionList(name='curriculums')

# Create multiple impressions
yuri_cv = Impression(name='Curriculum Yuri', pages=2, colored=False)
ana_cv = Impression(name='Curriculum Ana', pages=3, colored=True)
john_cv = Impression(name='Curriculum John', pages=1, colored=False)
mary_cv = Impression(name='Curriculum Mary', pages=2, colored=True)

# Queue all impressions
curriculum_list.queue(yuri_cv)
curriculum_list.queue(ana_cv)
curriculum_list.queue(john_cv)
curriculum_list.queue(mary_cv)

# Print all impressions in the list
curriculum_list.print_impressions()
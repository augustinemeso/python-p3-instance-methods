# lib/person.py
class Person:
    def talk(self):
        print("Hello World!")
        
    def walk(self):
        print("The person is walking.")

# Test the Person class
if __name__ == "__main__":
    john = Person()
    john.talk()  # Should print "Hello World!"
    john.walk()  # Should print "The person is walking."

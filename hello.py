def greet_user():
	"""Display a simple greeting"""
	print("hello world")

greet_user()

def greet_user(username):
	print("Hello, "+ username + "!")

greet_user('jesse')
greet_user('diana')

def describe_pet(animal, name):
	print("\n I have a "+ animal)
	print("Its name is "+name)

describe_pet("dog", 'vicky')

def desc_pet(animal, name):
        print("\n I have a "+ animal+".")
        print("Its name is "+name+".")

desc_pet(animal="cow",name="vicky")

def descr_pet(name,animal='Tiger'):
        print("\n I have a "+ animal+".")
        print("Its name is "+name+".")

descr_pet(animal="cow",name="ganesh")
descr_pet('dog','hamster')
descr_pet('gihub')

def des_pet(animal, name=None):
        print("\n I have a "+ animal+".")
        if name: 
           print("Its name is " + name + ".")

des_pet('hamster','harry')
des_pet('snake')

"""def get_full_name"""

age = int(input("enter your age"))


class AgeException(Exception):
    def __str__(self):
        return "age is less than 15 so,cannot create account"
    print("class")


try:
    if age<15:
        raise AgeException
    else:
        print("Eligible")
except AgeException as i:
    print(i)
print("checking done")
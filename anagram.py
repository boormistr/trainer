first = input()
second = input()

if sorted(first.lower()) == sorted(second.lower()):
    print(True)
else:
    print(False)
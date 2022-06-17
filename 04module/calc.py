# import simple , complex
# print(dir())

# print(simple.add(1,2))
# print(complex.sqr(5))


# from simple import sub

# print(dir())

# print(sub(4,2))


# from simple import mul as m

# print(m(2,3))



# from simple import add
# from complex import add

import complex , simple

def main():
    print(simple.add(1,4))
    complex.add(23)

# print(__name__)

if __name__ == '__main__':
    main()

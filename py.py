#! /usr/bin/python 

from ctypes import CDLL, CFUNCTYPE, POINTER, c_voidp, c_int, cast
from array import array

#Load the shared library like this
SO = CDLL("./mylib.so")

#Then you can start calling functions
SO.init(1)

#Register a callback (this is trickier)
def python_callback(a, count, lst):
    print("Py: Got " + str(a) + " :", end="")
    for i in range(count):
        print(" " + str(lst[i]), end="")
    print()

#You must "declare" the c function
CALLBACKTYPE = CFUNCTYPE(c_voidp, c_int, c_int, POINTER(c_int))

#Then you instantiate the CFUNCTYPE with your function
c_callback = CALLBACKTYPE(python_callback)
#WARNING the c_callback variable MUST NOT BE GARBAGE COLLECTED!
#Save it somewhere otherwise you will get undefined behaviour
#Also beware of threads created outside of python that may call this
#Read the note in: https://docs.python.org/3/library/ctypes.html#callback-functions

#Call the function to register the callback 
SO.registerCallback(c_callback)



#calling with a list:
py_list = [1, 2, 3, 4]

SO.addStuff(2000, 4, (c_int*len(py_list))(*py_list))
py_list.append(5)
SO.addStuff(3000, 5, (c_int*len(py_list))(*py_list))

#using a c_int list (usefull if the list has a fixed size):
c_list = (c_int * 3)(1, 2, 3) #You can define it here
for i in range(3): # or fill it in dynamically
    c_list[i] = c_int(i)
SO.addStuff(4000, 3, c_list)

#using array.array
py_array = array('i', [1, 2, 3, 4, 5, 6])
SO.addStuff(5000, len(py_array), cast(py_array.buffer_info()[0], POINTER(c_int)))
py_array.append(7)
SO.addStuff(6000, len(py_array), cast(py_array.buffer_info()[0], POINTER(c_int)))

#Call Variadic Functions
SO.addStuffVariadic(666, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
SO.addStuffVariadic(666, len(py_list), *py_list)
SO.addStuffVariadic(666, len(c_list), *c_list)


#Testing the callback 
SO.flush()

SO.shutdown();

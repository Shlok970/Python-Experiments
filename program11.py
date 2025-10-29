import numpy as np
print("---4. Array views vs copy--- ")
original_array=np.arange(5)
print(f"The original array is {original_array}")
view_array=original_array.view()
view_array[0]=99
print(f"View array modification: {view_array}")
print(f"Original array after modification: {original_array}")
original_array=np.arange(5)
copy_array=original_array.copy()
copy_array[0]=100
print(f"Copy array after modification: {copy_array}")
print(f"Original array after modification: {original_array}")
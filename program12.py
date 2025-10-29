import numpy as np
print("---\nManipulating array shapes---")
array_1d=np.arange(12)
print(f"Original 1D array: {array_1d} ")

array_2d=array_1d.reshape(3,4)
print(f"Reshaped to  3x4: \n{array_2d}")

flattened_array=array_2d.flatten()
print(f"Flattened array: {flattened_array}")

transposing_array=array_2d.T
print(f"Transpose matrix: \n{transposing_array}")
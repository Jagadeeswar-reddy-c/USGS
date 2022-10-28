import numpy as np
import Main 
error=True 
def my_main_function():
    Main.Main_pro()
    print('error')
while error:
    try:
        my_main_function() 
        error=False 
    except IOError: 
        error=True 
print("finished") 
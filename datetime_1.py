from datetime import datetime
import os
current_datetime = datetime.now()
print(f'{current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')

zero = """
   ■■■■  
 ■■    ■■ 
■■      ■■
■■      ■■
 ■■    ■■ 
   ■■■■  
"""

one = """
    ■■■   
 ■■■■■■   
    ■■■   
    ■■■   
    ■■■   
 ■■■■■■■■
"""

two = """
  ■■■■■■  
■■    ■■■
     ■■■
   ■■■   
 ■■■    
■■■■■■■■■
"""

three = """
■■■■■■ 
     ■■■
■■■■■■ 
     ■■■
     ■■■
■■■■■■
"""

four = """
■■      ■■
■■      ■■
■■      ■■
■■■■■■■■■■
        ■■
        ■■
"""

five = """
■■■■■■■■■
■■        
■■■■■■■■ 
        ■■
        ■■
■■■■■■■■ 
"""

six = """
■■■■■■■■
■■        
■■■■■■■■
■■     ■■
■■     ■■
 ■■■■■■■ 
"""

seven = """
 ■■■■■■■■■
        ■■
      ■■ 
    ■■   
    ■■   
    ■■  
"""

eight = """
  ■■■■■■ 
■■      ■■
  ■■■■■■ 
■■      ■■
■■      ■■
  ■■■■■■ 
"""

nine = """
  ■■■■■■ 
■■      ■■
■■      ■■
  ■■■■■■■■
        ■■
   ■■■■■■■
"""

dot = """
    ■■    
    ■■    
          
          
    ■■    
    ■■    
"""

nothing = """
          
          
          
          
          
          
"""

output_number = {
    "0": zero,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
    "8": eight,
    "9": nine,
    ":": dot,
    "empty": nothing,
}
def clear_screen():
    os.system(clear_screen)

    
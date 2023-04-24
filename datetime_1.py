from datetime import datetime
import os
now = datetime.now()
current_time = now.strftime('%H:%M:%S')
print('Current time =', current_time)
def clear_screen():
    os.system('clear')
    
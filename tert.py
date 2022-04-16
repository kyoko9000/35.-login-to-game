# importing the sys module
import sys

# appending the directory of mod.py
# in the sys.path list
sys.path.append('D:/9. python project/35. login to game/DoAn1/DoAn1')

# now we can import mod
import DoAn1.DoAn1.DoAn1

# calling the hello function of mod.py
DoAn1.DoAn1.DoAn1.start_menu()
# Simple Python Encoder and Decoder
# Matthew McCarty


#Encoding function 
def encoding(filepath,dfilepath,eDecode):
   print("\n Encoding in progress ...")
   infile = open(filepath)
   dncode = open(dfilepath, "w+")
   #Opens both files that the user wants to encode and decode
   s = infile.read()
   cr = ""
   ncode = ''
   count = 1
   prev = ''
   eDecode = []
   punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

   #Checks each character in the string and appends it to an array and adds to a string called ncode to be used to print to a file.
   for char in s:
      #checks to see if the file contains any unsupport characters and prints an error if it finds any
      if char not in punctuations: 
         if char != prev:
             if prev:
                ncode += str(count)
                ncode += prev
                entry = (prev,count)
                eDecode.append(entry)
      
             count = 1
             prev = char
         else:
            count += 1
      else:
         print("\n Unsupported Characters")
         menu(eDecode)
   else:      
      ncode += str(count)
      ncode += char
      entry = (char,count)
      eDecode.append(entry)  

   # writes to the files and closes them
   dncode.write(ncode)
   dncode.close()
   dncode = open(dfilepath, "r")

   #Finds length of both files and figures out the Compression Ratio
   s2 = dncode.read()
   cr = len(s)/len(s2)
   dncode.close()
   infile.close()

   print("\n Encoding completed ...")
   print("\n Compression Ration: " + str(cr))
   #Links back to the menu
   menu(eDecode)


def decoding(filepath,dfilepath,eDecode):
 #opens the files the user wants to decode from and to
 print("\n Decoding in progress ...")
 infile = open(filepath)
 dncode = open(dfilepath, "w+")
 s = infile.read()
 d = ''

 #Kinda cop out but it takes the info added to the array earlier to easily decode the files, obivously this methods has its own problems and cannot decode a file the the user has not just encoded
 for char, count in eDecode:
    for x in range(count):
      d+=char
 
 dncode.write(d)
 dncode.close()
 print('\n Decoding complete ...')
 menu(eDecode)  

def menu(eDecode):
   #Menu function that collects input from the user
   print("""
           1. Encode a File
           2. Decode a File
           3. Exit
       """)

   flag = True
   while flag:
      #While statements that waits for a correct input to proced to either encoding or decoding
       flag = input(" What would you like to do?: ")
       if flag == "1":
            filepath = input("\n Input Source Filepath: ")
            dfilepath = input (" Input Destination Filepath: ")
            flag = False
            encoding(filepath,dfilepath,eDecode)
       elif flag == "2":
            filepath = input("\n Input Source Filepath: ")
            dfilepath = input (" Input Destination Filepath: ")
            flag = False
            decoding(filepath,dfilepath,eDecode)
       elif flag == "3":
            print ("Goodbye")
            exit()
       elif flag != "" or flag > 3:
            print ("\n Not a Valid Choice Try Again\n")
    
eDecode = []
menu(eDecode)

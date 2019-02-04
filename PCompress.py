# +Python File Compressor and Decompressor
# Matthew McCarty
import argparse 
import math


#Encoding function 
def encoding(filepath):
   dfilepath = filepath + 'Encode'
   print("\n Encoding in progress ...")
   infile = open(filepath)
   dncode = open(dfilepath, "w+")

   s = infile.read()
   compratio = 0
   ncode = ''
   count = 1
   prev = ''
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
      
             count = 1
             prev = char
         else:
            count += 1
      else:
         print("\n Unsupported Characters")
   else:      
      ncode += str(count)
      ncode += char
      entry = (char,count)
        
   # writes to the files and closes them
   dncode.write(ncode)
   dncode.close()
   infile.close()
  
  #Compression Ratio using total character counts of both files
   compratio = (float(file_size(filepath))/float(file_size(dfilepath)))

   print("\n Encoding completed ...")
   print("\n Compression Ratio: " + str(compratio))
   



def decoding(filepath):
  #opens the files the user wants to decode from and to
  dfilepath = filepath + 'Decode'
  print("\n Decoding in progress ...")
  infile = open(filepath)
  dncode = open(dfilepath, "w+")

  s = infile.read()
  lastchar = ''
  buff = 0
  d = ''

  #Decode which checks if a character is a number, if it is, it skips an interation
  #else it adds the amount of characters to a temporary string
  for char in s:
    if is_number(char):
      buff = char
      continue
    else:
      i = 0
      print(buff)
      while i < int(buff):
        d += char
        i += 1

  print(d)
  dncode.write(d)
  dncode.close()
  print('\n Decoding complete ...')  



#Function that just returns the amount of charactes in any given file
def file_size(filepath):
    with open(filepath, 'r') as file:
        filename = file.read()
        len_chars = sum(len(word) for word in filename)
        return len_chars



#Checks to see whether or not a given character is a number
def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    pass

  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass 
  return False


#command line arguements 
parser = argparse.ArgumentParser()
parser.add_argument('-F')
parser.add_argument('-M')


args = parser.parse_args()
if args.M == 'Encode':
  encoding(args.F)
elif args.M == 'Decode':
  decoding(args.F)
else:
  print("Not a Valid Mode Option")


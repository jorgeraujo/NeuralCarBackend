from slugify import slugify
from os import listdir,remove,rename
from PIL import Image

for filename in listdir('./'):
  if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.gif') :
    try:
      img = Image.open('./'+filename) # open the image file
      img.verify() # verify that it is, in fact an image
      name = filename.split('-')
      print(name)
    except (IOError, SyntaxError) as e:
      name = filename.split('-')
      type = name[-1]
      name = ''.join(name[:-1])+'.'
      name = name+type
      rename(filename,name)
      print(name)
      print('Bad file:', filename) # print out the names of corrupt files
      print('deleted:', filename) # print out the names of corrupt files

  else:
      name = filename.split('-')
      type = name[-1]
      name = ''.join(name[:-1])+'.'
      name = name+type
      print(name)
      rename(filename,name)
      print('Bad file:', filename) # print out the names of corrupt files

      print('deleted:', filename) # print out the names of corrupt files

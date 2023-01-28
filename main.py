import time
from pylibdmtx.pylibdmtx import encode
from PIL import Image,ImageDraw,ImageFont
import ctypes
import os


#libdmtx ye dll mikhad ke vaqti exe mishe bayad kenaresh bashe
ctypes.windll.kernel32.SetDllDirectoryW(None)
ctypes.CDLL('libdmtx-64.dll')
print("\n**********  ***   *************.   ***         ***      ****     ************* \n**     **  ***    ***         **   ***         ***    ****       ***        ***\n**   ***  **      ***        ***   ***         *** ****          ***        ***\n**  **   **        **********      ***         * *******         ************\n**   **  ***      ***         ***  ***          ***   ****       ****   ****\n**    **   **     ***         ***  ***         ***      ****     ***      ***\n**********  **    *************    **** ****** ***        ****   ***       ****")
pooya=open('readme.txt','r')
pooyareadline=pooya.read().splitlines()
pooyacounter=-1
b=open('temp.txt','r')
readline=b.read().splitlines()
d = open('loc.txt', 'r')
locreadline = d.read().split(',')
e = open('tloc.txt', 'r')
tlocreadline = e.read().split(',')
#reads input prod.codes
kala=readline[1]
counter=0
#font that our barcodes are written in
title_font = ImageFont.truetype('./arial.ttf', 20)
uniquechk=0
#opens a text file and write barcodes in
with open('readme.txt', 'w') as f:
    for i in range(int(readline[0])):
        pooyacounter+=1
        counter+=1
        counterDARSAD1=(counter/int(readline[0]))*100
        counterDARSAD2="{:.2f}".format(counterDARSAD1)
        print(f'PROCESS : {counter} of {int(readline[0])} ({counterDARSAD2}%)',end='')
        barcodeasli=pooyareadline[pooyacounter]
        #pylibdmtx encoder
        encoded = encode(barcodeasli.encode('utf8'))
        #opens template img
        img1 = Image.open(f'./background/{readline[1]}.bmp').convert('RGB')
        img = Image.frombytes('RGB', (encoded.width, encoded.height), (encoded.pixels))
        #paste pylibdmtx generated barcode on it (on tloc position) (starting px 200 because it is in bottom middle and 100 px because it's in first one-third of org pic
        img1.paste(img,(int(locreadline[0]),int(locreadline[1])))
        #actives Pillow's ImageDraw func to draw (write) numbers of our barcode on image
        image_editable = ImageDraw.Draw(img1)
        image_editable.text(((int(tlocreadline[0]),int(tlocreadline[1]))), barcodeasli, (0, 0, 0),font=title_font)
        #rotates it for printer AND EXPANDS IT TO prevent making blank spaces
        img1=img1.rotate(90,expand=1)
        #saves it
        img1.save(f'./savedirectory/dotbox{i}.bmp')
        #writes generated barcode in our open txt file
        f.write(barcodeasli)
        if not (i==int(readline[0])-1):
            f.write('\n')
        print('\r',end='')

#closes our txt file to reduce ram usage
f.close()
b.close()
d.close()
e.close()
# ez-pylibdmtx
Iike its name, it's an EZ way to use pylibdmtx library the only thing you need to enter the location of data matrix and the content(number, symbols, word, etc) into txt files and define an background then just run the python script.
main.py in this project will get 4 txt files, 1 directory named /savedirectory and background from /background  from you.
1-Tloc.txt : the location of text that you want to be printed on final product (in my case it was a generated barcode)
2-loc.txt :  the location of generated data matrix that you want to be printred on final label.
3-temp.txt : the number of generated barcodes you want (for example you want it to generate 3000 unique barcodes and paste them on your background)
4-readme.txt: it's not a normal readme :)) it's your unique barcodes(yes all of 'em) in a text file.(the program will update this file everytime you run it)
pmet.py is a small extention that will read pmet.txt and find its background (pmet's second line in txt is for backgound) and print it with your default printer (in my case it was a zebra label printer)
printer.py will again use your temp and print all files in /savedirectory with your default printer.

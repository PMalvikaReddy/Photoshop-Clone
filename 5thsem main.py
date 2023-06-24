from os import system
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import edit
import filters
from rainbowFilter import rainbowFunction

def toContinue1():
    ans=input("do you want to continue? y/n >>>")
    if ans=='y':
        EditOption()
    else:
        exit()

def toContinue2():
    ans=input("do you want to continue? y/n >>>")
    if ans=='y':
        ChooseFilter()
    else:
        exit()

def DigitalImageEditor():
    while(1):
        print("|********************************|")
        print("| P H O T O S H O P -- C L O N E |")
        print("|   IMAGES GET A NEW DIMENSION   |")
        print("|                                |")
        print("|   1--> Properties of an Image  |")
        print("|                                |")
        print("|   2--> Edit an Image           |")
        print("|                                |")
        print("|   3--> Add Filters to an Image |")
        print("|                                |")
        print("|   4--> Exit                    |")
        print("|                                |")
        print("|                                |")
        print("|********************************|")
        print('\n')
        option1=int(input("choose an option>>> "))
        if option1==1:
            picture=input("enter the image name or url >>>")
            im = Image.open(picture)
            print(im.mode)
            print("the size of the image is:",im.size)
            print("the image fomat is: ",im.format)
            ans=input("do you want to continue? y/n >>>")
            if ans=='y':
                DigitalImageEditor()
            else:
                exit()
        elif option1==2:
            EditOption()
        elif option1==3:
            ChooseFilter()
        elif option1==4 or option1!=1 or option1!=2 or option1!=3:
            exit()


def EditOption():
    clear = lambda: system('clear')
    while(1):
        print("|********************************|")
        print("| P H O T O S H O P -- C L O N E |")
        print("|                                |")
        print("| EDITING IMAGE OPTIONS:         |")
        print("| ----------------------         |")
        print("| 1--> Display the image         |")
        print("|                                |")
        print("| 2--> Resize Image              |")
        print("|                                |")
        print("| 3--> Blur the Image            |")
        print("|                                |")
        print("| 4--> Rotate Image              |")
        print("|                                |")
        print("| 5--> Adjust Brigthness         |")
        print("|                                |")
        print("| 6--> Adjust Contrast           |")
        print("|                                |")
        print("| 7--> Exit                      |")
        print("|                                |")
        print("|********************************|")
    
        option2=int(input("select an edit option>>> "))
        picture=input("enter the image name or url >>>")
        img = Image.open(picture)
        if option2==1:
            edit.Show(img)
            toContinue1()            
        elif option2==2:
            edit.Crop_Image(img)
            toContinue1()
        elif option2==3:
            edit.Blur_Image(img)
            toContinue1()
        elif option2==4:
            edit.Image_Rotate(img) 
            toContinue1()   
        elif option2==5:
            edit.Adjust_Brightness(img)
            toContinue1()
        elif option2==6:
            edit.Adjust_Contrast(img)
            toContinue1()
        elif option2==7:             
            exit()


def ChooseFilter():
    print("|********************************|")
    print("| P H O T O S H O P -- C L O N E |")
    print("|                                |")
    print("| IMAGE FILTERS:                 |")
    print("| --------------                 |")
    print("| 1--> Grey Scale Filter         |")
    print("|      (Black and White)         |")
    print("|                                |")
    print("| 2--> Fire Red Filter           |")
    print("|                                |")
    print("| 3--> Bright Yellow Filter      |")
    print("|                                |")
    print("| 4--> Mirror Image Filter       |")
    print("|                                |")
    print("| 5--> Rainbow Image Filter      |")
    print("|                                |")
    print("| 6--> Exit                      |")
    print("|                                |")
    print("|                                |")
    print("|********************************|")
    print('\n')
    option3=int(input("choose a filter option>>> "))
    picture=input("enter the image name or url >>>")
    img = Image.open(picture)
    if option3==1:
        filters.GreyScaleFilter(img)
        toContinue2()            
    elif option3==2:
        filters.RedFilter(img)
        toContinue2()
    elif option3==3:
        filters.YellowFilter(img)
        toContinue2()
    elif option3==4:
        filters.MirrorImage(img) 
        toContinue2() 
    elif option3==5:
        rainbowFunction(img)
        toContinue2()  
    elif option3==6:             
            exit()  
    '''mirror image,greenscale,yellowscale,redscale,greyscale,imageoutline,rainbow'''#enhance property


if __name__ == "__main__":
    DigitalImageEditor()

 
from email.headerregistry import Address
from unicodedata import digit
from pdf2image import convert_from_path
from PIL import Image
from numpy import append
from pyparsing import Word
import pytesseract
import cv2
from distutils.command.config import config
from googletrans import Translator
import os
from PIL import Image
import re
import re
import numpy as np
import cv2
import pyautogui
import json


def andrapradesh():
    sent=""
    filename=input("enter the file name ")
    poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
    pdf_path = filename
    images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    file_names=[]
    for count, img in enumerate(images):
        img_name = f"page_{count+1}.png"
        img.save(img_name, "PNG")
        file_names.append(img_name)
    print(file_names)

    lan=input("enter the language: ")

    if lan=="kan":
        la='kn'
        state='karnataka'
    elif lan=="guj":
        la='gu'
        state="gujrat"
    elif lan=="tel":
        la='te'
        state="andrapradesh"    
    elif lan=="mal":
        la='ml'
        state="kerala" 
    else:
        la='hi'  
        state="delhi"      


    for file in file_names:
        img=cv2.imread(file)
        text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
        translator = Translator()
        translated = translator.translate(text, src=la, dest='en')
        string = translated.text
        sent=sent+string 

    with open("original.txt",'w') as f:
        print(sent,file=f)
    f.close()

    content=open("original.txt",'r').read()

    try:
        cn = re.search('(.*), father',content).group(1)

        cn_fat=re.search('father (.\w+.\s+.\w+)',content).group(1)

        ad=re.search('Suit No. 49/2019[\r\n]+([^\r\n]+)',content).group(1)
        add=re.search(ad+'[\r\n]+([^\r\n]+)',content).group(1)
        add=add[:-2]

        res_name = re.search('(.*), Father',content).group(1)

        res_fat=re.search('Father (.\w+)',content).group(1)

        res_age=re.search('(?<=Age )(\d+\d+)', content).group(1)

        res_add = re.search('Profession Business,(.*)',content).group(1)
        ress_add=re.search(res_add+'[\r\n]+([^\r\n]+)',content).group(1)
        resss_add=res_add+ress_add

        translator = Translator()
        translated1 = translator.translate(cn, src='en', dest=la)
        translated2 = translator.translate(add, src='en', dest=la)
        translated3 = translator.translate(res_name, src='en', dest=la)
        translated4 = translator.translate(resss_add, src='en', dest=la)
        translated5 = translator.translate(res_age, src='en', dest=la)
        translated6 = translator.translate(res_fat, src='en', dest=la)


        dict={

        'complainant':cn,
        'complainant_org':translated1.text,
        'complainant_address':add,
        'complainant_address_org':translated2.text,
        'age': res_age,
        'accused':res_name,
        'accused_org':translated3.text,
        'accused_address':resss_add,
        'address_org':translated4.text,
        'fathers_or_husband_name':res_fat,
        'fathers_or_husband_name_org':translated6.text,



        }

    except:
        
        cn=re.search('For the kingdom[\r\n]+([^\r\n]+)',content).group(1)
        cnn=cn[:-1]

        cn_add=re.search(cn+'[\r\n]+([^\r\n]+)',content).group(1)

        resn=re.search('And[\r\n]+([^\r\n]+)',content).group(1)
        resn=resn[:-1]

        res_fat=re.search('Father:(.\w+.\w+)',content).group(1)


        res_ad=re.search('Door.No.(.*)',content).group(1)
        res_add=re.search(res_ad+'[\r\n]+([^\r\n]+)',content).group(1)
        add=res_ad+res_add

        res_age=re.search('(?<=Age: )(\d+\d+)', content).group(1)


        translator = Translator()
        translated1 = translator.translate(cnn, src='en', dest=la)
        translated2 = translator.translate(cn_add, src='en', dest=la)
        translated3 = translator.translate(resn, src='en', dest=la)
        translated4 = translator.translate(res_fat, src='en', dest=la)
        translated5 = translator.translate(add, src='en', dest=la)

        dict={

        'complainant':cnn,
        'complainant_org':translated1.text,
        'complainant_address':cn_add,
        'complainant_address_org':translated2.text,
        'age':res_age,
        'accused':resn,
        'accused_org':translated3.text,
        'accused_address':add,
        'address_org':translated5.text,
        'fathers_or_husband_name':res_fat,
        'fathers_or_husband_name_org':translated4.text,



        }

    with open('data.json', 'w') as outfile:
        json.dump(dict, outfile,indent=2,ensure_ascii=False)
        


    print("ocr process completed")
    cv2.destroyWindow("Test")
    cv2.destroyWindow("Main")


def gujrat():

    def jud():
    
        sent=""
        ma="aee "

        filename=input("enter the file name ")
        poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
        pdf_path = filename
        images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
        file_names=[]
        for count, img in enumerate(images):
            img_name = f"page_{count+1}.png"
            img.save(img_name, "PNG")
            file_names.append(img_name)
        print(file_names)

        lan=input("enter the language: ")

        if lan=="kan":
            la='kn'
            state='karnataka'
        elif lan=="guj":
            la='gu'
            state="gujrat"
        else:
            la='hi'  
            state="delhi"      


        for file in file_names:
            img=cv2.imread(file)
            text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
            translator = Translator()
            translated = translator.translate(text, src=la, dest='en')
            string = translated.text
            sent=sent+string 


        try:
            with open("original.txt",'w') as f:
              print(sent,file=f)
            f.close()
            content=open("original.txt",'r').read()
            
            ap=re.search('::::: Appellant.[\r\n]+([^\r\n]+)', content).group(1)
            ac=re.search('(\w+)',ap).group(1)
            faha=re.search('/o (.*)', content).group(1)  
            st=re.search('(?<=stay )(.*)', content).group(1) 
            co=re.search('(.*)::::: Appellant.', content).group(1)    

            translator = Translator()
            translated1 = translator.translate(ac, src='en', dest='gu')
            translated2 = translator.translate(faha, src='en', dest='gu')
            translated3 = translator.translate(st, src='en', dest='gu')
            translated4 = translator.translate(co, src='en', dest='gu')

            dict={

            'complainant':co,
            'complainant_org':translated4.text,
            'age': " Not Found",
            'accused':ac,
            'accused_org':translated1.text,
            'address':st,
            'address_org':translated3.text,
            'fathers_or_husband_name':faha,
            'fathers_or_husband_name_org':translated2.text,

            }
        except:
            sent=sent.replace('(1)','a1a',4)
            sent=sent.replace('(2)','a2a',4)
            sent=sent.replace('(3)','a3a',4)
            sent=sent.replace('(4)','a4a',4)
            sent=sent.replace('(5)','a5a',4)

            with open("original.txt",'w') as f:
                print(sent,file=f)
            f.close()
            content=open("original.txt",'r').read()
            pet=[]
            if len(re.search('(?<=a1a )(.*)', content).group(1))!=0:
                pet.append(re.search('(?<=a1a )(.*)', content).group(1))
            if len(re.search('(?<=a2a )(.*)', content).group(1))!=0:
                pet.append(re.search('(?<=a2a )(.*)', content).group(1))
            if len(re.search('(?<=a3a )(.*)', content).group(1))!=0:
                pet.append(re.search('(?<=a3a )(.*)', content).group(1))

            ag=re.search('(?<=Samawala:- )(.*)', content).group(1)
            addr=re.search('(?<=Resident: )(.*)', content).group(1)
            addr1=re.search(''+addr+'[\r\n]+([^\r\n]+)', content).group(1)
            adr=addr+addr1      
            hm=re.search('(?<=Hometown: )(.*)', content).group(1)

            translator = Translator()
            translated1 = translator.translate(ag, src='en', dest='gu')
            translated2 = translator.translate(adr, src='en', dest='gu')
            translated3 = translator.translate(hm, src='en', dest='gu')
            ll=[]
            for ele in pet:
                translated4 = translator.translate(ele, src='en', dest='gu')
                ll.append(translated4.text)

            dict={

            'Petitioners':pet,
            'Petitioners_org':ll,
            'Against':ag,
            'Against_org':translated1.text,
            'Address':adr,
            'Address_org':translated2.text,
            'Hometown':hm,
            'Hometown_org':translated3.text,
            'Fathers_name':" Not Found" ,
            'Age': " Not Found",

            }
            

        with open('data.json', 'w') as outfile:
            json.dump(dict, outfile,indent=2,ensure_ascii=False)
            
        

        print("ocr process completed")
        cv2.destroyWindow("Test")
        cv2.destroyWindow("Main")



    def fir():

        
        sent=""
        ma="aee "

        filename=input("enter the file name: ")
        poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
        pdf_path = filename
        images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
        file_names=[]
        for count, img in enumerate(images):
            img_name = f"page_{count+1}.png"
            img.save(img_name, "PNG")
            file_names.append(img_name)
        print(file_names)

        lan=input("enter the language: ")

        if lan=="kan":
            la='kn'
            state='karnataka'
        elif lan=="guj":
            la='gu'
            state="gujrat"
        elif lan=="pan":
            la='pa'
            state="punjab"
        else:
            la='hi'  
            state="delhi"      


        for file in file_names:
            img=cv2.imread(file)
            text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
            translator = Translator()
            translated = translator.translate(text, src=la, dest='en')
            string = translated.text
            if file=='page_2.png':
                ma+=string
            sent=sent+string 

        with open("ma.txt",'w') as f:
            print(ma,file=f)
        lin=re.search('(?<=Under Section )(.* )', sent).group(1)

        string1=re.sub(r'\s*\([^)]+\)', '\n', sent)

        with open('output.txt', 'w', encoding='utf-8') as f:
            print("Under Section "+lin,file=f)
            print(string1, file=f)

        
        str="klkl  "
        cont=open('output.txt','r').read()
        full_cont=cont
        lists=['District ','Police ','Type of Information: ',' Date','Station r ','State ','Accused Name','Name'," Father's/Hu",'Nationality','Date from','Time from','Time to','Year',' Date / Year of Birth ']
        for val in lists:
            if val not in cont: 
                file_object = open('output.txt', 'a')
                file_object.write(val+' $')
                file_object.write('\n')
                file_object.close()  
        content=open('output.txt','r').read()


        if len(re.search("(?<=Father's/Hu )(.*)", content).group(1))==0:
            fname=re.search("Father's/Hu [\r\n]+([^\r\n]+)", content).group(1)
        else:    
            fname=re.search("(?<=Father's/Hu)(.*)", content).group(1)
            if len(re.search("(?<=Father's/Hu )(.*)", content).group(1))==0:
                fname=re.search("(?<= Father's / Hu )(.*)", content).group(1)


        if len(re.search("(?<=Station r 1)(.*)", content).group(1)) ==0:
            nat=re.search("Station r 1[\r\n]+([^\r\n]+)", content).group(1)
            nat1=re.search(nat+"[\r\n]+([^\r\n]+)",content).group(1)
            no=nat+nat1
        else:
            nat=re.search("(?<=Station r 1)(.*)", content).group(1)


        if len(re.search(" Date / Year of Birth(.*)", content).group(1))==0:
            fn='$'
        else:    
            fn=re.search(' Date / Year of Birth(.*)',content).group(1)    



        if len(re.search('(?<= Name)(.*)', content).group(1))==0:
            ina='$'
        else:    
            ina=re.search('(?<= Name)(.*)', content).group(1)    


        t=re.search("Accused Name Age[\r\n]+([^\r\n]+)", content).group(1)
        content=content.replace(t,'')
        tre=re.search("Accused Name Age[\r\n]+([^\r\n]+)", content).group(1)

        translator = Translator()
        translated = translator.translate(tre, src='gu', dest='en')
        string = translated.text
        age=re.findall(r'\b\d+\b', string)
        if age:
            ge=age[0]
            sd=re.search('(?<='+ge+' )(.*)', content).group(1)
        else:
            ge='$'
        res = re.findall('([a-zA-Z ]*)\d*.*', string)

        ere=re.search('Occupation[\r\n]+([^\r\n]+)', content).group(1),
        sec=re.search('(?<=Under Section )(.*)', content).group(1)

        ps=re.search('(?<=Police )(\w+\s+\w+\s+\w+\s+\w+)', content).group(1)
        di=re.search('(?<=District )(\w+ )', content).group(1)
        ma=open('output.txt','r').read()

        add=re.search('12[\r\n]+([^\r\n]+)',ma).group(1)
        ad=re.search(add+'[\r\n]+([^\r\n]+)',ma).group(1)
        doe=add+ad
        sc=re.search('(\w+\s+\w+)\s+Act',content).group(1)
        lal=[]
        lanr=[ps,ere[0],di,'indian',fname,ina,res[0],sc]
        translator = Translator()




        for i in range(0,8):
            translated = translator.translate(lanr[i], src='en', dest='gu')
            lal.append(translated.text)

        tdoe = translator.translate(doe, src='gu', dest='en')
        dsd = translator.translate(sd, src='gu', dest='en')
        dict={

            'district': di, 
            'police station':ps, 
            'type_of_info':re.search('(?<=Type of Information: )(.*)', content).group(1),
            'date_of_fir':re.search('Date to (.*)',content).group(1),
            'accused_name':res[0],
            'accused_name_org':lal[6],
            'accused_address':dsd.text,
            'accused_address_org':sd,
            'fir_no':no,
            'state':state,
            'act':sc,
            'act_org':lal[7],
            'date':re.search('(?<=Date to )(..........)',content).group(1),
            'complaint_informan_name':ina,
            'complaint_informan_name_org':lal[5],
            'age':ge,
            'address_of_complaint':tdoe.text,
            'address_org_of_complaint':doe,
            'complaint_informan_father_husband_name':fname,
            'complaint_informan_father_husband_name_org':lal[4],
            'complaint_informan_date_of_birth':fn,
            'nationality':'indian',
            'nationality_org':lal[3],
            'district_name_pdf':di,
            'district_name_pdf_org':lal[2],
            'fir_no_org':no,
            'occupation':ere[0],
            'occupation_org':lal[1],
            'occurence_of_offence_date_from':re.search('(?<=Date from )(..........)', content).group(1), 
            'occurence_of_offence_date_to':re.search('(?<=Date to )(..........)', content).group(1),  
            'occurence_of_offence_time_from':re.search('(?<=Time from )(.....)', content).group(1), 
            'occurence_of_offence_time_to':re.search('(?<=Time to )(.....)', content).group(1), 
            'police_station_org':lal[0], 
            'sections':sec, 
            'sections_org':sec,
            'year':re.search('(?<=Date to )(..........)', content).group(1)[6:], 

        }

        with open('data.json', 'w') as outfile:
            json.dump(dict, outfile,indent=2,ensure_ascii=False)
            
        

        print("ocr process completed")
        cv2.destroyWindow("Test")
        cv2.destroyWindow("Main")



    file=input("Enter the type of pdf ")
    if file=="fir":
        fir()
        exit(0)
    elif file=="jud":
        jud()
        exit(0)
    else:
        print("Invalid type")
        exit(0)        


def karanataka():
      
    sent=""
    ma="aee "

    filename=input("Enter the file name ")
    poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
    pdf_path = filename
    images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    file_names=[]
    for count, img in enumerate(images):
        img_name = f"page_{count+1}.png"
        img.save(img_name, "PNG")
        file_names.append(img_name)
    print(file_names)

    lan=input("enter the language: ")

    if lan=="kan":
        la='kn'
        state='karnataka'
    elif lan=="guj":
        la='gu'
        state="gujrat"
    else:
        la='hi'  
        state="delhi"      


    for file in file_names:
        img=cv2.imread(file)
        text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
        translator = Translator()
        translated = translator.translate(text, src=la, dest='en')
        string = translated.text
        sent=sent+string 


    with open("original.txt",'w') as f:
        print(sent,file=f)
    f.close()


    content = open("original.txt", 'r', encoding="utf8").read()
    NoneType = type(None)
    try:
        
        content=content.replace("According to the accused","accused")
        #content=content.replace("HOWE ADS:","Complainant")
        content=content.replace("Sah","address+")


        com=re.search('(.*)Police',content).group(1)


        c_add=re.search('Police Station (.*)',content).group(1)


        accused_name=re.search('1. (.\w+)',content).group(1)


        fat=re.search('father (\w+\s+\w+)',content).group(1)


        a_add=re.search('address+(.*)',content).group(1)


        age=re.search('Age (\d+\d+)',content).group(1)



        translator = Translator()
        translated1 = translator.translate(com, src='en', dest=la)
        translated2 = translator.translate(c_add, src='en', dest=la)
        translated3 = translator.translate(accused_name, src='en', dest=la)
        translated4 = translator.translate(fat, src='en', dest=la)
        translated5 = translator.translate(a_add, src='en', dest=la)

        dict={

        'complainant':com,
        'complainant_org':translated1.text,
        'complainant_address':c_add,
        'complainant_address_org':translated2.text,
        'accused_name':accused_name,
        'accused_name_org':translated3.text,
        'accused_address':a_add,
        'accused_address_org':translated5.text,
        'accused_age':age,
        'father_husband_name':fat,
        'father_husband_name_org':translated4.text
        }
    except:
        content=content.replace("father was","father")
        content=content.replace("Plaintiffs 8 . "," ")
        content=content.replace("Sah","address")
        content=content.replace("Age:","Age")
        content=content.replace("CD","address")
        content=content.replace("father, ","father")
        ss=re.search('Criminal Case No. (.*)',content).group(1)
        sss="Criminal Case No. "+ss


        com=re.search(sss+'[\r\n]+([^\r\n]+)',content).group(1)


        c_add=re.search('(.*)Police Station',content).group(1)


        accused_name=re.search("(.\w+)'s father",content).group(1)


        fat=re.search("father(.\w+\s+\w+)",content).group(1)


        a_add=re.search('address(.*)',content).group(1)



        age=re.search('(\d+\d+) years',content).group(1)




        translator = Translator()
        translated1 = translator.translate(com, src='en', dest=la)
        translated2 = translator.translate(c_add, src='en', dest=la)
        translated3 = translator.translate(accused_name, src='en', dest=la)
        translated4 = translator.translate(fat, src='en', dest=la)
        translated5 = translator.translate(a_add, src='en', dest=la)

        dict={

        'complainant':com,
        'complainant_org':translated1.text,
        'complainant_address':c_add,
        'complainant_address_org':translated2.text,
        'accused_name':accused_name,
        'accused_name_org':translated3.text,
        'accused_address':a_add,
        'accused_address_org':translated5.text,
        'accused_age':age,
        'father_husband_name':fat,
        'father_husband_name_org':translated4.text
        }


    with open('data.json', 'w') as outfile:
        json.dump(dict, outfile,indent=2,ensure_ascii=False)



    print("ocr process completed")
    cv2.destroyWindow("Test")
    cv2.destroyWindow("Main")


def kerala():

        
    def jud():
        sent=""
        ma="aee "

        filename=input("Enter the file name ")
        poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
        pdf_path = filename
        images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
        file_names=[]
        for count, img in enumerate(images):
            img_name = f"page_{count+1}.png"
            img.save(img_name, "PNG")
            file_names.append(img_name)
        print(file_names)

        lan=input("enter the language: ")

        if lan=="kan":
            la='kn'
            state='karnataka'
        elif lan=="guj":
            la='gu'
            state="gujrat"
        elif lan=="tel":
            la='te'
            state="andrapradesh"    
        elif lan=="mal":
            la='ml'
            state="kerala"  
        else:
            la='hi'  
            state="delhi"      


        for file in file_names:
            img=cv2.imread(file)
            text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
            translator = Translator()
            translated = translator.translate(text, src=la, dest='en')
            string = translated.text
            sent=sent+string 

        with open("output.txt",'w') as f:
            print(sent,file=f)
        f.close()

        ma1 = open('output.txt','r').read()
        ma1=ma1.replace('(Assistant Public Prosecution 389)','ope',1)

        with open('output.txt','w', encoding='utf-8') as f:
            print(ma1,file=f)



        complain=re.search('(?<=Plaintiff)(.*)', ma1).group(1)
        com=re.search('Plaintiff'+complain+'[\r\n]+([^\r\n]+)', ma1).group(1)
        address=re.search('(?<=Inspector )(.*)', ma1).group(1)
        accusedq=re.search('(?<=Accused > )(.\w+\s+\w+\s+\w+)', ma1).group(1)
        aage=re.search('aged(.*)', ma1).group(1)
        ooo=re.search('ope[\r\n]+([^\r\n]+)', ma1).group(1)
        acc_address=re.search(ooo+'[\r\n]+([^\r\n]+)', ma1).group(1)
        anil=re.search(acc_address+'[\r\n]+([^\r\n]+)', ma1).group(1)
        acc_address=acc_address+" "+anil
        
        NoneType = type(None)
        if type(re.search("(?<=Father's Name)(.*)", ma1)) == NoneType:
            father='Not Found'  
            
        else:
            father=re.search("(?<=Father's Name )(.*)", ma1).group(1)
        

        translator = Translator()
        translated1 = translator.translate(com, src='en', dest=la)
        translated2 = translator.translate(address, src='en', dest=la)
        translated3 = translator.translate(accusedq, src='en', dest=la)
        translated4 = translator.translate(acc_address, src='en', dest=la)



        dict={


        'complainant':com,
        'complainant_org':translated1.text,
        'address':address,
        'address_org':translated2.text,
        'accused_name':accusedq,
        'accused_name_org':translated3.text,
        'accused_age':aage,
        'accused_father_name':father,
        'accused_address':acc_address,
        'accused_address_org':translated4.text,


        }


        with open('data.json', 'w') as outfile:
            json.dump(dict, outfile,indent=2,ensure_ascii=False)
            


        print("ocr process completed")
        cv2.destroyWindow("Test")
        cv2.destroyWindow("Main")



    def fir():

        sent=""
        ma="aee "

        filename=input("Enter the file name ")
        poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
        pdf_path = filename
        images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
        file_names=[]
        for count, img in enumerate(images):
            img_name = f"page_{count+1}.png"
            img.save(img_name, "PNG")
            file_names.append(img_name)
        print(file_names)

        lan=input("enter the language: ")

        if lan=="kan":
            la='kn'
            state='karnataka'
        elif lan=="guj":
            la='gu'
            state="gujrat"
        elif lan=="pan":
            la='pa'
            state="punjab"
        elif lan=="ben":
            la='bn'
            state="west bengal"
        elif lan=="mal":
            la='ml'
            state="kerala"        
        else:
            la='hi'  
            state="delhi"      


        for file in file_names:
            img=cv2.imread(file)
            text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
            translator = Translator()
            translated = translator.translate(text, src=la, dest='en')
            string = translated.text
            sent=sent+string 
        with open('output.txt', 'w', encoding='utf-8') as f:
            print(sent, file=f)



        ma1 = open('output.txt','r').read()

        ma1=ma1.replace('(a) Name(@ate) :','complaintname',1)
        ma1=ma1.replace("(b) Father's Name(a moaning name) :",'fatherlname',1)
        ma1=ma1.replace('6. Ththanthanddhasinthannapan (Complainant/Informant):','complaintinfo',1)
        ma1=ma1.replace('(c) Date/Year of Birth:','yob',1)
        ma1=ma1.replace('(d) Nationality(a 10@@10) :','nationalityp',1)
        ma1=ma1.replace('1 |Present Address','adare',1)
        ma1=ma1.replace('(Present Address)','adare12',1)
        ma1=ma1.replace('11th floor (supervision)','accompt',1)
        ma1=ma1.replace('(Year) :','yyou',1)
        ma1=ma1.replace('. District(agiay):','distre',1)
        ma1=ma1.replace('(Pogees Station) :','popas',1)
        ma1=ma1.replace('(First Information Number) :','klkl',1)

        with open('output.txt','w', encoding='utf-8') as f:
            print(ma1,file=f)

        ma1 = open('output.txt','r').read()

        complain=re.search('complaintname (.\w+)', ma1).group(1)
        fname=re.search('fatherlname (.*)', ma1).group(1)
        aaa=re.search('complaintinfo[\r\n]+([^\r\n]+)',ma1).group(1)
        age=re.search('age (.\d+)',aaa).group(1)
        dob=re.search('yob (.*)', ma1).group(1)
        nat=re.search('nationalityp (.*)', ma1).group(1)
        ad1=re.search('adare (.*)', ma1).group(1)
        ad2=re.search('adare12 (.*)', ma1).group(1)
        add=ad1+ad2
        ac=re.search('accompt[\r\n]+([^\r\n]+)',ma1).group(1)
        ac1=re.search(ac+'[\r\n]+([^\r\n]+)',ma1).group(1)
        acc=re.search('(.*)age', ac1).group(1)
        acc_age=re.search('age(.*)', ac1).group(1)
        ac_ad=re.search(ac1+'[\r\n]+([^\r\n]+)',ma1).group(1)
        ac_add=re.search(ac_ad+'[\r\n]+([^\r\n]+)',ma1).group(1)
        ac_add1=re.search(ac_add+'[\r\n]+([^\r\n]+)',ma1).group(1)
        ac_add2=re.search(ac_add1+'[\r\n]+([^\r\n]+)',ma1).group(1)
        acc_add=ac_add+ac_add1+ac_add2
        adg=re.search('yyou (.*)', ma1).group(1)
        di=re.search('distre (.*)', ma1).group(1)
        ps=re.search('popas (.*)', ma1).group(1)
        no=re.search('klkl (.\d+)', ma1).group(1)


        translator = Translator()
        acc_org = translator.translate(acc, src='en', dest=la)
        acc_add_org = translator.translate(acc_add, src='en', dest=la)
        complain_org = translator.translate(complain, src='en', dest=la)
        add_org = translator.translate(add, src='en', dest=la)
        fname_org = translator.translate(fname, src='en', dest=la)
        nat_org = translator.translate(nat, src='en', dest=la)
        di_org = translator.translate(di, src='en', dest=la)


        dict={
            'district': di, 
            'police station':ps, 
            'type_of_info':"written",
            'accused_name':acc,
            'accused_name_org':acc_org.text,
            'accused_address':acc_add,
            'accused_address_org':acc_add_org.text,
            'fir_no':no,
            'state':state,
            'complaint_informan_name':complain,
            'complaint_informan_name_org':complain_org.text,
            'age':age,
            'address_of_complaint':add,
            'address_org_of_complaint':add_org.text,
            'complaint_informan_father_husband_name':fname,
            'complaint_informan_father_husband_name_org':fname_org.text,
            'complaint_informan_date_of_birth':dob,
            'nationality':nat,
            'nationality_org':nat_org.text,
            'district_name_pdf':di,
            'district_name_pdf_org':di_org.text,

        }

        with open('data.json', 'w') as outfile:
            json.dump(dict, outfile,indent=2,ensure_ascii=False)
            

        print("ocr process completed")
        cv2.destroyWindow("Test")
        cv2.destroyWindow("Main")








    file=input("enter the type of pdf ")    
    if file=="fir":
        fir()
        exit(0)
    elif file=="jud":
        jud()
        exit(0)
    else:
        print("Invalid type")
        exit(0)        


def madhyapradesh():

    sent=""
    ma="aee "

    filename=input("enter the file name ")
    poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
    pdf_path = filename
    images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    file_names=[]
    for count, img in enumerate(images):
        img_name = f"page_{count+1}.png"
        img.save(img_name, "PNG")
        file_names.append(img_name)
    print(file_names)

    lan=input("enter the language: ")

    if lan=="kan":
        la='kn'
        state='karnataka'
    elif lan=="guj":
        la='gu'
        state="gujrat"
    elif lan=="tel":
        la='te'
        state="gujrat"  
    elif lan=="hin":
        la='hi'
        state="madhyapradesh"      
    else:
        la='hi'  
        state="delhi"      


    for file in file_names:
        img=cv2.imread(file)
        text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
        translator = Translator()
        translated = translator.translate(text, src=la, dest='en')
        string = translated.text
        sent=sent+string 

    with open("original.txt",'w') as f:
        print(sent,file=f)
    f.close()

    content=open("original.txt",'r').read()


    try:

        c=re.search('CNR No.-(.*)',content).group(1)
        cn=re.search(c+'[\r\n]+([^\r\n]+)',content).group(1)


        cn_ad=re.search(cn+'[\r\n]+([^\r\n]+)',content).group(1)
        cn_add=(cn_ad[:-19])

        resn=re.search('(.*)father',content).group(1)
        resn=resn[:-3]

        res_fat=re.search('father(.\w+.\w+.\w+)',content).group(1)


        res_age=re.search('(?<=age )(\d+\d+)', content).group(1)

        res_add=re.search('Resident-(.*)',content).group(1)
        res_add=res_add[:-20]



        translator = Translator()
        translated1 = translator.translate(cn, src='en', dest=la)
        translated2 = translator.translate(cn_add, src='en', dest=la)
        translated3 = translator.translate(resn, src='en', dest=la)
        translated4 = translator.translate(res_fat, src='en', dest=la)
        translated5 = translator.translate(res_add, src='en', dest=la)
        dict={

        'complainant':cn,
        'complainant_org':translated1.text,
        'complanant_address':cn_add,
        'complainat_address_org':translated2.text,
        'age': res_age,
        'accused':resn,
        'accused_org':translated3.text,
        'accused_address':res_add,
        'accused_address_org':translated5.text,
        'fathers_or_husband_name':res_fat,
        'fathers_or_husband_name_org':translated4.text,



        }

    except:

        c=re.search('Filing No(.*)',content).group(1)
        cn=re.search(c+'[\r\n]+([^\r\n]+)',content).group(1)



        cn_ad=re.search(cn+'[\r\n]+([^\r\n]+)',content).group(1)
        cn_add=(cn_ad[:-19])


        resn=re.search('(.*)husband',content).group(1)
        resn=resn[:-1]


        res_fat=re.search('husband(.\w+.\w+.\w+)',content).group(1)


        res_age=re.search('(?<=age )(\d+\d+)', content).group(1)

        res_add=re.search('Resident-(.*)',content).group(1)
        res_add=res_add[:-20]




        translator = Translator()
        translated1 = translator.translate(cn, src='en', dest=la)
        translated2 = translator.translate(cn_add, src='en', dest=la)
        translated3 = translator.translate(resn, src='en', dest=la)
        translated4 = translator.translate(res_fat, src='en', dest=la)
        translated5 = translator.translate(res_add, src='en', dest=la)
        dict={

        'complainant':cn,
        'complainant_org':translated1.text,
        'complanant_address':cn_add,
        'complainat_address_org':translated2.text,
        'age': res_age,
        'accused':resn,
        'accused_org':translated3.text,
        'accused_address':res_add,
        'accused_address_org':translated5.text,
        'fathers_or_husband_name':res_fat,
        'fathers_or_husband_name_org':translated4.text,
        }


    with open('data.json', 'w') as outfile:
        json.dump(dict, outfile,indent=2,ensure_ascii=False)
        


    print("ocr process completed")
    cv2.destroyWindow("Test")
    cv2.destroyWindow("Main")


def maharashtra():
      
    sent=""
    ma="aee "

    filename=input("enter the file name ")
    poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
    pdf_path = filename
    images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    file_names=[]
    for count, img in enumerate(images):
        img_name = f"page_{count+1}.png"
        img.save(img_name, "PNG")
        file_names.append(img_name)
    print(file_names)

    lan=input("enter the language: ")

    if lan=="kan":
        la='kn'
        state='karnataka'
    elif lan=="guj":
        la='gu'
        state="gujrat"
    elif lan=="tel":
        la='te'
        state="gujrat"  
    elif lan=="hin":
        la='hi'
        state="madhyapradesh"      
    else:
        la='hi'  
        state="delhi"        


    for file in file_names:
        img=cv2.imread(file)
        text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
        translator = Translator()
        translated = translator.translate(text, src=la, dest='en')
        string = translated.text
        sent=sent+string 


    with open("original.txt",'w') as f:
        print(sent,file=f)
    f.close()

    NoneType=type(None)
    content = open("original.txt", 'r', encoding="utf8").read()
    try:
        
        ss=re.search('Regular Criminal Khatla No.(.*)',content).group(1)
        sss="Regular Criminal Khatla No."+ss
        com=re.search(sss+'[\r\n]+([^\r\n]+)',content).group(1)

        c_add1=re.search(com+'[\r\n]+([^\r\n]+)',content).group(1)
        c_add2=re.search(c_add1+'[\r\n]+([^\r\n]+)',content).group(1)
        c_add3=re.search(c_add2+'[\r\n]+([^\r\n]+)',content).group(1)
        c_add=c_add1+c_add2+c_add3
        c_add=c_add[:-15]


        acc=[]
        accused_name1=re.search("against[\r\n]+([^\r\n]+)",content).group(1)
        acc.append(accused_name1[2:])
        accused_name2=re.search("2. (.*)",content).group(1)
        acc.append(accused_name2)
        accused_name3=re.search("3. (.*)",content).group(1)
        acc.append(accused_name3)


        rr=re.search('All accused(.*)',content).group(1)
        r='All accused'+rr
        a_add=re.search(r+"[\r\n]+([^\r\n]+)",content).group(1)
        a_add=r+a_add[:-12]

        a_age=[]
        accused_age_1=re.search(accused_name1+"[\r\n]+([^\r\n]+)",content).group(1)
        accused_age_1=accused_age_1[4:7]
        a_age.append(accused_age_1)

        accused_age_2=re.search(accused_name2+"[\r\n]+([^\r\n]+)",content).group(1)
        accused_age_2=accused_age_2[4:7]
        a_age.append(accused_age_2)

        accused_age_3=re.search(accused_name3+"[\r\n]+([^\r\n]+)",content).group(1)
        accused_age_3=accused_age_3[4:7]
        a_age.append(accused_age_3)

        if type(re.search('father (\w+\w+)',content)) == NoneType:
            fat="not found"
            
        else:
            fat=re.search('father (\w+\w+)',content).group(1)

        translator = Translator()
        translated1 = translator.translate(com, src='en', dest=la)
        translated2 = translator.translate(c_add, src='en', dest=la)
        cac=[]
        for ele in acc:
            translated3 = translator.translate(ele, src='en', dest=la)
            cac.append(translated3.text)
        translated4 = translator.translate(a_add, src='en', dest=la)
        translated5 = translator.translate(fat, src='en', dest=la)


        dict={

        'complainant':com,
        'complainant_org':translated1.text,
        'complainant_address':c_add,
        'complainant_address_org':translated2.text,
        'accused_name':acc,
        'accused_name_org':cac,
        'accused_address':a_add,
        'accused_address_org':translated4.text,
        'accused_age':a_age,
        'father_husband_name':fat,
        'father_husband_name_org':translated5.text
        }




    #############################################################
    ###############-------------mh2---------#####################


    except:
        try:
            com=re.search('Name and address - (.*)',content).group(1)

            c_add=re.search(com+'[\r\n]+([^\r\n]+)',content).group(1)

            accused_name=re.search('Name and address of the accused - (.*)',content).group(1)

            a_add1=re.search(accused_name+'[\r\n]+([^\r\n]+)',content).group(1)
            a_add2=re.search(a_add1+'[\r\n]+([^\r\n]+)',content).group(1)
            a_add=a_add2
            a_age=re.search('Age - (\d\d)',content).group(1)

            if type(re.search('father (\w+\w+)',content)) == NoneType:
                fat="not found"
            
            else:
                fat=re.search('father (\w+\w+)',content).group(1)

            translator = Translator()
            translated1 = translator.translate(com, src='en', dest=la)
            translated2 = translator.translate(c_add, src='en', dest=la)
            translated3 = translator.translate(accused_name, src='en', dest=la)
            translated4 = translator.translate(a_add, src='en', dest=la)
            translated5 = translator.translate(fat, src='en', dest=la)


            dict={

            'complainant':com,
            'complainant_org':translated1.text,
            'complainant_address':c_add,
            'complainant_address_org':translated2.text,
            'accused_name':accused_name,
            'accused_name_org':translated3.text,
            'accused_address':a_add,
            'accused_address_org':translated4.text,
            'accused_age':a_age,
            'father_husband_name':fat,
            'father_husband_name_org':translated5.text
            }



    #####################--------------mh3-----------#################
        except:
            try:
                content=content.replace("(Police","Police")
                content=content.replace("Se)","Se")
                com1=re.search('CNR No. (.*)',content).group(1)
                com1="CNR No. "+com1
                co=re.search(com1+'[\r\n]+([^\r\n]+)',content).group(1)
                com=co[0:-8]

                c_add1=re.search(co+'[\r\n]+([^\r\n]+)',content).group(1)
                c_add2=re.search(c_add1+'[\r\n]+([^\r\n]+)',content).group(1)
                c_add=c_add1+c_add2
                c_add=c_add[0:-13]


                accused_name=re.search('- against -[\r\n]+([^\r\n]+)',content).group(1)


                prof=re.search('Profession - (.*)',content).group(1)
                pro="Profession - "+prof
                a_add=re.search(pro+'[\r\n]+([^\r\n]+)',content).group(1)
                a_add=a_add[:-11]

                a_age=re.search('Age - (\d\d)',content).group(1)

                if type(re.search('father (\w+\w+)',content)) == NoneType:
                    fat="not found"
            
                else:
                    fat=re.search('father (\w+\w+)',content).group(1)

                translator = Translator()
                translated1 = translator.translate(com, src='en', dest=la)
                translated2 = translator.translate(c_add, src='en', dest=la)
                translated3 = translator.translate(accused_name, src='en', dest=la)
                translated4 = translator.translate(a_add, src='en', dest=la)
                translated5 = translator.translate(fat, src='en', dest=la)


                dict={

                'complainant':com,
                'complainant_org':translated1.text,
                'complainant_address':c_add,
                'complainant_address_org':translated2.text,
                'accused_name':accused_name,
                'accused_name_org':translated3.text,
                'accused_address':a_add,
                'accused_address_org':translated4.text,
                'accused_age':a_age,
                'father_husband_name':fat,
                'father_husband_name_org':translated5.text
                }


    ############################---------------m4-------------########################
    ###########--------to be checked---------################
            except:
                #content=content.replace("ol","qr")
                com1=re.search('CNR No. (.*)',content).group(1)
                


                co=re.search('ol[\r\n]+([^\r\n]+)',content).group(1)
                com=co[:-2]


                c_add1=re.search(co+'[\r\n]+([^\r\n]+)',content).group(1)
                c_add2=re.search(c_add1+'[\r\n]+([^\r\n]+)',content).group(1)
                c_add3=re.search(c_add2+'[\r\n]+([^\r\n]+)',content).group(1)
                c_add=c_add1+c_add2+c_add3
                c_add=c_add[:-17]


                acc=[]
                accused_name=re.search('- against -[\r\n]+([^\r\n]+)',content).group(1)
                accused=accused_name[2:]
                acc.append(accused)
                
                accused_name2=re.search('2. (.*)',content).group(1)
                acc.append(accused_name2)



                acc_add=[]
                a_ad=re.search(accused+'[\r\n]+([^\r\n]+)',content).group(1)
                a_add1=re.search(a_ad+'[\r\n]+([^\r\n]+)',content).group(1)
                a_add2=re.search(a_add1+'[\r\n]+([^\r\n]+)',content).group(1)
                a_add3=re.search(a_add2+'[\r\n]+([^\r\n]+)',content).group(1)
                a_add10=a_add1+a_add2+a_add3
                acc_add.append(a_add10)

                a_ad4=re.search(accused_name2+'[\r\n]+([^\r\n]+)',content).group(1)
                a_add5=re.search(a_ad4+'[\r\n]+([^\r\n]+)',content).group(1)
                a_add6=re.search(a_add1+'[\r\n]+([^\r\n]+)',content).group(1)
                a_add7=re.search(a_add2+'[\r\n]+([^\r\n]+)',content).group(1)
                a_add11=a_add5+a_add6+a_add7
                acc_add.append(a_add11)


                a_age=[]
                a_ag=re.search(accused+'[\r\n]+([^\r\n]+)',content).group(1)
                a_age1=re.search('Age - (\d\d)',a_ag).group(1)
                a_age.append(a_age1)

                a_agg=re.search(accused_name2+'[\r\n]+([^\r\n]+)',content).group(1)
                a_age2=re.search('Age - (\d\d)',a_agg).group(1)
                a_age.append(a_age2)


                if type(re.search('father (\w+\w+)',content)) == NoneType:
                    fat="not found"
            
                else:
                    fat=re.search('father (\w+\w+)',content).group(1)

                translator = Translator()
                translated1 = translator.translate(com, src='en', dest=la)
                translated2 = translator.translate(c_add, src='en', dest=la)
                ac=[]
                for ele in acc:
                    translated3 = translator.translate(ele, src='en', dest=la)
                    ac.append(translated3.text)
                ad=[]    
                for ele in acc_add:
                    translated4 = translator.translate(ele, src='en', dest=la)
                    ad.append(translated4.text)

                translated5 = translator.translate(fat, src='en', dest=la)


                dict={

                'complainant':com,
                'complainant_org':translated1.text,
                'complainant_address':c_add,
                'complainant_address_org':translated2.text,
                'accused_name':acc,
                'accused_name_org':ac,
                'accused_address':acc_add,
                'accused_address_org':ad,
                'accused_age':a_age,
                'father_husband_name':fat,
                'father_husband_name_org':translated5.text
                }

    with open('data.json', 'w') as outfile:
        json.dump(dict, outfile,indent=2,ensure_ascii=False)



    print("ocr process completed")
    cv2.destroyWindow("Test")
    cv2.destroyWindow("Main")


def punjab():

    sent=""

    filename=input("enter the file name ")
    poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
    pdf_path = filename
    ima1ges = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    file_names=[]
    for count, img in enumerate(ima1ges):
        img_name = f"page_{count+1}.png"
        img.save(img_name, "PNG")
        file_names.append(img_name)
    print(file_names)

    lan=input("enter the language: ")

    if lan=="kan":
        la='kn'
        state='karnataka'
    elif lan=="guj":
        la='gu'
        state="gujrat"
    elif lan=="pan":
        la='pa'
        state="punjab"
    else:
        la='hi'  
        state="delhi"      


    for file in file_names:
        img=cv2.imread(file)
        text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
        translator = Translator()
        translated = translator.translate(text, src=la, dest='en')
        string = translated.text
        sent=sent+string 

    lin=re.search('(?<=Under Section )(.* )', sent).group(1)

    with open('output1.txt', 'w', encoding='utf-8') as f:
        print("Under Section "+lin,file=f)
        print(sent, file=f)


    ma1 = open('output1.txt','r').read()

    try:  
        ma1=ma1.replace('(Station)','PStation',1)
        ma1=ma1.replace('(first);','Dist',1)
        ma1=ma1.replace('(a) Name','nna',1)
        ma1=ma1.replace('(Serial No) (Name ) (Surname) (Name of Relative) (Address)','ask',1)

        with open('output1.txt','w', encoding='utf-8') as f:
            print(ma1,file=f)



        complain=re.search('(?<=nna)(.*)', ma1).group(1)
        complain=re.sub(r'\s*\([^)]+\)', '', complain)
        address=re.search('(?<=1 Present Address )(.*)', ma1).group(1)
        accusedq=re.search('ask[\r\n]+([^\r\n]+)', ma1).group(1)
        accused=re.search('1 (\w+\s+\w+)', accusedq).group(1)
        accused_father=re.search('(\w+\s+\w+) 1. ', accusedq).group(1)
        acc_address=re.search(' 1. (.*)', accusedq).group(1)
        anil=re.search(acc_address+'[\r\n]+([^\r\n]+)', ma1).group(1)
        acc_address=acc_address+" "+anil
        if len(re.search("(?<=Father's/Mother's/Husband's Name)(.*)", ma1).group(1))!=0:
            father=re.search("(?<=Father's/Mother's/Husband's Name )(.*)", ma1).group(1)
        else:
            father='$'
        

        translator = Translator()
        tran1=translator.translate(complain, src='en', dest=la)
        tran2=translator.translate(address, src='en', dest=la)
        tran3=translator.translate(accused, src='en', dest=la)
        tran4=translator.translate(accused_father, src='en', dest=la)
        tran5=translator.translate(acc_address, src='en', dest=la)

        dict={


        'complainant':complain,
        'complainant_org':tran1.text,
        'complaint_father_name':father,
        'address':address,
        'address_org':tran2.text,
        'accused_name':accused,
        'accused_name_org':tran3.text,
        'accused_father_name':accused_father,
        'accused_father_name_org':tran4.text,
        'accused_address':acc_address,
        'accused_address_org':tran5.text,


        }
    except:
        ma1 = open('output1.txt','r').read()
        ma1=ma1.replace('(Station)','PStation',1)
        ma1=ma1.replace('(first);','Dist',1)
        ma1=ma1.replace('(a) Name','nna',1)
        ma1=ma1.replace('(Serial No) (Name ) (Surname) (Name of Relative)','ask',1)

        with open('output1.txt','w', encoding='utf-8') as f:
            print(ma1,file=f)


        #ps=re.search('(?<=PStation: )(\w+\s+\w+)', ma1).group(1)
        #dis=re.search('(?<=Dist )(\w+\s+\w+)', ma1).group(1)
        complain=re.search('(?<=nna)(.*)', ma1).group(1)
        complain=re.sub(r'\s*\([^)]+\)', '', complain)
        address=re.search('(?<=1 Present Address )(.*)', ma1).group(1)
        accusedq=re.search('ask[\r\n]+([^\r\n]+)', ma1).group(1)
        if re.search("1 '(\w+)", accusedq).group(1)!='Unknown':
            accused=re.search("1 '(\w+)", accusedq).group(1)
            accused_father=re.search('(\w+\s+\w+) 1. ', accusedq).group(1)
            acc_address=re.search(' 1 (.*)', accusedq).group(1)
            anil=re.search(acc_address+'[\r\n]+([^\r\n]+)', ma1).group(1)
            acc_address=acc_address+" "+anil

        
            

        else:
            accused='Unknown'
            acc_address="Not Found"
            accused_father="Not Found"

        if len(re.search("(?<=Father's Name:)(.*)", ma1).group(1))!=0:
                father=re.search("(?<=Father's Name:)(.*)", ma1).group(1)
        else:
                father='$'    
        


        translator = Translator()
        tran1=translator.translate(complain, src='en', dest=la)
        tran2=translator.translate(address, src='en', dest=la)
        tran3=translator.translate(accused, src='en', dest=la)
        tran4=translator.translate(accused_father, src='en', dest=la)
        tran5=translator.translate(acc_address, src='en', dest=la)

        dict={


        'complainant':complain,
        'complainant_org':tran1.text,
        'complaint_father_name':father,
        'address':address,
        'address_org':tran2.text,
        'accused_name':accused,
        'accused_name_org':tran3.text,
        'accused_father_name':accused_father,
        'accused_father_name_org':tran4.text,
        'accused_address':acc_address,
        'accused_address_org':tran5.text,


        }


    with open('data.json', 'w') as outfile:
        json.dump(dict, outfile,indent=2,ensure_ascii=False)
        
    

    print("ocr process completed")
    cv2.destroyWindow("Test")
    cv2.destroyWindow("main")


def westbengal():    

    sent=""
    ma="aee "

    filename=input("enter the file name ")
    poppler_path = r'/opt/homebrew/Cellar/poppler/22.06.0/bin'
    pdf_path = filename
    images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    file_names=[]
    for count, img in enumerate(images):
        img_name = f"page_{count+1}.png"
        img.save(img_name, "PNG")
        file_names.append(img_name)
    print(file_names)

    lan=input("enter the language: ")

    if lan=="kan":
        la='kn'
        state='karnataka'
    elif lan=="guj":
        la='gu'
        state="gujrat"
    elif lan=="tel":
        la='te'
        state="andrapradesh"    
    elif lan=="mal":
        la='ml'
        state="kerala"  
    elif lan=="ben":
        la='bn'
        state="west bengal" 
    else:
        la='hi'  
        state="delhi"   


    for file in file_names:
        img=cv2.imread(file)
        text=pytesseract.image_to_string(Image.open(file), lang='eng+'+lan)
        translator = Translator()
        translated = translator.translate(text, src=la, dest='en')
        string = translated.text
        sent=sent+string 


    with open("original.txt",'w') as f:
        print(sent,file=f)
    f.close()


    content=open("original.txt",'r').read()

    NoneType = type(None)

    try:
        cvn=re.search('Case No-(.*)',content).group(1)
        cn1=re.search('1. (\w+\s+\w+)',content).group(1)
        cn2=re.search('2. (\w+\s+\w+)',content).group(1)
        
        if type(re.search('age (\d+\d+)',content)) == NoneType:
            age="not found"
            
        else:
            age=re.search('age (\d+\d+)',content).group(1)

        if type(re.search('address (.*)',content)) == NoneType:
            c_add="not found"
            
        else:
            c_add=re.search('address (.*)',content).group(1)
            

        resn=re.search('vs[\r\n]+([^\r\n]+)',content).group(1)


        if type(re.search("father's name (\w+\w+)",content)) == NoneType:
            fat="not found"
            
        else:
            fat=re.search("father's name (\w+\w+)",content).group(1)
            
        if type(re.search('a address (.*)',content)) == NoneType:
                a_add="not found"
            
        else:
                a_add=re.search('a address (.*)',content).group(1)
                


        translator = Translator()
        translated1 = translator.translate(cn1, src='en', dest=la)
        translated2 = translator.translate(cn2, src='en', dest=la)
        translated3 = translator.translate(resn, src='en', dest=la)
        translated6 = translator.translate(a_add, src='en', dest=la)
        translated5 = translator.translate(fat, src='en', dest=la)
        translated4 = translator.translate(c_add, src='en', dest=la)



        com=[cn1,cn2]
        com_org=[translated1.text,translated2.text]

        dict={

        'complainant':com,
        'complainant_org':com_org,
        'complainant_address':c_add,
        'complainant_address_org':translated4.text,
        'accused_name':resn,
        'accused_name_org':translated3.text,
        'accused_address':a_add,
        'accused_address_org':translated6.text,
        'accused_age':age,
        'father_husband_name':fat,
        'father_husband_name_org':translated5.text
        }


    except:
        try:

            c=re.search('Reg:(.*)',content).group(1)
            cn=re.search(c+'[\r\n]+([^\r\n]+)',content).group(1)


            resn=re.search('vs[\r\n]+([^\r\n]+)',content).group(1)

            if type(re.search('address (.*)',content)) == NoneType:
                c_add="not found"
            
            else:
                c_add=re.search('address (.*)',content).group(1)
                

            if type(re.search("father's name (\w+\w+)",content)) == NoneType:
                fat="not found"
            
            else:
                fat=re.search("father's name (\w+\w+)",content).group(1)

    

            if type(re.search('age (\d+\d+)',content)) == NoneType:
                age="not found"
            
            else:
                age=re.search('age (\d+\d+)',content).group(1)

            if type(re.search('a address (.*)',content)) == NoneType:
                a_add="not found"
            
            else:
                a_add=re.search('a address (.*)',content).group(1)





            translator = Translator()
            translated1 = translator.translate(cn, src='en', dest=la)
            translated3 = translator.translate(resn, src='en', dest=la)
            translated6 = translator.translate(a_add, src='en', dest=la)
            translated4 = translator.translate(fat, src='en', dest=la)
            translated5 = translator.translate(c_add, src='en', dest=la)
            dict={

            'complainant':cn,
            'complainant_org':translated1.text,
            'complainant_address':c_add,
            'complainant_address_org':translated5.text,
            'accused_name':resn,
            'accused_org':translated3.text,
            'accused_address':a_add,
            'accused_address_org':translated6.text,
            'accused_age':age,
            'father_husband_name':fat,
            'father_husband_name_org':translated4.text
            }

        except:

            content=content.repl('1)-','111',1)
            content=content.repl('2)-','222',1)
            content=content.repl('3)-','333',1)
            with open("original.txt",'w') as f:
                print(sent,file=f)
            content=open('original.txt','r').read()    

            acc=[]
            acc.append(re.search('111 (.*)',content).group(1))
            acc.append(re.search('222 (.*)',content).group(1))
            acc.append(re.search('333 (.*)',content).group(1))

            
            cn1=re.search('dated(.*)',content).group(1)
            content=content.replace("dated "+cn1,"complainant")
            cn=re.search('complainant[\r\n]+([^\r\n]+)',content).group(1)

            if type(re.search('address (.*)',content)) == NoneType:
                c_add="not found"
            
            else:
                c_add=re.search('address (.*)',content).group(1)


            if type(re.search('age (\d+\d+)',content)) == NoneType:
                age="not found"
            
            else:
                age=re.search('age (\d+\d+)',content).group(1)


            if type(re.search('a address (.*)',content)) == NoneType:
                a_add="not found"
            
            else:
                a_add=re.search('a address (.*)',content).group(1)


            if type(re.search("father's name (\w+\w+)",content)) == NoneType:
                fat="not found"
            
            else:
                fat=re.search("father's name (\w+\w+)",content).group(1)
                
            translator = Translator()
            translated1 = translator.translate(cn, src='en', dest=la)
            ll=[]
            for ele in acc:
                translated5 = translator.translate(ele, src='en', dest=la)
                ll.append(translated5.text)
            translated6 = translator.translate(c_add, src='en', dest=la)
            translated7 = translator.translate(a_add, src='en', dest=la)
            translated8 = translator.translate(fat, src='en', dest=la)
            
            
            acc_org=[translated3.text,translated4.text,translated5.text]
            
            dict={

            'complainant_name':cn,
            'complainant_name_org':translated1.text,
            'complainant_address':c_add,
            'complainant_address_org':translated6.text,
            'accused':acc,
            'accused_org':ll,
            'accused_address':a_add,
            'accused_address_org':translated7.text,
            'accused_age':age,
            'father_husband_name':fat,
            'father_husband_name_org':translated8.text
            }

    with open('data.json', 'w') as outfile:
        json.dump(dict, outfile,indent=2,ensure_ascii=False)



    print("ocr process completed")
    cv2.destroyWindow("Test")
    cv2.destroyWindow("Main")



inp=input("Enter the state: ")
if inp=="ka":
    karanataka()
elif inp=="ap":
    andrapradesh()
elif inp=="wb":
    westbengal()
elif inp=="pb":
    punjab()
elif inp=="mh":
    maharashtra()
elif inp=="mp":
    madhyapradesh()
elif inp=="gu":
   gujrat()
elif inp=="kl":
    kerala()
else:
    print("invalid state")    


# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

"""
String converter for English/Russian WEH001602 CGRAM tabe
Made by Mikalai Kavalchuk 2019    
"""

import sys

dict = {
        u'\u0410':0x41, #А
        u'\u0411':0xA0, #Б
        u'\u0412':0x42, #В
        u'\u0413':0xA1, #Г
        u'\u0414':0xE0, #Д
        u'\u0415':0x45, #Е
        u'\u0416':0xA3, #Ж
        u'\u0417':0xA4, #З
        u'\u0418':0xA5, #И
        u'\u0419':0xA6, #Й
        u'\u041A':0x4B, #К
        u'\u041B':0xA7, #Л
        u'\u041C':0x4D, #М
        u'\u041D':0x48, #Н
        u'\u041E':0x4F, #О
        u'\u041F':0xA8, #П
        u'\u0420':0x50, #Р
        u'\u0421':0x43, #С
        u'\u0422':0x54, #Т
        u'\u0423':0xA9, #У
        u'\u0424':0xAA, #Ф
        u'\u0425':0x58, #Х
        u'\u0426':0xE1, #Ц
        u'\u0427':0xAB, #Ч
        u'\u0428':0xAC, #Ш
        u'\u0429':0xE2, #Щ
        u'\u042A':0xAD, #Ъ
        u'\u042B':0xAE, #Ы
        u'\u042C':0xC4, #Ь
        u'\u042D':0xAF, #Э
        u'\u042E':0xB0, #Ю
        u'\u042F':0xB1, #Я 
        
        u'\u0430':0x61, #а
        u'\u0431':0xB2, #б
        u'\u0432':0xB3, #в
        u'\u0433':0xB4, #г
        u'\u0434':0xE3, #д
        u'\u0435':0x65, #е        
        u'\u0436':0xB6, #ж
        u'\u0437':0xB7, #з
        u'\u0438':0xB8, #и
        u'\u0439':0xB9, #й
        u'\u043A':0xBA, #к
        u'\u043B':0xBB, #л
        u'\u043C':0xBC, #м
        u'\u043D':0xBD, #н
        u'\u043E':0x6F, #о
        u'\u043F':0xBE, #п
        u'\u0440':0x70, #р
        u'\u0441':0x63, #с
        u'\u0442':0xBF, #т
        u'\u0443':0x79, #у
        u'\u0444':0xE4, #ф
        u'\u0445':0x87, #х
        u'\u0446':0xE5, #ц
        u'\u0447':0xC0, #ч
        u'\u0448':0xC1, #ш
        u'\u0449':0xE6, #щ
        u'\u044A':0xC2, #ъ
        u'\u044B':0xC3, #ы
        u'\u044C':0xC4, #ь
        u'\u044D':0xC5, #э
        u'\u044E':0xC6, #ю
        u'\u044F':0xC7, #я
        
        u'\u0401':0xA2, #Ё
        u'\u0451':0xB5, #ё      
        }


def convert(input_string):
    """Converting string characters to right WEH001602 CGRAM table codes """
    array = []
    
    if sys.version_info[0] < 3:
        input_string = input_string.decode('utf-8')

    for char in input_string:
        if char in dict.keys():
            array.append(dict[char])
        else:
            array.append(ord(char))  
                
    return "".join(chr(n) for n in array)
    

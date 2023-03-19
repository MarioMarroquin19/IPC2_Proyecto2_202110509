from msilib.schema import Component, Font

BACKGROUND = "#121212"
BACKGROUND1 = "#FFFFFF"
FONT = ("Arial", 12)
COMPONENT = "#363636"
TEXT = "#84C9FB"
TEXT1 = "#121212"
Font_Titulos = ("Arial", 24, "bold")
Text_Titulos = "#FFFFFF"
Font_Sub_Titulos = ("Arial", 16, "bold")
Text_sub_Titulos = "#FFFFFF"
FONT2 = ("Arial", 12, "bold")


STYLE = {
    "font": FONT,
    "bg": COMPONENT,
    "fg": TEXT}

STYLE1 = {
    "font": FONT,
    "bg": BACKGROUND,
    "fg": TEXT}

STYLE2 = {
    "font": Font_Titulos,
    "bg": BACKGROUND,
    "fg": Text_Titulos    
}

STYLE3 = {
    "font": Font_Sub_Titulos,
    "bg": BACKGROUND,
    "fg": TEXT    
}

STYLE4 = {
    "font": FONT2,
    "bg": BACKGROUND,
    "fg": Text_sub_Titulos
}

STYLE5 = {
    "font": FONT,
    "bg": BACKGROUND1,
    "fg": TEXT1
}
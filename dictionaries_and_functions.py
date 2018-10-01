english_to_vietnamese = {"one": "mot","two":"hai","three":"ba", "four":"bon","five":"nam","six":"sau","seven":"bay","eight":"tam","nine":"chin","ten":"muoi"
}

def translate(eng_word):
    if eng_word in english_to_vietnamese:
        return english_to_vietnamese[eng_word]
    else:
        return "Oh no! That word doesn't exist in Vietnamese!"
    

one = translate("one")
print one

twenty = translate("twenty")
print twenty
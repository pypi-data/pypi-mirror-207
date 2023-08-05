import pyautogui
import time

def move_mouse(x, y, z=0.5):
    print(f"Moving mouse to ({x}, {y}) in {z} seconds")
    pyautogui.moveTo(x, y, z)

def move_to_image(image_file, confidence=0.9, grayscale=True, offset_x=0, offset_y=0, region=None, verbose=False):
    if verbose==True:
        print(f"Moving to image: {image_file} with {confidence} confidence")
    try:
        x, y = pyautogui.locateCenterOnScreen(image_file, confidence=confidence, grayscale=grayscale, region=region)
    except TypeError as e:
        # print(e)
        # The default error message is not very helpful
        # raise ValueError("Image not found" + "\n" + str(e))
        print("Image not found" + "\n" + str(e))
    try:
        x, y = (x + offset_x), (y + offset_y)
        pyautogui.moveTo(x, y)
        print(f"Mouse moved to ({x}, {y})")
        return x, y
    except UnboundLocalError as e:
        print(e)
    
    return None

def victory_dance():
    # Get current mouse position
    x, y = pyautogui.position()
    i = 0
    while i < 2:
        # Move mouse 100 pixels to the right
        move_mouse(x + 50, y)
        # Move mouse 100 pixels to the left
        move_mouse(x - 50, y)
        i += 1
    # Move mouse back to original position
    move_mouse(x, y)
    exit()

def paste(verbose=False):
    if verbose==True:
        print('Sending ctrl+v command')
    pyautogui.hotkey('ctrl', 'v')

def paste2(text, verbose=False):
    pyautogui.typewrite(text)

def paste3(verbose=False):
    import pyperclip
    pyperclip.paste()

def copy(verbose=False):
    if verbose==True:
        print('Sending ctrl+c command')
    pyautogui.hotkey('ctrl', 'c')

def copy2(text):
    import pyperclip
    pyperclip.copy(text)

def filter_message(message):
    naughty_words = ['sex', 'boob', 'boobs', 'fucking', 'fuck', 'blood', 'sultry', 'arrested', 'jinping', 'chinese president', 'xi', 'terry richardson', 'intimate', 'sucking', 'bathing', 'breast', 'negro', '69', 'afghani', 'mccurry', 'explicit', 'seduction', 'gore', 'in jail', 'tied up', 'handcuffed', 'afghani', 'negra']
    naughty_words2 = ['Ass', 'Bitch', 'Motherfucker', 'Cunt', 'Shit', 'Slut', 'Pussy', 'Dick', 'Dildo', 'Virgin', 'Anal', 'Peepee', 'Lube', 'Rimming', 'Oral', 'Fuckers', 'Masturbate']
    naughty_words3 = ['Blood', 'Bloodbath', 'Crucifixion', 'Bloody', 'Flesh', 'Bruises', 'Car crash', 'Corpse', 'Crucified', 'Cutting', 'Decapitate', 'Infested', 'Gruesome', 'Kill', 'Infected', 'Sadist', 'Slaughter', 'Teratoma', 'Tryphophobia', 'Wound', 'Cronenberg', 'Khorne', 'Cannibal', 'Cannibalism', 'Visceral', 'Guts', 'Bloodshot', 'Gory', 'Killing', 'Surgery', 'Vivisection', 'Massacre', 'Hemoglobin', 'Suicide', 'Female Body Parts', 'ahegao', 'pinup', 'ballgag', 'Playboy', 'Bimbo', 'pleasure', 'bodily fluids', 'pleasures', 'boudoir', 'rule34', 'brothel', 'seducing', 'dominatrix', 'seductive', 'erotic seductive', 'fuck', 'sensual', 'Hardcore', 'sexy', 'Hentai', 'Shag', 'horny', 'shibari', 'incest', 'Smut', 'jav', 'succubus', 'Jerk off king at pic', 'thot', 'kinbaku', 'transparent', 'legs spread', 'twerk', 'making love', 'voluptuous', 'naughty', 'wincest', 'orgy', 'Sultry', 'XXX', 'Bondage', 'Bdsm', 'Dog collar', 'Slavegirl', 'Transparent and Translucent', 'Arse', 'Labia', 'Ass', 'Mammaries', 'Badonkers', 'Minge', 'Big Ass', 'Mommy Milker', 'Booba', 'Nipple', 'Booty', 'Oppai', 'Bosom', 'Organs', 'Breasts', 'Ovaries', 'Busty', 'Penis', 'Clunge', 'Phallus', 'Crotch', 'sexy female', 'Dick', 'Skimpy', 'Girth', 'Thick', 'Honkers', 'Vagina', 'Hooters', 'Veiny', 'Knob', 'no clothes', 'au naturale', 'no shirt', 'bare chest', 'nude', 'barely dressed', 'bra', 'risqué', 'clear', 'scantily', 'clad', 'cleavage', 'stripped', 'full frontal unclothed', 'invisible clothes', 'wearing nothing', 'lingerie with no shirt', 'naked', 'without clothes on', 'negligee', 'zero clothes', 'Taboo', 'Fascist', 'Nazi', 'Prophet Mohammed', 'Slave', 'Coon', 'Honkey', 'Drugs', 'Cocaine', 'Heroin', 'Meth', 'Crack', 'Torture', 'Disturbing', 'Farts', 'Fart', 'Poop', 'Warts', 'Shit', 'Brown pudding', 'Bunghole', 'Vomit', 'Voluptuous', 'Seductive', 'Sperm', 'Hot', 'Sexy', 'Sensored', 'Censored', 'Silenced', 'Deepfake', 'Inappropriate', 'Pus', 'Waifu', 'mp5', 'Succubus', '1488', 'Surgery']
    naughty_words.extend(naughty_words2)
    naughty_words.extend(naughty_words3)
    
    # Remove any duplicates
    naughty_words = list(set(naughty_words))
    
    import re

    # Create a regex pattern to match all naughty words in a case-insensitive manner
    pattern = r'\b(' + '|'.join(f'{re.escape(word)}' for word in naughty_words) + r')\b'
    
    # Replace all occurrences of naughty words with an empty string
    filtered_message = re.sub(pattern, '', message, flags=re.IGNORECASE)

    return filtered_message

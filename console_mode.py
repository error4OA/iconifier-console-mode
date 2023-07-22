import argparse
import json
import random
import webbrowser
import requests
import emoji
import textwrap
import clipboard
import os

lookalikes = requests.get("https://gist.githubusercontent.com/StevenACoffman/a5f6f682d94e38ed804182dc2693ed4b/raw/fa2ed09ab6f9b515ab430692b588540748412f5f/some_homoglyphs.json").json()
leet_dict = {
    'A': '4', 'a': '4', 'B': '8', 'b': '8', 'E': '3', 'e': '3', 'G': '6', 'g': '6', 'I': '1', 'i': '1',
    'O': '0', 'o': '0', 'S': '5', 's': '5', 'T': '7', 't': '7', 'Z': '2', 'z': '2',
    'C': '(', 'c': '(', 'D': '|)', 'd': '|)', 'F': '|=', 'f': '|=', 'H': '#', 'h': '#', 'K': '|<', 'k': '|<',
    'L': '1', 'l': '1', 'M': '|\\/|', 'm': '|\\/|', 'N': '|\\|', 'n': '|\\|', 'P': '|*', 'p': '|*', 'Q': '(,)',
    'q': '(,)', 'R': '|2', 'r': '|2', 'U': '|_|', 'u': '|_|', 'V': '\\/', 'v': '\\/', 'W': '\\/\\/', 'w': '\\/\\/',
    'X': '><', 'x': '><', 'Y': '`/', 'y': '`/'
}

github_v = requests.get("https://raw.githubusercontent.com/error4OA/iconifier-console-mode/main/do-not-mess/info.json").json()
curr_v = "beta1"

print("Iconifier: Console Mode\nMade by: podemb\nCurrent version: {}".format(curr_v))

if github_v["CURR_V"] != curr_v:
    if "supress-updates.icm_setting" in os.listdir(os.getcwd()):
        print("You are using an outdated version of ICM. It is recommended to update now.")
    else:
        print("You are using an outdated version of ICM. To never be redirected to the official repository again, make a \"supress-updates.icm_setting\" file in this directory")
        webbrowser.open("https://github.com/error4OA/iconifier-console-mode/releases")
        exit()

parser = argparse.ArgumentParser(description=textwrap.dedent("""
Iconifier, but without GUI.
Possible styles:
1. 「」
2. 〘〙
3. (none)
                                                             
Possible text styles:
1. Normal
2. Lookalike
3. l33t
"""))
parser.add_argument("-e", "--emoji", help="The emoji to use.", required=False, default="cat")
parser.add_argument("-t", "--text", help="The text to use.", required=False, default="podemb")
parser.add_argument("-s", "--style", help="The style to use", required=False, default="1")
parser.add_argument("-ts", "--text-style", help="The text style to use", required=False, default="1")
parser.add_argument("-lp", "--load-preset", help="Load a .icm-preset file; will cancel out almost all parameters", required=False)
parser.add_argument("-c", "--copy-to-clipboard", required=False, help="Copy result to clipboard if passed.", action="store_true")
args = parser.parse_args()

if args.load_preset:
    with open(args.load_preset, "r") as f:
        data = json.load(f)
        emoj = data["emoji"]
        text = data["text"]
        text_style = data["text_style"]
        styl = data["style"]
    emojized = emoji.emojize(f":{emoj}:", variant="emoji_type")
    if styl == "1":
        style = "「」"
    elif styl == "2":
        style = "〘〙"
    elif styl == "3":
        style = "  "

    currentText = ""

    if text_style == "1":
        currentText = text
    elif text_style == "2":
        for letter in text:
            try:
                currentText = currentText + random.choice(lookalikes.get(letter.lower()))
            except:
                currentText = currentText + letter
    elif text_style == "3":
        for char in text:
            if char in leet_dict:
                currentText += leet_dict[char]
            else:
                currentText += char
else:
    emojized = emoji.emojize(f":{args.emoji}:", variant="emoji_type")
    if args.style == "1":
        style = "「」"
    elif args.style == "2":
        style = "〘〙"
    elif args.style == "3":
        style = "  "

    currentText = ""

    if args.text_style == "1":
        currentText = args.text
    elif args.text_style == "2":
        for letter in args.text:
            try:
                currentText = currentText + random.choice(lookalikes.get(letter.lower()))
            except:
                currentText = currentText + letter
    elif args.text_style == "3":
        for char in args.text:
            if char in leet_dict:
                currentText += leet_dict[char]
            else:
                currentText += char

result = style[0] + emojized + style[1] + currentText

print("Your result is: {}\nDont be worried if some of the text doesnt appear, it is normal".format(result))
if args.copy_to_clipboard:
    clipboard.copy(result)
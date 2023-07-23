# Iconifier: Console Mode (ICM; aka CLI Iconifier)
"Iconify your text, without the need of a GUI"

A python-pure open-source program that allows text iconification! Without a gui.

Original can be found [here](https://github.com/error4OA/iconifier "this app but with an actual GUI")

## Instructions
1. Go to [releases](https://github.com/error4OA/iconifier-console-mode/releases)
2. Download the latest release
3. Drag it to somewhere, id recommend putting it in a folder
4. Open command prompt on that directory and type `.\ICM.exe -h`
5. Youre ready to go

## Examples
1. `.\ICM.exe -e cat -t "some text"`
2. `.\ICM.exe -lp .\preset.icm-preset`
3. `.\ICM.exe -e cheese_wedge -t Cheesehead -s 2 -ts 3 -c`
4. `.\ICM.exe -e red_heart -t epic -sp .\preset.icm-preset -st .\output.txt`

### What the console will output, as of version beta2
```
Iconifier: Console Mode
Made by: podemb
Current version: beta2
usage: ICM.exe [-h] [-e EMOJI] [-t TEXT] [-s STYLE] [-ts TEXT_STYLE] [-lp LOAD_PRESET] [-st SAVE_OUTPUT_TO]
               [-sp SAVE_PRESET] [-c]

Iconifier, but without GUI. Possible styles: 1. 「」 2. 〘〙 3. (none) Possible text styles: 1. Normal 2. Lookalike 3.
l33t

options:
  -h, --help            show this help message and exit
  -e EMOJI, --emoji EMOJI
                        The emoji to use.
  -t TEXT, --text TEXT  The text to use.
  -s STYLE, --style STYLE
                        The style to use
  -ts TEXT_STYLE, --text-style TEXT_STYLE
                        The text style to use
  -lp LOAD_PRESET, --load-preset LOAD_PRESET
                        Load a .icm-preset file; will cancel out almost all parameters
  -st SAVE_OUTPUT_TO, --save-output-to SAVE_OUTPUT_TO
                        Save output to a file
  -sp SAVE_PRESET, --save-preset SAVE_PRESET
                        Save settings to a .icm-preset file
  -c, --copy-to-clipboard
                        Copy result to clipboard if passed.
```

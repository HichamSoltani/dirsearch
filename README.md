HI

NOTICE:
THIS SCRIPT IS DANGER DON'T USE IT WITHOUT PERMISSION.

this is my own dirsearch tool.

you can use it by just download necessary files.

all necessary files are attached in this repository.

USAGE:
        python dirsearch.py <url> [-start -code -ext -nex -w -exclude -exc -t -find -nofind -all -no -api]

information about args:
        <-start:int> \t\t resume from number
        <-code:int> \t\t Status code to be shown alongside with 200
        <-ext:str or list> \t Extension to be chosed (will use this list only in scan)
        <-nex:str> \t\t replace extention with yours (like php with jsp)
        <-w:path> \t\t wordlist path to use
        <-exclude:str> \t\t Exclude Extension from wordlist (like server reject 'php')
        <-exc:int> \t\t Exclude Status Code To Be Shown
        <-t:float> \t\t Time between requests default=0
        <-find:str> \t\t find And Include Those In Wordlist
        <-nofind:str> \t\t Don't Include Those In Wordlist
        -all \t\t\t show all status_code except 404
        -no \t\t\t no write in log file
        -api \t\t\t use special default api wordlist

Examples :
        - python dirsearch.py http://example.com/ -s:400 -code:403 -ext:.js,.php,.json -exclude:html -no
				- python dirsearch.py http://example.com -ext:php -nex:jsp -w:<your_wordlist_path> -t:2.5 -all -no

I'M happy to listen your feedback.

HAPPY HUNTING.

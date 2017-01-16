import urllib

def read_text():
    quotes = open("C:\Users\Dennis\Desktop\Projects\Udacity\Python\profanity alert\movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    convert_to_pirate(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if "true" in output:
        print("profanity alert")
    elif "false" in output:
        print("no curse words")
    else:
        print("could not scan document")
    connection.close()

def convert_to_pirate(text_to_convert):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_convert)
    output = connection.read()
    print(output)
read_text()

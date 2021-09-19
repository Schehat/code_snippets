import re
import os

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
"""

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r"abc")
matches = pattern.finditer(text_to_search)

print("pattern 'abc':")
for match in matches:
    print(match)  # output: span - indexes of match
print(text_to_search[1:4])  # can use span to filter


def regex(reg_pattern, text="", file=None, group=False, index=range(1)):
    pattern = re.compile(reg_pattern)
    matches = None

    if file is None:
        matches = pattern.finditer(text)
    else:
        os.chdir(os.path.dirname(__file__))
        with open(file, "r", encoding="UTF-8") as f:
            f_reader = f.read()

            matches = pattern.finditer(f_reader)

    print(f"\npattern {reg_pattern}:")

    for match in matches:
        if group is True:
            output = ""
            for i in index:
                output += match.group(i)  # concatenate the groups for better printing
            print(output)
        else:
            print(match)


regex(r"coreyms\.com", text=text_to_search)

# \b only matches words which begin with the pattern, in this case Ha
regex(r"\bHa", text=text_to_search)

# ^ only matches the first phrase in the string
regex(r"^Start", text=sentence)

regex(r"end$", text=sentence)

regex(r"\d\d\d-\d\d\d-\d\d\d", text=text_to_search)

# allow multiple characters in this position with the so called character set []
# Note: in [] the character point(.) doesent need to be escaped
regex(r"\d\d\d[.-]\d\d\d[.-]\d\d\d", text=text_to_search)

regex(r"[89]00[.-]\d\d\d[.-]\d\d\d", text=text_to_search)

# dash(-) indicates a range, works for letters as well
regex(r"[1-3]", text=text_to_search)
regex(r"[a-c]", text=text_to_search)
regex(r"[a-cA-D]", text=text_to_search)

# ^-character negates whats in the character set
regex(r"[^1-8a-yA-Y]", text=text_to_search)

regex(r"[^b]at", text=text_to_search)

regex(r"\d{3}\.\d{3}\.\d{4}", text=text_to_search)

regex(r"M(r|s|rs)\.?\s[A-Z]\w*", text=text_to_search)

regex(r"615-\d\d\d-\d\d\d", file="data.txt")

emails = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

regex(
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    text=emails,
)

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# expressions in curve brackets building a group, index=0 is the match
regex(r"https?://(www\.)?(\w+)(\.\w+)", text=urls, group=True, index=[2, 3])

# back reference possible instead to access the groups
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
subbed_urls = pattern.sub(r"\2\3", urls)
print(f"\nback reference: {subbed_urls}")

# flags
# ignorecase I & search gives instead of finditer only the first match
pattern = re.compile(r"start", re.I)
print(pattern.search(sentence))

import re

for statement in ("I love Mary",
                  "Ich liebe Margot",
                  "Je t'aime Marie",
                  "Te amo Maria"):

    if m := re.match(r"I love (\w+)", statement):
        print("He loves", m.group(1))

    elif m := re.match(r"Ich liebe (\w+)", statement):
        print("Er liebt", m.group(1))

    elif m := re.match(r"Je t'aime (\w+)", statement):
        print("Il aime", m.group(1))

    else:
        print()
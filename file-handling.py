
try:
    with open("exercise3.txt") as file:
        pituus = 0

        testi = ""

        for d in sorted(file):
            if len(testi) < len(d):
                print(d)
                testi = d
            else:
                print(d)

except:
    print("file not found")
# def make_shirt(size, text):
#     print("Your ordered a " + 
#         size.lower() + " shirt with the text: '" + text + "'.")
# make_shirt("large", "Have a nice day.")

def make_shirt(size="large", text="I love Python."):
    if size[0].lower() == "e":
        print("Your ordered an " + size.lower() + " shirt with the text: '" + 
        text + "'.")
    else: 
        print("Your ordered a " + size.lower() + " shirt with the text: '" + 
        text + "'.")
make_shirt()
make_shirt("medium")
make_shirt("small", "Have a nice day.")
make_shirt(text="Have a nicer day.", size="extra-large")


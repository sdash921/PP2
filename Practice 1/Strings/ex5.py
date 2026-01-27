age = 36
# nope, this won’t work: "My name is John, I am " + age, we need our savioutr its f!!!

# f string save us, please
txt = f"My name is John, I am {age}" # perfect
print(txt)  # My name is not John but you get the point, I am 36 btw

price = 59
print(f"The price is {price} dollars")        # nicee
print(f"The price is {price:.2f} dollars")    # nice and neat with 2 decimals
print(f"The price is {20 * 59} dollars")      # mmph very cool

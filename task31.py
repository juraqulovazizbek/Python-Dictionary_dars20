from time import sleep

def count_letters(text: str) -> dict[str, int]:
    az = {}
    for ch in text:
        if ch.isalpha():  
            az[ch] = az.get(ch, 0) + 1
    return az

text = "assalomu alaykum"
print(text)
sleep(2)
print(count_letters(text))

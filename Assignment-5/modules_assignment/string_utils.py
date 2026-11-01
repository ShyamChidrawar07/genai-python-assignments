def capitalize_words(text: str) -> str:
    return text.title()

def reverse_string(text:str)-> str:
    return text[::-1]

def word_count(text:str)-> int:
    return len(text.split())
    
if __name__=="__main__":
    strs="shyam gajanan chidrawar"
    print(capitalize_words(strs))
    print(reverse_string(strs))
    print("Words in string = ",word_count(strs))
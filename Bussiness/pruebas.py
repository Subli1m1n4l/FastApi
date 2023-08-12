def find_words_with_two_vowels(words):
  result = [word for word in words if len(list(filter(lambda vowel: vowel in 'aeiouAEIOU', word))) == 2]
  return result



result=find_words_with_two_vowels(["text", "test", "python", "example"])

def count_words_by_length(words):
  result= {len(palabra):len(list(filter(lambda vol:vol if len(palabra) == len(vol) else 0,words))) for palabra in words}
  return result

res=count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

# print(res)
def filter_user_messages(messages, user):
  result=list(filter(lambda item:item if item['sender']==user else None,messages))
  return result

 
  


messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

user = 'Alice'
tt=filter_user_messages(messages, user)


print(tt)
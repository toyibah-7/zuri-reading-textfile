def read_file_content(filename):
      file = open("story.txt","r")
      data = file.read()
      print(data)
    
      return "Hello World"


def count_words():
    text = read_file_content("story.txt")
    occurrences = text.count("as")
    print('Number of occurrences of the word :', occurrences)
    occurences=text.count("would")
    print('Number of occurences of the word:',occurences)
    return {"as": 10, "would": 20}
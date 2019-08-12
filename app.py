from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import wordnet
import random
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        abc = ""
        result = request.form
        text = result['subject']
        print(text)
        word_list = []
        print(word_tokenize(text))
        tokens = word_tokenize(text)
        tag = nltk.pos_tag(tokens)

        syn = wordnet.synsets("empty")
        print(syn[0].examples())

        print(tag)
        for i in tag:
            # print(i[1])
            if i[1] == "NN":
                print(i[0])
                # syns = wordnet.synsets(str(i[0]))
                try:
                    syn = wordnet.synsets(str(i[0]))[0]
                    # print(syns[0].examples())
                    for i in syn.hyponyms():
                        print("Word Generated", i.name())
                        word_list.append(i.name())

                    print("---------------------------------------------")
                    for i in syn.hypernyms():
                        print("Hypernym Generated", i.name())

                    print("\n")
                except:
                    print('Error Occured')

        print(len(word_list))
        a = random.randint(0, (len(word_list)-1))
        print(a)
        print(word_list[a])
        final_word = word_list[a]
        for i in final_word:
            if i == "_":
                abc = abc + " "
            elif i == ".":
                break
            else:
                abc = abc + i
        return render_template('index.html', final_word=abc, text=text)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
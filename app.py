from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import wordnet
import random
from selenium import webdriver
import time


app = Flask(__name__)
browser = webdriver.Chrome()
browser.get('https://www.cleverbot.com/')

@app.route('/', methods = ['POST', 'GET'])
def hello_world():
    global browser
    if request.method == 'POST':
        noun_list = []
        verb_list = []
        adv_list = []
        adj_list = []
        example_list = []
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
                noun_list.append(i[0])
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

            elif i[1] == 'VB':
                verb_list.append(i[0])

            elif i[1] == 'RB':
                adv_list.append(i[0])

            elif i[1] == 'JJ':
                adj_list.append(i[0])

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
        try:
            print(noun_list[0])
            print(noun_list)
        except:
            print('not found')

        try:
            print(verb_list[0])
            print(verb_list)
        except:
            print('not found')

        try:
            print(adv_list[0])
            print(adv_list)
        except:
            print('not found')

        try:
            print(adj_list[0])
            print(adj_list)
        except:
            print('not found')

        for final_word in word_list:
            abcd = ""
            for i in final_word:
                if i == "_":
                    abcd = abcd + " "
                elif i == ".":
                    break
                else:
                    abcd = abcd + i
            print("Words of word list", abc)
            try:
                syns = wordnet.synsets(str(abcd))
                print(syns[0].definition())
                sentence = syns[0].definition()
                print(syns[0].examples())
                example = syns[0].examples()[0]
                example_list.append(example)
            except:
                sentence = ""
                example = ""
                print('Error Occured')


        len_example = len(example_list)
        a = random.randint(0, len_example)
        print(a)
        print(example_list[a])
        example = example_list[a]

        text_box = browser.find_element_by_class_name('stimulus')
        text_box.send_keys(str(example))

        button_click = browser.find_element_by_class_name('sayitbutton')
        button_click.click()

        time.sleep(10)
        result = browser.find_elements_by_class_name('bot')
        for i in result:
            print(i.text)
            example = i.text

        return render_template('index.html', final_word=abc, text=text, example=example)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
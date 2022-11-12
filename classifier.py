import os


if os.path.exists("resulting_data.csv"):
  os.remove("resulting_data.csv")
else:
  print("The file does not exist, creating a new file...")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', "..."]

fh_tweet = open("project_twitter_data.csv", "r", encoding='utf-8')
fh_positive = open("positive_words.txt")
fh_negative = open("negative_words.txt")

fr_tweet = fh_tweet.readlines()
fr_positive = fh_positive.read()
fr_negative = fh_negative.read()

#function to remove the punctuation of words
def strip_punctuation(word):
    for x in punctuation_chars:
        word = word.replace(x, "") 
    return word

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#function to count the positive words of one sentence
def get_pos(sentence):
    words_list = list(sentence.split())
    positive_count = 0
    for x in words_list:
        x = strip_punctuation(x)
        x = x.lower()
        if x in positive_words:
            positive_count += 1
    return positive_count

#function to count the negative words of one sentence
def get_neg(sentence):
    words_list = list(sentence.split())
    negative_count = 0
    for x in words_list:
        x = strip_punctuation(x)
        x = x.lower()
        if x in negative_words:
            negative_count += 1
    return negative_count

del fr_tweet[0]

#list of data separated
fr_split = []

# separating the data
for x in fr_tweet:
    x = x.rstrip()+",0,0,0"
    
    fr_split.append(x.split(","))
    


#Doing a replace on fr_split to take off the punctuations
c = 0   
for x in fr_split:
   sentence = strip_punctuation(x[0])
   fr_split[c][0] = strip_punctuation(x[0])
   c+=1

#getting the count of all the positives and negatives words!
c = 0
for y in fr_split:
    
    
    #print(f"{c} sentenca: {get_pos(y[0])} positives and {get_neg(y[0])} negatives, total of sentiments: {get_pos(y[0])+get_neg(y[0])}")
    
    fr_split[c][3] = str(get_pos(y[0]))
    fr_split[c][4] = str(get_neg(y[0]))
    fr_split[c][5] = str(int(get_pos(y[0])-get_neg(y[0])))
    del fr_split[c][0]
    c+=1

join_list = []

f = open("resulting_data.csv", "x")
for lines in fr_split:
    join_list.append(",".join(lines))

#print(join_list)

f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
for lines in join_list:
    f.write(lines+"\n")
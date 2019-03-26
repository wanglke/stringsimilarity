punctunation = [",", ":", ".", "'", "?", "/", "-", "+", "&", "(", ")"]
sent = ["I love sky, I love sea.", "i love sky, I love sea.", "I want to go to beijing", "I want to go to shang hai", "i want to go to beijing", "you are happy","how are you",\
        "today is sunday","I am liming"]
clean_tokenized = []
# for item in sent:
#     clean_tokenized.append(item.split(" "))
#
# sent = clean_tokenized
# clean_tokenized = []


for s in sent:
    s = s.lower()
    for punc in punctunation:
        s = s.replace(punc, "")
    clean_tokenized.append(s)
print("clean_tokenized:",clean_tokenized)
texts = []
for item in clean_tokenized:
    texts.append(item.split(" "))
all_list = []
for text in texts:
    all_list += text
print(all_list)
corpus = set(all_list)
corpus_dict = dict(zip(corpus, range(len(corpus))))
print("corpus:", corpus)
print("corpus_dict:",corpus_dict)
print("text：",texts)



def vector_rep(text,corpus_dict):
    vec = []
    for key in corpus_dict.keys():
        if key in text:
            vec.append((corpus_dict[key], text.count(key)))
        else:
            vec.append((corpus_dict[key], 0))
    vec = sorted(vec, key=lambda x: x[0])
    vec_only = []
    for ve in vec:
        vec_only += [ve[1]]
    return vec_only

for i in texts:
    print(i)
vec1 = vector_rep(texts[0], corpus_dict)
vec2 = vector_rep(texts[1], corpus_dict)
print(vec1)
from math import sqrt
def similarity(vec1,vec2):
    inner_value = 0
    square_length_vec1 = 0
    square_length_vec2 = 0
    for tup1, tup2 in zip(vec1, vec2):
        inner_value += tup1 * tup2
        square_length_vec2 += tup1 ** 2
        square_length_vec1 += tup2 ** 2
    return(inner_value / sqrt(square_length_vec1*square_length_vec2))

def position(vec_list):
    x = 0
    y = 0
    min_dis = -1000
    similarityv = -1000
    for i in range(0, len(vec_list)):
        for j in range(i+1, len(vec_list)):
            similarityv = similarity(vec_list[i], vec_list[j])
            if similarityv > min_dis:
                min_dis = similarityv
                x = i
                y = j
    return x, y

def listadd(listx,listy):
    return [(listx[i]+listy[i])/2 for i in range(0, len(listx))]

print(listadd(vec1,vec2))

def cluster(list, n):
    vec_list = []
    log = []
    for li in list:
        vec_list.append(vector_rep(li, corpus_dict))
    print("vex_list:", vec_list)
    while len(vec_list) > n:
        x,y = position(vec_list)
        log.append((x, y))
        addlist = listadd(vec_list[x], vec_list[y])
        vec_list.append(addlist)
        del vec_list[x]
        del vec_list[y-1]
    return log




log_list = cluster(texts, 4)
print("log_list:", log_list)
for lo in log_list:
    tem = sent[lo[0]] + sent[lo[1]]
    if lo[0]<lo[1]:
        del sent[lo[0]]
        del sent[lo[1]-1]
    else:
        del sent[lo[1]]
        del sent[lo[0]-1]

    sent.append(tem)
print(sent)

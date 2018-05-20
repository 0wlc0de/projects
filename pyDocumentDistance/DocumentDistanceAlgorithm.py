from math import sqrt, acos


# read File
def read_docs(docName):
    with open(docName, 'r') as doc:
        return doc.readlines()


# split them into array/list of words then return the array
def split_to_words(doc):
    words = []
    table = str.maketrans('{}\n', ' '*3)
    for line in doc:
        for word in line.split(" "):
            words.append(word.translate(table))
    return words


# calculate how much the word is repeated in the document word array
def calculate_frequency(words):
    dict__ = {}
    for word in words:
        if word not in dict__:
            dict__[word] = 1
        elif word in dict__:
            dict__[word] += 1

    return dict__


# the innerProduct or let's say the dot product of the two array or vectors
def dotProduct(dictA, dictB):
    num = 0
    for word in dictA:
        if word in dictB:
            num += dictA[word] * dictB[word]

    return num


# the calculation base on MIT OpenCourseWare
# arccos(|L1| * |L2| / sqrt of (|L1| * |L1|)*(|L2| * |L2|))
# then return it

# The result will be 0.0 if it is identical and if not: the maximum result will 1.50... :D
def document_distance_equation(dictA, dictB):
    innerProduct = dotProduct(dictA, dictB)
    base = sqrt(dotProduct(dictA, dictA) * dotProduct(dictB, dictB))
    return acos(innerProduct/base)


x = input("Enter 1st doc name: ")
y = input("Enter 2nd doc name: ")

docA = calculate_frequency(split_to_words(read_docs(x)))
docB = calculate_frequency(split_to_words(read_docs(y)))
print("This is the document distance of the two files: ", document_distance_equation(docA, docB))

def PatternCount(Text, Pattern):
    count =0
    for i in range(len(Text)) :
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count

def frequent_words(text, k):
    frequent_pattern = []
    count = []
    for i in range(len(text) - k + 1):
        pattern = text[i:(i + k)]
        count.append(PatternCount(text, pattern))
    maxcount = max(int(x) for x in count)
    for i in range(len(text) - k + 1):
        if count[i] == maxcount:
            frequent_pattern.append(text[i:(i + k)])
    frequent_pattern = set(frequent_pattern)
    return frequent_pattern
def ReverseComplement(Pattern):
    Xpattern=reversed(Pattern)
    CXpattern=''
    for i in Xpattern:
        if i =='A':
            CXpattern=CXpattern+'T'
        elif i=='T':
            CXpattern=CXpattern+'A'
        elif i == 'C':
            CXpattern=CXpattern+'G'
        elif i=='G':
            CXpattern=CXpattern+'C'
    return CXpattern
def PatternMatching(Pattern, Genome):
    pos =[]
    for i in range(len(Genome)):
        if Genome[i:i + len(Pattern)] == Pattern:
            pos.append(i)
    print(*pos)


def ClumpFinding(genome, k, L, t):
    clumps = []
    for i in range(0, len(genome), k):# stride k speeds it up
        split_words = {}
        length= genome[i:L+i]
        for j in range(len(length)):
            pattern = length[j:k+j]
            try:
                split_words[pattern] += 1
            except KeyError:
                split_words[pattern] = 1
        to_add = [k for k, val in split_words.items() if t== val]
        clumps += to_add
    return set(clumps)
#str=
#print(frequent_words("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA",3))
#print(PatternCount("CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC", "CGCG"))
#print(ClumpFinding(str,9,500,3))
#print(ReverseComplement("GATTACA"))
print(PatternMatching("CGC","ATGACTTCGCTGTTACGCGC"))

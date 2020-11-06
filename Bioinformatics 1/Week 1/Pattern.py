from pip._vendor.msgpack.fallback import xrange


def PatternToNumber(Pattern):
    if Pattern=="":
        return 0
    else:
        SymbolToNumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        n = len(Pattern)
        prefix = Pattern[:n - 1]
        symbol = Pattern[n - 1]
    return 4 * PatternToNumber(prefix) + SymbolToNumber[symbol]
def NumberToPattern(number,k):
    NumberToSymbol =  {0:'A', 1:'C', 2:'G', 3:'T'}
    if k == 1:
        return NumberToSymbol[number]
    prefixNumber = number // 4
    r = number % 4
    symbol = NumberToSymbol[r]
    return NumberToPattern(prefixNumber,k-1) + symbol
def ComputingFrequencies(Text, k):
    ra=(4**k) -1
    FrequencyArray=[0 for _ in xrange(4**k)]
    tlen=len(Text)-k
    for i in xrange(len(Text) - k + 1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray

#str=ComputingFrequencies("ACGGGAACGAATTCCGGTGCACCGAATTACGATTTTGCAGGAATCTCATCCATATGGGGTCGCCGGGGAGTTAGGCGTACTTGCTATAGTCCTATTGTGTGAGGCCCTGGTTAACCTGCCAAGGCTCAGGGTTCTCTTCATTGATGCGTACCACCTCAATCGCTGTACGAAGACAGCAAGCGCCTCAGTAAGCATTCCGTATGTTGTACTTCCTGACTCTCGCATACCTTGTGTAACGTGTCTCGCGAACCCTGTACATCCCTAACTGTAAGCCTGATGGTAAGCGGTGATTCGGCTTCAGAACTCAGTTCGATCCCCACATTGCTTTTAATAATCGAATATGCTTACTTCAAACGGCCAACATGTGTATTTTAAAGAAGTCAGGATAATCAGTTCCCCGCTGACAGTAGCAGCAATGACAGAAACGGTCAGCGTCACATTTGCCTAATACCTCGTCGGAATGAACGTTTCTAGTTGGAGCTATGATTGTATTGAGGTCTAACCCACAGGATCATTTTATGAAACACTGAGTCTTATTGCCCATTGGAGCTACATTGAGTGTGCGGCAAAACTACCTCCAGTGGTGCCGCTCGCCCGACCGTGCCCTTACCGCTCCACCCCTCTTGCACTAGGGTCAGTTGTGCGCCACGCCTCGGGTGTTTAGCAATTCTTAAACATTAGAACTTCGAATTTGCGCGATGCGTACTTGGAGCACAAAGACTC",8)
#print(*str,sep=' ')
print(NumberToPattern(7704,9))
def tmcalculation (DNA:str):

    base = [0,0,0,0] #A, C, G, T

    tm = 0

    for x in range(len(DNA)):
        if DNA[x] == 'A':
            base[0] += 1
        elif DNA[x] == 'C':
            base[1] += 1
        elif DNA[x] == 'G':
            base[2] += 1
        else:
            base[3] += 1

    if len(DNA) <= 13:
        tm = (base[0] + base[3]) * 2 + (base[1] + base[2]) * 4
    else:
        tm = 64.9 + (base[1] + base[2] - 16.4) * 41 / len(DNA)

    return 'Tm is:                    ' + str(tm)

def palindrome (DNA:str):

    palcoord = []
    palindromes = []

    for x in range(len(DNA)-1):
        for y in range(x + 1, len(DNA)):
            if DNA[x] == DNA[y]:
                half = (y - x) // 2
                flag = 0
                for z in range(half):
                    if DNA[x + z + 1] == DNA[y - z - 1]:
                        flag += 1
                if flag == half:
                    palcoord.append([x, y])
                    
    for x in range(len(palcoord)):
        flip = ''
        for y in range(palcoord[x][0], palcoord[x][1] + 1):
            flip += DNA[y]
        if palindromes == []:
            palindromes.append(flip)
        elif len(flip) > len(palindromes[0]):
            palindromes = []
            palindromes.append(flip)

    return 'Longest Palindrome is:    ' + palindromes[0]

def translation (DNA:str):

    case1 = DNA
    case1 = case1.replace('', ' ')
    case1 = case1.split(' ')
    case1.pop()
    case1.pop(0)
    case2 = DNA
    case2 = case2.replace('', ' ')
    case2 = case2.split(' ')
    case2.pop()
    for x in range(2):
        case2.pop(0)
    case3 = DNA
    case3 = case3.replace('', ' ')
    case3 = case3.split(' ')
    case3.pop()
    for x in range(3):
        case3.pop(0)

    number1 = len(case1) // 3
    number2 = len(case2) // 3
    number3 = len(case3) // 3

    polypeptide1 = []
    polypeptide2 = []
    polypeptide3 = []

    chain1 = ''
    chain2 = ''
    chain3 = ''

    #print(case1)
    for x in range(number1):
        nowstring = case1[3 * x] + case1[3 * x + 1] + case1[3 * x + 2]
        #print(nowstring, end=', ')
        if nowstring == 'GCA' or nowstring == 'GCC' or nowstring == 'GCG' or nowstring == 'GCT':
            polypeptide1.append('A')
        elif nowstring == 'TGC' or nowstring == 'TGT':
            polypeptide1.append('C')
        elif nowstring == 'GAC' or nowstring == 'GAT':
            polypeptide1.append('D')
        elif nowstring == 'GAA' or nowstring == 'GAG':
            polypeptide1.append('E')
        elif nowstring == 'TTC' or nowstring == 'TTT':
            polypeptide1.append('F')
        elif nowstring == 'GGA' or nowstring == 'GGC' or nowstring == 'GGG' or nowstring == 'GGT':
            polypeptide1.append('G')
        elif nowstring == 'CAC' or nowstring == 'CAT':
            polypeptide1.append('H')
        elif nowstring == 'ATA' or nowstring == 'ATC' or nowstring == 'ATT':
            polypeptide1.append('I')
        elif nowstring == 'AAA' or nowstring == 'AAG':
            polypeptide1.append('K')
        elif nowstring == 'CTA' or nowstring == 'CTC' or nowstring == 'CTG' or nowstring == 'CTT' or nowstring == 'TTA' or nowstring == 'TTG':
            polypeptide1.append('L')
        elif nowstring == 'ATG':
            polypeptide1.append('M')
        elif nowstring == 'AAC' or nowstring == 'AAT':
            polypeptide1.append('N')
        elif nowstring == 'CCA' or nowstring == 'CCC' or nowstring == 'CCG' or nowstring == 'CCT':
            polypeptide1.append('P')
        elif nowstring == 'CAA' or nowstring == 'CAG':
            polypeptide1.append('Q')
        elif nowstring == 'AGA' or nowstring == 'AGG' or nowstring == 'CGA' or nowstring == 'CGC' or nowstring == 'CGG' or nowstring == 'CGT':
            polypeptide1.append('R')
        elif nowstring == 'AGC' or nowstring == 'AGT' or nowstring == 'TCA' or nowstring == 'TCC' or nowstring == 'TCG' or nowstring == 'TCT':
            polypeptide1.append('S')
        elif nowstring == 'ACA' or nowstring == 'ACC' or nowstring == 'ACG' or nowstring == 'ACT':
            polypeptide1.append('T')
        elif nowstring == 'GTA' or nowstring == 'GTC' or nowstring == 'GTG' or nowstring == 'GTT':
            polypeptide1.append('V')
        elif nowstring == 'TGG':
            polypeptide1.append('W')
        else:
            polypeptide1.append('Y')

    #print(case2)
    for x in range(number2):
        nowstring = case2[3 * x] + case2[3 * x + 1] + case2[3 * x + 2]
        #print(nowstring, end=', ')
        if nowstring == 'GCA' or nowstring == 'GCC' or nowstring == 'GCG' or nowstring == 'GCT':
            polypeptide2.append('A')
        elif nowstring == 'TGC' or nowstring == 'TGT':
            polypeptide2.append('C')
        elif nowstring == 'GAC' or nowstring == 'GAT':
            polypeptide2.append('D')
        elif nowstring == 'GAA' or nowstring == 'GAG':
            polypeptide2.append('E')
        elif nowstring == 'TTC' or nowstring == 'TTT':
            polypeptide2.append('F')
        elif nowstring == 'GGA' or nowstring == 'GGC' or nowstring == 'GGG' or nowstring == 'GGT':
            polypeptide2.append('G')
        elif nowstring == 'CAC' or nowstring == 'CAT':
            polypeptide2.append('H')
        elif nowstring == 'ATA' or nowstring == 'ATC' or nowstring == 'ATT':
            polypeptide2.append('I')
        elif nowstring == 'AAA' or nowstring == 'AAG':
            polypeptide2.append('K')
        elif nowstring == 'CTA' or nowstring == 'CTC' or nowstring == 'CTG' or nowstring == 'CTT' or nowstring == 'TTA' or nowstring == 'TTG':
            polypeptide2.append('L')
        elif nowstring == 'ATG':
            polypeptide2.append('M')
        elif nowstring == 'AAC' or nowstring == 'AAT':
            polypeptide2.append('N')
        elif nowstring == 'CCA' or nowstring == 'CCC' or nowstring == 'CCG' or nowstring == 'CCT':
            polypeptide2.append('P')
        elif nowstring == 'CAA' or nowstring == 'CAG':
            polypeptide2.append('Q')
        elif nowstring == 'AGA' or nowstring == 'AGG' or nowstring == 'CGA' or nowstring == 'CGC' or nowstring == 'CGG' or nowstring == 'CGT':
            polypeptide2.append('R')
        elif nowstring == 'AGC' or nowstring == 'AGT' or nowstring == 'TCA' or nowstring == 'TCC' or nowstring == 'TCG' or nowstring == 'TCT':
            polypeptide2.append('S')
        elif nowstring == 'ACA' or nowstring == 'ACC' or nowstring == 'ACG' or nowstring == 'ACT':
            polypeptide2.append('T')
        elif nowstring == 'GTA' or nowstring == 'GTC' or nowstring == 'GTG' or nowstring == 'GTT':
            polypeptide2.append('V')
        elif nowstring == 'TGG':
            polypeptide2.append('W')
        else:
            polypeptide2.append('Y')

    #print(case3)
    for x in range(number3):
        nowstring = case3[3 * x] + case3[3 * x + 1] + case3[3 * x + 2]
        #print(nowstring, end=', ')
        if nowstring == 'GCA' or nowstring == 'GCC' or nowstring == 'GCG' or nowstring == 'GCT':
            polypeptide3.append('A')
        elif nowstring == 'TGC' or nowstring == 'TGT':
            polypeptide3.append('C')
        elif nowstring == 'GAC' or nowstring == 'GAT':
            polypeptide3.append('D')
        elif nowstring == 'GAA' or nowstring == 'GAG':
            polypeptide3.append('E')
        elif nowstring == 'TTC' or nowstring == 'TTT':
            polypeptide3.append('F')
        elif nowstring == 'GGA' or nowstring == 'GGC' or nowstring == 'GGG' or nowstring == 'GGT':
            polypeptide3.append('G')
        elif nowstring == 'CAC' or nowstring == 'CAT':
            polypeptide3.append('H')
        elif nowstring == 'ATA' or nowstring == 'ATC' or nowstring == 'ATT':
            polypeptide3.append('I')
        elif nowstring == 'AAA' or nowstring == 'AAG':
            polypeptide3.append('K')
        elif nowstring == 'CTA' or nowstring == 'CTC' or nowstring == 'CTG' or nowstring == 'CTT' or nowstring == 'TTA' or nowstring == 'TTG':
            polypeptide3.append('L')
        elif nowstring == 'ATG':
            polypeptide3.append('M')
        elif nowstring == 'AAC' or nowstring == 'AAT':
            polypeptide3.append('N')
        elif nowstring == 'CCA' or nowstring == 'CCC' or nowstring == 'CCG' or nowstring == 'CCT':
            polypeptide3.append('P')
        elif nowstring == 'CAA' or nowstring == 'CAG':
            polypeptide3.append('Q')
        elif nowstring == 'AGA' or nowstring == 'AGG' or nowstring == 'CGA' or nowstring == 'CGC' or nowstring == 'CGG' or nowstring == 'CGT':
            polypeptide3.append('R')
        elif nowstring == 'AGC' or nowstring == 'AGT' or nowstring == 'TCA' or nowstring == 'TCC' or nowstring == 'TCG' or nowstring == 'TCT':
            polypeptide3.append('S')
        elif nowstring == 'ACA' or nowstring == 'ACC' or nowstring == 'ACG' or nowstring == 'ACT':
            polypeptide3.append('T')
        elif nowstring == 'GTA' or nowstring == 'GTC' or nowstring == 'GTG' or nowstring == 'GTT':
            polypeptide3.append('V')
        elif nowstring == 'TGG':
            polypeptide3.append('W')
        else:
            polypeptide3.append('Y')

    for x in range(len(polypeptide1)):
        chain1 += polypeptide1[x]
        if x != len(polypeptide1) - 1:
            chain1 += ' - '

    for x in range(len(polypeptide2)):
        chain2 += polypeptide2[x]
        if x != len(polypeptide2) - 1:
            chain2 += ' - '

    for x in range(len(polypeptide3)):
        chain3 += polypeptide3[x]
        if x != len(polypeptide3) - 1:
            chain3 += ' - '

    return 'Polypeptide Sequence(s): \n' + chain1 + '\n' + chain2 + '\n' + chain3

DNA = str(input("Input DNA Sequence here: "))

print("\n--------------Analysis Result--------------")
print(tmcalculation(DNA))
print(palindrome(DNA))
print(translation(DNA))
print("-------------------------------------------\n")

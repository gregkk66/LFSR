aDict = dict(zip('abcdefghijklmnopqrstuvwxyz.!?()-ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                              ['00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001',
                              '11010','11011','11100','11101','11110','11111',
                              '00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001']))
ab=aDict["a"]+aDict["b"]
sq=aDict["s"]+aDict["q"]
seed1=""
for i in range(len(ab)):      ####### βρίσκουμε ένα seed από την κρυπτογράφηση της εκφώνησης
    if ab[i]!=sq[i]:
        seed1+="1"
    else:
        seed1+="0"

text1="i!))aiszwykqnfcyc!?secnncvch" ######  ciphertext

def stringxor(str1,str2): ### stringxor
    xor=""
    for i in range(len(str1)):
        xor+=str(int(str1[i])^int(str2[i]))
    return xor

def stringtobin(str1):      ###### textstring to binary string
    binstring=""
    for i in str1:
        binstring+=aDict[i]
    return binstring

def bintostring(str1):     ######## binary string to textstring
    inv_map = {v: k for k, v in aDict.items()}
    result=""
    for i in range(0,len(str1),5):
        result+=inv_map[str1[i:i+5]]
    return result

def lfsr(seed):            #### LFSR
    lista=[seed]
    temp=""
    while True:
        i=lista[-1]
        temp+= str(int(i[9])^int(i[8])^int(i[6])^int(i[5]))  ####### χαρακτηριστικό πολυώνυμο
        temp+=i[:9]
        if temp not in lista:
            lista.append(temp)
            temp=""
        else:           
            break       ########### το loop σπάει στην περίοδο του lfsr
    return lista       ############ output μια λίστα με όλα τα seeds
    
def decrypt(seeds,text1): ########## αποκρυπτογράφηση για όλα τα seeds
    cipherbin=stringtobin(text1)
    key1=""
    lista=[]
    k=0
    seed1=seeds+seeds
    while len(lista)<len(seeds):  
        for i in range(k,len(cipherbin)+k):     ####### ξεκινάμε από το k seed,
            key1+=seed1[i][-1]                  ####### το κλειδ΄ί που σχηματίζεται από το k seed με len(cipherbin) μεταθέσεις
        plaintext=stringxor(key1,cipherbin)     ####### xor
        lista.append(bintostring(plaintext))    
        k+=1                                    ####### πάμε στο κ+1 seed
        key1=""                                 ####### το loop τελειώνει όταν φτάσουμε στο αρχικό seed
    return lista     ##### output όλα τα plaintexts

plaintexts=decrypt(lfsr(seed1),text1)        

def makesense(lista):  ####### δημιουργούμε καινούργια λίστα με τα plaintexts που δεν έχουν σύμβολα.
    lista2=[]
    flag=False
    for i in lista:
        for j in ".!?()-":
            if j in i:
                flag=True   ######## το flag γίνεται True όταν υπάρχει σύμβολο μέσα στο plaintext
        if not flag:       
            lista2.append(i)  
        flag=False
    return lista2            

print("plaintext is : " + makesense(plaintexts)[-1])


        



#!/usr/bin/env python
# coding: utf-8

# In[6]:


def populasi (nPop, nKromosom): 
    populasi = [] 
    for i in range(nPop): 
        populasi.append(np.random.permutation(nKromosom)) 
    return populasi

def connectedNode (myNode, koorx, koory): 
    kx = 0 
    ky = 0 
    jarak = 0 
    a = 0.01 
    #menghindari tak hingga 
    temparray = [] 
    for j in range(len(myNode)-1): 
        # mencari jarak 
        kx = (koorx[myNode[j]] + koorx[myNode[j+1]])**2 
        ky = (koory[myNode[j]] + koory[myNode[j+1]])**2 
        jarak = jarak + ((kx + ky)**1/2) 
        #menghitung fitness 
        maksimasi = jarak 
        minimasi = 1/(jarak + a) 
        temparray.append([jarak, maksimasi, minimasi]) 
    return connectedNode

#seleksi orang tua def randomparent(): return int(round(random.uniform(0,nKromosom))) #dengan ini kita membandingkan antar kromosom yang melakukan node dari 0 kembali ke 0. nah disitu di random agar membandingkan antar kromosom satu ke kromosom lainnya.

if __name__ == 'main': #banyaknya gen (bebas) nGen = 10 myNode = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] koorx = [82, 96, 50, 49, 13, 29, 58, 84, 14, 2, 3, 5, 98, 84, 61, 1] koory = [76, 44, 5, 8, 7, 89, 30, 39, 24, 39, 82, 10, 52, 25, 59, 69]

    #ketentuan
    pCross = 0.8
    pMutasi = 0.2

    #banyaknya populasi (bebas cuy)
    nPop = 5
    nKromosom = len(myNode)

    #Inisialisasi Populasi
    populasi = genPopulasi(nPop, nKromosom)

    while (i <= 15):
        for j in range(nPop/2):
            parentcuy = randomparent(nPop-1) #dikurangi satu karena sudah di ambil satu persatu
            parentwoy = randomparent(nPop-1)
            #seleksi orang tua


        #coba hitung masing masing di jadikan 20%

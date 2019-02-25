import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state=0,multi_class='auto',solver='lbfgs')
from mlxtend.plotting import plot_decision_regions

def trainlogreg():
    model.fit(X,y)
    plot_decision_regions(X=X, y=y, clf=model, legend=2)
    plt.title("Klasifikasi {} menggunakan Logistic Regression".format(ytitle), {'fontsize':17})
    if var == "1":
        plt.xlabel(xtitle, {'fontsize':10})
        plt.ylabel(ytitle, {'fontsize':10})
    else:
        plt.xlabel(x1title, {'fontsize':10})
        plt.ylabel(x2title, {'fontsize':10})
    plt.show()


def inputx1():
    print("Masukkan nama variabel x1 (default: x)")
    xtitle = input().strip()
    if xtitle == '':
        xtitle="X"
    print("Masukkan nilai x1 (pisahkan dengan koma)","\n","Contoh : 2, 3, 4, 5, dst","\n")
    # Input variabel X1
    x = input()
    x = list(x.split(','))
    x1 = [float(i) for i in x]
    return np.array(x1), xtitle

def inputx2():
    print("Masukkan nama variabel x2 (default: x)")
    xtitle = input().strip()
    if xtitle == '':
        xtitle="X"
    print("Masukkan nilai x2 (pisahkan dengan koma)","\n","Contoh : 2, 3, 4, 5, dst","\n")
    # Input variabel X1
    x = input()
    x = list(x.split(','))
    x2 = [float(i) for i in x]
    return np.array(x2), xtitle
    #x = np.array([float(i) for i in x])


def inputy():
    print("Masukkan nama kelas klasifikasi y (default: y)")
    ytitle = input().strip()
    if ytitle == '':
        ytitle="y"
    print("Masukkan nilai y (pisahkan dengan koma)","\n",
        "Keterangan : Nilai y harus berupa angka yg dimulai dari 0, jadi jika kelas klasifikasi ada 2 gunakan 0 dan 1","\n",
            "Contoh : Lulus, Lulus, Tidak Lulus --> menjadi 1, 1, 0 dst")
    # Input variabel y
    y = input()
    y = list(y.split(','))
    y = [int(i) for i in y]
    return np.array(y), ytitle

print("Program Menampilkan Klasifikasi menggunakan Logistic Regression",end="\n\n")
print("Berapa jumlah input yang diinginkan ? input dengan nilai 1 / 2 (maks 2) ")
var = input().strip()

if var == "1":
    X, xtitle = inputx1()
    y, ytitle = inputy()
    if X.shape == y.shape:
        X = X[:, np.newaxis]
        trainlogreg()
    else :
        print("Jumlah data X dan y tidak sama, silahkan ulangi lagi")
elif var == "2":
    x1, x1title = inputx1()
    x2, x2title = inputx2()
    if x1.shape == x2.shape:
        X = np.stack((x1,x2),axis=-1)
        y, ytitle = inputy()
        if len(X) == len(y):
            trainlogreg()
        else:
            print("Jumlah data antara X dan y tidak sama, silahkan ulangi lagi")
    else:
        print("Jumlah data antara variabel x1 dan x2 tidak sama, silahkan ulangi lagi")    
else:
    print("Masukkan nilai 1 atau 2, silahkan ulangi lagi")

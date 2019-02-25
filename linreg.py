import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)

def trainlinreg():
    # Fitting / Training Linear Regression model
    model.fit(X[:, np.newaxis], y)
    xfit = np.linspace(X.min(), X.max())
    yfit = model.predict(xfit[:,np.newaxis])
    plt.scatter(X,y,c='g')
    plt.plot(xfit,yfit,c='r')
    plt.title("Grafik Linear Regresi {} berdasarkan {}".format(ytitle,xtitle), {'fontsize':17})
    plt.xlabel(xtitle,{'fontsize':10})
    plt.ylabel(ytitle,{'fontsize':10})
    intercept, slope = model.intercept_, model.coef_[0]
    leg_text = 'intercept: %.2f\nslope: %.2f' % (intercept, slope)
    plt.legend([leg_text], loc='best')
    plt.show()

def inputx():
    print("Masukkan nama variabel X (default: x)")
    xtitle = input().strip()
    if xtitle == '':
        xtitle="X"
    print("Masukkan nilai X (pisahkan dengan koma)","\n","Contoh : 2, 3, 4, 5, dst","\n")
    # Input variabel X1
    x = input()
    x = list(x.split(','))
    x = [float(i) for i in x]
    return np.array(x), xtitle

def inputy():
    print("Masukkan nama kelas klasifikasi y (default: y)")
    ytitle = input().strip()
    if ytitle == '':
        ytitle="y"
    print("Masukkan nilai y (pisahkan dengan koma)","\n","Contoh : 2, 3, 4, 5, dst","\n")
    # Input variabel y
    y = input()
    y = list(y.split(','))
    y = [int(i) for i in y]
    return np.array(y), ytitle

print("Program Menghitung Regresi Linear dari 1 variabel independen",end="\n")
X, xtitle = inputx()
y, ytitle = inputy()
if X.shape == y.shape:
    print("Fitting Model")
    trainlinreg()
    
else :
    print("Jumlah data x dan y tidak sama, silahkan ulangi lagi")
    
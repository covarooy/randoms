import numpy as np

def monthly(yrs, pv, inter = 8.5):
    pm = np.pmt(inter/100/12, 12*yrs, pv)
    return pm

def repay_spread(MinLoan, MaxLoan, Price, num = 50):
    
    initial = [] 
    for val in np.linspace(MinLoan, MaxLoan, num, endpoint = True):
        initial.append(monthly(20, val))

    eventual = []

    for val in np.linspace((Price - MinLoan), (Price - MaxLoan), num, endpoint = True):
        eventual.append(monthly(15, -np.fv(0.08, 10, 0, val)))

    return initial, eventual

def main():
    Price = 3.6E6
    MinBankLoan = 1.6E6
    MaxBankLoan = 2.2E6
    Y0, Y10 = repay_spread(MinBankLoan, MaxBankLoan, Price)
    print(Y0)
    print(Y10)




if __name__ == '__main__':
    main()

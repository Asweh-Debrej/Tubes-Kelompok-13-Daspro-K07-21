import C01_fungsiDasar as fd
import C02_fungsiBuatan as fb

def history(_history, _loggedUser):
    """Menampilkan riwayat pembelian dari matriks berukuran minimal 5x1
    """
    if fd.mtrxFind(_history, _loggedUser[0], 3) == -1:
        print("Anda belum pernah membeli game apapun. Ketik \"buy game\" untuk membeli game.")
        return

    lengths = fb.maxLengths(_history)
    line1 = "| {0[0]:^{1[0]}} | {0[1]:^{1[1]}} | {0[2]:^{1[2]}} | {0[4]:^{1[4]}} |".format(_history[0], lengths)
    print('_'*fd.len(line1))
    print(line1)
    print("| {} | {} | {} | {} |".format(lengths[0]*'-', lengths[1]*'-', lengths[2]*'-', lengths[4]*'-'))
    for i in range(1, fd.len(_history)):
        if _loggedUser[0] == _history[i][3]:
            print("| {0[0]:<{1[0]}} | {0[1]:<{1[1]}} | {0[2]:<{1[2]}} | {0[4]:<{1[4]}} |".format(_history[i], lengths))
    print('‾'*fd.len(line1))

    return


if __name__ == "__main__":
    pass


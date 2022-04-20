import fungsiDasar as fd
import fungsiBuatan as fb

def history(history, loggedUser):
    """Menampilkan riwayat pembelian dari matriks berukuran minimal 5x1
    """
    if fd.mtrxFind(history, loggedUser[0], 3) == -1:
        print("Anda belum pernah membeli game apapun. Ketik \"buy game\" untuk membeli game.")
        return

    lengths = fb.maxLengths(history)
    line1 = "| {0[0]:^{1[0]}} | {0[1]:^{1[1]}} | {0[2]:^{1[2]}} | {0[4]:^{1[4]}} |".format(history[0], lengths)
    print('_'*fd.len(line1))
    print(line1)
    print("| {} | {} | {} | {} |".format(lengths[0]*'-', lengths[1]*'-', lengths[2]*'-', lengths[4]*'-'))
    for i in range(1, fd.len(history)):
        if loggedUser[0] == history[i][3]:
            print("| {0[0]:<{1[0]}} | {0[1]:<{1[1]}} | {0[2]:<{1[2]}} | {0[4]:<{1[4]}} |".format(history[i], lengths))
    print('‾'*fd.len(line1))

    return


if __name__ == "__main__":
    pass
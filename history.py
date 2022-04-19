import fungsiDasar as fd
import fungsiBuatan as fb

def history(history):
    """Menampilkan riwayat pembelian dari matriks berukuran minimal 5x1
    """
    lengths = fb.maxLengths(history)
    line1 = "| {0[0]:^{1[0]}} | {0[1]:^{1[1]}} | {0[2]:^{1[2]}} | {0[4]:^{1[4]}} |".format(history[0], lengths)
    print('_'*fd.len(line1))
    print(line1)
    print("| {} | {} | {} | {} |".format(lengths[0]*'-', lengths[1]*'-', lengths[2]*'-', lengths[4]*'-'))
    for i in range(1, fd.len(history)):
        print("| {0[0]:<{1[0]}} | {0[1]:<{1[1]}} | {0[2]:<{1[2]}} | {0[4]:<{1[4]}} |".format(history[i], lengths))
    print('‾'*fd.len(line1))


if __name__ == "__main__":
    import tes
    history(tes.history)
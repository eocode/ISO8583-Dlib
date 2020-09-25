# Parser for iso8583
from iso8583_dlib.parser import Parser


def run():
    message = "ISO0260000700200B23E842128A1801A00000000100000BC0010000000000070020707203500000013153459070724050707070705161199999999999274231453201761925=2405226096000000000619P0891218        INBURSA CASHBACK      CD MEXICO    001MX0277126834            00010101484016B036PRO1+0000000019B359    00000000000370& 0000700370! C000026              113000       ! C400012 000000021082! Q200002 03! B200158 7FF900008000800080008251FFC4F2FDE21D0000000070020000000000003C00002A48448420070700BE967302000706010A03A4B80200000"
    data = Parser(message)
    print(data.get_json(save=True))


if __name__ == '__main__':
    run()

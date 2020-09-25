def hex_to_binary(string):
    n = int(string, 16)
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr.zfill(4)

# Copyright (c) Noah Dominic Silvio <ndsilvio@gmail.com>
# version 1.0.0

# rz() [stable as of version 1.0.0]
# accepts array inputbytes
# returns encodedbytes in rz unipolar encoding
def rz(inputbytes):
    outputbytes = []
    for i in inputbytes:
        outputbytes.append((i > 0) * 5)
    return outputbytes


# nrz() [stabl as of version 1.0.0]
# accepts array inputbytes
# returns encodedbytes in nrz bipolar line encoding
def nrz(inputbytes):
    outputbytes = []
    for i in inputbytes:
        outputbytes.append(10 * (i > 0) - 5)
    return outputbytes


# nrzi() [stable as of version 1.0.0]
# accepts array inputbytes
# returns encodedbytes in nrz bipolar inverted encoding
def nrzi(inputbytes):
    outputbytes = []
    tempbyte = 0
    for i in inputbytes:
        nextbyte = (tempbyte) != (i > 0)
        outputbytes.append(10 * nextbyte - 5)
        tempbyte = nextbyte
    return outputbytes

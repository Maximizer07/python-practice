import struct


def f31(binary: bytes) -> dict:
    def struct_a(offset: int) -> dict:
        a1 = struct_b(offset)
        offset += 10
        [a2] = struct.unpack('< H', binary[offset: offset + 2])
        offset += 2
        a3 = list(struct.unpack('< 2B', binary[offset: offset + 2]))
        offset += 2
        [a4] = struct.unpack('< I', binary[offset: offset + 4])
        offset += 4
        a5 = struct_d(offset)
        offset += 8 + 1 + 8 + 8 + 4 + 4 + 1
        [a6] = struct.unpack('< B', binary[offset: offset + 1])
        offset += 1
        a7 = list(struct.unpack('< 7B', binary[offset: offset + 7]))
        offset += 7
        [a8] = struct.unpack('< d', binary[offset: offset + 8])
        return {
            'A1': a1,
            'A2': a2,
            'A3': a3,
            'A4': a4,
            'A5': a5,
            'A6': a6,
            'A7': a7,
            'A8': a8
        }

    def struct_b(offset: int) -> dict:
        [length] = struct.unpack('< L', binary[offset: offset + 4])
        offset += 4
        [link_list] = struct.unpack('< H', binary[offset: offset + 2])
        offset += 2
        list_links = [struct.unpack('< L', binary[link_list + i * 4: link_list + (i + 1) * 4])[0]
                      for i in range(length)]
        b1 = [struct_c(list_links[i]) for i in range(length)]

        [length] = struct.unpack('< H', binary[offset: offset + 2])
        offset += 2
        [link_str] = struct.unpack('< H', binary[offset: offset + 2])
        b2 = str([struct.unpack('<' + str(length) + 's', binary[link_str: link_str + length])])[4:-4]

        return {
            'B1': b1,
            'B2': b2
        }

    def struct_c(offset: int) -> dict:
        [c1, c2] = struct.unpack('< f d', binary[offset: offset + 4 + 8])
        return {
            'C1': c1,
            'C2': c2
        }

    def struct_d(offset: int) -> dict:
        [d1, d2, d3, d4, d5, d6, d7] = struct.unpack('< d B Q q f l B',
                                                     binary[offset: offset + 8 + 1 + 8 + 8 + 4 + 4 + 1])
        return {
            'D1': d1,
            'D2': d2,
            'D3': d3,
            'D4': d4,
            'D5': d5,
            'D6': d6,
            'D7': d7
        }

    return struct_a(5)


print(f31(b'\x82WCRP\x04\x00\x00\x00y\x00\x02\x00\x89\x00\xaf\x1f#a\xb9\xf4r\x9a\x18'
          b'\x9b\\L\x91\xf3\xe8?|\xf7\x99\xe4\xcb\xccP\xaa\xd0\xc5s\x9e\x10'
          b'\x0c\x91\xa7\xdf\xdf\xd7\xc5=+\x9e\x9a\xd9r\x06H\xfe\xcfQL<j\xccV\x9c'
          b'\x98\x13\xfb\xd9?x\x00n?\xb4\x87SUr\x9f\xe8?\xef\xf5\xa5>\xd0\xa6\x9f'
          b' \x8c\xe6\xe1\xbf\xfcN\x8d\xbe\x0e\xfe\x067\x97\xa4\xea?FUv?\xa8Tm^\xd04\xdf'
          b'\xbfI\x00\x00\x00U\x00\x00\x00a\x00\x00\x00m\x00\x00\x00ae'))
print(f31(b'\x82WCRP\x03\x00\x00\x00m\x00\x02\x00y\x00\xa7\xb9\x071)\x12\\\xa3\xe0'
          b"\x0c\xdd'\xa3\x8e\xc2\xbf\xed\x8e\xc3g\xe4\xbf=\xafM\xb28\x98\x96\xb9!\xb0V"
          b'\xeb\xd85\xbf\xa1\xbb\x8f\x1a\xc7y`\xd3\xfb\xedXN\xfdL3\x9d{\x8cw\xd8'
          b'?j\x9e\x97\xbe\xe0_\xdc-\x03\x84\xe2?V\xa8i\xbfvJ\x82\xbcm1\xe2?\x9e\xe3i'
          b'=\xb8\xa71\xb5\xc3m\xe9\xbfI\x00\x00\x00U\x00\x00\x00a\x00\x00\x00sh'))

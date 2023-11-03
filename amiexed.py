#!/usr/bin/env python3

import sys

"""
Very rough word-by-word m68k decompiler for 
bfc and its generated output.

In python to get a feel for an alogrithm and how many
different op-codes are used and how they might be
distinguished.

Definitely buggy at this point, although it seems to parse
everything and give some result.

Suspect the bra, bcc, blo.b codes have problems, but that's
likely not all.

"""


# http://goldencrystal.free.fr/M68kOpcodes-v2.3.pdf

# should be 2 byte keys...
OLD_KEYS = {

   '0x12': ('move.b', 1, 0, '(a3)+,d1??'),
   '0x18': ('move.b', 1, 0, '(a5),d4??'),
   '0x1a': ('move.b', 1, 0, 'd3,(a5)??'),

   '0x24': ('move.l', 1, 0, 'a5,a2'),
   '0x28': ('move.l', 1, 0, 'd0,a4'),
   '0x2c': ('move.l', 1, 0, '(a4),a6'),

   '0x35': ('move.w', 1, 2, ',-(a2)'),

   '0x42': ('clr.b', 1, 0, '??'),
   '0x47': ('lea (', 1, 2, ',pc), a3'),
   '0x4b': ('lea (', 1, 2, ',pc), a5'),
   '0x4e': ('jsr', 1, 2, '(a6)'),

   '0x51': ('dbcc', 1, 2, '??'),

   '0x70': ('moveq',0, 1, ', d0'),
   '0x76': ('moveq',0, 1, ', d3'),
   '0x7a': ('moveq',0, 1, ', d5'),

   '0xb8': ('cmp.b', 1, 0, ', (a3)+,d4??'),
   }


KEYS = {

   '0x121b': ('move.b', 0, '(a3)+,d1'),
   '0x1815': ('move.b', 0, '(a5),d4'),
   '0x1a83': ('move.b', 0, 'd3,(a5)'),
   '0x1a1b': ('move.b', 0, '(a3)+,d5'),
   '0x1adb': ('move.b', 0, '(a3)+,(a5)+'),


   '0x2008': ('move.l', 0, 'a0,d0'),
   '0x205a': ('move.l', 0, '(a2)+,a0'),
   '0x2200': ('move.l', 0, 'd0,d1'),
   '0x224e': ('move.l', 0, 'a6,a1'),
   '0x240d': ('move.l', 0, 'a5,d2'),
   '0x244d': ('move.l', 0, 'a5,a2'),
   '0x250d': ('move.l', 0, 'a5,-(a2)'),
   '0x2840': ('move.l', 0, 'd0,a4'),
   '0x2c40': ('move.l', 0, 'd0,a6'),
   '0x2c54': ('move.l', 0, '(a4),a6'),

   '0x3100': ('move.w', 0, 'd0,-(a0)'),
   '0x353c': ('move.w', 2, ',-(a2)'),
   '0x3ac0': ('move.w', 0, 'd0,(a5)+'),

   '0x4215': ('clr.b', 0, '(a5)'),
   '0x421a': ('clr.b', 0, '(a2)+'),
   '0x4440': ('neg.w', 0, 'd0'),
   '0x47fa': ('lea (', 2, ', pc), a3'),
   '0x4843': ('swap', 0, 'd3'),
   '0x4a04': ('tst.b', 0, 'd4'),
   '0x4bfa': ('lea (', 2, ', pc), a5'),
   '0x4e75': ('rts', 0, ''),
   '0x4eae': ('jsr', 2, '(a6)'),

   '0x5005': ('addq.b', 0, '#8,d5()'),
   '0x51cd': ('dbcc d5, ', 2, ''),  # dbra d5?
   '0x5215': ('addq.b', 0, ' #1,a5'),  # from bfc compiled output
   '0x528d': ('addq.l', 0, ' #1,a5'), 
   '0x5301': ('subq.b', 0, '#1,d1'),
   '0x5315': ('subq.b', 0, '#1,a5'),
   '0x538d': ('subq.l', 0, '#1,a5'),
   '0x5605': ('addq.b', 0, '#3,d5'),
   '0x5940': ('subq.w', 0, '#4,d0'),

   '0x60': ('bra', 2, ''),    # dc.w    $6000  | in compiled output
   '0x64': ('bcc.s', -1, ''),  # Bcc CS blo.b .. ?   
   '0x65': ('blo.b', -1, ''),  # Bcc CS blo.b .. ?   

   '0x66': ('bne.b', 2, ''),  # dc.w    $6600  | in compiled output 

   '0x70': ('moveq', -1, ', d0'),
   '0x76': ('moveq', -1, ', d3'),
   '0x7a': ('moveq', -1, ', d5'),

   '0x908d': ('sub.l', 0, 'a5,d0'),

   '0xb81b': ('cmp.b', 0, ' (a3)+,d4'),
   '0xd7c5': ('add.l', 0, 'd5,a3'), 
   }


def main():
    infile = sys.argv[1]
    with open(infile, 'rb') as f:
        while 1: 
            b = f.read(2)
            if not b:
                break
            i = f.tell()
            if i > 64:
                k = f'{b[0]:#0{4}x}' + f'{b[1]:#0{4}x}'[2:]
                moveq = k.startswith('0x7') or k.startswith('0x6')
                if k in KEYS or moveq:
                    if moveq:
                        op, d, end = KEYS[k[:4]]
                    else:
                        op, d, end = KEYS[k]
                    if d == -1:
                        data = k[4:] 
                    else:
                        data = ''.join([f'{v:#0{4}x}'[2:] for v in f.read(d)])
                    if data:
                        data = '0x' + data
                    print(f'{k}: {op} {data}{end}')
                else:
                    print( f"{i}: {k}")


if __name__ == '__main__':
    main()

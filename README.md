# python-Z80-Disassember

## Introduction:

This is a very simple Z80 disassembler for a project to reverse engineer the operations of an old 'homebrew' 8-bit computer. The original owner had dumped the ROM to a 4KB binary file. The code was designed to be quick to write (less than a day), faster to run and just do what was required - nothing fancy.

## Usage:
The code reads in a binary dump of the ROM and prints the disassembled code and symbol table to STDOUT

```
~/Projects/Z80$ ./dasm.py 
usage: -b <binfile> | --bin <binfile>
```

## Example run:

Using the following command line:

```
~/Projects/Z80$ ./dasm.py -b 'tos 4-15.bin' -s symbol.txt > dump.asm
```

The input file looked like:
```
~/Projects/Go/src/hexdump$ ./hexdump 'tos 4-15.bin' 
0000 :  31 00 00 c3 74 e0 ff ff c3 e3 e3 ff ff ff ff ff  : 1...t...........
0010 :  c3 e6 e3 ff ff ff ff ff ff ff ff ff ff ff ff ff  : ................
0020 :  ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff  : ................
0030 :  ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff  : ................
0040 :  ff ff ff ff ff ff ff ff ff ff ff 7c cd b7 e3 7d  : ...........|...}
0050 :  cd b7 e3 3e 20 cd e6 e3 06 08 3e 20 cd e6 e3 0e  : ...> .....> ....
0060 :  02 7e cd b7 e3 23 0d 20 f8 10 ef 3e 20 cd e6 e3  : .~...#. ...> ...
0070 :  c9 ff ff ff 3e ff d3 02 d3 02 d3 03 3e 00 d3 03  : ....>.......>...
0080 :  db 00 e6 8f d3 01 cb 07 30 f6 db 00 e6 8f d3 01  : ........0.......
0090 :  cb 07 38 f6 3e 00 d3 01 11 ac e0 db 00 e6 0f 87  : ..8.>...........
00A0 :  83 5f 1a 6f 13 1a 67 a5 3c 28 d5 e9 00 00 00 e1  : ._.o..g.<(......
```

example output disassmbled file started:

```
0000 31 00 00     :           LD SP,0000  [SYM_0000]
0003 C3 74 E0     :           JP E074  [SYM_E074]
0006 FF           :           RST 38
0007 FF           :           RST 38
0008 C3 E3 E3     :           JP E3E3  [SYM_E3E3]
000B FF           :           RST 38
000C FF           :           RST 38
000D FF           :           RST 38
000E FF           :           RST 38
000F FF           :           RST 38
0010 C3 E6 E3     :           JP E3E6  [SYM_E3E6]
```

At the very end of the disassembly, the symbol table is dumped out:

```
SYM_0000 = 0000
SYM_E074 = E074
SYM_E3E3 = E3E3
SYM_E3E6 = E3E6
SYM_E3B7 = E3B7
SYM_0061 = 0061
SYM_005A = 005A
SYM_0080 = 0080
SYM_008A = 008A
SYM_E0AC = E0AC
SYM_E300 = E300
```

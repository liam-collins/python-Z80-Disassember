#!/usr/bin/env python3
"""Z80 Disassembler:

    This is a very simple Z80 disassembler for a project to reverse engineer 
    the operations of an old 'homebrew' 8-bit computer. The original owner 
    had dumped the ROM to a 4KB binary file.

    The code works by using lookup tables to covert the op-code to a mnemonic, 
    op-code size and if a label (address) needs to be generated for a symbol
    table. Normal opcode use the 'opcode' dictionary while the extended ones
    (see below) used their own: cb_opcode, dd_opcode, ed_opcode and fd_opcode.

    The Z80 op-codes are fairly simple for most hex-values but the ones starting
    with '0xCB', '0xDD', '0xED' and '0xFD' have extended features that need to
    be handled seperately.

    The format of the lookup tables are the same:

        - mnenomic              The name of the opcode
        - instruction_length    How many bytes does the instruction take up
        - symbols               Does the instruction use a memory location. If
                                it does then remember the address so that it can
                                be added to the symbol table
        - relative_addr         Is the address used absolute location or relative
                                to the current program counter (PC)?

    The code was designed to be quick to write (less than a day), faster to run
    and just do what was required - nothing fancy.
"""
from optparse import OptionParser
import os
import sys
from opcode import opcode, cb_opcode, dd_opcode, ed_opcode, fd_opcode

def init() :
    """This just handle the argument processing and reading in the dumped
        ROM into memory for later processing
    """
    parser = OptionParser()
    parser.add_option( '-b', '--bin', dest='binfile', default=None)
    (opt, arg) = parser.parse_args()

    if not opt.binfile :
        print( 'usage: -b <binfile> | --bin <binfile>')
        sys.exit(1)

    try:
        with open( opt.binfile, 'rb' ) as fh :
            memory = fh.read()
    
    except Exception as  e:
        print( e )
        sys.exit(1)

    return( memory )

# Useful Constants...

mem = [ 0XD5, 0X1B, 0X7A, 0XB3, 0X00, 0X20, 0XFA, 0XD1, 0XC9 ]

EXTENDED_CB = 0xcb
EXTENDED_DD = 0xdd
EXTENDED_ED = 0xed
EXTENDED_FD = 0xfd

OPCODE_NEEDS_BYTE = 2
OPCODE_NEEDS_WORD = 3
NORMAL_OPCODE_SIZE = 1
EXTENDED_OPCODE_SIZE = 2
EXTENDED_OPCODE_OFFSET = 1
EXTEND_BYTE_OFFSET = 2
EXTEND_HI_BYTE_OFFSET = 3
NORMAL_BYTE_OFFSET = 1
NORMAL_HI_BYTE_OFFSET = 2

BYTE_FORMAT = '{:02X}'
WORD_FORMAT = '{:04X}'
ADDR_FORMAT = '{:02X}{:02X}'
TAB_FORMAT  = '{:12.12s}'

def get_opcode( pc, memory, symbol_table ) :
    """Using the current program counter (PC), look in the loaded Z80
        memory and convert the hex-value to a mnemonic. The code returns:

            new_pc:         The next location in memory to be disassembled
            pretty_pc:      Pretty (printable) version of the PC
            opcode_value:   Nicely formated (hex-printable) version of
                            the instruction and any values/addresses
            pretty_mnenomic:Printable mnemoic and symbols/values
            symbol_table:   New version of the symbol table dictionary

        The code is fairly simple as it uses lookup tables to do the 
        'heavy lifting'.
    """
    opcode_byte = memory[ pc ]
    opcode_hex = BYTE_FORMAT.format( opcode_byte )
    instruction_length = 0
    low_byte = None
    hi_byte = None
    label = None
    opcode_entry = opcode[ opcode_hex ]

    # If this is one of the extended OP-codes that work out which table
    # needs to be used and lookup that byte in it.
    if not opcode_entry :
        extended_opcode_hex = BYTE_FORMAT.format( memory[ pc + EXTENDED_OPCODE_OFFSET] )
        if opcode_byte == EXTENDED_CB :
            extended_opcode_entry = cb_opcode[ extended_opcode_hex ]
        elif opcode_byte == EXTENDED_DD :
            extended_opcode_entry = dd_opcode[ extended_opcode_hex ]
        elif opcode_byte == EXTENDED_ED :
            extended_opcode_entry = ed_opcode[ extended_opcode_hex ] 
        elif opcode_byte == EXTENDED_FD :
            extended_opcode_entry = fd_opcode[ extended_opcode_hex ] 
        else :
            print( 'Something very bad happened')
            print( extended_opcode_hex )            
            sys.exit(1)

        ( mnenomic, instruction_length, symbols, relative_addr ) = extended_opcode_entry

        # If the opcode uses a memory location then generate a symbol and workout the
        # address (hi_byte and low_byte) for later conversion
        if symbols :
            number_value_bytes = instruction_length - EXTENDED_OPCODE_SIZE
            low_byte = memory[pc + EXTEND_BYTE_OFFSET ]
            if number_value_bytes == OPCODE_NEEDS_BYTE :
                hi_byte = memory[pc + EXTEND_HI_BYTE_OFFSET ]

        opcode_value =  BYTE_FORMAT.format( opcode_byte ) + " " + \
                        BYTE_FORMAT.format( memory[ pc + EXTENDED_OPCODE_OFFSET] )

    else :
        ( mnenomic, instruction_length, symbols, relative_addr ) = opcode_entry

        # If the opcode uses a memory location then generate a symbol and workout the
        # address (hi_byte and low_byte) for later conversion
        if symbols :
            number_value_bytes = instruction_length - NORMAL_OPCODE_SIZE
            low_byte = memory[pc + NORMAL_BYTE_OFFSET ]
            if number_value_bytes == OPCODE_NEEDS_BYTE :
                hi_byte = memory[pc + NORMAL_HI_BYTE_OFFSET ]
        
        opcode_value = BYTE_FORMAT.format( opcode_byte )

    if low_byte == None :
        pretty_mnenomic = mnenomic
    elif hi_byte == None :
        pretty_mnenomic = mnenomic.format( byte=low_byte )
        opcode_value += " " + BYTE_FORMAT.format( low_byte )
        
        # Relative addressing is where the address is not absolute but
        # based on the Z80's program counter (PC). This value is a
        # signed 8-bit number so that it can address up and down memory
        if relative_addr :
            if low_byte > 127 :
                rel_pc = low_byte - 256
            else :
                rel_pc = low_byte

            label = 'SYM_' + WORD_FORMAT.format(pc + instruction_length + rel_pc)
            symbol_table[ label ] = WORD_FORMAT.format(pc + instruction_length + rel_pc)
            pretty_mnenomic += '  [{}]'.format(label)

    else :
        label = 'SYM_'+ ADDR_FORMAT.format(hi_byte, low_byte )
        symbol_table[ label ] = ADDR_FORMAT.format(hi_byte, low_byte )
        pretty_mnenomic = mnenomic.format( hi_byte=hi_byte, low_byte=low_byte ) + \
                            '  [{}]'.format(label)
        opcode_value += " " + BYTE_FORMAT.format( low_byte ) + \
                         " " + BYTE_FORMAT.format( hi_byte )

    pretty_pc = WORD_FORMAT.format( pc )
    
    pc = pc + instruction_length

    opcode_value = '{:12.12s}'.format(opcode_value +  20*' ' )

    return ( pc, pretty_pc, opcode_value, pretty_mnenomic, symbol_table )
                

if __name__ == "__main__" :
    memory = init()

    pc = 0
    mem_size = len(memory)
    symbol_table = {}

    # This is a simple disassembly of the ROM and does not try to do any
    # logic follow analysis. Basically it starts a memory address 0000H 
    # and steps through memory until it runs out of opcodes to process
    # (mem_size). This means that it will disassemble any lookup tables
    # in memory but that was not seen as much of a problem.
    while pc < mem_size :
        ( pc, prt_pc, prt_op, mne, symbol_table ) = get_opcode( pc, memory, symbol_table )
        print( '{} {} :           {}'.format( prt_pc, prt_op, mne ))
    
    for label in symbol_table :
        print( '{} = {}'.format( label, symbol_table[ label ]))

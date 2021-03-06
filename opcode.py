"""
    Z80 Opcode Tables
    =================

    opcode      : Standard Op-Codes
    cb_opcode   : Extended set with the starting byte "CB xx..."
    dd_opcode   : Extended set with the starting byte "DD xx..."
    ed_opcode   : Extended set with the starting byte "EE xx..."
    fd_opcode   : Extended set with the starting byte "FD xx..."

    Each table is a dictionary that returns a tuple with the following
    format:

        <string> :  Op-code Mnenomic
                    When the op-code has extra bytes (values or addresses)
                    it will contain one of the following string "format"
                    labels:
                        + {byte:02X}     - This is a single byte
                        + (hi_byte:02X)  - This is the high order byte of 16 bits
                        + {low_byte:02X} - This is the low order byte of 16 bits

        <int>   :   Number of bytes the op-code uses including itself.
                    For the "extended" op-codes ('CB', 'DD', 'ED' and 'FD')
                    the associated tables show the extended op-code (second byte)
                    but the byte count is the length of the full op-code.
                    e.g.:

                    The op-code for "LD IX,(<address>)", part of the 'DD' 
                    extended set has the entry "2A" and an op-code length
                    of "4" as the full op-code is "DD 2A xx xx"

        <boolean>:  This command contains an address that would be label in 
                    the original code. The user code can use this information
                    to create a symbol table that contains addresses or values.
                    REMEMBER: Some commands use relative addresses, from the PC,
                    so they will only have a byte value but will need to be
                    converted to a 16 bit address.
"""

opcode = {
    '00' : ( 'NOP',1, False, False ),
    '01' : ( 'LD BC,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    '02' : ( 'LD (BC),A',1, False, False ),
    '03' : ( 'INC BC',1, False, False ),
    '04' : ( 'INC B',1, False, False ),
    '05' : ( 'DEC B',1, False, False ),
    '06' : ( 'LD B,{byte:02X}',2, True, False ),
    '07' : ( 'RLCA',1, False, False ),
    '08' : ( 'EX AF,AF???',1, False, False ),
    '09' : ( 'AHL,BC',1, False, False ),
    '0A' : ( 'LD A,(BC)',1, False, False ),
    '0B' : ( 'DEC BC',1, False, False ),
    '0C' : ( 'INC C',1, False, False ),
    '0D' : ( 'DEC C',1, False, False ),
    '0E' : ( 'LD C,{byte:02X}',2, True, False ),
    '0F' : ( 'RRCA',1, False, False ),
    '10' : ( 'DJNZ {byte:02X}',2, True, True ),
    '11' : ( 'LD DE,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    '12' : ( 'LD (DE),A',1, False, False ),
    '13' : ( 'INC DE',1, False, False ),
    '14' : ( 'INC D',1, False, False ),
    '15' : ( 'DEC D',1, False, False ),
    '16' : ( 'LD D,{byte:02X}',2, True, False ),
    '17' : ( 'RLA',1, False, False ),
    '18' : ( 'JR {byte:02X}',2, True, True ),
    '19' : ( 'ADD HL,DE',1, False, False ),
    '1A' : ( 'LD A,(DE)',1, False, False ),
    '1B' : ( 'DEC DE',1, False, False ),
    '1C' : ( 'INC E',1, False, False ),
    '1D' : ( 'DEC E',1, False, False ),
    '1E' : ( 'LD E,{byte:02X}',2, True, False ),
    '1F' : ( 'RRA',1, False, False ),
    '20' : ( 'JR NZ,{byte:02X}',2, True, True ),
    '21' : ( 'LD HL,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    '22' : ( 'LD ({hi_byte:02X}{low_byte:02X}),HL',3, True, False ),
    '23' : ( 'INC HL',1, False, False ),
    '24' : ( 'INC H',1, False, False ),
    '25' : ( 'DEC H',1, False, False ),
    '26' : ( 'LD H,{byte:02X}',2, True, False ),
    '27' : ( 'DAA',1, False, False ),
    '28' : ( 'JR Z,{byte:02X}',2, True, True ),
    '29' : ( 'AHL,HL',1, False, False ),
    '2A' : ( 'LD HL,({hi_byte:02X}{low_byte:02X})',3, True, False ),
    '2B' : ( 'DEC HL',1, False, False ),
    '2C' : ( 'INC L',1, False, False ),
    '2D' : ( 'DEC L',1, False, False ),
    '2E' : ( 'LD L,{byte:02X}',2, True, False ),
    '2F' : ( 'CPL',1, False, False ),
    '30' : ( 'JR NC,{byte:02X}',2, True, True ),
    '31' : ( 'LD SP,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    '32' : ( 'LD ({hi_byte:02X}{low_byte:02X}),A',3, True, False ),
    '33' : ( 'INC SP',1, False, False ),
    '34' : ( 'INC (HL)',1, False, False ),
    '35' : ( 'DEC (HL)',1, False, False ),
    '36' : ( 'LD (HL),{byte:02X}',2, True, False ),
    '37' : ( 'SCF',1, False, False ),
    '38' : ( 'JR C,{byte:02X}',2, True, True ),
    '39' : ( 'AHL,SP',1, False, False ),
    '3A' : ( 'LD A,({hi_byte:02X}{low_byte:02X})',3, True, False ),
    '3B' : ( 'DEC SP',1, False, False ),
    '3C' : ( 'INC A',1, False, False ),
    '3D' : ( 'DEC A',1, False, False ),
    '3E' : ( 'LD A,{byte:02X}',2, True, False ),
    '3F' : ( 'CCF',1, False, False ),
    '40' : ( 'LD B,B',1, False, False ),
    '41' : ( 'LD B,C',1, False, False ),
    '42' : ( 'LD B,D',1, False, False ),
    '43' : ( 'LD B,E',1, False, False ),
    '44' : ( 'LD B,H',1, False, False ),
    '45' : ( 'LD B,L',1, False, False ),
    '46' : ( 'LD B,(HL)',1, False, False ),
    '47' : ( 'LD B,A',1, False, False ),
    '48' : ( 'LD C,B',1, False, False ),
    '49' : ( 'LD C,C',1, False, False ),
    '4A' : ( 'LD C,D',1, False, False ),
    '4B' : ( 'LD C,E',1, False, False ),
    '4C' : ( 'LD C,H',1, False, False ),
    '4D' : ( 'LD C,L',1, False, False ),
    '4E' : ( 'LD C,(HL)',1, False, False ),
    '4F' : ( 'LD C,A',1, False, False ),
    '50' : ( 'LD D,B',1, False, False ),
    '51' : ( 'LD D,C',1, False, False ),
    '52' : ( 'LD D,D',1, False, False ),
    '53' : ( 'LD D,E',1, False, False ),
    '54' : ( 'LD D,H',1, False, False ),
    '55' : ( 'LD D,L',1, False, False ),
    '56' : ( 'LD D,(HL)',1, False, False ),
    '57' : ( 'LD D,A',1, False, False ),
    '58' : ( 'LD E,B',1, False, False ),
    '59' : ( 'LD E,C',1, False, False ),
    '5A' : ( 'LD E,D',1, False, False ),
    '5B' : ( 'LD E,E',1, False, False ),
    '5C' : ( 'LD E,H',1, False, False ),
    '5D' : ( 'LD E,L',1, False, False ),
    '5E' : ( 'LD E,(HL)',1, False, False ),
    '5F' : ( 'LD E,A',1, False, False ),
    '60' : ( 'LD H,B',1, False, False ),
    '61' : ( 'LD H,C',1, False, False ),
    '62' : ( 'LD H,D',1, False, False ),
    '63' : ( 'LD H,E',1, False, False ),
    '64' : ( 'LD H,H',1, False, False ),
    '65' : ( 'LD H,L',1, False, False ),
    '66' : ( 'LD H,(HL)',1, False, False ),
    '67' : ( 'LD H,A',1, False, False ),
    '68' : ( 'LD L,B',1, False, False ),
    '69' : ( 'LD L,C',1, False, False ),
    '6A' : ( 'LD L,D',1, False, False ),
    '6B' : ( 'LD L,E',1, False, False ),
    '6C' : ( 'LD L,H',1, False, False ),
    '6D' : ( 'LD L,L',1, False, False ),
    '6E' : ( 'LD L,(HL)',1, False, False ),
    '6F' : ( 'LD L,A',1, False, False ),
    '70' : ( 'LD (HL),B',1, False, False ),
    '71' : ( 'LD (HL),C',1, False, False ),
    '72' : ( 'LD (HL),D',1, False, False ),
    '73' : ( 'LD (HL),E',1, False, False ),
    '74' : ( 'LD (HL),H',1, False, False ),
    '75' : ( 'LD (HL),L',1, False, False ),
    '76' : ( 'HALT',1, False, False ),
    '77' : ( 'LD (HL),A',1, False, False ),
    '78' : ( 'LD A,B',1, False, False ),
    '79' : ( 'LD A,C',1, False, False ),
    '7A' : ( 'LD A,D',1, False, False ),
    '7B' : ( 'LD A,E',1, False, False ),
    '7C' : ( 'LD A,H',1, False, False ),
    '7D' : ( 'LD A,L',1, False, False ),
    '7E' : ( 'LD A,(HL)',1, False, False ),
    '7F' : ( 'LD A,A',1, False, False ),
    '80' : ( 'AA,B',1, False, False ),
    '81' : ( 'AA,C',1, False, False ),
    '82' : ( 'AA,D',1, False, False ),
    '83' : ( 'AA,E',1, False, False ),
    '84' : ( 'AA,H',1, False, False ),
    '85' : ( 'AA,L',1, False, False ),
    '86' : ( 'AA,(HL)',1, False, False ),
    '87' : ( 'AA,A',1, False, False ),
    '88' : ( 'ADC A,B',1, False, False ),
    '89' : ( 'ADC A,C',1, False, False ),
    '8A' : ( 'ADC A,D',1, False, False ),
    '8B' : ( 'ADC A,E',1, False, False ),
    '8C' : ( 'ADC A,H',1, False, False ),
    '8D' : ( 'ADC A,L',1, False, False ),
    '8E' : ( 'ADC A,(HL)',1, False, False ),
    '8F' : ( 'ADC A,A',1, False, False ),
    '90' : ( 'SUB A,B',1, False, False ),
    '91' : ( 'SUB A,C',1, False, False ),
    '92' : ( 'SUB A,D',1, False, False ),
    '93' : ( 'SUB A,E',1, False, False ),
    '94' : ( 'SUB A,H',1, False, False ),
    '95' : ( 'SUB A,L',1, False, False ),
    '96' : ( 'SUB A,(HL)',1, False, False ),
    '97' : ( 'SUB A,A',1, False, False ),
    '98' : ( 'SBC A,B',1, False, False ),
    '99' : ( 'SBC A,C',1, False, False ),
    '9A' : ( 'SBC A,D',1, False, False ),
    '9B' : ( 'SBC A,E',1, False, False ),
    '9C' : ( 'SBC A,H',1, False, False ),
    '9D' : ( 'SBC A,L',1, False, False ),
    '9E' : ( 'SBC A,(HL)',1, False, False ),
    '9F' : ( 'SBC A,A',1, False, False ),
    'A0' : ( 'AND B',1, False, False ),
    'A1' : ( 'AND C',1, False, False ),
    'A2' : ( 'AND D',1, False, False ),
    'A3' : ( 'AND E',1, False, False ),
    'A4' : ( 'AND H',1, False, False ),
    'A5' : ( 'AND L',1, False, False ),
    'A6' : ( 'AND (HL)',1, False, False ),
    'A7' : ( 'AND A',1, False, False ),
    'A8' : ( 'XOR B',1, False, False ),
    'A9' : ( 'XOR C',1, False, False ),
    'AA' : ( 'XOR D',1, False, False ),
    'AB' : ( 'XOR E',1, False, False ),
    'AC' : ( 'XOR H',1, False, False ),
    'AD' : ( 'XOR L',1, False, False ),
    'AE' : ( 'XOR (HL)',1, False, False ),
    'AF' : ( 'XOR A',1, False, False ),
    'B0' : ( 'OR B',1, False, False ),
    'B1' : ( 'OR C',1, False, False ),
    'B2' : ( 'OR D',1, False, False ),
    'B3' : ( 'OR E',1, False, False ),
    'B4' : ( 'OR H',1, False, False ),
    'B5' : ( 'OR L',1, False, False ),
    'B6' : ( 'OR (HL)',1, False, False ),
    'B7' : ( 'OR A',1, False, False ),
    'B8' : ( 'CP B',1, False, False ),
    'B9' : ( 'CP C',1, False, False ),
    'BA' : ( 'CP D',1, False, False ),
    'BB' : ( 'CP E',1, False, False ),
    'BC' : ( 'CP H',1, False, False ),
    'BD' : ( 'CP L',1, False, False ),
    'BE' : ( 'CP (HL)',1, False, False ),
    'BF' : ( 'CP A',1, False, False ),
    'C0' : ( 'RET NZ',1, False, False ),
    'C1' : ( 'POP BC',1, False, False ),
    'C2' : ( 'JP NZ,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'C3' : ( 'JP {hi_byte:02X}{low_byte:02X}',3, True, False ),
    'C4' : ( 'CALL NZ,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'C5' : ( 'PUSH BC',1, False, False ),
    'C6' : ( 'AA,{byte:02X}',2, True, False ),
    'C7' : ( 'RST 00',1, False, False ),
    'C8' : ( 'RET Z',1, False, False ),
    'C9' : ( 'RET',1, False, False ),
    'CA' : ( 'JP Z,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'CB' : None,
    'CC' : ( 'CALL Z,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'CD' : ( 'CALL {hi_byte:02X}{low_byte:02X}',3, True, False ),
    'CE' : ( 'ADC A,{byte:02X}',2, True, False ),
    'CF' : ( 'RST 08',1, False, False ),
    'D0' : ( 'RET NC',1, False, False ),
    'D1' : ( 'POP DE',1, False, False ),
    'D2' : ( 'JP NC,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'D3' : ( 'OUT ({byte:02X}),A',2, True, False ),
    'D4' : ( 'CALL NC,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'D5' : ( 'PUSH DE',1, False, False ),
    'D6' : ( 'SUB A,{byte:02X}',2, True, False ),
    'D7' : ( 'RST 10',1, False, False ),
    'D8' : ( 'RET C',1, False, False ),
    'D9' : ( 'EXX',1, False, False ),
    'DA' : ( 'JP C,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'DB' : ( 'IN A,({byte:02X})',2, True, False ),
    'DC' : ( 'CALL C,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'DD' : None,
    'DE' : ( 'SBC A,{byte:02X}',2, True, False ),
    'DF' : ( 'RST 18',1, False, False ),
    'E0' : ( 'RET PO',1, False, False ),
    'E1' : ( 'POP HL',1, False, False ),
    'E2' : ( 'JP PO,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'E3' : ( 'EX (SP),HL',1, False, False ),
    'E4' : ( 'CALL PO,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'E5' : ( 'PUSH HL',1, False, False ),
    'E6' : ( 'AND {byte:02X}',2, True, False ),
    'E7' : ( 'RST 20',1, False, False ),
    'E8' : ( 'RET PE',1, False, False ),
    'E9' : ( 'JP (HL)',1, False, False ),
    'EA' : ( 'JP PE,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'EB' : ( 'EX DE,HL',1, False, False ),
    'EC' : ( 'CALL P,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'ED' :  None,
    'EE' : ( 'XOR {byte:02X}',2, True, False ),
    'EF' : ( 'RST 28',1, False, False ),
    'F0' : ( 'RET P',1, False, False ),
    'F1' : ( 'POP AF',1, False, False ),
    'F2' : ( 'JP P,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'F3' : ( 'DI',1, False, False ),
    'F4' : ( 'CALL P,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'F5' : ( 'PUSH AF',1, False, False ),
    'F6' : ( 'OR {byte:02X}',2, True, False ),
    'F7' : ( 'RST 30',1, False, False ),
    'F8' : ( 'RET M',1, False, False ),
    'F9' : ( 'LD SP,HL',1, False, False ),
    'FA' : ( 'JP M,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'FB' : ( 'EI',1, False, False ),
    'FC' : ( 'CALL M,{hi_byte:02X}{low_byte:02X}',3, True, False ),
    'FD' : None,
    'FE' : ( 'CP {byte:02X}',2, True, False ),
    'FF' : ( 'RST 38',1, False, False ),
}

"""
    The second byte values for the extended op-code set 'CB xx'

    The op-codes mainly focus around rotate and bit operations
"""
cb_opcode = {
    '00' : ( 'RLC B',2, False, False ),
    '01' : ( 'RLC C',2, False, False ),
    '02' : ( 'RLC D',2, False, False ),
    '03' : ( 'RLC E',2, False, False ),
    '04' : ( 'RLC H',2, False, False ),
    '05' : ( 'RLC L',2, False, False ),
    '06' : ( 'RLC (HL)',2, False, False ),
    '07' : ( 'RLC A',2, False, False ),
    '08' : ( 'RRC B',2, False, False ),
    '09' : ( 'RRC C',2, False, False ),
    '0A' : ( 'RRC D',2, False, False ),
    '0B' : ( 'RRC E',2, False, False ),
    '0E' : ( 'RRC (HL)',2, False, False ),
    '0F' : ( 'RRC A',2, False, False ),
    '10' : ( 'RL B',2, False, False ),
    '11' : ( 'RL C',2, False, False ),
    '12' : ( 'RL D',2, False, False ),
    '13' : ( 'RL E',2, False, False ),
    '14' : ( 'RL H',2, False, False ),
    '15' : ( 'RL L',2, False, False ),
    '16' : ( 'RL (HL)',2, False, False ),
    '17' : ( 'RL A',2, False, False ),
    '18' : ( 'RR B',2, False, False ),
    '19' : ( 'RR C',2, False, False ),
    '1A' : ( 'RR D',2, False, False ),
    '1B' : ( 'RR E',2, False, False ),
    '1C' : ( 'RR H',2, False, False ),
    '1D' : ( 'RR L',2, False, False ),
    '1E' : ( 'RR (HL)',2, False, False ),
    '1F' : ( 'RR A',2, False, False ),
    '20' : ( 'SLA B',2, False, False ),
    '21' : ( 'SLA C',2, False, False ),
    '22' : ( 'SLA D',2, False, False ),
    '23' : ( 'SLA E',2, False, False ),
    '24' : ( 'SLA H',2, False, False ),
    '25' : ( 'SLA L',2, False, False ),
    '26' : ( 'SLA (HL)',2, False, False ),
    '27' : ( 'SLA A',2, False, False ),
    '28' : ( 'SRA B',2, False, False ),
    '29' : ( 'SRA C',2, False, False ),
    '2A' : ( 'SRA D',2, False, False ),
    '2B' : ( 'SRA E',2, False, False ),
    '2C' : ( 'SRA H',2, False, False ),
    '2D' : ( 'SRA L',2, False, False ),
    '2E' : ( 'SRA (HL)',2, False, False ),
    '2F' : ( 'SRA A',2, False, False ),
    '30' : ( 'SLS B',2, False, False ),
    '31' : ( 'SLS C',2, False, False ),
    '32' : ( 'SLS D',2, False, False ),
    '33' : ( 'SLS E',2, False, False ),
    '34' : ( 'SLS H',2, False, False ),
    '35' : ( 'SLS L',2, False, False ),
    '36' : ( 'SLS (HL)',2, False, False ),
    '37' : ( 'SLS A',2, False, False ),
    '38' : ( 'SRL B',2, False, False ),
    '39' : ( 'SRL C',2, False, False ),
    '3A' : ( 'SRL D',2, False, False ),
    '3B' : ( 'SRL E',2, False, False ),
    '3C' : ( 'SRL H',2, False, False ),
    '3D' : ( 'SRL L',2, False, False ),
    '3E' : ( 'SRL (HL)',2, False, False ),
    '3F' : ( 'SRL A',2, False, False ),
    '40' : ( 'BIT 0,B',2, False, False ),
    '41' : ( 'BIT 0,C',2, False, False ),
    '42' : ( 'BIT 0,D',2, False, False ),
    '43' : ( 'BIT 0,E',2, False, False ),
    '44' : ( 'BIT 0,H',2, False, False ),
    '45' : ( 'BIT 0,L',2, False, False ),
    '46' : ( 'BIT 0,(HL)',2, False, False ),
    '47' : ( 'BIT 0,A',2, False, False ),
    '48' : ( 'BIT 1,B',2, False, False ),
    '49' : ( 'BIT 1,C',2, False, False ),
    '4A' : ( 'BIT 1,D',2, False, False ),
    '4B' : ( 'BIT 1,E',2, False, False ),
    '4C' : ( 'BIT 1,H',2, False, False ),
    '4D' : ( 'BIT 1,L',2, False, False ),
    '4E' : ( 'BIT 1,(HL)',2, False, False ),
    '4F' : ( 'BIT 1,A',2, False, False ),
    '50' : ( 'BIT 2,B',2, False, False ),
    '51' : ( 'BIT 2,C',2, False, False ),
    '52' : ( 'BIT 2,D',2, False, False ),
    '53' : ( 'BIT 2,E',2, False, False ),
    '54' : ( 'BIT 2,H',2, False, False ),
    '55' : ( 'BIT 2,L',2, False, False ),
    '56' : ( 'BIT 2,(HL)',2, False, False ),
    '57' : ( 'BIT 2,A',2, False, False ),
    '58' : ( 'BIT 3,B',2, False, False ),
    '59' : ( 'BIT 3,C',2, False, False ),
    '5A' : ( 'BIT 3,D',2, False, False ),
    '5B' : ( 'BIT 3,E',2, False, False ),
    '5C' : ( 'BIT 3,H',2, False, False ),
    '5D' : ( 'BIT 3,L',2, False, False ),
    '5E' : ( 'BIT 3,(HL)',2, False, False ),
    '5F' : ( 'BIT 3,A',2, False, False ),
    '60' : ( 'BIT 4,B',2, False, False ),
    '61' : ( 'BIT 4,C',2, False, False ),
    '62' : ( 'BIT 4,D',2, False, False ),
    '63' : ( 'BIT 4,E',2, False, False ),
    '64' : ( 'BIT 4,H',2, False, False ),
    '65' : ( 'BIT 4,L',2, False, False ),
    '66' : ( 'BIT 4,(HL)',2, False, False ),
    '67' : ( 'BIT 4,A',2, False, False ),
    '68' : ( 'BIT 5,B',2, False, False ),
    '69' : ( 'BIT 5,C',2, False, False ),
    '6A' : ( 'BIT 5,D',2, False, False ),
    '6B' : ( 'BIT 5,',2, False, False ),
    '6C' : ( 'BIT 5,H',2, False, False ),
    '6D' : ( 'BIT 5,L',2, False, False ),
    '6E' : ( 'BIT 5,(HL)',2, False, False ),
    '6F' : ( 'BIT 5,A',2, False, False ),
    '70' : ( 'BIT 6,B',2, False, False ),
    '71' : ( 'BIT 6,C',2, False, False ),
    '72' : ( 'BIT 6,D',2, False, False ),
    '73' : ( 'BIT 6,E',2, False, False ),
    '74' : ( 'BIT 6,H',2, False, False ),
    '75' : ( 'BIT 6,L',2, False, False ),
    '76' : ( 'BIT 6,(HL)',2, False, False ),
    '77' : ( 'BIT 6,A',2, False, False ),
    '78' : ( 'BIT 7,B',2, False, False ),
    '79' : ( 'BIT 7,C',2, False, False ),
    '7A' : ( 'BIT 7,D',2, False, False ),
    '7B' : ( 'BIT 7,E',2, False, False ),
    '7C' : ( 'BIT 7,H',2, False, False ),
    '7D' : ( 'BIT 7,L',2, False, False ),
    '7E' : ( 'BIT 7,(HL)',2, False, False ),
    '7F' : ( 'BIT 7,A',2, False, False ),
    '80' : ( 'RES 0,B',2, False, False ),
    '81' : ( 'RES 0,C',2, False, False ),
    '82' : ( 'RES 0,D',2, False, False ),
    '83' : ( 'RES 0,E',2, False, False ),
    '84' : ( 'RES 0,H',2, False, False ),
    '85' : ( 'RES 0,L',2, False, False ),
    '86' : ( 'RES 0,(HL)',2, False, False ),
    '87' : ( 'RES 0,A',2, False, False ),
    '88' : ( 'RES 1,B',2, False, False ),
    '89' : ( 'RES 1,C',2, False, False ),
    '8A' : ( 'RES 1,D',2, False, False ),
    '8B' : ( 'RES 1,E',2, False, False ),
    '8C' : ( 'RES 1,H',2, False, False ),
    '8D' : ( 'RES 1,L',2, False, False ),
    '8E' : ( 'RES 1,(HL)',2, False, False ),
    '8F' : ( 'RES 1,A',2, False, False ),
    '90' : ( 'RES 2,B',2, False, False ),
    '91' : ( 'RES 2,C',2, False, False ),
    '92' : ( 'RES 2,D',2, False, False ),
    '93' : ( 'RES 2,E',2, False, False ),
    '94' : ( 'RES 2,H',2, False, False ),
    '95' : ( 'RES 2,L',2, False, False ),
    '96' : ( 'RES 2,(HL)',2, False, False ),
    '97' : ( 'RES 2,A',2, False, False ),
    '98' : ( 'RES 3,B',2, False, False ),
    '99' : ( 'RES 3,C',2, False, False ),
    '9A' : ( 'RES 3,D',2, False, False ),
    '9B' : ( 'RES 3,E',2, False, False ),
    '9C' : ( 'RES 3,H',2, False, False ),
    '9D' : ( 'RES 3,L',2, False, False ),
    '9E' : ( 'RES 3,(HL)',2, False, False ),
    '9F' : ( 'RES 3,A',2, False, False ),
    'A0' : ( 'RES 4,B',2, False, False ),
    'A1' : ( 'RES 4,C',2, False, False ),
    'A2' : ( 'RES 4,D',2, False, False ),
    'A3' : ( 'RES 4,',2, False, False ),
    'A4' : ( 'RES 4,H',2, False, False ),
    'A5' : ( 'RES 4,L',2, False, False ),
    'A6' : ( 'RES 4,(HL)',2, False, False ),
    'A7' : ( 'RES 4,A',2, False, False ),
    'A8' : ( 'RES 5,B',2, False, False ),
    'A9' : ( 'RES 5,C',2, False, False ),
    'AA' : ( 'RES 5,D',2, False, False ),
    'AB' : ( 'RES 5,E',2, False, False ),
    'AC' : ( 'RES 5,H',2, False, False ),
    'AD' : ( 'RES 5,L',2, False, False ),
    'AE' : ( 'RES 5,(HL)',2, False, False ),
    'AF' : ( 'RES 5,A',2, False, False ),
    'B0' : ( 'RES 6,B',2, False, False ),
    'B1' : ( 'RES 6,C',2, False, False ),
    'B2' : ( 'RES 6,D',2, False, False ),
    'B3' : ( 'RES 6,E',2, False, False ),
    'B4' : ( 'RES 6,H',2, False, False ),
    'B5' : ( 'RES 6,L',2, False, False ),
    'B6' : ( 'RES 6,(HL)',2, False, False ),
    'B7' : ( 'RES 6,A',2, False, False ),
    'B8' : ( 'RES 7,B',2, False, False ),
    'B9' : ( 'RES 7,C',2, False, False ),
    'BA' : ( 'RES 7,D',2, False, False ),
    'BB' : ( 'RES 7,E',2, False, False ),
    'BC' : ( 'RES 7,H',2, False, False ),
    'BD' : ( 'RES 7,L',2, False, False ),
    'BE' : ( 'RES 7,(HL)',2, False, False ),
    'BF' : ( 'RES 7,A',2, False, False ),
    'C0' : ( 'SET 0,B',2, False, False ),
    'C1' : ( 'SET 0,C',2, False, False ),
    'C2' : ( 'SET 0,D',2, False, False ),
    'C3' : ( 'SET 0,E',2, False, False ),
    'C4' : ( 'SET 0,H',2, False, False ),
    'C5' : ( 'SET 0,L',2, False, False ),
    'C6' : ( 'SET 0,(HL)',2, False, False ),
    'C7' : ( 'SET 0,A',2, False, False ),
    'C8' : ( 'SET 1,B',2, False, False ),
    'C9' : ( 'SET 1,C',2, False, False ),
    'CA' : ( 'SET 1,D',2, False, False ),
    'CB' : ( 'SET 1,E',2, False, False ),
    'CC' : ( 'SET 1,H',2, False, False ),
    'CD' : ( 'SET 1,L',2, False, False ),
    'CE' : ( 'SET 1,(HL)',2, False, False ),
    'CF' : ( 'SET 1,A',2, False, False ),
    'D0' : ( 'SET 2,B',2, False, False ),
    'D1' : ( 'SET 2,C',2, False, False ),
    'D2' : ( 'SET 2,D',2, False, False ),
    'D3' : ( 'SET 2,E',2, False, False ),
    'D4' : ( 'SET 2,H',2, False, False ),
    'D5' : ( 'SET 2,L',2, False, False ),
    'D6' : ( 'SET 2,(HL)',2, False, False ),
    'D7' : ( 'SET 2,A',2, False, False ),
    'D8' : ( 'SET 3,B',2, False, False ),
    'D9' : ( 'SET 3,C',2, False, False ),
    'DA' : ( 'SET 3,D',2, False, False ),
    'DB' : ( 'SET 3,E',2, False, False ),
    'DC' : ( 'SET 3,H',2, False, False ),
    'DD' : ( 'SET 3,L',2, False, False ),
    'DE' : ( 'SET 3,(HL)',2, False, False ),
    'DF' : ( 'SET 3,A',2, False, False ),
    'E0' : ( 'SET 4,B',2, False, False ),
    'E1' : ( 'SET 4,C',2, False, False ),
    'E2' : ( 'SET 4,D',2, False, False ),
    'E3' : ( 'SET 4,E',2, False, False ),
    'E4' : ( 'SET 4,H',2, False, False ),
    'E5' : ( 'SET 4,L',2, False, False ),
    'E6' : ( 'SET 4,(HL)',2, False, False ),
    'E7' : ( 'SET 4,A',2, False, False ),
    'E8' : ( 'SET 5,B',2, False, False ),
    'E9' : ( 'SET 5,C',2, False, False ),
    'EA' : ( 'SET 5,D',2, False, False ),
    'EB' : ( 'SET 5,E',2, False, False ),
    'EC' : ( 'SET 5,H',2, False, False ),
    'ED' : ( 'SET 5,L',2, False, False ),
    'EE' : ( 'SET 5,(HL)',2, False, False ),
    'EF' : ( 'SET 5,A',2, False, False ),
    'F0' : ( 'SET 6,B',2, False, False ),
    'F1' : ( 'SET 6,C',2, False, False ),
    'F2' : ( 'SET 6,D',2, False, False ),
    'F3' : ( 'SET 6,E',2, False, False ),
    'F4' : ( 'SET 6,H',2, False, False ),
    'F5' : ( 'SET 6,L',2, False, False ),
    'F6' : ( 'SET 6,(HL)',2, False, False ),
    'F7' : ( 'SET 6,A',2, False, False ),
    'F8' : ( 'SET 7,B',2, False, False ),
    'F9' : ( 'SET 7,C',2, False, False ),
    'FA' : ( 'SET 7,D',2, False, False ),
    'FB' : ( 'SET 7,E',2, False, False ),
    'FC' : ( 'SET 7,H',2, False, False ),
    'FD' : ( 'SET 7,L',2, False, False ),
    'FE' : ( 'SET 7,(HL)',2, False, False ),
    'FF' : ( 'SET 7,A',2, False, False ),
}

"""
    The second byte values for the extended op-code set 'DD xx'

    The op-codes mainly focus around the IX and IY registers
"""
dd_opcode = {
    '09' : ( 'AIX,BC',2, False, False ),
    '19' : ( 'AIX,DE',2, False, False ),
    '21' : ( 'LD IX,{hi_byte:02X}{low_byte:02X}',4, True, False ),
    '22' : ( 'LD ({hi_byte:02X}{low_byte:02X}),IX',4, True, False ),
    '23' : ( 'INC IX',2, False, False ),
    '24' : ( 'INC IXH',2, False, False ),
    '25' : ( 'DEC IXH',2, False, False ),
    '26' : ( 'LD IXH,{byte:02X}',3, True, False ), 
    '29' : ( 'AIX,IX',2, False, False ),
    '2A' : ( 'LD IX,({hi_byte:02X}{low_byte:02X})',4, True, False ),
    '2B' : ( 'DEC IX',2, False, False ),
    '2C' : ( 'INC IXL',2, False, False ),
    '2D' : ( 'DEC IXL',2, False, False ),
    '2E' : ( 'LD IXL,{byte:02X}',3, True, False ),
    '34' : ( 'INC (IX+{byte:02X})',3, True, False ),
    '35' : ( 'DEC (IX+{byte:02X})',3, True, False ),
    '39' : ( 'AIX,SP',2, False, False ),
    '44' : ( 'LD B,IXH',2, False, False ),
    '45' : ( 'LD B,IXL',2, False, False ),
    '46' : ( 'LD B,(IX+{byte:02X})',3, True, False ),
    '4C' : ( 'LD C,IXH',2, False, False ),
    '4D' : ( 'LD C,IXL',2, False, False ),
    '4E' : ( 'LD C,(IX+{byte:02X})',3, True, False ),
    '54' : ( 'LD D,IXH',2, False, False ),
    '55' : ( 'LD D,IXL',2, False, False ),
    '5E' : ( 'LD E,(IX+{byte:02X})',3, True, False ),
    '60' : ( 'LD IXH,B',2, False, False ),
    '61' : ( 'LD IXH,C',2, False, False ),
    '62' : ( 'LD IXH,D',2, False, False ),
    '63' : ( 'LD IXH,E',2, False, False ),
    '64' : ( 'LD IXH,IXH',2, False, False ),
    '65' : ( 'LD IXH,IXL',2, False, False ),
    '66' : ( 'LD H,(IX+{byte:02X})',3, True, False ),
    '67' : ( 'LD IXH,A',2, False, False ),
    '68' : ( 'LD IXL,B',2, False, False ),
    '69' : ( 'LD IXL,C',2, False, False ),
    '6A' : ( 'LD IXL,D',2, False, False ),
    '6B' : ( 'LD IXL,E',2, False, False ),
    '6C' : ( 'LD IXL,IXH',2, False, False ),
    '6D' : ( 'LD IXL,IXL',2, False, False ),
    '6E' : ( 'LD L,(IX+{byte:02X})',2, True, False ),
    '6F' : ( 'LD IXL,A',2, False, False ),
    '70' : ( 'LD (IX+{byte:02X}),B',3, True, False ),
    '71' : ( 'LD (IX+{byte:02X}),C',3, True, False ),
    '72' : ( 'LD (IX+{byte:02X}),D',3, True, False ),
    '73' : ( 'LD (IX+{byte:02X}),E',3, True, False ),
    '74' : ( 'LD (IX+{byte:02X}),H',3, True, False ),
    '75' : ( 'LD (IX+{byte:02X}),L',3, True, False ),
    '77' : ( 'LD (IX+{byte:02X}),A',3, True, False ),
    '7C' : ( 'LD A,IXH',2, False, False ),
    '7D' : ( 'LD A,IXL',2, False, False ),
    '7E' : ( 'LD A,(IX+{byte:02X})',3, True, False ),
    '84' : ( 'AA,IXH',2, False, False ),
    '85' : ( 'AA,IXL',2, False, False ),
    '86' : ( 'AA,(IX+{byte:02X})',3, True, False ),
    '8C' : ( 'ADC A,IXH',2, False, False ),
    '8D' : ( 'ADC A,IXL',2, False, False ),
    '8E' : ( 'ADC A,(IX+{byte:02X})',3, True, False ),
    '94' : ( 'SUB A,IXH',2, False, False ),
    '95' : ( 'SUB A,IXL',2, False, False ),
    '96' : ( 'SUB A,(IX+{byte:02X})',3, True, False ),
    '9C' : ( 'SBC A,IXH',2, False, False ),
    '9D' : ( 'SBC A,IXL',2, False, False ),
    '9E' : ( 'SBC A,(IX+{byte:02X})',3, True, False ),
    'A4' : ( 'AND IXH',2, False, False ),
    'A5' : ( 'AND IXL',2, False, False ),
    'A6' : ( 'AND (IX+{byte:02X})',3, True, False ),
    'AC' : ( 'XOR IXH',2, False, False ),
    'AD' : ( 'XOR IXL',2, False, False ),
    'AE' : ( 'XOR (IX+{byte:02X})',3, True, False ),
    'B4' : ( 'OR IXH',2, False, False ),
    'B5' : ( 'OR IXL',2, False, False ),
    'B6' : ( 'OR (IX+{byte:02X})',3, True, False ),
    'BC' : ( 'CP IXH',2, False, False ),
    'BD' : ( 'CP IXL',2, False, False ),
    'BE' : ( 'CP (IX+{byte:02X})',3, True, False ),
    'E1' : ( 'POP IX',2, False, False ),
    'E3' : ( 'EX (SP),IX',2, False, False ),
    'E5' : ( 'PUSH IX',2, False, False ),
    'E9' : ( 'JP (IX)',2, False, False ),
}

"""
    The second byte values for the extended op-code set 'ED xx'

    The op-codes mainly focus around IO operations 
"""
ed_opcode = {
'40' : ( 'IN B,(C)',2, False, False ),
'41' : ( 'OUT (C),B',2, False, False ),
'42' : ( 'SBC HL,BC',2, False, False ),
'43' : ( 'LD ({hi_byte:02X}{low_byte:02X}),BC',4, True, False ),
'44' : ( 'NEG',2, False, False ),
'45' : ( 'RETN',2, False, False ),
'46' : ( 'IM 0',2, False, False ),
'47' : ( 'LD I,A',2, False, False ),
'48' : ( 'IN C,(C)',2, False, False ),
'49' : ( 'OUT (C),C',2, False, False ),
'4A' : ( 'ADC HL,BC',2, False, False ),
'4B' : ( 'LD BC,({hi_byte:02X}{low_byte:02X})',4, True, False ),
'4D' : ( 'RETI',2, False, False ),
'4F' : ( 'LD R,A',2, False, False ),
'50' : ( 'IN D,(C)',2, False, False ),
'51' : ( 'OUT (C),D',2, False, False ),
'52' : ( 'SBC HL,DE',2, False, False ),
'53' : ( 'LD ({hi_byte:02X}{low_byte:02X}),DE',4, True, False ),
'56' : ( 'IM 1',2, False, False ),
'57' : ( 'LD A,I',2, False, False ),
'58' : ( 'IN E,(C)',2, False, False ),
'59' : ( 'OUT (C),E',2, False, False ),
'5A' : ( 'ADC HL,DE',2, False, False ),
'5B' : ( 'LD DE,({hi_byte:02X}{low_byte:02X})',4, True, False ),
'5E' : ( 'IM 2',2, False, False ),
'5F' : ( 'LD A,R',2, False, False ),
'60' : ( 'IN H,(C)',2, False, False ),
'61' : ( 'OUT (C),H',2, False, False ),
'62' : ( 'SBC HL,HL',2, False, False ),
'63' : ( 'LD ({hi_byte:02X}{low_byte:02X}),HL',4, True, False ),
'67' : ( 'RRD',2, False, False ),
'68' : ( 'IN L,(C)',2, False, False ),
'69' : ( 'OUT (C),L',2, False, False ),
'6A' : ( 'ADC HL,HL',2, False, False ),
'6B' : ( 'LD HL,({hi_byte:02X}{low_byte:02X})',4, True, False ),
'6F' : ( 'RLD',2, False, False ),
'70' : ( 'IN F,(C)',2, False, False ),
'71' : ( 'OUT (C),F',2, False, False ),
'72' : ( 'SBC HL,SP',2, False, False ),
'73' : ( 'LD ({hi_byte:02X}{low_byte:02X}),SP',4, True, False ),
'78' : ( 'IN A,(C)',2, False, False ),
'79' : ( 'OUT (C),A',2, False, False ),
'7A' : ( 'ADC HL,SP',2, False, False ),
'7B' : ( 'LD SP,({hi_byte:02X}{low_byte:02X})',4, True, False ),
'A0' : ( 'LDI',2, False, False ),
'A1' : ( 'CPI',2, False, False ),
'A2' : ( 'INI',2, False, False ),
'A3' : ( 'OTI',2, False, False ),
'A8' : ( 'LDD',2, False, False ),
'A9' : ( 'CPD',2, False, False ),
'AA' : ( 'IND',2, False, False ),
'AB' : ( 'OTD',2, False, False ),
'B0' : ( 'LDIR',2, False, False ),
'B1' : ( 'CPIR',2, False, False ),
'B2' : ( 'INIR',2, False, False ),
'B3' : ( 'OTIR',2, False, False ),
'B8' : ( 'LDDR',2, False, False ),
'B9' : ( 'CPDR',2, False, False ),
'BA' : ( 'INDR',2, False, False ),
'BB' : ( 'OTDR',2, False, False ),
}

"""
    The second byte values for the extended op-code set 'FD xx'

    The op-codes mainly focus around ...
"""
fd_opcode = {
    '09' : ( 'AIY,BC',2, False, False ),
    '19' : ( 'AIY,DE',2, False, False ),
    '21' : ( 'LD IY,{hi_byte:02X}{low_byte:02X}',4, True, False ),
    '22' : ( 'LD ({hi_byte:02X}{low_byte:02X}),IY',4, True, False ),
    '23' : ( 'INC IY',2, False, False ),
    '24' : ( 'INC IYH',2, False, False ),
    '25' : ( 'DEC IYH',2, False, False ),
    '26' : ( 'LD IYH,{byte:02X}',3, True, False ),
    '29' : ( 'AIY,IY',2, False, False ),
    '2A' : ( 'LD IY,({hi_byte:02X}{low_byte:02X})',4, True, False ),
    '2B' : ( 'DEC IY',2, False, False ),
    '2C' : ( 'INC IYL',2, False, False ),
    '2D' : ( 'DEC IYL',2, False, False ),
    '2E' : ( 'LD IYL,{byte:02X}',3, True, False ),
    '34' : ( 'INC (IY+{byte:02X})',3, True, False ),
    '35' : ( 'DEC (IY+{byte:02X})',3, True, False ),
    '39' : ( 'AIY,SP',2, False, False ),
    '44' : ( 'LD B,IYH',2, False, False ),
    '45' : ( 'LD B,IYL',2, False, False ),
    '46' : ( 'LD B,(IY+{byte:02X})',3, True, False ),
    '4C' : ( 'LD C,IYH',2, False, False ),
    '4D' : ( 'LD C,IYL',2, False, False ),
    '4E' : ( 'LD C,(IY+{byte:02X})',3, True, False ),
    '54' : ( 'LD D,IYH',2, False, False ),
    '55' : ( 'LD D,IYL',2, False, False ),
    '5E' : ( 'LD E,(IY+{byte:02X})',3, True, False ),
    '60' : ( 'LD IYH,B',2, False, False ),
    '61' : ( 'LD IYH,C',2, False, False ),
    '62' : ( 'LD IYH,D',2, False, False ),
    '63' : ( 'LD IYH,E',2, False, False ),
    '64' : ( 'LD IYH,IYH',2, False, False ),
    '65' : ( 'LD IYH,IYL',2, False, False ),
    '66' : ( 'LD H,(IY+{byte:02X})',3, True, False ),
    '67' : ( 'LD IYH,A',2, False, False ),
    '68' : ( 'LD IYL,B',2, False, False ),
    '69' : ( 'LD IYL,C',2, False, False ),
    '6A' : ( 'LD IYL,D',2, False, False ),
    '6B' : ( 'LD IYL,E',2, False, False ),
    '6C' : ( 'LD IYL,IYH',2, False, False ),
    '6D' : ( 'LD IYL,IYL',2, False, False ),
    '6E' : ( 'LD L,(IY+{byte:02X})',2, True, False ),
    '6F' : ( 'LD IYL,A',2, False, False ),
    '70' : ( 'LD (IY+{byte:02X}),B',3, True, False ),
    '71' : ( 'LD (IY+{byte:02X}),C',3, True, False ),
    '72' : ( 'LD (IY+{byte:02X}),D',3, True, False ),
    '73' : ( 'LD (IY+{byte:02X}),E',3, True, False ),
    '74' : ( 'LD (IY+{byte:02X}),H',3, True, False ),
    '75' : ( 'LD (IY+{byte:02X}),L',3, True, False ),
    '77' : ( 'LD (IY+{byte:02X}),A',3, True, False ),
    '7C' : ( 'LD A,IYH',2, False, False ),
    '7D' : ( 'LD A,IYL',2, False, False ),
    '7E' : ( 'LD A,(IY+{byte:02X})',3, True, False ),
    '84' : ( 'AA,IYH',2, False, False ),
    '85' : ( 'AA,IYL',2, False, False ),
    '86' : ( 'AA,(IY+{byte:02X})',3, True, False ),
    '8C' : ( 'ADC A,IYH',2, False, False ),
    '8D' : ( 'ADC A,IYL',2, False, False ),
    '8E' : ( 'ADC A,(IY+{byte:02X})',3, True, False ),
    '94' : ( 'SUB A,IYH',2, False, False ),
    '95' : ( 'SUB A,IYL',2, False, False ),
    '96' : ( 'SUB A,(IY+{byte:02X})',3, True, False ),
    '9C' : ( 'SBC A,IYH',2, False, False ),
    '9D' : ( 'SBC A,IYL',2, False, False ),
    '9E' : ( 'SBC A,(IY+{byte:02X})',3, True, False ),
    'A4' : ( 'AND IYH',2, False, False ),
    'A5' : ( 'AND IYL',2, False, False ),
    'A6' : ( 'AND (IY+{byte:02X})',3, True, False ),
    'AC' : ( 'XOR IYH',2, False, False ),
    'AD' : ( 'XOR IYL',2, False, False ),
    'AE' : ( 'XOR (IY+{byte:02X})',3, True, False ),
    'B4' : ( 'OR IYH',2, False, False ),
    'B5' : ( 'OR IYL',2, False, False ),
    'B6' : ( 'OR (IY+{byte:02X})',3, True, False ),
    'BC' : ( 'CP IYH',2, False, False ),
    'BD' : ( 'CP IYL',2, False, False ),
    'BE' : ( 'CP (IY+{byte:02X})',3, True, False ),
    'E1' : ( 'POP IY',2, False, False ),
    'E3' : ( 'EX (SP),IY',2, False, False ),
    'E5' : ( 'PUSH IY',2, False, False ),
    'E9' : ( 'JP (IY)',2, False, False ),
}
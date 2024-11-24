###
# Quest 10
# 11/22/2024
###
from collections import Counter


def solve1(input):
    result = 0
    inputArray = [list(line) for line in input.split("\n") if line]
    print(inputArray)
    output = [["." for _ in range(4)] for _ in range(4)]
    for row in range(2, 6):
        for col in range(2, 6):
            curRow = inputArray[row]
            curCol = [inputRow[col] for inputRow in inputArray]
            intersection = list(set(curRow) & set(curCol))
            for unique in intersection:
                # print(intersection)
                if unique != ".":
                    output[row - 2][col - 2] = unique
                    # print("Found unique: " + unique)
                    break
    print(output)
    result = "".join("".join(row) for row in output)
    return result


def calculateBlockPower(block):
    result = 0
    print("Before:\t" + str(block))

    while True:
        changed = False
        for row in range(8):
            for col in range(8):
                # Update logic for "." and "?"
                if block[row][col] == ".":
                    row_values = set(block[row])
                    col_values = set([block[r][col] for r in range(8)])
                    candidates = row_values & col_values
                    candidates.discard(".")
                    candidates.discard("?")
                    if len(candidates) == 1:
                        block[row][col] = candidates.pop()
                        changed = True
        for row in range(8):
            for col in range(8):
                if block[row][col] == "?":
                    # Collect row and column characters
                    row_values = {block[row][cc] for cc in range(8)}
                    col_values = {block[rr][col] for rr in range(8)}

                    # Check row-based conditions
                    if "*" not in row_values:
                        dots = [cc for cc in range(8) if block[row][cc] == "."]
                        if len(dots) == 1:
                            dot_col = Counter(block[rr][dots[0]] for rr in range(8))
                            opts = [
                                k for k, v in dot_col.items() if v == 1 and k != "."
                            ]
                            if len(opts) == 1:
                                block[row][col] = opts[0]
                                changed = True

                    # Check column-based conditions
                    if "*" not in col_values:
                        dots = [rr for rr in range(8) if block[rr][col] == "."]
                        if len(dots) == 1:
                            dot_row = Counter(block[dots[0]][cc] for cc in range(8))
                            opts = [
                                k for k, v in dot_row.items() if v == 1 and k != "."
                            ]
                            if len(opts) == 1:
                                block[row][col] = opts[0]
                                changed = True
        if not changed:
            break
    print("After:\t" + str(block))

    # Score calculation
    result = 0
    i = 0
    for row in range(2, 6):
        for col in range(2, 6):
            if block[row][col] != "." and block[row][col] != "?":
                ch_int = ord(block[row][col]) - ord("A") + 1
                i += 1
                result += i * ch_int
            else:
                print("Unsolvable")
                return (block, 0)
    print("Block score: " + str(result))
    return block, result


def solve2(input):
    result = 0
    inputArray = [
        list(line.replace(" ", ""))
        for line in input.strip().splitlines()
        if line.strip()
    ]
    # print(inputArray)
    blocks = []
    for i in range(0, len(inputArray)):
        blocksByRow = []
        for j in range(0, len(inputArray[0]), 8):
            blockByRow = inputArray[i][j : j + 8]
            # print(blockByRow)
            blocksByRow.append(blockByRow)
        blocks.append(blocksByRow)
    # print(blocks)
    for i in range(0, len(blocks), 8):
        for j in range(len(blocks[0])):
            block = [row[j] for row in blocks[i : i + 8]]
            (_, blockPower) = calculateBlockPower(block)
            result += blockPower

    return result


def solve3(input):
    result = 0
    inputArray = [
        list(line.replace(" ", ""))
        for line in input.strip().splitlines()
        if line.strip()
    ]
    # print(inputArray)

    while True:
        changed = False
        for br in range(0, len(inputArray), 6):
            if br + 8 - 1 >= len(inputArray):
                continue
            for bc in range(0, len(inputArray[br]), 6):
                if bc + 8 - 1 >= len(inputArray[br]):
                    continue

                block = [
                    [inputArray[br + r][bc + c] for c in range(8)] for r in range(8)
                ]
                for row in range(8):
                    for col in range(8):
                        # Update logic for "." and "?"
                        if block[row][col] == ".":
                            row_values = set(block[row])
                            col_values = set([block[r][col] for r in range(8)])
                            candidates = row_values & col_values
                            candidates.discard(".")
                            candidates.discard("?")
                            if len(candidates) == 1:
                                inputArray[br + row][bc + col] = candidates.pop()
                                changed = True
                for row in range(8):
                    for col in range(8):
                        if block[row][col] == "?":
                            # Collect row and column characters
                            row_values = {block[row][cc] for cc in range(8)}
                            col_values = {block[rr][col] for rr in range(8)}

                            # Check row-based conditions
                            if "*" not in row_values:
                                dots = [cc for cc in range(8) if block[row][cc] == "."]
                                if len(dots) == 1:
                                    dot_col = Counter(
                                        block[rr][dots[0]] for rr in range(8)
                                    )
                                    opts = [
                                        k
                                        for k, v in dot_col.items()
                                        if v == 1 and k != "."
                                    ]
                                    if len(opts) == 1:
                                        inputArray[br + row][bc + col] = opts[0]
                                        changed = True

                            # Check column-based conditions
                            if "*" not in col_values:
                                dots = [rr for rr in range(8) if block[rr][col] == "."]
                                if len(dots) == 1:
                                    dot_row = Counter(
                                        block[dots[0]][cc] for cc in range(8)
                                    )
                                    opts = [
                                        k
                                        for k, v in dot_row.items()
                                        if v == 1 and k != "."
                                    ]
                                    if len(opts) == 1:
                                        inputArray[br + row][bc + col] = opts[0]
                                        changed = True
        # print(changed)
        if not changed:
            break

    for br in range(0, len(inputArray), 6):
        if br + 8 - 1 >= len(inputArray):
            continue
        for bc in range(0, len(inputArray[br]), 6):
            if bc + 8 - 1 >= len(inputArray[br]):
                continue
            block = [[inputArray[br + r][bc + c] for c in range(8)] for r in range(8)]
            # print(block)
            ok = True
            block_score = 0
            i = 0
            for r in [2, 3, 4, 5]:
                for c in [2, 3, 4, 5]:
                    if block[r][c] == "." or block[r][c] == "?":
                        ok = False
                    else:
                        ch_int = ord(block[r][c]) - ord("A") + 1
                        i += 1
                        block_score += i * ch_int
            if ok:
                # print(f"{br=} {bc=} {block_score=}")
                result += block_score
    return result


def main():
    inputExample = """
**PCBS**
**RLNW**
BV....PT
CR....HZ
FL....JW
SG....MN
**FTZV**
**GMJH**
"""
    input = """
**HFVL**
**WCTS**
HL....FR
WD....SG
TC....XB
JV....MK
**BMDX**
**JGRK**
"""
    print("Part 1 answer:")
    print(solve1(input))

    input = """
**XCQS** **CNRX** **LNRW** **MRCB** **BZDS** **CSZQ** **BTCF** **VFND** **TDGR** **GJZQ** **QNDW** **ZMNB** **JLPC** **ZQRH** **LBGH**
**NTGM** **LDMP** **CMQT** **XVNK** **RWTJ** **MKFP** **LQNZ** **CWPT** **WNXK** **SCMP** **CMLZ** **JHGP** **SXRF** **PKFN** **RZVM**
GT....ZN HB....XR ND....SZ RT....KD TV....XZ LW....XT GQ....WN XL....BS FG....KT PW....VN JD....ZG BK....RD FP....SL GH....TF BG....QH
HK....JS PM....QV GW....JQ LZ....SB JF....LM NC....QK LF....CP PV....FM MN....QW LK....TC CW....MP VC....NM QN....ZM ZL....NR VL....NC
DB....RV WZ....NC RT....LH HX....PN RN....CQ BM....HZ TD....BS WT....QC BD....ZP ZD....JS SB....KL FP....ZH GR....VK DQ....BP JX....RK
QC....MX JL....GD VM....CP WV....CM BS....WD SJ....PF MJ....ZR JR....DN XR....SC RM....QG NQ....FH XW....GJ CX....JB WM....JK MZ....FP
**KJHZ** **HVWG** **GHPD** **TZDH** **XNQV** **WTNX** **MPJD** **RJQM** **BFPZ** **VNWD** **GBPH** **RDKV** **KGBV** **TLMJ** **QXJC**
**RVBD** **QBJZ** **SJZV** **LPSW** **MLFC** **JHLB** **GRSW** **LSXB** **SCQM** **LRKT** **KJFS** **CXFW** **NMQZ** **WGBD** **FNPK**

**TMHR** **MNPT** **JXNH** **QLWX** **WTVX** **CMJW** **DJHR** **NWRB** **VZGL** **HRLX** **ZHKS** **XJBK** **QWKZ** **VJTM** **CJPG**
**FZXK** **BHWQ** **VPMW** **RFHJ** **NGPL** **RGSZ** **GZVT** **ZCTL** **HBSF** **JVFT** **GRBT** **LNQT** **XHGN** **NWXS** **RTWX**
FR....PW WC....HD MV....HF CR....FS MN....TL KT....BV RV....GL ZB....TF DN....GM MG....XD KF....MT SG....WV WD....QJ NC....HG KN....JR
HM....TB ZX....TK LR....XK DK....ZH KD....GX CG....DZ WN....JP DN....KR QT....ZR VH....FZ PX....BD KL....BF XV....FH SJ....TV WX....BC
DN....LK RP....QM ZQ....BT QJ....WL CP....WQ RS....FL BS....MK QM....CJ VF....WS JK....LT WH....ZN ZM....HN CL....NG LZ....BK TV....GP
ZX....GQ NL....FB NP....WJ PN....XT HJ....VB WN....MJ ZD....TH WS....LV BL....HP RN....QS LS....RG TQ....XJ ZM....KS XF....WM SH....DZ
**DLNG** **ZKLD** **ZFQB** **NKSC** **DQMC** **VFKT** **NSPW** **MKSJ** **MWPT** **SKQZ** **MFWN** **MVZW** **SCFJ** **FHGC** **HBZN**
**QWPB** **CRXF** **LTKR** **DTPZ** **BHKJ** **NBDL** **MLKB** **VFQD** **QNRD** **DGMN** **DXLP** **SFGH** **LMDV** **ZBKL** **VDKS**

**CNQR** **PXCR** **BXVZ** **TCLX** **SZVQ** **WKCV** **TPDN** **QRVB** **KVDB** **DPFL** **XNSF** **SFLJ** **TNLB** **CRFK** **PFJW**
**KDBM** **MBNT** **FDPR** **DJMR** **MWGR** **SDNL** **CSWK** **XTLJ** **ZGTR** **VHCK** **HTGL** **TQVK** **FVKD** **PHTG** **CKRZ**
TZ....SP XQ....JS BD....RP MR....VJ ZT....KS JM....TB NV....MZ RM....QB VW....ZD MZ....VJ XG....NP MZ....NV KM....DH ZH....LW PV....QJ
DX....MC FV....WC QG....LF BQ....WX XR....VM WD....FR PG....QH DT....LK TR....PL TK....NW HS....QR BF....CP FX....VL BK....NT ZX....SG
NR....QJ BR....NP ZV....CX LC....ZD BG....QP NZ....VK WC....SK ZX....VH BS....HM BL....PF WB....FD LD....SK GQ....BN GP....FR TN....FC
GB....FK DM....HT MW....HS GK....TH CD....WL SH....CL DF....XT PN....GJ FG....KC DH....CX ZT....LJ XJ....QT ZS....TR JC....SQ KR....BW
**JFXZ** **VHDS** **HQLW** **VHBG** **BPTC** **ZTMJ** **ZVMQ** **NHMZ** **LPFW** **WMZJ** **WRDQ** **PDCB** **QMRX** **BJWZ** **SGNT**
**SPTG** **QFJW** **CSMG** **QWKZ** **DXLK** **BHFR** **HXGF** **DGPK** **HMSC** **BTNX** **ZBJP** **ZMXN** **HZGS** **LNSQ** **BQXV**

**GQMB** **TFMQ** **QXVD** **XDQZ** **DKCF** **SPXJ** **RGMX** **JCTS** **PSHN** **MGLP** **CKRF** **SJFC** **VJFN** **GTNK** **SFZV**
**CFZR** **KGRL** **WHLN** **SCHN** **BSGN** **QGZR** **BTSC** **PWQL** **JZMV** **XHTZ** **MHSZ** **WPRV** **ZSGB** **QHRL** **PJRQ**
RF....CM LM....FH NZ....FP RB....NM MP....LW QR....HZ MG....NQ LQ....XJ DG....HR QX....CL KX....TN FJ....DV XP....CB BN....WQ NV....ZT
SQ....NL RP....WK DW....SJ KJ....FH BS....NG KF....LV JX....HR RC....BV PL....SV WN....SP FM....WP SK....RT NM....KL KX....TS QP....RJ
BH....WG TQ....SG TK....VX VC....XQ FC....KQ SM....GX TB....SC ZS....NP JQ....NM KH....TR LS....ZH CG....MZ SF....QV HM....LZ BS....HD
PZ....DX XV....BZ LC....QH SD....ZP DX....VH JP....BW LZ....FW TK....MW XW....BZ MZ....GJ VJ....CR PX....LW RJ....ZG GV....PR FG....XW
**SWHD** **XPSZ** **FSZC** **FRMK** **QHLV** **WKBM** **FZWL** **MZBR** **GQWB** **KSJC** **LVNT** **GTLX** **XPLR** **MBZP** **WTBD**
**XPLN** **HVBW** **TPJK** **BJPV** **PWXM** **VHLF** **NHJQ** **VXNK** **XDLR** **WQNR** **XPWJ** **DMZK** **KMCQ** **XVSW** **NHXG**

**CDJB** **GPMC** **TGJQ** **KZTS** **MLXZ** **DGTF** **LZXG** **MCQN** **WPSL** **BVKL** **VXBC** **XTGB** **BVJC** **FCBJ** **HKCP**
**VSQT** **LWRV** **VWSX** **MNBG** **TQSV** **RXQJ** **PQKD** **WTBK** **VHJF** **DGSM** **WJTR** **MCVQ** **TLDR** **NXWV** **TXJQ**
NV....PF WV....GM NJ....TP MZ....ST GT....HB LG....VF WX....PM PV....BT FP....WG GT....ND QS....BX FX....KS QB....LJ CD....KV BF....QK
JT....CW PL....RC SV....FG PC....BG QR....DZ ZT....RX QJ....LC HQ....RL BZ....VK JL....VB VP....GR MN....QT WD....VR HN....JL PJ....HW
GM....SB DX....NH QM....CW QN....JX VL....XP NC....JD GS....ZV FK....XW RS....ND MQ....CS NT....CJ CB....LV KT....XC BS....FQ TC....GX
XK....DQ QB....ZF BL....XK FW....RK SJ....MN QK....WS KH....BD NZ....CM HL....JX PR....KW WZ....MK DJ....GH SZ....NF XP....MW RN....VM
**MNGX** **NFZQ** **MPCF** **CPQF** **PBHJ** **WKNZ** **VWSC** **VLZR** **XBKZ** **QRJW** **NZPK** **JDNH** **WSKQ** **DHKQ** **BWNG**
**KWPF** **BDHX** **KLBN** **XWRJ** **RNDG** **VCLS** **HBJM** **HXFP** **RDGN** **PCTN** **QGMS** **LKSF** **NXFZ** **MSLP** **MRFV**

**WCKX** **DQXC** **PMJS** **PQJN** **NWSR** **VTKD** **ZLMC** **HSDG** **VJKR** **LTPF** **KTBS** **JXHV** **NSGD** **TPJK** **VPDW**
**BSNR** **ZMVJ** **RZGX** **GSFM** **KXPJ** **GBLS** **KXVW** **RFXM** **BCQZ** **DMNC** **HLCG** **CDTR** **ZRQX** **NVWH** **JBFQ**
DZ....MR XZ....MJ PM....ND XL....VZ FV....XC DJ....TQ KL....WV SN....CZ FC....SV ZT....SD LJ....GB KD....BC BL....GR PG....MR TD....QS
WF....XG VC....KW ZG....KX QP....FM JW....PK GF....PM PJ....TS HD....WG HP....DB BC....GN TC....HQ HW....RS JH....MP VW....SN FB....MX
TB....KC LP....NF BS....TW SG....DJ BT....SH CH....LS QN....BD QJ....TF KM....ZJ HM....PF NP....XS XN....VQ SV....ZX TC....LK PN....VG
NS....HL SQ....DR HV....JR NK....BR LR....NZ ZB....KV ZC....XM PM....XR RW....QG XV....LW MV....WK MJ....PT NC....QD ZJ....HX WJ....LR
**MZFL** **FPLN** **KVWN** **LRZX** **CZFB** **JCQZ** **TJDN** **NPQZ** **MGSF** **GBZW** **XPVQ** **QPKB** **BCPH** **ZXRM** **MSRG**
**HGDT** **KWSR** **TBDH** **BVKD** **HTLV** **HFMP** **QBPS** **TWCJ** **WHPD** **HXVS** **JMNW** **WSNM** **JMVL** **GLCS** **TLNX**

**JZDW** **WDRQ** **SGXV** **BPDX** **KWMP** **HMFG** **DTGB** **RKLP** **NSXT** **DMVX** **TVJN** **ZWGQ** **SDKZ** **KHNC** **TBPV**
**MBXL** **KPBX** **HNQC** **FSKJ** **XSJB** **SRTC** **MFVR** **SBMT** **JZQK** **WRBF** **BZSH** **FTCB** **GFTV** **RBPJ** **WGDQ**
LM....KQ RD....QG SZ....KG HW....TM CK....BJ NX....BD TK....PR XS....MG RJ....XV GH....CQ TF....WS HM....KB NL....VC LW....JS MH....BS
CG....VS KL....CT PN....QC XC....KB DH....WN SJ....QC VB....MW KL....RT WF....KS LT....MV BZ....HK TC....FQ PD....KG RT....MZ RG....PK
DJ....ZW WB....XM RM....TW JP....LF LF....MP MT....PG FC....GJ JF....DC TG....CP FR....WJ RJ....VM NL....RW JX....FT HK....DP VD....TX
BX....RT ZV....SP HD....VX DV....SN TX....QS RH....VF QN....DX ZB....VP ZN....MQ XB....DS XN....QC JV....ZG ZR....HS QC....BN NL....QW
**TKSR** **GMZV** **PDRZ** **VHWM** **NCTH** **DJBV** **JQKC** **DXVG** **PCGR** **GQJT** **RCKW** **KHNR** **XCRP** **QSWM** **MLHS**
**CGQV** **STLC** **MTKW** **TCLN** **FLDQ** **PXQN** **PWXN** **ZCJF** **WVFM** **LSCH** **QFXM** **LJMV** **NHLJ** **LZTD** **KXNR**
"""
    print("Part 2 answer:")
    print(solve2(input))
    inputExample = """
**XFZB**DCST**
**LWQK**GQJH**
?G....WL....DQ
BS....H?....CN
P?....KJ....TV
NM....Z?....SG
**NSHM**VKWZ**
**PJGV**XFNL**
WQ....?L....YS
FX....DJ....HV
?Y....WM....?J
TJ....YK....LP
**XRTK**BMSP**
**DWZN**GCJV**
"""
    input = """
**BGVF**MLNW**VQGD**MRWF**QBRJ**TPXW**XDGC**PHLR**QVCT**RLMK**HFZD**RNLS**FBZP**XMQR**QCVK**TPMB**JVRC**PCXZ**XMVF**NKXG**
**QLDH**XBHT**MKZF**PXDH**GDFW**ZBHK**QVKN**TKNV**GSLX**WSTJ**TKVM**GWQC**DQRL**KVHF**DTSJ**HFRX**WDQM**RBSQ**WDTL**LTCP**
WX....GD....?T....VD....H?....BG....TM....?C....HZ....X?....JW....D?....NR....?C....NR....?T....ZB....V?....?P....VD....KC
LZ....BS....WK....B?....?W....ZQ....?R....BD....T?....MC....?N....CV....GK....?B....?G....CF....H?....QD....LB....?Q....GX
QM....FP....NM....Q?....?M....DF....XW....?G....?P....SF....TB....?F....SX....D?....?M....SW....RX....C?....GS....W?....LH
CR....HV....L?....GF....RN....?V....PH....N?....W?....QV....LR....M?....LW....T?....H?....JD....PM....?W....?R....FN....PB
**?R??**RGKF**RLNJ**SVJZ**NVZH**VRMJ**BHTR**CGDJ**MKWR**BNGV**JWBQ**FXKD**TSXK**BZPT**WMHF**DSLJ**XPBL**LTJG**QGNZ**MBHW**
**X?MZ**SPDV**BXTW**GBNQ**XPSM**DFQG**MWPJ**WQZB**PZHF**CXQF**CLRN**HVZM**NWGC**NCGD**GXRN**WZQC**HNTZ**NVDW**PRBS**VQFD**
JF....WX....ZW....VH....?J....W?....LN....?Y....NY....MV....XY....SX....FQ....KB....BY....?H....WJ....NB....GY....RT....QB
ZT....PV....CX....YT....YZ....MY....ZP....SL....?X....?S....PR....Y?....GR....?Y....DL....TQ....R?....VK....HP....YG....LY
RK....SG....MR....?Q....TG....BZ....Y?....CM....RT....HR....FD....HB....CY....NW....?X....YS....BY....YQ....F?....HV....RZ
NH....MC....?Y....SR....RQ....LC....QW....FZ....WD....BY....?C....KC....B?....PS....WS....WF....SN....R?....JQ....?J....T?
**VNJ?**MQZW**XVTN**ZQJL**QFTX**FZTS**PZKM**GWPK**MQRZ**JHCQ**BTZN**VBRG**WZPM**KSNV**ZHCB**CLND**FSLN**KHJS**BPLF**NVHS**
**KFTG**VDPC**GKCZ**SWCV**PGND**WQCG**SHXD**SBJF**DLBP**RSZV**LPQS**PCFZ**HQRX**QHTZ**XNJL**TKWS**CZPQ**DRPQ**TQGJ**PKWF**
TQ....HD....?L....GK....CL....?N....WZ....K?....ZJ....M?....CH....B?....R?....MB....?V....BX....?N....MZ....?H....BL....HS
GS....KX....?Z....VD....FZ....B?....?Q....MX....WS....?R....G?....QK....G?....HX....NR....C?....?R....PG....R?....FZ....NT
PW....JN....M?....SN....MQ....?K....CJ....P?....BV....K?....V?....PX....S?....QW....?D....LJ....TV....Q?....J?....PC....VR
BL....VF....Q?....TX....WJ....D?....?S....HL....FG....Q?....JF....?N....?Z....PJ....KZ....?H....?K....CL....?D....QG....KW
**???W**LXJR**SRLP**TGFM**BCJZ**BKPN**RVFW**DHLV**WJTS**KPFG**KFJH**DKXS**DBGV**RMPD**QSTR**BRVH**MKTW**GCZM**CRZH**GBTQ**
**QDXB**KNFH**WMDQ**KDNX**LWMK**JDXV**QJCL**ZRMX**VKGF**TDLM**VGCX**QLNT**JFCS**BJWX**DVKG**GXQJ**RVDG**XFLT**DKXS**LZCR**
NC....LS....KW....CQ....LB....YC....PY....SR....FH....?T....J?....VP....GC....NQ....YT....DW....F?....Q?....YB....RD....TS
GZ....WX....TB....LP....?H....GS....?R....YN....YS....BD....YM....KY....?Y....?C....DM....K?....YV....BY....?P....?J....QG
DK....PM....ZV....DM....RS....?F....JC....FW....CL....CS....QC....Q?....LN....TY....K?....NG....BZ....TC....RM....YW....RY
VQ....FB....FR....SH....QY....TL....LS....?D....J?....YX....DL....TL....JP....LP....NH....TY....MX....RM....LD....QF....?N
**GFMK**NYLC**VTKZ**TJFH**THVZ**TNJW**CKFG**SXJL**MGNT**PDVR**GLFC**RMBZ**CSDQ**GJQZ**LRQZ**TDFJ**FCSQ**MJGB**XRTD**GZFW**
**?ZVC**?QSP**BCHF**XPWK**KFMG**PDVX**XDVW**DWMH**QVWP**ZSBJ**KNZJ**JTXH**ZRFK**BNTK**FVMH**BPVS**RKNB**CQVN**SLMF**HVNQ**
XW....GF....PD....F?....TR....?C....N?....DG....J?....VM....TD....K?....RH....X?....JT....?H....?T....FK....G?....XL....HV
VB....ZR....?Q....ZM....PX....?Z....WH....?C....T?....NF....JS....X?....PZ....?L....B?....CF....PN....X?....D?....SQ....NJ
KS....DM....T?....KG....WN....?M....PX....F?....W?....KG....ZR....M?....?B....QF....Z?....RS....WV....?Q....?W....FC....DZ
HQ....CN....JW....V?....HJ....?D....RJ....K?....SH....?Q....BW....?N....TJ....S?....N?....LM....?J....ZS....?J....TR....GW
**B?Q?**YBSD**QDPJ**VNCR**PCDW**ZHMC**RPHQ**TGKC**FXSK**TQNW**RSDM**FCKL**BVPH**CLDS**JTSC**CMQH**PJDX**FKWZ**VBQN**JSXL**
**DH?W**WZ?Q**GMWR**GBZM**NXRJ**RFGK**TMNJ**FVQB**LHBJ**FKGM**XTBW**VPGN**TLXJ**FPVX**PNBG**WRLN**ZWVT**SDXR**WCGJ**CRTD**
KV....XS....LX....JW....SM....NC....KV....HT....JR....?C....CK....MB....YP....XJ....F?....XJ....LV....H?....QT....M?....FD
LT....QW....BD....HP....XL....ZR....Q?....FY....XB....DY....DG....VK....CW....MY....YR....YM....ZC....VY....KG....WY....WN
RP....DM....GK....MC....BD....JT....WL....?V....H?....KS....QY....?C....NQ....?P....ZV....?B....DY....PG....D?....TH....ZP
BC....HZ....TS....QR....FH....WP....SY....JB....YZ....ZM....R?....GY....M?....ZG....NM....ZK....?K....ST....YN....ZL....?Y
**?TCV**NYXT**HXSC**SL?W**ZFHL**HQDK**MLXT**PFWM**VCWR**BLDK**RWGZ**DQNC**VRXS**SWHL**TGKH**WBJX**XFQS**ZNMJ**TPDR**NCDX**
**KP?Z**RSK?**LTKB**GVYX**BTMS**VBMP**CBSV**GXNZ**MTJH**VCSM**JFPD**BLFG**FDGT**TNJP**VNFQ**DNML**VNTM**HCLW**MXSQ**BKJW**
NL....VB....?G....LS....MD....Z?....KM....?J....PZ....?H....?N....WR....QB....F?....WP....F?....?D....TS....?H....XQ....BM
SF....CZ....?V....NH....XV....?S....?D....XB....WQ....X?....LS....?Z....SL....?R....?Z....KJ....RN....V?....MG....?F....DK
HP....KX....JC....X?....FR....J?....QR....?T....?N....JG....?M....GV....PN....?V....?D....GX....MP....?F....DN....T?....WZ
DR....MT....?Q....BK....WN....?T....VP....G?....?K....VT....PK....?T....C?....KG....?S....QV....?L....QX....WZ....?R....NC
**S?X?**WYV?**JQWN**H?NW**WVND**GZJS**DKQJ**TJSK**ZQPK**RPTX**MVSN**PVJW**CPLK**ZVXR**ZSDJ**PQTR**BWJC**VSXT**LWFG**TZMR**
**DBNR**KQMC**FGVP**KYGL**RGXJ**NTLR**RGPN**QLCB**XGFN**JGNH**LKBT**ZTRS**JQNB**FKGD**XWLP**KGVF**PDRL**DQFG**ZNHJ**FQSP**
JM....SB....MC....PV....FQ....VR....WT....PG....VY....NC....MH....RZ....YC....L?....RH....BW....XS....KL....NW....RK....RN
XL....FZ....DF....HN....XP....GT....MR....FK....SN....S?....Y?....V?....?T....CJ....SZ....ZN....YD....?P....YR....YD....Y?
QT....HD....GL....XJ....DL....NK....SJ....XD....ZK....YF....ZV....QG....LQ....NH....?Y....FY....QR....YW....VZ....J?....TG
GR....WN....ZS....WQ....CH....JW....VZ....QN....?G....RW....DQ....MY....PK....VY....LF....D?....?B....ZX....S?....LG....QS
**?TJM**YMQK**CMXL**LH?S**KLQT**ZPQ?**WZXF**KJCH**FPMQ**RQPD**VPHT**RGDZ**KJLZ**FBHZ**SFDW**RGWN**BQJD**ZPGM**JCGV**SMHK**
**WG??**T?GD**ZHDS**RNYB**PCHF**YGJC**VSMT**ZLRS**KCSN**GJZX**KCRG**HWPF**XBNS**WQMG**JTVK**VSFZ**ZRKV**NSKJ**XKDZ**NGJZ**
RQ....DT....?B....NX....RP....L?....NB....?F....?R....PT....XB....?C....FD....L?....G?....KX....FN....K?....ZH....?J....ZF
CK....LG....P?....HW....BW....?T....XC....?W....?B....VM....GD....H?....MW....?S....W?....VL....ZM....?D....PN....?K....NR
SB....WZ....FT....?M....CX....?H....GZ....?D....ZH....?S....JR....?S....ZG....?V....?R....SD....HR....B?....MS....?D....SM
XM....JF....J?....SZ....?M....FK....QJ....S?....?X....FQ....?Z....PV....RJ....?X....?C....JT....?G....JQ....LG....W?....HG
**FSKD**DF?Y**NQFT**CHYX**WBMX**?JTX**QLJC**XFDV**VHJB**WBMF**DJWZ**KVSJ**GDVF**XCLV**QRGM**TKHD**NTMG**CLTH**LWNS**BFDC**
**R?BC**JTBK**PBJW**JW?Q**GDRJ**LDYB**GBND**WMTB**ZXRT**TVNS**XLBS**TCML**MWRH**RKSN**XLZC**XMLJ**WFCH**QVBD**MHBP**VXRW**
MW....XF....ZB....PC....HN....XR....NK....LP....RF....HL....XN....MB....NJ....DG....WJ....QR....QR....WT....FT....NP....K?
LC....KZ....KR....QJ....LD....QM....GR....SJ....PC....VX....QR....LW....LR....WP....PZ....LN....HP....DN....JM....SV....PV
PB....RH....HM....FT....CG....KB....WZ....BD....MW....BZ....FH....ZJ....ZT....FM....MF....GV....XB....FC....WD....GL....YJ
GT....SD....XN....WV....SV....JW....VH....CQ....TQ....NJ....VS....KD....XH....VC....SB....CX....VM....GJ....RZ....HB....XG
**LZMH**JQKM**KVXR**Y?HD**QNCL**DKMZ**PVZS**VYP?**NMWL**?MQY**QKHR**YPLS**CZNJ**HV?W**PFSN**?CZQ**XPDR**YC?L**ZVGD**YPJX**
**TPGW**LH?Y**MHCZ**BSRZ**HVSK**?WVY**WRHK**GJMX**FQCP**RWFS**FNVM**ZQG?**LXTP**MYQS**VBJW**YGVP**VJQB**KFTQ**TFJR**SD?Q**
"""
    print("Part 3 answer:")
    print(solve3(input))


if __name__ == "__main__":
    main()

import math

d = {"BCL2": 51, "SIRT1": 217, "NOTCH3": 168, "ITGA2": 135, "MAP2K1_2.pS217_221": 149, "H3histon": 118, "EGFR": 92, "BAD": 45, "H3K4Me2": 120, "PLT": 21, "H3K27Me3": 119, "BM.MONOCYTES": 15, "Patient_id": 0, "MTOR.pS2448": 162, "BIRC2": 56, "SMAD4": 223, "PRKCA.pS657": 194, "BM.BLAST": 14, "GAB2.pY452": 111, "STAT5A_B": 240, "SSBP2": 234, "RPS6KB1": 212, "CTNNA1": 85, "NPM1.3542": 170, "LDH": 22, "KIT": 142, "CCNE1": 72, "FN1": 106, "CDKN1B.pS10": 201, "JUN.pS73": 140, "CDK4": 78, "PRIOR.XRT": 6, "CDKN2A": 80, "MYC": 163, "PA2G4": 174, "STAT5A_B.pY694": 241, "CDK1": 76, "PIK3R1_2": 184, "CASP8": 63, "MAPT": 155, "HIF1A": 125, "ELK1.pS383": 100, "TP53": 250, "PTGS2": 204, "AIFM1": 36, "ASH2L": 41, "ATF3": 43, "GAPDH": 112, "CBL": 68, "EGLN1": 94, "CD44": 74, "BIRC5": 57, "LEF1": 144, "XPO1": 259, "EIF4E": 99, "PLAC1": 187, "CD20": 32, "TSC2": 254, "ARC": 40, "BM.PROM": 16, "SOCS2": 227, "PRIOR.MAL": 4, "PRKAA1_2.pT172": 192, "CCND1": 70, "NOTCH1.cl1744": 167, "PRKCB.II": 196, "YWHAZ": 263, "TGM2": 248, "CD19": 34, "PRKCD.pS645": 197, "EGFR.pY992": 93, "PARP1.cl214": 180, "NRP1": 172, "ERG": 104, "EIF2AK2": 95, "PDK1.pS241": 182, "YAP1p": 261, "PIM2": 186, "SMAD1": 218, "SMAD2": 219, "EIF2S1.pS51.": 98, "STAT1": 235, "MDM2": 157, "JUNB": 139, "CD33": 28, "TP53.pS15": 251, "KDR": 141, "MCL1": 156, "BCL2L11": 53, "GSKA_B": 116, "BID": 55, "HNRNPK": 126, "CD10": 31, "EIF2AK2.pT451": 96, "HDAC2": 123, "STAT3.pY705": 239, "PDK1": 181, "BAD.pS136": 47, "RPS6KB1.pT389": 213, "BAD.pS112": 46, "ERBB2.pY1248": 102, "SMAD3": 222, "SPI1": 228, "CREB1": 83, "INPPL1": 133, "RAC1_2_3": 207, "GATA3": 114, "ITGAL": 136, "resp.simple": 266, "CASP7.cl198": 62, "ATG7": 44, "PIM1": 185, "PA2G4.pT37_46": 176, "PRKCD.pS664": 198, "PTPN11": 206, "SPP1": 229, "D835": 9, "STMN1": 244, "TRIM62": 253, "SEX": 1, "ABS.BLST": 13, "MDM4": 158, "CAV1": 67, "CREB1.pS133": 84, "DUSP6": 91, "NCL": 164, "ITD": 8, "ERBB3": 103, "CCND3": 71, "ITGB3": 137, "STAT3": 237, "IGF1R": 130, "Age.at.Dx": 2, "GAB2": 110, "STAT1.pY701": 236, "AKT1_2_3.pS473": 38, "PRKCD.pT507": 199, "NF2.pS518": 166, "PA2G4.pS65": 175, "SMAD5": 224, "AKT1_2_3.pT308": 39, "PTK2": 205, "YWHAE": 262, "SFN": 216, "AKT1": 37, "MAP2K1": 148, "HDAC1": 122, "CDK2": 77, "STK11": 243, "PPARG": 189, "WBC": 12, "BMI1": 58, "PB.BLAST": 17, "LSD1": 146, "NPM1": 169, "CREATININE": 25, "ALBUMIN": 23, "SRC.pY527": 233, "VASP": 255, "CDKN1A": 79, "RPS6.pS240_244": 215, "CASP9": 64, "SMAD2.pS465": 221, "HLA.DR": 33, "ERBB2": 101, "NF2": 165, "PIK3CA": 183, "VHL": 256, "MET.pY1230_1234_1235": 159, "BRAF": 59, "TAZ.pS89": 246, "TAZ": 245, "PTEN": 202, "PPARA": 188, "GRP78": 115, "IRS1.pS1101": 134, "BCL2L1": 52, "HSP90AA1_B1": 127, "YAP1": 260, "Fli1": 105, "CD34": 29, "SMAD2.pS245": 220, "HDAC3": 124, "PB.MONO": 18, "Overall_Survival": 268, "SRC.pY416": 232, "STAT6.pY641": 242, "JMJD6": 138, "CTSG": 88, "FOXO3": 108, "STAT3.pS727": 238, "TRIM24": 252, "RPS6.pS235_236": 214, "ODC1": 173, "MAPK9": 154, "CCNE2": 73, "ASNS": 42, "HSPB1": 129, "LGALS3": 145, "BAD.pS155": 48, "H3K4Me3": 121, "ACTB": 35, "COPS5": 82, "CD13": 27, "XIAP": 258, "Remission_Duration": 267, "PRIOR.CHEMO": 5, "Infection": 7, "FOXO3.S318_321": 109, "SRC": 231, "BILIRUBIN": 24, "BAX": 50, "ZNF296": 264, "PRKAA1_2": 191, "CLPP": 81, "PPP2R2A_B_C_D": 190, "GATA1": 113, "MSI2": 160, "CDKN1B": 200, "CCNB1": 69, "CTNNB1": 86, "GSKA_B.pS21_9": 117, "DIABLO": 89, "RPS6": 211, "PA2G4.pT70": 177, "Ras.Stat": 10, "PARK7": 178, "CASP9.cl330": 66, "IGFBP2": 131, "SQSTM0": 230, "SMAD5.pS463": 225, "AHD": 3, "CTNNB1.pS33_37_41": 87, "WTAP": 257, "TCF4": 247, "LCK": 143, "PTEN.pS380T382T383": 203, "EIF2S1": 97, "HSPA1A_L": 128, "RB1.pS807_811": 209, "Chemo.Simplest": 11, "MAPK14.pT180Y182": 153, "ZNF346": 265, "LYN": 147, "RB1": 208, "SMAD6": 226, "MAPK14": 152, "CASP3": 60, "HGB": 20, "MAPK1": 150, "CD74": 75, "CASP9.cl315": 65, "CASP3.cl175": 61, "MTOR": 161, "PB.PROM": 19, "DLX1": 90, "RELA": 210, "PARP1": 179, "FIBRINOGEN": 26, "BAK1": 49, "FOXO1.pT24_FOXO3.pT32": 107, "CD7": 30, "BECN1": 54, "PRKCA": 193, "NR4A1": 171, "MAPK1_3.pT202Y204": 151, "PRKCB.I": 195, "INPP5D": 132, "TNK1": 249}

def dispatch(l):
    if l[d["Chemo.Simplest"]] == "Anthra-Plus":
        anthra_plus(l)
    elif l[d["Chemo.Simplest"]] == "HDAC-Plus":
        hdac_plus(l)
    elif l[d["Chemo.Simplest"]] == "Flu-HDAC":
        flu_hdac(l)
    elif l[d["Chemo.Simplest"]] == "Anthra-HDAC":
        anthra_hdac(l)
    elif l[d["Chemo.Simplest"]] == "StdAraC-Plus":
        stdarac_plus(l)
    else:
        print("bad parse on therapy")

def anthra_plus(l):
    v = -5.34
      - 0.1711*l[d["Age.at.Dx"]]
      + 3.78*l[d["ALBUMIN"]]
      + 0.01072*l[d["FIBRINOGEN"]]
      + 2.904*l[d["CASP7.cl198"]]
      - 1.747*l[d["CASP8"]]
      - 3.62*l[d["EGFR.pY992"]]
      - 4.34*l[d["ERG"]]
      + 2.915*l[d["GSKA_B.pS21_9"]]
      + 4.90*l[d["H3K4Me3"]]
      + 2.033*l[d["IRS1.pS1101"]]
      + 3.199*l[d["PIK3CA"]]
      + 3.658*l[d["PTEN.pS380T382T383"]]
      - 1.243*l[d["RELA"]]
      - 2.678*l[d["RPS6KB1.pT389"]]
      + 2.815*l[d["VASP"]]
    p = math.exp(v)/(1+math.exp(v))
    
    remission_duration = -5.070*l[d["Age.at.Dx"]]
                       + 61.7l*l[d["ERBB2.pY1248"]]
                       - 1.395*l[d["BM.BLAST"]]
                       - 72.5*l[d["ARC"]]
                       - 46.2*l[d["CBL"]]]
                       - 25.0*l[d["CCND3"]]
                       - 42.0*l[d["CCNE2"]]
                       - 46.4*l[d["CDK2"]]
                       + 68.1*l[d["DIABLO"]]
                       - 65.7*l[d["EIF2AK2"]]
                       - 79.5*l[d["ERG"]]
                       + 49.9*l[d["INPPL1"]]
                       + 106.7*l[d["MDM4"]]
                       + 32.0*l[d["MET.pY1230_1234_1235"]]
                       - 79.2*l[d"PTGS2"]]
                       + 40.9*l[d["PTK2"]]
                       + 94.4*l[d["PTPN11"]]
                       + 61.8*l[d["TNK1"]]
                       - 134.2*l[d["TRIM24"]]
    overall_survival = -3.463*l[d["Age.at.Dx"]]
                     - 0.593*l[d["WBC"]]
                     + 82*l[d["CAV1"]]
                     + 20.62*l[d["HGB"]]
                     + 41.1*l[d["BAD.pS136"]]
                     + 48.1*l[d["BIRC2"]]
                     + 35.9*l[d["CTNNB1"]]
                     - 67.2*l[d["DLX1"]]
                     + 31.1*l[d["H3K27Me3"]]
                     - 29.8*l[d["PRKAA1_2.pT172"]]
                     + 63.7*l[d["SRC.pY416"]]
                     - 75.3*l[d["TGM2"]]
                     + 35.4*l[d["TNK1"]]
    if p<0.5:
        outcome = "COMPLETE_REMISSION"
        if l[d["Ras.Stat"] == -1:
            r_constant = 517.1
            remission_duration = r_constant + remission_duration
        elif l[d["Ras.Stat"]] == 0:
            r_constant = 430
            remission_duration = r_constant + remission_duration
        else:
            r_constant = 514.3
            remission_duration = r_constant + remission_duration
        if l[d["PRIOR.CHEMO"]] == 0:
            s_constant = 198.3
            overall_survival = overall_survival + s_constant
        else:
            s_constant = 122.4
            overall_survival = overall_survival + s_constant
        print(l[d["Patient_id"]], outcome, remission_duration, overall_survival)
    else:
        outcome = "RESISTANT"
        remission_duration = "NA"
        if l[d["PRIOR.CHEMO"]] == 0:
            s_constant = 198.3
            overall_survival = overall_survival + s_constant
        else:
            s_constant = 122.4
            overall_survival = overall_survival + s_constant
        print(l[d["Patient_id"]], outcome, remission_duration, overall_survival)



def flu_hdac(l):
    remission_duration = -3.689*l[d["BM.BLAST"]]
                       - 52.2*l[d["CASP9"]]
                       - 43.0*l[d["EIF2AK2"]]
                       - 238.2*l[d["Fli1"]]
                       + 80.2*l[d["HRNNPK"]]
                       + 41.1*l[d["MAPK14.pT180Y182"]]
                       - 43.4*l[d["PA2G4.pT37_46"]]
                       - 97.5*l[d["PIM1"]]
    overall_survival = -145.9*l[d["Fli1"]] - 152.3*l[d["SMAD3"]]
    if l[d["Ras.Stat"] == -1:
        r_constant = 557.5
        s_constant = 334.5
        remission_duration = r_constant + remission_duration
        overall_survival = overall_survival + s_constant
    elif l[d["Ras.Stat"]] == 0:
        r_constant = 104.4
        s_constant = -133
        remission_duration = r_constant + remission_duration
        overall_survival = overall_survival + s_constant
    else:
        r_constant = 346.5
        s_constant = 142.4
        remission_duration = r_constant + remission_duration
        overall_survival = overall_survival + s_constant
    print(l[d["Patient_id"]], "COMPLETE REMISSION", remission_duration, overall_survival)
        

def hdac_plus(l):
    v = 2.18 + 7.38*l[62]
    p = math.exp(v)/(1+math.exp(v))
    survival_duration = -12.02
                      + 312.9*l[d["H3histon"]]
                      + 6.149*l[d["CD19"]]
                      - 125.2*l[d["ZNF346"]]
                      + 81.5*l[d["INPPL1"]]
                      - 28.4*l[d["STAT1"]]
    if p < 0.5:
        remission_duration = -55.9
                           + 3.71006*l[d["BM.BLAST"]]
                           - 24.2804*l[d["CD20"]]
                           - 0.063989*l[d["BAD"]]
                           - 1.88277*l[d["CDKN2A"]]
                           + 7.84340*l[d["CTSG"]]
                           - 23.9177*l[d["NOTCH3"]]
                           + 158.370*l[d["RAC1_2_3"]]
        print(l[0], "COMPLETE REMISSION", remission_duration, survival_duration)
    else:
        remission_duration = "NA"
        print(l[0], "RESISTANT", remission_duration, survival_duration)

def stdarac_plus(l):
    v = 1.883 + (3.84 * l[262])
    p = math.exp(v)/(1+math.exp(v))
    if l[7] == 0:
        survival_days = 155.5       # constant
                      - 0.998*l[d["CD34"]]
                      + 58.8*l[d["FN1"]]
                      + 7.3*l[d["LYN"]]
                      + 77.8*l[d["NCL"]]
                      - 54.6*l[d["PIK3CA"]]
                      + 79.7*l[d["STAT1.pY701"]]
                      + 105.1*l[d["ERBB2.pY1248"]]
                      + 5.1*l[d["TAZ.pS89"]]
                      - 20.2*l[d["PRKAA1_2.pT172"]]
                      + 24.8*l[d["CBL"]]
    else:
        survival_days = 298.8       # constant
                      - 0.998*l[d["CD34"]]
                      + 58.8*l[d["FN1"]
                      + 7.3*l[d["LYN"]]
                      + 77.8*l[d["NCL"]]
                      - 54.6*l[d["PIK3CA"]]
                      + 79.7*l[d["STAT1.pY701"]]
                      + 105.1*l[d["ERBB2.pY1248"]]
                      + 5.1*l[d["TAZ.pS89"]]
                      - 20.2*l[d["PRKAA1_2.pT172"]]
                      + 24.8*l[d["CBL"]]
    if p < 0.5:
        #COMPLETE REMISSION
        remission_days = 130.740        # constant
                       + 0.000254*l[d["ABS.BLST"]]
                       + 0.506072*l[d["AKT1_2_3.pT308"]]
                       + 113.185*l[d["ASNS"]]
                       + 0.107952*l[d["FN1"]]
                       + 4.39748*l[d["GATA3"]]
                       + 4.65318*l[d["KIT"]
                       - 17.7418*l[d["MAP2K1_2.pS217_221"]]
                       + 44.774*l[d["MSI2"]]
                       - 0.018507*l[d["RPS6KB1"]]
                       - 55.9748*l[d["TP53.pS15"]]
                       - 24.9313*l[d["WTAP"]]
                       - 2.04675*l[d["ZNF296"]]
        print(l[0], "COMPLETE_REMISSION", remission_days, survival_days)
    else:
        #RESISTANT
        remission_days = "NA"
        print(l[0], "RESISTANT", remission_days, survival_days)





def anthra_hdac_calc(somelist):
    v = 1.02 
    v = v-0.0773*somelist[17] #PB.Blast
    v = v+ 1.864*somelist[20] # HGB
    v = v-0.18*somelist[29] #CD34
    v = v-0.1496*somelist[34] #CD19
    v= v+8.42*somelist[92] #EGFR
    v= v-4.12*somelist[141] #KDR
    v= v-4.25*somelist[172] #NRP1
    v= v+3.68*somelist[196] #PRKCB.II
    v= v-7.13*somelist[198] #PRKCD.pS664
    v= v-1.534*somelist[221] #SMAD2.pS465
    v= v+9.53*somelist[245] #TAZ

    numerator = math.exp(v)

    denominator = 1+math.exp(v)
    solution = numerator/denominator
    if solution > 0.5 :
        #don't have to calculate for days in remission. (set as NA)
        #calculate for survival days
        #finally return a string to stdout with patientid#, remission_status, remission days, and survival days.
        resdur = 260.8 - 0.956*14 - 0.482*21 - 1.202*27 + 47.7*35
                - 35.1*28 - 87.9*42 - 24.05*45 + 39.8*55 + 181.0*56
                - 83.9*68 + 42.24*75 - 67.4*90 - 173.8*103 + 44.6*119
                + 42.1*122 + 111.6*135 - 67.7*150 - 27.5*185 + 75.4*188
                + 34.4*271 + 59.0*226 - 50.7*247 + 116.5*258
        

    else:
        #calculate for days in remission

        #calculate for survival days
        #finally return a string to stdout with patientid#, remission_status, remission days, and survival days.



def anthra_hdac_calc(somelist):

    #remisssion probability
    v = 1.02 - 0.0773*somelist[d['PB.BLAST']] + 1.864*somelist[d['HGB']] - 0.1800*somelist[d['CD34']] - 0.1496*somelist[d['CD19']] + 8.42*somelist[d['EGFR']] - 4.12*somelist[d['KDR']]
         - 4.25*somelist[d['NRP1']] + 3.68*somelist[d['PRKCB.II']] - 7.13*somelist[d['PRKCD.pS664']] - 1.534*somelist[d['SMAD2.pS465']] + 9.53*somelist[d['TAZ']]
    numerator = math.exp(v)
    denominator = 1+math.exp(v)
    solution = numerator/denominator

    #
    
    if solution > 0.5 :
        #don't have to calculate for days in remission. (set as NA)
        remstatus = 'RESISTANT'
        remdur = 'NA'

    else:
        remstatus = 'COMPLETE_REMISSION'
                                                                                                      
        #calculate for days in remission
        remdur = 260.8 - 0.956*somelist[d['BM.BLAST']] - 0.482*somelist[d['PLT']]- 1.202*somelist[d['CD13']] + 47.7*somelist[d['ACTB']]
                     - 35.1*somelist[d['AKT1_2_3.pS473']] - 87.9*somelist[d['ASNS']] - 24.05*somelist[d['BAD']] + 39.8*somelist[d['BID']] + 181.0*somelist[d['BIRC2']]
                     - 83.9*somelist[d['CBL']] + 42.24*somelist[d['CD74']] - 67.4*somelist[d['DLX1']] - 173.8*somelist[d['ERBB3']] + 44.6*somelist[d['H3K27Me3']]
                     + 42.1*somelist[d['HDAC1']] + 111.6*somelist[d['ITGA2']] - 67.7*somelist[d['MAPK1']] - 27.5*somelist[d['PIM1']] + 75.4*somelist[d['PPARA']]
                     + 34.4*somelist[d['SIRT1']] + 59.0*somelist[d['SMAD6']] - 50.7*somelist[d['TCF4']] + 116.5*somelist[d['XIAP']]

    if (somelist[1]== 0):
        Overall_Survival = 503.1 - 4.960*somelist[d['Age.at.Dx']] - 0.2212*somelist[d['FIBRINOGEN']] + 33.8*somelist[d['BAD.pS155']]
                            + 95.6*somelist[d['BIRC2']] - 59.0*somelist[d['BMI1']] - 103.0somelist[d['DLX1']]- 79.1*somelist[d['ERG']] + 50.4*somelist[d['H3histon']]
                            - 36.3*somelist[d['IRS1.pS1101']] + 37.3*somelist[d['MAPK14.pT180Y182']] + 58.3*somelist[d['MDM4']] + 98.6*somelist[d['MSI2']]
                            - 29.7*somelist[d['PRKAA1_2.pT172']] - 34.8*somelist[d['PRKCD.pT507']] + 62.9*somelist[d['PTK2']]
                            - 41.0*somelist[d['RB1.pS807_811']] - 119.0*somelist[d['SMAD5.pS463']] + 69.8*somelist[d['WTAP']]
        print(somelist[0], remstatus, remdur, Overall_Survival)

    else:
        Overall_Survival = 503.1 - 4.960*somelist[d['Age.at.Dx']] - 0.2212*somelist[d['FIBRINOGEN']] + 33.8*somelist[d['BAD.pS155']]
                            + 95.6*somelist[d['BIRC2']] - 59.0*somelist[d['BMI1']] - 103.0somelist[d['DLX1']]- 79.1*somelist[d['ERG']] + 50.4*somelist[d['H3histon']]
                            - 36.3*somelist[d['IRS1.pS1101']] + 37.3*somelist[d['MAPK14.pT180Y182']] + 58.3*somelist[d['MDM4']] + 98.6*somelist[d['MSI2']]
                            - 29.7*somelist[d['PRKAA1_2.pT172']] - 34.8*somelist[d['PRKCD.pT507']] + 62.9*somelist[d['PTK2']]
                            - 41.0*somelist[d['RB1.pS807_811']] - 119.0*somelist[d['SMAD5.pS463']] + 69.8*somelist[d['WTAP']]
        print(somelist[0], remstatus, remdur, Overall_Survival)





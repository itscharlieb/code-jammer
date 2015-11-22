import math

def hdac_plus(l):
    v = 2.18 + 7.38*l[62]
    p = math.exp(v)/(1+math.exp(v))
    survival_duration = -12.02
                      + 312.9*l[118] # H3histon
                      + 6.149*l[34]  # CD19
                      - 125.2*l[265] # ZNF346
                      + 81.5*l[133]  # INPPL1
                      - 28.4*l[235]  # STAT1
    if p < 0.5:
        remission_duration = -55.9
                           + 3.71006*l[14] # BM.BLAST
                           - 24.2804*l[32] # CD20
                           - 0.063989*l[45]# BAD
                           - 1.88277*l[80] # CDKN2A
                           + 7.84340*l[88] # CTSG
                           - 23.9177*l[168]# NOTCH3
                           + 158.370*l[207]# RAC1_2_3
        print(l[0], "COMPLETE REMISSION", remission_duration, survival_duration)
    else:
        remission_duration = "NA"
        print(l[0], "RESISTANT", remission_duration, survival_duration)

def stdarac_plus(l):
    v = 1.883 + (3.84 * l[262])
    p = math.exp(v)/(1+math.exp(v))
    if l[7] == 0:
        survival_days = 155.5       # constant
                      - 0.998*l[29] # CD34
                      + 58.8*l[106] # FN1
                      + 7.3*l[147]  # LYN
                      + 77.8*l[164] # NCL
                      - 54.6*l[183] # PIK3CA
                      + 79.7*l[236] # STAT1.pY701
                      + 105.1*l[102]# ERBB2.pY1248
                      + 5.1*l[246]  # TAZ.pS89
                      - 20.2*l[192] # PRKAA1_2.pT172
                      + 24.8*l[68]  # CBL
    else:
        survival_days = 298.8       # constant
                      - 0.998*l[29] # CD34
                      + 58.8*l[106] # FN1
                      + 7.3*l[147]  # LYN
                      + 77.8*l[164] # NCL
                      - 54.6*l[183] # PIK3CA
                      + 79.7*l[236] # STAT1.pY701
                      + 105.1*l[102]# ERBB2.pY1248
                      + 5.1*l[246]  # TAZ.pS89
                      - 20.2*l[192] # PRKAA1_2.pT172
                      + 24.8*l[68]  # CBL
    if p < 0.5:
        #COMPLETE REMISSION
        remission_days = 130.740        # constant
                       + 0.000254*l[13] # ABS.BLST
                       + 0.506072*l[39] # AKT1_2_3.pT308
                       + 113.185*l[42]  # ASNS
                       + 0.107952*l[106]# FN1
                       + 4.39748*l[114] # GATA3
                       + 4.65318*l[142] # KIT            
                       - 17.7418*l[149] # MAP2K1_2.pS217_221
                       + 44.774*l[160]  # MSI2
                       - 0.018507*l[212]# RPS6KB1
                       - 55.9748*l[251] # TP53.pS15
                       - 24.9313*l[258] # WTAP
                       - 2.04675*l[264] # ZNF296
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



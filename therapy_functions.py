import math

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

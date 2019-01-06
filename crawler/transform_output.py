# import json
#
# p = open("/Users/architdwivedi/Documents/a.csv").read().split("\n")[:-1]
# dt = {
#
# }
# for e in p:
#     title,url = e.split("@@")
#     dt[title] = url
#
# p2 = json.loads(open("/Users/architdwivedi/Downloads/all.json").read())
#
# p2['com']['Metamucil'].update(p2['com']['Metamucil Generic'])
# del p2['com']['Metamucil Generic']
#
# p2['com']['Organic India'].update(p2['com']['ORGANIC INDIA'])
# del p2['com']['ORGANIC INDIA']
#
#
# dt = p2['com']['']
# for key, value in dt.items():
#     if 'Benefiber' in key:
#         p2['com']['Benefiber'][key] = value
#     if 'Metamucil' in key:
#         p2['com']['Metamucil'][key] = value
#     if 'Prima' in key:
#         p2['com']['Yerba Prima'][key] = value
#
# del p2['com']['']
# f = open('all_url.json', "w+")
# f.write(json.dumps(p2))
#
#


crawled_urls = {'B015X2CGSS': True, 'B07JW6FJBZ': True, 'B00CX3ASFE': True, 'B000MM2RZM': True, 'B01KJ8TKEO': True, 'B01AFQAA8K': True, 'B00Y98KB6C': True, 'B00XFFR0ZK': True, 'B01IAIN72G': True, 'B077RG1DDY': True, 'B015VBRIXE': True, 'B00CX3ASFO': True, 'B00ZQUDM1I': True, 'B01IAILP7A': True, 'B00CX3ASG8': True, 'B01M1P8RUY': True, 'B01978FIZC': True, 'B000KF861U': True, 'B01CAXK25M': True, 'B074TZL3MK': True, 'B01CZ5GTZC': True, 'B077FGC1F1': True, 'B01M0M4WC0': True, 'B004H2YFKI': True, 'B002HI1LSI': True, 'B007P4VNUK': True, 'B000052Y5Q': True, 'B00G4EM9PA': True, 'B01BS52GXE': True, 'B0013I4WJS': True, 'B06WVKL6CR': True, 'B006TGVASK': True, 'B00EEELBSI': True, 'B000XEEFTK': True, 'B0013HX164': True, 'B000GG1Y7G': True, 'B00BNWSHV8': True, 'B0013I1H9G': True, 'B01KCJ8I1Q': True, 'B0015EGWMU': True, 'B079JKPWGW': True, 'B0062NSWB8': True, 'B01N9692HZ': True, 'B01N4L4D7H': True, 'B001V9OMH6': True, 'B06W2PJCVP': True, 'B001N0LPIC': True, 'B01IAI1EAI': True, 'B001G7QVAE': True, 'B0013I4WLG': True, 'B01F803620': True, 'B003CT2YQY': True, 'B001G7QVPE': True, 'B001G7QVAY': True, 'B0039283FU': True, 'B01IPNOHUM': True, 'B001TH7K0G': True, 'B01CLIZH9C': True, 'B01CLIZGYI': True, 'B0077STR16': True, 'B0013OW2KS': True, 'B00JDOAKRM': True, 'B01M11KMUJ': True, 'B0016AXN7A': True, 'B0015R9DD2': True, 'B0015R9EAY': True, 'B0015R78DO': True, 'B000F4SX1E': True, 'B00QSEJ7GU': True, 'B0013JX59U': True, 'B005UO7U1S': True, 'B07HKJH7SB': True, 'B001E0XFHK': True, 'B00024D5IS': True, 'B01NBAL2TZ': True, 'B000QYBMUC': True, 'B00014G38S': True, 'B01MTQLS8I': True, 'B001E0ZFUK': True, 'B01ATPBE6O': True, 'B000IRLIKG': True, 'B001E1AZH2': True, 'B000Z90KFG': True, 'B001E14OQA': True, 'B07743LDYM': True, 'B00013Z128': True, 'B000264L9I': True, 'B00424VPZ4': True, 'B00U0K6YMS': True, 'B00AMP46GW': True, 'B01N4MU58I': True, 'B01E5TCPI6': True, 'B01JD1PN62': True, 'B00YDES7JU': True, 'B00F3J329O': True, 'B00Z8JN852': True, 'B06VY6PMLV': True, 'B0012DEKUK': True, 'B00IYDFN0W': True, 'B00DP328NG': True, 'B00NX5HJE4': True, 'B01MYZ7AW3': True, 'B00IZN1VUW': True, 'B004GMC2N6': True, 'B007729FFK': True, 'B00EZLA7A8': True, 'B0009NBCVY': True, 'B077T2MYK5': True, 'B001TJZIQW': True, 'B00U8HT2K4': True, 'B0019LRWFK': True, 'B005LHMVF4': True, 'B00OTR2V7K': True, 'B001G7R158': True, 'B0014UUQX6': True, 'B0015R9EG8': True, 'B000F4F9KW': True, 'B00DZG47BE': True, 'B003FG8AVM': True, 'B00014IZO8': True, 'B010CPSBWQ': True, 'B0010WD338': True, 'B0039OZ5KE': True, 'B002JWZXKY': True, 'B001F0QZBC': True, 'B000YMDVP0': True, 'B00E4MNEW6': True, 'B018NHB5L4': True, 'B001F0R76O': True, 'B004B8F85Y': True, 'B00B8YUQXS': True, 'B004ZKX73I': True, 'B00JI4WCGO': True, 'B0728NQ4W4': True, 'B07KN57Z6P': True, 'B07K7NHY8Y': True, 'B01I60PXQ6': True}


import json
p2 = json.loads(open("/Users/architdwivedi/Downloads/amz_hld_vita_india_uk_mix.json").read())
p3 = json.loads(open("/Users/architdwivedi/Downloads/wallmart.json").read())
p2.update(p3)

c = 0
for co, br in p2.items():
    for e1,v1 in br.items():
        for brand,value in v1.items():
            c+= len(value['reviews'])


# f = open('/Users/architdwivedi/Downloads/amz_hld_vita_india_uk_wallmartmix.json', "w+")
# f.write(json.dumps(p2))
print(c)

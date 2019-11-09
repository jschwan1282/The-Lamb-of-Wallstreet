import pandas as pd

nov1to7 = pd.read_json('nov1to7.json', encoding='utf-8')
nov7to14 = pd.read_json('nov7to14.json', encoding='utf-8')
nov14to21 = pd.read_json('nov14to21.json', encoding='utf-8')
nov21to28 = pd.read_json('nov21to28.json', encoding='utf-8')
nov28todec5 = pd.read_json('nov28todec5.json', encoding='utf-8')
dec5todec12 = pd.read_json('dec5todec12.json', encoding='utf-8')
dec12todec19 = pd.read_json('dec12todec19.json', encoding='utf-8')
dec19todec26 = pd.read_json('dec19todec26.json', encoding='utf-8')
dec26tojan02 = pd.read_json('dec26tojan02.json', encoding='utf-8')
jan02to09 = pd.read_json('jan02to09.json', encoding='utf-8')
jan09to16 = pd.read_json('jan09to16.json', encoding='utf-8')
jan16to23 = pd.read_json('jan16to23.json', encoding='utf-8')
jan23to30 = pd.read_json('jan23to30.json', encoding='utf-8')
jan30tofeb06 = pd.read_json('jan30tofeb06.json', encoding='utf-8')
feb06to13 = pd.read_json('feb06to13.json', encoding='utf-8')
feb13to20 = pd.read_json('feb13to20.json', encoding='utf-8')
feb20to27 = pd.read_json('feb20to27.json', encoding='utf-8')
feb27tomar06 = pd.read_json('feb27tomar06.json', encoding='utf-8')
mar06to13 = pd.read_json('mar06to13.json', encoding='utf-8')
mar13to20 = pd.read_json('mar13to20.json', encoding='utf-8')
mar20to27 = pd.read_json('mar20to27.json', encoding='utf-8')
mar27toapr03 = pd.read_json('mar27toapr03.json', encoding='utf-8')
apr03to10 = pd.read_json('apr03to10.json', encoding='utf-8')
apr10to17 = pd.read_json('apr10to17.json', encoding='utf-8')
apr17to24 = pd.read_json('apr17to24.json', encoding='utf-8')
apr24tomay01 = pd.read_json('apr24tomay01.json', encoding='utf-8')
may01to08 = pd.read_json('may01to08.json', encoding='utf-8')
may08to15 = pd.read_json('may08to15.json', encoding='utf-8')
may15to22 = pd.read_json('may15to22.json', encoding='utf-8')
may22to29 = pd.read_json('may22to29.json', encoding='utf-8')
may29tojun05 = pd.read_json('may29tojun05.json', encoding='utf-8')
jun05to12 = pd.read_json('jun05to12.json', encoding='utf-8')
jun12to19 = pd.read_json('jun12to19.json', encoding='utf-8')

master_merged = pd.concat([nov1to7, nov7to14, nov14to21, nov21to28, nov28todec5, dec5todec12, 
                          dec12todec19, dec19todec26, dec26tojan02, jan02to09, jan09to16, jan16to23, 
                          jan23to30, jan30tofeb06, feb06to13, feb13to20, feb20to27, feb27tomar06, 
                          mar06to13, mar13to20, mar20to27, mar27toapr03, apr03to10, apr10to17, 
                          apr17to24, apr24tomay01, may01to08, may08to15, may15to22, may22to29, may29tojun05,
                          jun05to12, jun12to19], ignore_index=True)



master_merged['timestamp'] = pd.to_datetime(master_merged['timestamp']).dt.date

clean = master_merged[['timestamp','likes','retweets','text']]


clean_group.dtypes

clean.to_csv('cleanedtweets.csv', index=False)
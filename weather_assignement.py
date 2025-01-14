import json 
import string
seattle_results = {}
csv_seattle = ['Seattle,WA,GHCND:US1WAKG0038']
seattle_station_code = 'GHCND:US1WAKG0038'
months = [ '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
with open ('stations.csv', encoding = 'utf-8') as file:
   code_content = file.read() 

seattle= []
with open ('precipitation.json', 'r') as file: 
    contents= json.load(file) 
    for element in contents: 
        if element['station'] == seattle_station_code:
            seattle.append(element)

    monthly_precipitation = []
    total_monthly_precipitation = 0
    for month in months:
        for  key in seattle:
            if key['date'] >= f'2010-{month}-01' and key['date'] <= f'2010-{month}-31':
                monthly_precipitation.append(key['value'])
                total_monthly_precipitation = total_monthly_precipitation + key['value']

        print(f'{month}', total_monthly_precipitation)
    
        seattle_results[month] = {
        'total_monthly_precipitation' : total_monthly_precipitation, 
    }
with open ('results.json', 'w') as file:
    json.dump(seattle_results, file, indent = 4)
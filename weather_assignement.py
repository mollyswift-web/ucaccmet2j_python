import json 
import string
import csv
seattle_ = {}
csv_seattle = ['Seattle,WA,GHCND:US1WAKG0038']
seattle_station_code = 'GHCND:US1WAKG0038'
months = [ '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
with open ('stations.csv', encoding = 'utf-8') as file:
   code_content = file.read() 

seattle_data= []
with open ('precipitation.json', 'r') as file: 
    contents= json.load(file) 
    for element in contents: 
        if element['station'] == seattle_station_code:
            seattle_data.append(element)

    monthly_precipitation = []
    for month in months:
        total_monthly_precipitation = 0
        for  key in seattle_data:
            if key['date'] >= f'2010-{month}-01' and key['date'] <= f'2010-{month}-31':
                total_monthly_precipitation = total_monthly_precipitation + key['value']

       
        print(f'{month}', total_monthly_precipitation)
        monthly_precipitation.append(total_monthly_precipitation)

    total_year_precipitation = sum(monthly_precipitation)
    
    print(total_year_precipitation)
    
    relative_month = []
    for number in monthly_precipitation:
        total_year_precipitation = sum(monthly_precipitation)
        relative_monthly_precipitation = number / total_year_precipitation
        relative_month.append(relative_monthly_precipitation)
    
    print('total year precipitation', total_year_precipitation)
    print('relative_monthly_precipitation',relative_month)

seattle = {
    'total_monthly_precipitation' : monthly_precipitation, 
    'total_year_precipitation' : total_year_precipitation,
    'relative_monthly_precipitation' : relative_month 
    }
with open ('results.json', 'w') as file:
     json.dump(seattle, file, indent = 4)
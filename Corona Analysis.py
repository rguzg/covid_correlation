import csv
import datetime

date = datetime.datetime(2020,5,18)
cases_relation = {}
counter = 0

# csvdate = '{0:%d}/{0:%m}/{0:%y}'.format(date.date())

# print(csvdate)
with open('D:\\raulg\\Desktop\\200518COVID19MEXICO.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        counter += 1
        
        if counter == 1000:
            break

        print("Checking {0}".format(row['FECHA_ACTUALIZACION']))

        cases_per_day = 0
        obesity_cases = 0
        if(row['FECHA_ACTUALIZACION'] == str(date.date())):
            cases_per_day += 1
            # A number two means that the pacient is obese
            if(row['OBESIDAD'] == '2'):
                obesity_cases += 1
        
        if(cases_per_day in cases_relation):
            cases_relation[cases_per_day] += obesity_cases
        else:
            cases_relation[cases_per_day] = obesity_cases

        print("Out of {0} cases, {1} were obese".format(cases_per_day, obesity_cases))

with open('D:\\raulg\\Desktop\\obesity_cases.csv', newline='') as obese_file:
    writer = csv.writer(obese_file)

    for key in cases_relation:
        writer.writerow(key, cases_relation[key])







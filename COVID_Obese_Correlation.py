import csv
import datetime

current_date = datetime.datetime(2020,1,1)
cases_relation = {}
counter = 0
cases_per_day = 0
obesity_cases = 0

with open('D:\\raulg\\Desktop\\200518COVID19MEXICO.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        counter += 1
        print("Checking case #{0}".format(counter), end='\r')

        if(row['FECHA_INGRESO'] == "{0:%d}/{0:%m}/{0:%y}".format(current_date)):
            if(row['RESULTADO'] == '2'):
                cases_per_day += 1
            # A number two means that the pacient is obese
            if(row['OBESIDAD'] == '2'):
                obesity_cases += 1
        else:
            print("\nChecked {0}".format(row['FECHA_INGRESO']))
            current_date = current_date + datetime.timedelta(days = 1)

            cases_relation[str(current_date.date())] = {'cases_per_day': cases_per_day, 'obesity_cases': obesity_cases}

            print("\nOut of {0} cases, {1} were obese".format(cases_per_day, obesity_cases))

            cases_per_day = 0
            obesity_cases = 0


with open('D:\\raulg\\Desktop\\obesity_cases.csv', newline='', mode='w') as obese_file:
    writer = csv.writer(obese_file)

    for key in cases_relation:
        writer.writerow([cases_relation[key]['obesity_cases'], cases_relation[key]['cases_per_day']])

    print("\nCSV written")







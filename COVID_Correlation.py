import csv
import datetime
import sys
import os

try:
    input_file = sys.argv[1]
    start_date = sys.argv[2]
    csv_column = sys.argv[3]
    output_path = os.path.dirname(input_file)

    current_date = datetime.date.fromisoformat(start_date)
    cases_relation = {}

    counter = 0
    cases_per_day = 0
    check_constraint = 0
    deaths_per_day = 0
    with open(input_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            counter += 1
            print("Checking case #{0}".format(counter), end='\r')

            if(row['FECHA_INGRESO'] == "{0:%d}/{0:%m}/{0:%y}".format(current_date)):
                if(row['RESULTADO'] == '1'):
                    cases_per_day += 1
                # A number one means that the constraint asserts to true
                if(row[csv_column] == '1'):
                    check_constraint += 1
                if(row['FECHA_DEF'] != '9999-99-99'):
                    deaths_per_day += 1
            else:
                print("\nChecked {0}".format(row['FECHA_INGRESO']))
                current_date = current_date + datetime.timedelta(days = 1)

                cases_relation[str(current_date)] = {'cases_per_day': cases_per_day, 'check_constraint': check_constraint, 'deaths_per_day': deaths_per_day}

                print("\nOut of the {0} checked cases, {1} cases asserted true to the constraint: {2} and {3} people died".format(cases_per_day, check_constraint, csv_column, deaths_per_day))

                cases_per_day = 0
                check_constraint = 0
                deaths_per_day = 0


    with open('{0}/output.csv'.format(output_path), newline='', mode='w') as output_file:
        writer = csv.writer(output_file)

        writer.writerow([csv_column, "CASES_PER_DAY", "DEATHS_PER_DAY"])

        for key in cases_relation:
            writer.writerow([cases_relation[key]['check_constraint'], cases_relation[key]['cases_per_day'], cases_relation[key]['deaths_per_day']])

        print("\nCSV saved as {0}\output.csv".format(os.path.abspath(output_path)))
except IndexError as error:
    print("Please specify the input csv file, starting date and the column to check")
except ValueError as error:
    print("The date should be in ISO format -> YYYY-MM-DD")






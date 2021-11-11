open_file = open("CupcakeInvoices.csv")
# print(open_file)


#loop through all the data and print each row

# for line in open_file:
#     print(line)

#Loop through all the data and print the type of cupcakes purchased


# for line in open_file:
#     values = line.split(',')                                #split(seperator, maxsplit) method spting a string into alist 
#     print(values[2])    #2 what index to print                # seperator is an optional param, specifies the separtor to use when splitting the string, by default any whitespace is the seperator
                                                             #maxsplit: optional, specifies how many to split, default is -1, which is "all occurrences"


#Loop through all the data and print out the total for each invoice 
#(Note: this data is not provided by the csv, you will need to calculate it. 
#Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. 
#Research how to do this.).

#my solution
# for line in open_file:
#     values = line.split(',') 
#     print(float(values[3]) * float(values[4]))
# # answer key
# for line in open_file:
#   values = line.split(',')
#   total = int(values[3]) * float(values[4])
#   print(total)

# Loop through all the data, and print out the total for all invoices combined.
invoice_total = 0

for line in open_file:
    values = line.split(',')
    invoice_total += (float(values[3]) * float(values[4]))


print(invoice_total)


open_file.close()
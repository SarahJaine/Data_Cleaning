## Purpose: Change exported custom templates in PowerSchool from html tagged nightmare to a two column csv spreadsheet.
#### > The first column will contain the Name as described in the custom template.
#### > The second column will contain the PowerSchool Field as described in the custom template.

## Directions:
#### > Paste the name of your file in the "" marks on the line below. Be sure to include the file extension, the file should be saved in .csv format.
#### > The file you are using must be saved in the same folder as this script.
#### > Your new file will be named "output_template.csv".

your_original_file="" 

with open("your_original_file.csv", "r") as input_template:
	template = input_template.read().split(',')

	title=["Title"]
	field=["Field"]

	for each in template:
		if "<Title>" in each:
			title_start=each.find('''<Title>''')+7
			title_stop=each.find('''</Title>''')
			title.append(each[title_start:title_stop])
		if "<Field>" in each:
			field_start=each.find('''<Field>''')+7
			field_stop=each.find('''</Field>''')
			if each[field_start:field_stop] !="Tab" and each[field_start:field_stop] !="CSV":
				field.append(each[field_start:field_stop])

output_data=[]
for left, right in zip(title,field):
	output_data.extend([left,",", right,"\n"])

with open("output_template.csv","w") as output_template:
	output_template.write("")
	for each in output_data:
		output_template.write("".join(each))

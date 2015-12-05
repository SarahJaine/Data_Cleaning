def gender(x):
	if x == " ":
		return " "
	else:
		if x == "1":
			return "M"
		elif x == "2":
			return "F"
		else:
			return "No Response"
def date_format_MMDDYY(x):
	if x == "      ":
		return "      "
	else:
		month = int(x[0:2])
		day = int(x[2:4])
		yr = int(x[4:7])
		if yr < 20:
			year = int("20"+x[4:7])
		else:
			year = int("19"+x[4:7])
		return "{0}/{1}/{2}".format(month, day, year)
def date_format_MMYY(x):
	if x == "    ":
		return "    "
	else:
		month = int(x[0:2])
		year = 2000+int(x[3:5])
		return "{0}/{1}".format(month, year)
def date_format_MMDDYYYY(x):
	if x == "        ":
		return "        "
	else:
		month = x[0:2]
		day = x[2:4]
		year = x[4:8]
		return "{0}/{1}/{2}".format(month, day, year)
def ed_level_to_grade(x):
	if x == " ":
		return " "
	else:
		x = int(x)
		if x >1 and x<=6:
			return str(x+6)
		elif x == 1:
			return "Not yet in 8th grade"
		elif x == 7:
			return "No longer in high school"
		elif x == 9:
			return "No Response"
		else:
			return "Unknown"
def phone_format(x):
	if x == "          ":
		return "          "
	else:
		area = x[0:3]
		a = x[3:6]
		b = x[6:10]
		return "({0}) {1}-{2}".format(area,a,b)


column_headers="cb_hs_code,last_name,first_name,middle_initial,\
sex,DOB,street_address,city,state,zip_code,residence_code,\
telephone_number,hs_graduation_date,foreign_address_indicator,\
test_date,grade_level,revised_score_indicator,\
critical_reading,mathematics,writing,essay,writing_mult_choice,\
sat_admin_2,sat_admin_3,sat_admin_4,sat_admin_5,sat_admin_6,\
subject_test_date,subject_grade_level,subject_revised_score_indicator,subject_test_code_1,subject_test_score_1,\
subject_test_1_sub_1,subject_test_1_sub_2,subject_test_1_sub_3,remaining_subject_tests,\
prev_subject_test_scores,critical_reading_p_nat,critical_reading_p_state,mathematics_p_nat,mathematics_p_state,writing_p_nat,writing_p_state,email,subject_test_p,remaining_data\r"

output_data=[column_headers]

with open("SAT_Rcvd2015.05.06.csv", "r") as nondelimit_file:
	nondelimit = nondelimit_file.read().split('\r')
	# for each in test:
	for index, row in enumerate(nondelimit):
		# split_data = row[0:7], ",", row[7:9], ",",row[9]
	
		##set student_info
		cb_hs_code = row[0:6]
		last_name = row[6:21]
		first_name = row[21:33]
		middle_initial = row[33]
		sex = gender(row[34])
		DOB = date_format_MMDDYY(row[35:41])
		street_address = row[50:75]

		##split domestic_address
		city = row[75:90]
		state = row[91:93]
		zip_code = row[94:103]
		residence_code = row[106:111]

		##split other_student_information
		telephone_number = phone_format(row[116:126])
		hs_graduation_date = date_format_MMYY(row[126:130])
		foreign_address_indicator = row[135]

		##split latest_sat_scores
		test_date = date_format_MMDDYYYY(row[139:147])
		grade_level = ed_level_to_grade(row[147])
		revised_score_indicator = row[149]
		critical_reading = row[150:153]
		mathematics = row[153:156]
		writing = row[156:159]
		essay = row[159:161]
		writing_mult_choice = row[161:163]

		##split previous_sat_scores
		sat_admin_2 = row[163:187]
		sat_admin_3 = row[187:211]
		sat_admin_4 = row[211:235]
		sat_admin_5 = row[235:259]
		sat_admin_6 = row[259:283]

		##split latest_subject_test_scores
		subject_test_date = date_format_MMDDYYYY(row[283:291])
		subject_grade_level = ed_level_to_grade(row[291])
		subject_revised_score_indicator = row[293]
		subject_test_code_1 = row[294:296]
		subject_test_score_1 = row[296:299]
		subject_test_1_sub_1 = row[299:301]
		subject_test_1_sub_2 = row[301:303]
		subject_test_1_sub_3 = row[303:305]
		remaining_subject_tests = row[305:327]

		##split pevious_subject_test_scores
		prev_subject_test_scores = row[327:614]

		## latest_percentiles
		critical_reading_p_nat = row[614:616]
		critical_reading_p_state = row[616:618]
		mathematics_p_nat = row[618:620]
		mathematics_p_state = row[620:622]
		writing_p_nat = row[622:624]
		writing_p_state = row[624:626]
		email = row[626:676]
		subject_test_p = row[676:710]

		##remaining data
		remaining_data = row[710:]

		##combine variables into individual sections
		student_info = cb_hs_code + "," + last_name + "," + first_name + "," + middle_initial + "," + sex + "," + DOB + "," + street_address + "," + city
		domestic_address = state + "," + zip_code + "," + residence_code
		other_student_information = telephone_number + "," + hs_graduation_date + "," + foreign_address_indicator
		latest_sat_scores = test_date + "," + grade_level + "," + revised_score_indicator + "," + critical_reading + "," + mathematics + "," + writing + "," + essay + "," + writing_mult_choice
		previous_sat_scores = sat_admin_2 + "," + sat_admin_3 + "," + sat_admin_4 + "," + sat_admin_5 + "," + sat_admin_6
		latest_subject_test_scores = subject_test_date + "," + subject_grade_level + "," + subject_revised_score_indicator + "," + subject_test_code_1 + "," + subject_test_score_1 + "," + subject_test_1_sub_1 + "," + subject_test_1_sub_2 + "," + subject_test_1_sub_3 + "," + remaining_subject_tests + "," + prev_subject_test_scores
		latest_percentiles = critical_reading_p_nat + "," + critical_reading_p_state + "," + mathematics_p_nat + "," + mathematics_p_state + "," + writing_p_nat + "," + writing_p_state + "," + email + "," + subject_test_p

		##combine sections into split_data
		split_data = student_info + "," + domestic_address + "," + other_student_information + "," + latest_sat_scores + "," + previous_sat_scores + "," + latest_subject_test_scores + "," + prev_subject_test_scores + "," + remaining_data
		output_data.append(split_data)
		output_data.append('\r')

## output_data.append("cb_hs_code \r")
with open("output_sat.csv","w") as output_file:
	output_file.write("")
	for each in output_data:
		output_file.write("".join(each))

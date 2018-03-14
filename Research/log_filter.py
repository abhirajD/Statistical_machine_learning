'''
Code to match profile_logs with highlevel functions found in function tree.
Uses simple regex.
'''

import re

functions = []
counter = 0
with open('function_tree.txt') as f:
	for line in f.readlines():
			if '-function' in line:
				counter += 1
				if '=' in line:
					function_regex = r'-function\s+.*=\s+(?P<func>\w*)[\W]'
					result = re.search(function_regex, line)
					functions.append(result.group('func'))
				else:
					function_regex = r'-function\s+(?P<func>\w*)\W'
					result = re.search(function_regex, line)
					functions.append(result.group('func'))

#Number of functions discvered should be equal to the number of line starteing with function.
print('Number of function lines = {} \nNumber of functions discovered = {}'.format(counter,len(functions)))

#Now that we have all the functions,
#Lets match them with Profile_logs and keep only those functions which match high level functions
#obtained from function tree

with open('filtered_profile_logs.txt', 'w') as new_log:
	with open('profile_log.txt') as f:
		for line in f.readlines():
			if any(function in line for function in functions):
				new_log.write(line)

#Done


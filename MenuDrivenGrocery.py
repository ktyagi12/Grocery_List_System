print '*'* 140
print '\n\t\t\t\t\t\t\t\t','WELCOME TO GROFERS'
print '='* 140

choice = 0
grocery_list = []

while (choice!=6):
	print '\n\t\t\t\t\t\t\t\t','PICK FOR YOUR GROCERY LIST'
	print '\t\t\t\t\t\t\t\t','1. ADD THE ITEM','\n\t\t\t\t\t\t\t\t','2. INSERT THE ITEM'
	print '\t\t\t\t\t\t\t\t','3. REMOVE THE ITEM','\n\t\t\t\t\t\t\t\t','4. UPDATE THE ITEM','\n\t\t\t\t\t\t\t\t','5. DISPLAY GROCERY LIST','\n\t\t\t\t\t\t\t\t','6. EXIT'
	choice = int(raw_input('Enter your choice: '))
	if (choice ==1):
		num_items = int(raw_input('\nHow many items you wanna add to your grocery list: '))
		for i in range(0,num_items,1):
			grocery_list.append(raw_input('\nEnter the ' + str(i + 1) + ' element: ').upper())
			print '\nGrocery List: ', grocery_list
	
	elif (choice ==2):
		num_items = int(raw_input('\nHow many items you wanna add more: '))
		for i in range(0,num_items,1):
			pos = int(raw_input('\nAt which position you want to insert item No.' + str(i+1) + ': '))
			grocery_list.insert(pos,raw_input('\nEnter the new element to insert: ').upper())
			print '\nGrocery List after insertion: ' , grocery_list

	
	elif (choice ==3):
		rem_ele = raw_input('\nWhich item you want to remove: ').upper()
		if(rem_ele in grocery_list):
			grocery_list.remove(rem_ele)
			print '\nGrocery List after removal: ' , grocery_list
		else:
			print '\nOops!! No such element in your list..'
	
	elif(choice ==4):
		pos = int(raw_input('\nAt which position you want to update the item: '))
		if (pos <= len(grocery_list)):
			grocery_list[pos]= raw_input('\nEnter the updated item: ').upper()
			print '\nGrocery List after updation: ' , grocery_list
		else:
			print '\nOops!! Sorry No such position in your grocery list..'
	
	elif(choice ==5):
		print '\nYour grocery list is: '
		for i in range(0,len(grocery_list),1):
			print (grocery_list[-(i+1)])
	
	elif(choice ==6):
		exit()
	else:
		print '\nOops!! Sorry!! No such option is available with us..'
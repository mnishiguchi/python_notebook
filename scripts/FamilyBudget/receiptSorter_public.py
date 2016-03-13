######################################
##  ReceiptSorter.py     
##  Author: Masatoshi Nishiguchi   
##  Date:   July 9, 2014            
######################################


from datetime import datetime
import csv

# list of all the spending CATEGORIES
CATEGORIES = ['Groceries', 'Family_misc', 'Gas', 'Car', 'Medical', 'Dental',
              'Clothing', 'Grooming','Eating_out', 'Gifts', 'Educational', 'Hobbies', 'Extraordinary']

# path to directry where you want to create files
PATH = 'C:\Users\user\FamilyBudget\\'

# get date and time
now = datetime.now()
formatNow = "%d-%02d-%02d_%02d%02d" % (now.year, now.month, now.day, now.hour, now.minute)


def receiptSorter(CATEGORIES):
    '''param: list of categories; 
       return: None'''
    
    # temporary storages
    previousFile = []                    # for loaded data
    history = []                         # for editting history
    spendings = [0.0] * len(CATEGORIES)  # for user input
    print
    print ">>> HELLO!!!"
    
    # ask user if he/she wants to read previous file
    userInput0 = raw_input(">>> Hit [ENTER] to start with a clean slate, or type [R] to read saved data: ")
           
    if userInput0 == 'r' or userInput0 == 'R':
        try:  
            readFile = PATH + "temp.csv"
            previousFile = csvReader(readFile)    # list of lists
            
            if previousFile == []:
                print
                print '>>> You created a CSV file in the last session. Saved data is empty.'
                return
            
            # extract spending values from each row of previousFile   
            for i in range( len(CATEGORIES) ):
                spendings[i] = float( previousFile[i][1] )
                
            if len(previousFile) != len(CATEGORIES):
                history.extend( previousFile[ len(CATEGORIES): ] )
                # record this session on history
                history.append(['updated', formatNow]) 
            else:
                print
                print ">>> No history error. "
                
        except IOError:
            print
            print ">>> Couldn't read a temp file. Please make sure the path is correct."
            print ">>> Currently specified path: %s" % readFile
            return
        except:
            print
            print ">>> File format error. "
            return
    else:
        history.append(['',''])
                
        # record this session on history
        history.append(['created', formatNow])
        
    while True:
        # show the categories list for user to reference
        print
        print '--------------------------------------------------------------------------------------------------------'
        print '[CATEGORY CODES]'  
        for i in enumerate(CATEGORIES) :
            if i[0] != 0 and i[0]%6 == 0 or i[0] == len(CATEGORIES)-1:
                print i   # next line
            else:
                print i,  # same line
        print '--------------------------------------------------------------------------------------------------------'  
                    
        # prompt for category number
        while True: 
            code = raw_input(">>> Enter a category code: ")
            if code.isdigit() and int(code) >= 0 and int(code) < len(CATEGORIES):
                break
            else:
                print ">>> Oops!  That was no valid number.  Try again..." 
        
        # prompt for dollar amount spent
        while True:
            try:
                spent = float( raw_input('>>> Enter a dollar amount spent: ') )
                break
            except (ValueError, TypeError) as e:
                print ">>> Oops!  That was no valid number.", e
                   
        # remember spending        
        spendings[ int(code) ] += float(spent)
        
        # ask user if he/she wants to continue
        wantResult = raw_input('>>> Hit [ENTER] to continue, or type [R] for a result. ')
        if wantResult == 'r' or wantResult == 'R':
            
            # list of result (list of tuples)
            result = zip(CATEGORIES, spendings)
            
            # print result
            print
            print '**************************************' 
            print '[RESULT]', formatNow
            for (category, spending) in result:
                print '    {:<15} {:>10}'.format(category, spending)              
            print '**************************************'     
            print '    Total : {:>18} dollars'.format( sum(spendings) ) 
            
            # create data for csv (convert result to list of lists)
            data = []
            for (category, spending) in result:
                item = (category, spending)
                data.append( list(item) )
            data.extend(history)    # add editting history to data
            
            tempFileName = 'temp.csv'
            while True:
                # ask user if he/she wants to create a csvfile
                closure = raw_input('>>> Type [E] to exit, [S] to save, or [C] to create a csv file: ')
                
                if closure == 'S' or closure == 's':
                    try:  # call csvWriter
                        csvWriter(data, PATH + tempFileName)
                    except IOError:
                        print 
                        print ">>> Couldn't create a temp file. Please make sure the path is correct."
                        print ">>> Currently specified path: %s" % PATH
                        return
                    # successful
                    print
                    print ">>> Your data is successfully saved as \"" + tempFileName + "\" at", PATH
                    return
                
                elif closure == 'c' or closure == 'C':
                    # call csvWriter
                    try:
                        
                        fileName = 'spending_' + formatNow + '.csv'
                        csvWriter(data, PATH + fileName)
                        
                        # empty temp file
                        data = []
                        
                        csvWriter(data, PATH + tempFileName)
                        
                    except IOError:
                        print
                        print ">>> Couldn't create a csv file. Please make sure the path is correct."
                        print ">>> Currently specified path: %s" % PATH
                        return
                    # successful
                    print
                    print ">>> A csv file \"" + fileName + "\" has been created at", PATH
                    return
                # exit without creating a csv file
                elif closure == 'e' or closure == 'E':
                    return
                else:
                    print
                    print ">>> Invalid input."
        # continue    
        else:
            print


def csvWriter(data, PATH):
    '''Create a new csvfile and write data in it. 
        param1 data: list of lists
        param2 PATH: path of csv file
        return None
    '''
    with open(PATH, 'wb') as csvfile:
        
        # configure writer
        wr = csv.writer(csvfile, delimiter=';')
            
        # write a line for each row
        for line in data:
            wr.writerow(line)

def csvReader(readFile):
    '''Read temp csvfile, convert it to list of list
       param1 readFile  csvfile
       return aList
    '''
    with open(readFile, 'rb') as csvfile:
        
        aList = []
        # configure writer
        csvReader = csv.reader(csvfile, delimiter=';')
            
        # read each row as a string and store as list of strings
        for row in csvReader:
            aList.append(','.join(row))  # aList: list of strings
        
        # split each string into smaller strings
        index = 0
        for item in aList:
            aList[index] = item.split(',')
            index += 1
        print
        print aList    # aList: list of lists
    return aList

# call function   
receiptSorter(CATEGORIES)
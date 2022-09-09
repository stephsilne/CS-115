from cs115 import*
'''Name: Stephaan Silne'''
'''Pledge: I pledge my honor that I have abided by the Stevens Honor System.'''

DATA_FILE = 'musicrecplus.txt'

def loadUser(filename):
    '''Reads in a file of stored users' preferences stores in the file
'filename'. Returns a dictionary containing a mapping of users names to a list
preffered artists'''
    try:
        file = open(filename,'r')
        '''open the file given as a parameter to read'''
        userMap = {}
        '''initialize userMap as an empty dictionary that will take in the usernames and their list of artists as values'''
        for line in file:
            '''read and parse a single line'''
            [userName,bands] = line.strip().split(':')
            '''separate each line containing the username and list of artists through a colon and remove any leading or trailing whie spaces'''
            bandList = bands.split(',')
            '''split the list of artists by commas'''
            bandList.sort()
            '''sort the list of artists'''
            userMap[userName] = bandList
            '''append this data to userMap, where the users are the keys and the list of artists are the values'''
        file.close()
        '''close the file upon finishing computations'''
        return userMap
        '''return the dictionary made'''
    except (FileNotFoundError,ValueError):
        '''if there is no file that exists in the first place, leading to an error'''
        input_file = open(filename,'w')
        '''write into the file using the filename, thus creating a new file'''
        
def enterPreferences(userName,userMap):
    '''enters the preferences of the user by updating the dictionary userMap'''
    prefs = []
    '''initializes prefs as an empty list to be changed'''
    userMap[userName] = prefs
    '''updates the userMap of the given key (userName) so that the key value is the list of artist inputted'''
    newpref = input('Enter an artist that you like (Enter to finish): ')
    '''establishes newpref as an input that takes in the users preferences upon giving the prompt'''
    while newpref != '':
        '''while newpref isnt an empty string, keeps asking for user input'''
        prefs.append(newpref.strip().title())
        '''append the input given by newpref into prefs through every iteration until the user skips'''
        newpref = input ('Enter an artist that you like (Enter to finish): ')
        '''further prompts the user for their input'''
    prefs.sort()
    '''upon the breaking of the loop, sort prefs which is just a list of artists'''
    userMap[userName] = prefs
    '''update the dictionary value of the userName as the key, thus entering the preference so other calculations can ensue'''
    
def getRecommendations(userName,prefs,userMap):
    '''obtains recommendations for the userName by using their prefs and the userMap'''
    thebestUser = findBetterUser(userName,prefs,userMap)
    '''a list of users that BEST fit the given userName for recommendations to give'''
    recommendations = []
    '''intializes recommendations as an empty list'''
    recs = []
    '''initializes recs as an empty list'''
    if len(userMap) == 0 or len(thebestUser) == 0:
        '''if there is nothing in the dictionary or their isnt a single user that can give recommendations'''
        print('No recommendations available at this time.')
        '''print whats above'''
    else:
        for user in thebestUser:
            '''for every user in this list of user that can give recommendations'''
            recommendations += [drop(prefs,userMap[user])]
            '''append a list of lists of recommended artists that given the drop function that takes two list and returns what isnt in the other list'''
        recom = standardizeAll(recommendations)
        '''standardize all these recommendations'''
        for ele in recom:
            '''for each list of artists in recommendations'''
            ele.sort()
            '''sort the artists in these lists'''
            recs += ele
            '''append each list to recs so that a single list of recommended artists can be made'''
        newrecs = noDuplicates(recs)
        '''initializes newrecs which uses noDuplicates so that no duplicates are found in this list of recommendations'''
        newrecs.sort()
        '''sort this new list'''
        for ele in newrecs:
            '''for every artist in this list'''
            print(ele)
            '''print them out one by one'''

def findBestUser(userName,prefs,userMap):
    '''returns a list of list of users and their score of matches to userName'''
    bestUser = []
    '''initializes bestUser to an empty list'''
    users = []
    '''initializes user to be an empty list'''
    for user in userMap.keys():
        '''for each user in the userMap'''
        score = countMatches(prefs,userMap[user])
        '''initializes score to be the amount of matches between the the preferences of each user and the userName'''
        if userName != user and user[-1] != '$':
            '''as long as the user is not the userName given and the last element of the users name isnt a dollar sign(private)'''
            bestUser += [[user,score]]
            '''appends a list containing the user and the amount of matches they have with the userName'''
    for ele in bestUser:
        '''for every element in this list of lists of scores and users'''
        if len(userMap[ele[0]]) != ele[1]:
            '''if the amount of matches they have doesnt equal the amount of artists they had to begin with (meaning they CAN give any recommendations)'''
            users += [ele]
            '''append the list containing the user and their score to the list called users'''
        else:
            users += []
            '''if the numbers are the same, meaning they have the same artists as the userName, then add an empty list'''
    return users
    '''return this list of lists of users and their score'''

def findBetterUser(userName,prefs,userMap):
    '''returns a list of users with best recommendations'''
    bestscore = -1
    '''initialize bestscore as -1'''
    bestUser = findBestUser(userName,prefs,userMap)
    '''initializes the variable bestUser to be the list of lists of users and their score of matches to userName'''
    thebestUser = []
    '''initializes thebestUser to be an empty list for the following loops to manipulate'''
    for ele in bestUser:
        '''for every element in bestUser'''
        if ele[1] > bestscore:
            '''if the users score is greater than bestscore = -1'''
            bestscore = ele[1]
            '''changes bestscore to be the score of the user, so that bestscore is now the highest matchscore in all users'''
    for ele in bestUser:
        '''for each element in bestUsers'''
        if bestscore == 0:
            '''if bestscore came to be zero'''
            thebestUser += []
            '''append an empty list'''
        elif ele[1] == bestscore:
            '''if the users score matches the highest amount of matches'''
            thebestUser += [ele[0]]
            '''append that user to theBestUser to create a list of users that can give userName the best recommendations'''
    return thebestUser
    '''return this list of users'''
                    
def drop(list1,list2):
    '''returns a new list that contains only the elements in list2 that are not in list1'''
    list3 = []
    '''initialize list3 to be an empty list'''
    i = 0
    '''initializes i to 0'''
    j = 0
    '''initializes j to 0'''
    while i < len(list1) and j < len(list2):
        '''while i and j are less then the lengths of list1 and list 2'''
        if list1[i].title() == list2[j].title():
            '''if first elements of both lists equal each other'''
            i += 1
            '''increment i'''
            j += 1
            '''increment j, then check the rest of the elements'''
        elif list1[i].title() < list2[j].title():
            '''if the elements do not match''' 
            i += 1
            '''increment i'''
        else:
            list3.append(list2[j].title())
            '''otherwise append the rest of list 2 if there is anything left'''
            j += 1
            '''increment j'''
    while j < len(list2):
        '''whilej is less than the length of list2; otherwise break out of the loop'''
        list3.append(list2[j].title())
        '''add elements in list2 into list3'''
        j += 1
        '''keep incrementing j'''
    return list3
    '''return the final list'''

def countMatches(list1,list2):
    '''returns the number of elements that match between two sorted list'''
    matches = 0
    '''initializes matches to equal zero'''
    i = 0
    '''initialize i to be zero'''
    j = 0
    '''initialize j to be 0'''
    while i < len(list1) and j < len(list2):
        '''while i is less than the length of list1 and j is less than the length of list2'''
        if list1[i].title() == list2[j].title():
            '''if list1[i] equals list2[j]'''
            matches += 1
            '''increase the number of matches'''
            i += 1
            '''increment i to check other elements'''
            j += 1
            '''increment j to check other elements'''
        elif list1[i].title() < list2[j].title():
            '''otherwise is list2[j] is greater than list1[i]'''
            i += 1
            '''increment i to see other matches'''
        else:
            j += 1
            '''otherwise increment j to see other matches'''
    return matches
    '''return the value of matches'''

def standardizeAll(storedPrefs):
    '''takes in a list of lists and returns a list of lists'''
    standardStoredPrefs = []
    '''initializes standardStoredPrefs to be an empty list'''
    for i in range(len(storedPrefs)):
        '''for i in range of 0 to the length of storedPrefs'''
        standardStoredUser = []
        '''initialize standardStoredUser to be an empty list'''
        for j in range(len(storedPrefs[i])):
            '''for j in range of 0 to the length of storedPrefs[i]'''
            standardStoredUser.append(storedPrefs[i][j].strip().title())
            '''append storedPrefs upon getting rid of whitespace and leaving the preferences(artists) in title case into standardStoredUser'''
        standardStoredPrefs.append(standardStoredUser)
        '''append this list into the standrdStoredPrefs list'''
    return standardStoredPrefs
    '''returns the final list after every iteration is complete'''

def showMostPopularArtist(userMap):
    '''returns the most popular artist(s) using userMap'''
    try:
        most = -1
        '''initializes most to be -1 for comparisons'''
        artists = []
        '''initializes artists to be an empty list'''
        for ele in mostPophelper(userMap):
            '''for every list in list of artists and how many times they occur'''
            if ele[0] > most:
                '''if how many times they occur is greater than most'''
                most = ele[0]
                '''equate most to that value, thus after all iterations, most will be the highest number possible'''
        for ele in mostPophelper(userMap):
            '''for every element in the list of lists'''
            if ele[0] == most:
                ''' if the occurCount number of the artists equals the highest number possible'''
                artists += [ele[1]]
                '''append the artist into the empty list'''
        mostpopartist = noDuplicates(artists)
        '''mostpopartist is now the same list but without any duplicates'''
        mostpopartist.sort()
        '''sort this list'''
        for ele in mostpopartist:
            '''for each artist in this list'''
            print(ele)
            '''print the artist(s)'''
    except:
        print('Sorry, no artists found.')

def howPopisMostArtist(userMap):
    '''using userMap, returns the most popular artist'''
    try:
        popnumber = -1
        '''initializes popnumber to be -1 for comparisons'''
        for ele in mostPophelper(userMap):
            '''for every element in list of artists'''
            if ele[0] > popnumber:
                '''if how many times they occur is greater than popnumber'''
                popnumber = ele[0]
                '''equate popnumber to be the number given, thus making popnumber to be the HIGHEST occurrence after all iterations'''
        print(popnumber)
        '''print the highest number'''
    except:
        print('Sorry, no artists found.')

def whichUser(userMap):
    '''returns the user that likes the most artists using userMap'''
    users = []
    '''initializes users to be an empty list'''
    num = -1
    '''initializes num to be -1 for comparisons'''
    theuser = []
    '''initializes theuser to be an empty list'''
    try:
        for user in userMap.keys():
            '''for each user in the keys of userMap'''
            if user[-1] != '$':
                '''as long as the user isnt in private mode'''
                users += [[len(userMap[user]),user]]
                '''append a list to the list 'users' containing the length of the list of their preferences and the user'''
        for ele in users:
            '''upon each iteration, for each list in the list'''
            if ele[0] > num:
                '''if length of their preferences is greater than num'''
                num = ele[0]
                '''equate num to be the given length of preferences; after completion, the highest number of artists will be num'''
        for ele in users:
            '''for each element in users'''
            if ele[0] == num:
                '''if the users amount of preferences equals the highest number'''
                theuser += [ele[1]]
                '''append the users name to the list (theusers)'''
        for ele in theuser:
            '''for each user in this list'''
            print(ele)
            '''output each user if more than one, or just the one user'''
    except:
        print('Sorry, no user found')
        '''if there is an error in finding the user, then prints whats above'''

def mostPophelper(userMap):
    '''returns a list of lists of artists and how many times they occur in the giant bank of artists (their popularity)'''
    aList = listofArtists(userMap)
    '''the variable 'alist' is now the giant bank of artists using listofArtists function'''
    values = []
    '''initializes values to be an empty list'''
    for artist in aList:
        '''for every artist in the giant bank'''
        values += [[occurCount(aList,artist),artist]]
        '''append a list of how many times it occurred (using occurCount), and the artist in question'''
    return values
    '''returns the list of lists'''

def noDuplicates(lst):
    '''takes in a list and returns a new list without any duplicates in the list'''
    nodupes = []
    '''initializes nodupes to be an empty list'''
    for i in lst:
        '''for every element in the list given'''
        if i not in nodupes:
            '''if the element is not already in the list we created'''
            nodupes += [i]
            '''append it to nodupes'''
    return nodupes
    '''returns the new list without any duplicates'''
                           
def occurCount(lst,var):
    '''takes in a list and a given variable, to return the amount of times that variable occurred in the lst'''
    count = 0
    '''initializes count to be zero'''
    for ele in lst:
        '''for every element in the list'''
        if (ele == var):
            '''if the element equals the variable in question'''
            count += 1
            '''increase the count by 1'''
    return count
    '''returns the count(amount of times in list'''

def listofArtists(userMap):
    '''returns a giant bank of all user preferences, that are not in private mode'''
    lstr = []
    '''initializes lstr to be an empty list'''
    newlstr = []
    '''intializes newlstr to be an empty list'''
    for user in userMap.keys():
        '''for every user in the keys of userMap'''
        if user[-1] != '$':
            '''as long as the last element of the users name isnt a $, (meaning not in private mode)'''
            lstr += [userMap[user]]
            '''append the users preferences to lstr, creating a list of list of artists'''
        else:
            None
            '''otherwise if in private mode dont do anything as they should be excluded from calculations'''
        lst = standardizeAll(lstr)
        '''lst should be lstr bt standardized'''
    for ele in lst:
        '''for every element in lst'''
        newlstr += ele
        '''append each element to newlstr so that a giant list of just artists names are made'''
    return newlstr
    '''return this giant list'''
                             
def saveUserPreferences(userName, prefs, userMap, DATA_FILE):
    '''writes all of the users preferences to the file. Returns nothing.'''
    userMap[userName] = prefs
    '''establishes that userName is a key to which prefs are its value in the userMap dictionary'''
    file = open(DATA_FILE, 'w')
    '''write into the file upon opening'''
    for user in userMap:
        '''for each element in the userMap'''
        toSave = str(user) + ':' + ','.join(userMap[user]) + '\n'
        '''add the user as a string, followed by a colon, following by the preferences followed by '\n' to the variable toSave'''
        file.write(toSave)
        '''write this variable into the file for each user'''
    file.close()
    '''close the file once every iteration is complete'''

def main():
    userMap = loadUser(DATA_FILE)
    '''establishes userMap to be dictionary created by loadUser upon reading into the DATA_FILE'''
    userName = input('Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ')
    '''establishes userName which takes in the input of the user so that they may enter their name for operations'''
    if userName in userMap.keys():
        '''if the userName is already in the set of userMap keys, the menu should be prompted immediately'''
        while True:
            print("""
            Enter a letter to choose an option:
            e - Enter preferences
            r - Get recommendations
            p - Show most popular artists
            h - How popular is the most popular
            m - Which user has the most likes
            q - Save and quit
            """)
            selection = input()
            '''sets selection to be the input given by the user for certain options in the menu'''
            if selection == "e":
                '''if the user selects e'''
                enterPreferences(userName,userMap)
                '''call enterPreferences'''
            if selection == "r":
                '''if the user selects r'''
                getRecommendations(userName,userMap[userName],userMap)
                '''call getRecommendations'''
            if selection == "p":
                '''if the user selects p'''
                showMostPopularArtist(userMap)
                '''calls showMostPopularArtist'''
            if selection == "h":
                '''if the user selects h'''
                howPopisMostArtist(userMap)
                '''call howPopisMostArtist'''
            if selection == "m":
                '''if the user selects m'''
                whichUser(userMap)
                '''call whichUser'''
            if selection == "q":
                '''if the user selects q'''
                saveUserPreferences(userName, userMap[userName], userMap, DATA_FILE)
                '''call saveUserPreferences'''
                break
                '''breaks after function call to quit'''
    else:
        enterPreferences(userName,userMap)
        '''otherwise if the userName is not in the userMap'''
        while True:
            print("""
            Enter a letter to choose an option:
            e - Enter preferences
            r - Get recommendations
            p - Show most popular artists
            h - How popular is the most popular
            m - Which user has the most likes
            q - Save and quit
            """)
            selection = input()
            '''sets selection to be the user input according to the different selections given by the menu'''
            if selection == "e":
                '''if the user selects e'''
                enterPreferences(userName,userMap)
                '''call enterPreferences'''
            if selection == "r":
                '''if the user selects r'''
                getRecommendations(userName,userMap[userName],userMap)
                '''call getRecommendations'''
            if selection == "p":
                '''if the user selects p'''
                showMostPopularArtist(userMap)
                '''calls showMostPopularArtist'''
            if selection == "h":
                '''if the user selects h'''
                howPopisMostArtist(userMap)
                '''calls howPopisMostArtist'''
            if selection == "m":
                '''if the user selects m'''
                whichUser(userMap)
                '''calls whichUser'''
            if selection == "q":
                '''if the user selects q'''
                saveUserPreferences(userName, userMap[userName], userMap, DATA_FILE)
                '''call saveUserPreferences'''
                break
                '''break out of loop to quit after saving'''
if __name__== '__main__':main()


    

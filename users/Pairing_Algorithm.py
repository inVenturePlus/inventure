entrepreneur = get_object_or_404(Entrepreneur, pk=e)
ventureCapital = get_object_or_404(VentureCapital, pk=vc)

# VC Field Names:
# company_name
# company_city
# company_state
# company_fund_size
# stages_interested
# sectors_avoid
# locations_interested
# locations_avoid
# sectors_interested
# company_mission
# check_size
# previous_investments

# Entrepreneur Field Names:
# company_name
# company_state
# current_stage
# company_city
# company_state
# company_mission
# sector
# locations_interested
# check_size
# other 

# 1) Name- magnitude of 1

# Make code more efficient for actual implementation
# i.e. add check for commonWords before appending to words array
# also, make sure to change input to all lowercase

separators = []
separators[0] = " "
separators[1] = "-"
separators[2] = ","

commonWords = []
commonWords[0] = "the"
commonWords[1] = "a"
commonWords[2] = "and"
commonWords[3] = "&"

# Add proper code to import names
# entrepreneurName
entrepreneur.company_name = ""
# vcName 
ventureCapital.company_name = ""
nameScore = 0

words = []
if len(entrepreneur.company_name) > len(ventureCapital.company_name):
    wordLength = 0
    wordStart = 0
    for letter in range(len(entrepreneur.company_name)):
        if not (entrepreneur.company_name[letter] in separators):
            wordLength = wordLength + 1
        else: 
            words.append(entrepreneur.company_name[wordStart:wordStart + wordLength])
            wordStart = letter
            wordLength = 0
    wordLength = 0
    wordStart = 0
    for letter in range(len(ventureCapital.company_name)):
        if not (ventureCapital.company_name[letter] in separators):
            wordLength = wordLength + 1
        else: 
            if (ventureCapital.company_name[wordStart:wordStart + wordLength] in words
                and ventureCapital.company_name[wordStart:wordStart + wordLength] not in commonWords):
                nameScore = nameScore + 1
            wordStart = letter
            wordLength = 0
    
else: 
    wordLength = 0
    wordStart = 0
    for letter in range(len(ventureCapital.company_name)):
        if not (ventureCapital.company_name[letter] in separators):
            wordLength = wordLength + 1
        else: 
            words.append(ventureCapital.company_name[wordStart:wordStart + wordLength])
            wordStart = letter
            wordLength = 0
    wordLength = 0
    wordStart = 0
    for letter in range(len(entrepreneur.company_name)):
        if not (entrepreneur.company_name[letter] in separators):
            wordLength = wordLength + 1
        else: 
            if (entrepreneur.company_name[wordStart:wordStart + wordLength] in words
               and entrepreneur.company_name[wordStart:wordStart + wordLength] not in commonWords):
                nameScore = nameScore + 1
            wordStart = letter
            wordLength = 0       
            

# 2) City- magnitude of 3

# Add proper code to import city names
# entrepreneurCity
entrepreneur.company_city = ""
# vcCity 
ventureCapital.company_city = ""
cityScore = 0

if (entrepreneur.company_city == ventureCapital.company_city):
    cityScore = cityScore + 1


# 3) State- magnitude of 2

# Add proper code to import state numbers
# entrepreneurStateNumber
entrepreneur.company_state = 0
# vcStateNumber
ventureCapital.company_state = 0
stateScore = 0

if (entrepreneur.company_state == ventureCapital.company_state):
    stateScore = stateScore + 1
    

# 4) Mission- magnitude of 3

# See if there is a better way to design this system than delimiting each and 
# every case one at a time

# Add proper code to import mission statements

# entrepreneurMission
entrepreneur.company_mission = ""
# vcMission 
ventureCapital.company_mission = ""

entrepreneurMissionWords = []
vcMissionWords = []

breaks = []
breaks[0] = "."
breaks[1] = ","
breaks[2] = " "
breaks[3] = "-"
breaks[4] = ";"
breaks[5] = "_"
breaks[6] = "!"
breaks[7] = "?"
breaks[8] = "\'"
breaks[9] = "\""
breaks[10] = "\\"
breaks[11] = "/"
breaks[12] = "["
breaks[13] = "]"
breaks[14] = "("
breaks[15] = ")"
breaks[16] = "#"
breaks[17] = "%"
breaks[18] = "@"
breaks[19] = "*"
breaks[20] = "~"
breaks[21] = "+"
breaks[22] = "-"
breaks[23] = "="
breaks[24] = "$"

regWords = []
regWords[0] = "the"
regWords[1] = "a"
regWords[2] = "and"
regWords[3] = "&"
regWords[4] = "so"
regWords[5] = "like"
regWords[6] = "also"
regWords[7] = "additionally"
regWords[8] = "in"
regWords[9] = "it"
regWords[10] = "is"
regWords[11] = "on"
regWords[12] = "we"
regWords[13] = "want"
regWords[14] = "to"
regWords[15] = "too"
regWords[16] = "for"
regWords[17] = "from"
regWords[18] = "that"
regWords[19] = "then"
regWords[20] = "than"
regWords[21] = "when"
regWords[22] = "who"
regWords[23] = "what"
regWords[24] = "where"
regWords[25] = "were"
regWords[26] = "are"
regWords[27] = "will"
regWords[28] = "how"
regWords[29] = "why"
regWords[30] = "s"
regWords[31] = "t"
regWords[32] = "have"
regWords[33] = "should"
regWords[34] = "could"
regWords[35] = "can"
regWords[36] = "do"
regWords[37] = "something"
regWords[38] = "thing"
regWords[39] = "things"

missionScore = 0

wordLength = 0
wordStart = 0
# make sure if statements actually prevent over-counting duplicate words

for letter in range(len(entrepreneur.company_mission)):
    if not (entrepreneur.company_mission[letter] in breaks):
            wordLength = wordLength + 1
    else: 
            if (entrepreneur.company_mission[wordStart:wordStart + wordLength] not in regWords
                and entrepreneur.company_mission[wordStart:wordStart + wordLength] not in entrepreneurMissionWords):
                entrepreneurMissionWords.append(entrepreneur.company_mission[wordStart:wordStart + wordLength])
            wordStart = letter
            wordLength = 0
            
wordLength = 0
wordStart = 0
for letter in range(len(ventureCapital.company_mission)):
    if not (ventureCapital.company_mission[letter] in breaks):
            wordLength = wordLength + 1
    else: 
            if (ventureCapital.company_mission[wordStart:wordStart + wordLength] not in regWords 
            and ventureCapital.company_mission[wordStart:wordStart + wordLength] not in vcMissionWords):
                vcMissionWords.append(ventureCapital.company_mission[wordStart:wordStart + wordLength])
            wordStart = letter
            wordLength = 0

for word1 in entrepreneurMissionWords:
    for word2 in entrepreneurMissionWords:
        if (word1 == word2):
            missionScore = missionScore + 1
            
# 5) Stages Interested- magnitude of 2

# Find way to import data so status either matches value for "interested" or "not interested" or "neutral"
# entrepreneurPreSeedStatus = 0
# entrepreneurSeedStatus = 0
# entrepreneurSeriesAStatus = 0
# entrepreneurSeriesBStatus = 0
# entrepreneurSeriesCStatus = 0

entrepreneur.company_stage = 0

# vcPreSeedStatus = 0
# vcSeedStatus = 0
# vcSeriesAStatus = 0
# vcSeriesBStatus = 0
# vcSeriesCStatus = 0

ventureCapital.stages_interested = ""

stageScore = 0

# Figure out how this data is going to be imported from the form to change the algorithm

if (entrepreneurPreSeedStatus == vcPreSeedStatus):
    stageScore = stageScore + 1
elif (entrepreneurPreSeedStatus == -1 * vcPreSeedStatus):
    stageScore = stageScore - 1 

if (entrepreneurSeedStatus == vcSeedStatus):
    stageScore = stageScore + 1
elif (entrepreneurSeedStatus == -1 * vcSeedStatus):
    stageScore = stageScore - 1
    
if (entrepreneurSeriesAStatus == vcSeriesAStatus):
    stageScore = stageScore + 1
elif (entrepreneurSeriesAStatus == -1 * vcSeriesAStatus):
    stageScore = stageScore - 1
    
if (entrepreneurSeriesBStatus == vcSeriesBStatus):
    stageScore = stageScore + 1
elif (entrepreneurSeriesBStatus == -1 * vcSeriesBStatus):
    stageScore = stageScore - 1
    
if (entrepreneurSeriesCStatus == vcSeriesCStatus):
    stageScore = stageScore + 1
elif (entrepreneurSeriesCStatus == -1 * vcSeriesCStatus):
    stageScore = stageScore - 1

# 6) Locations Interested- magnitude of 3

# Not sure if this dictionary will be needed for anything
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

locationScore = 0

# entrepreneurState
entrepreneur.state = ""

ventureCapital.locations_interested = ""
ventureCapital.locations_avoid = ""

# ^^^Figure out how these arrays are going to be imported from the form to change the algorithm

# statesInterested = []
# statesNotInterested = []
# statesNeutral = []

# iterate through the 50 radio button selections
# differentiate between states "interested" and "not interested" to determine how to adjust
# come up with a more efficient way to do this

for state in range(len(statesInterested)):
    if statesInterested[state] == entrepreneurState:
        locationScore = locationScore + 1

for state in range(len(statesNotInterested)):
    if statesNotInterested[state] == entrepreneurState:
        locationScore = locationScore - 1

# 7) Check Size- magnitude of 4
# add method to import appropriate data from entrepreneur form
checkScore = 0
# entrepreneurCheckSize 
entrepreneur.check_size = 0

# checkSize1 = 0
# checkSize2 = 0
# checkSize3 = 0
# checkSize4 = 0
# checkSize5 = 0
# checkSize6 = 0
# checkSize7 = 0

ventureCapital.check_size = 0

# ^^^Figure out how this data is going to be imported from the form to change algorithm

if entrepreneurCheckSize == 1:
    checkScore = checkScore + checkSize1
elif entrepreneurCheckSize == 2:
    checkScore = checkScore + checkSize2
elif entrepreneurCheckSize == 3:
    checkScore = checkScore + checkSize3
elif entrepreneurCheckSize == 4:
    checkScore = checkScore + checkSize4
elif entrepreneurCheckSize == 5:
    checkScore = checkScore + checkSize5
elif entrepreneurCheckSize == 6:
    checkScore = checkScore + checkSize6
elif entrepreneurCheckSize == 7:
    checkScore = checkScore + checkSize7

# 8) Sectors Interested- magnitude of 4

# entrepreneurSector
entrepreneur.sector = ""
sectorScore = 0

ventureCapital.sectors_interested = ""
ventureCapital.sectors_avoid = ""

# Import dictionary of sectors with their associated scores
sectors = {}

for sector in range(len(sectors)):
    if sectors.keys()[sector] == entrepreneurSector:
        sectorScore = sectorScore + sectors.values()[sector]

# We should double check all my Python code lol
# Implement data weighting algorithm here to accurately reflect the importance of each category

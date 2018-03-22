from django.shortcuts import (get_object_or_404, get_list_or_404, render, render_to_response)
from users.forms import *
from users.models import *

def pairing(request, entrepreneur_id, venturecapitalist_id):
    entrepreneur = get_object_or_404(Entrepreneur, pk=entrepreneur_id)
    ventureCapital = get_object_or_404(VentureCapital, pk=venturecapitalist_id)

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

    separators = [" ", "-", ","]

    commonWords = ["the", "a", "and", "&"]

    nameScore = 0
    entrepreneurNameSpaces = 0
    vcNameSpaces = 0

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


    for entry in range(len(entrepreneur.company_name)):
        if (entrepreneur.company_name[entry] in separators):
            entrepreneurNameSpaces = entrepreneurNameSpaces + 1

    for entry in range(len(ventureCapital.company_name)):
        if (ventureCapital.company_name[entry] in separators):
            vcNameSpaces = vcNameSpaces + 1

    avgWordLength = min(len(entrepreneur.company_name), len(ventureCapital.company_name)) / min(entrepreneurNameSpaces, vcNameSpaces)
    nameScoreNormalized = nameScore / avgWordLength

    # 2) City- magnitude of 3

    cityScore = 0

    if (entrepreneur.company_city == ventureCapital.company_city):
        cityScore = cityScore + 1

    # 3) State- magnitude of 2

    stateScore = 0

    if (entrepreneur.company_state == ventureCapital.company_state):
        stateScore = stateScore + 1


    # 4) Mission- magnitude of 3

    # See if there is a better way to design this system than delimiting each and
    # every case one at a time

    entrepreneurMissionWords = []
    vcMissionWords = []

    breaks = [".", ",", " ", "-", ";", "_", "!", "?", "\'", "\"", "\\", "/", "[", "]", "(", ")", "#", "%", "@", "*", "~", "+", "-", "=", "$"]

    regWords = ["the", "a", "and", "&", "so", "like", "also", "additionally", "in", "it", "is", "on", "we", "want", "to", "too", "for", "from", "that", "then", "than", "when", "who", "what", "where", "were", "are", "will", "how", "why", "s", "t", "have", "should", "could", "can", "do", "something", "thing", "things"]

    missionScore = 0

    wordLength = 0
    wordStart = 0
    entrepreneurMissionSpaces = 0
    vcMissionSpaces = 0
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


    for entry in range(len(entrepreneur.company_mission)):
        if (entrepreneur.company_mission[entry] in breaks):
            entrepreneurMissionSpaces = entrepreneurMissionSpaces + 1

    for entry in range(len(ventureCapital.company_mission)):
        if (ventureCapital.company_mission[entry] in breaks):
            vcMissionSpaces = vcMissionSpaces + 1

    meanWordLength = min(len(entrepreneur.company_mission), len(ventureCapital.company_mission)) / min(entrepreneurMissionSpaces, vcMissionSpaces)
    missionScoreNormalized = missionScore / meanWordLength

    # 5) Stages Interested- magnitude of 2

    stageScore = 0

    if (entrepreneur.current_stage in ventureCapital.stages_interested):
        stageScore = stageScore + 4
    elif (entrepreneur.current_stage + 1 in ventureCapital.stages_interested):
        stageScore = stageScore + 1
    elif (entrepreneur.current_stage - 1 in ventureCapital.stages_interested):
        stageScore = stageScore + 1

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

    # statesInterested = []
    # statesNotInterested = []
    # statesNeutral = []

    # iterate through the 50 radio button selections
    # differentiate between states "interested" and "not interested" to determine how to adjust
    # come up with a more efficient way to do this

    for state in range(len(ventureCapital.locations_interested)):
        if ventureCapital.locations_interested[state] == entrepreneur.company_state:
            locationScore = locationScore + 1

    for state in range(len(ventureCapital.locations_avoid)):
        if VentureCapital.locations_avoid[state] == entrepreneur.company_state:
            locationScore = locationScore - 1

    # 7) Check Size- magnitude of 4
    # add method to import appropriate data from entrepreneur form
    checkScore = 0


    if (entrepreneur.check__size == ventureCapital.check_size):
        checkScore = checkScore + 4
    elif (entrepreneur.check__size + 1 == ventureCapital.check_size):
        checkScore = checkScore + 1
    elif (entrepreneur.check__size - 1 == ventureCapital.check_size):
        checkScore = checkScore + 1

    # 8) Sectors Interested- magnitude of 4

    # entrepreneurSector
    entrepreneur.sector = ""
    sectorScore = 0

    ventureCapital.sectors_interested = ""
    ventureCapital.sectors_avoid = ""

    # Import dictionary of sectors with their associated scores
    for sector in range(len(ventureCapital.sectors_interested)):
        if ventureCapital.locations_sectors_interested[sector] == entrepreneur.sector:
            sectorScore = sectorScore + 1

    for sector in range(len(ventureCapital.sectors_avoid)):
        if VentureCapital.sectors_avoid[sector] == entrepreneur.sector:
            sectorScore = sectorScore - 1

    # TotalScore
    TotalScore = nameScoreNormalized + (3.0 * cityScore) + (2.0 * stateScore) + (3.0 * missionScoreNormalized) + (2.5 * (stageScore / 6.0)) + (3.0 * locationScore) + (4.5 * (checkScore / 6.0)) + (4.0 * sectorScore)

    # We should double check all my Python code lol
    # Implement data weighting algorithm here to accurately reflect the importance of each category

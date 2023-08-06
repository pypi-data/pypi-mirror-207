import random
from time import sleep


def DiscussionPost(self, access_token, comment, environment):
    """This function will post a new discussion for the user. Pass the comment i.e., message to be
    posted to the discussion, access_token, and environment (1 for Prod, 2 for Dev2, 3 for Beta, 4 for Dev1)"""

    if environment == 1:
        envURL = "https://unstop.com"
    elif environment == 2:
        envURL = "https://dev2.dare2compete.com"
    elif environment == 3:
        envURL = "https://beta.dare2compete.com"
    elif environment == 4:
        envURL = "http://dev1.d2c.pw/"
    else:
        envURL = "https://unstop.com"

    # posting a discussions
    # sleep(random.randint(5, 10))
    for i in range(0, 10):
        disRes = self.client.post(url=envURL + '/api/competition/50340/discussions',
                                  name='12.submit discussion ~ time=' + str(i), timeout=120,
                                  allow_redirects=False, headers={'Accept': 'application/json, text/plain, */*',
                                                                  'Authorization': 'Bearer ' + access_token},
                                  json={'newDiscussion': {'title': comment}, 'page': 1, 'perPage': 6})
        # print(response.text)
        if "data" in disRes.text:
            sleep(random.randint(10, 20))
            break
        elif i == 9:
            print("Test Failed permanently at discussions" + ' time-' + str(i), disRes.text)
            return "Failed"
        else:
            print("Test Failed at discussions" + ' time-' + str(i), disRes.text)
            sleep(5)


def OpportunityReview(self, access_token, review, environment):
    """This function will post a new opportunity review for the user. Pass the review message i.e., message to be
        posted to the review, access_token, and environment (1 for Prod, 2 for Dev2, 3 for Beta, 4 for Dev1)"""

    if environment == 1:
        envURL = "https://unstop.com"
    elif environment == 2:
        envURL = "https://dev2.dare2compete.com"
    elif environment == 3:
        envURL = "https://beta.dare2compete.com"
    elif environment == 4:
        envURL = "http://dev1.d2c.pw/"
    else:
        envURL = "https://unstop.com"

    rating = random.randint(1, 6)

    for i in range(0, 10):
        revRes = self.client.post(url=envURL + '/api/competition/50340/reviews',
                                  name='submit reviews', timeout=120,
                                  allow_redirects=False, headers={'Accept': 'application/json, text/plain, */*',
                                                                  'Authorization': 'Bearer ' + access_token},
                                  json={'rating': rating, 'title': '', 'feedback': review,
                                        'user': None})
        # print(response.text)
        if "data" in revRes.text:
            sleep(random.randint(10, 20))
            break
        elif i == 9:
            print("Test Failed permanently at opp review" + ' time-' + str(i), "\n", revRes.text)
            sleep(99999999999999999)
        else:
            print("Test Failed at review" + ' time-' + str(i), revRes.text)
            sleep(3)


def RegisterationNormal(self, access_token, environment, mobile, userEmail, compIds, returnValue):
    """This function will perform normal individual registration for the user. Pass the access_token, environment
    (1 for Prod, 2 for Dev2, 3 for Beta, 4 for Dev1), mobile, userEmail, compIds in "ARRAY", returnValue
    ("1" for getting compete data, 0 for no data)!"""

    if environment == 1:
        envURL = "https://unstop.com"
    elif environment == 2:
        envURL = "https://dev2.dare2compete.com"
    elif environment == 3:
        envURL = "https://beta.dare2compete.com"
    elif environment == 4:
        envURL = "http://dev1.d2c.pw/"
    else:
        envURL = "https://unstop.com"

    alphaChoice = ["A", "B", "C", "D", "E", "F", "G", "H"]
    name = "DumPlay" + random.choice(alphaChoice) + str(random.randint(10000, 999999))

    null = ""
    true = True
    false = False

    for i in range(0, 10):
        regResponse = self.client.post(url=envURL + '/api/competition/registration',
                                       name='registration',
                                       timeout=120,
                                       allow_redirects=False, headers={'authorization': 'Bearer ' + access_token,
                                                                       'Accept': 'application/json, text/plain, '
                                                                                 '*/*'},
                                       json={"team": {"name": name, "subscription": 0,
                                                      "players": [{"id": 0, "name": "dummy",
                                                                   "mobile": mobile,
                                                                   "email": userEmail,
                                                                   "organisationName": "S.C.B. Medical College, Cuttack",
                                                                   "others": null,
                                                                   "others_gender": null,
                                                                   "others_course_specialization": "",
                                                                   "organisation": {"id": 145665,
                                                                                    "name": "S.C.B. Medical College, "
                                                                                            "Cuttack",
                                                                                    "logo": null, "logoUrl": "",
                                                                                    "logoUrl2": "",
                                                                                    "public_url": "c/scb-medical"
                                                                                                  "-college-cuttack"
                                                                                                  "-placement-"
                                                                                                  "interview-"
                                                                                                  "competitions"
                                                                                                  "-articles- "
                                                                                                  "videos-145665"}
                                                                      , "player_type": 1, "gender": "M",
                                                                   "location": "India", "differently_abled": 0,
                                                                   "errors": {"nameErrorStatus": false,
                                                                              "nameErrorMsg": "",
                                                                              "emailErrorStatus": false,
                                                                              "emailErrorMsg": "",
                                                                              "mobileErrorStatus": false,
                                                                              "mobileErrorMsg": "",
                                                                              "locationErrorStatus": false,
                                                                              "locationErrorMsg": "",
                                                                              "organisationNameErrorStatus": false,
                                                                              "organisationNameErrorMsg": "",
                                                                              "user_typeErrorStatus": false,
                                                                              "user_typeErrorMsg": "",
                                                                              "study_yearErrorStatus": false,
                                                                              "course_programmeErrorMsg": "",
                                                                              "course_durationErrorMsg": "",
                                                                              "study_yearErrorMsg": "",
                                                                              "course_programmeErrorStatus": false,
                                                                              "course_durationErrorStatus": false,
                                                                              "passing_out_yearErrorStatus": false,
                                                                              "passing_out_yearErrorMsg": "",
                                                                              "work_experienceErrorStatus": false,
                                                                              "work_experienceErrorMsg": "",
                                                                              "course_pursuingErrorStatus": false,
                                                                              "course_pursuingErrorMsg": "",
                                                                              "course_streamErrorStatus": false,
                                                                              "course_streamErrorMsg": "",
                                                                              "course_specializationErrorStatus": false,
                                                                              "course_specializationErrorMsg": "",
                                                                              "differently_abledErrorStatus": false,
                                                                              "differently_abledErrorMsg": "",
                                                                              "genderErrorStatus": false,
                                                                              "school_yearErrorStatus": false},
                                                                   "formValidStatus": true, "formValidMsg": "",
                                                                   "noGender": true, "user_type": 5,
                                                                   "course_pursuing": null, "course_stream": null,
                                                                   "course_specialization": null,
                                                                   "study_year": null, "passing_out_year": 2022,
                                                                   "course_programme": null,
                                                                   "course_duration": null, "work_experience": null}],
                                                      "formValidStatus": true, "formValidMsg": ""}
                                           , "competitionIds": compIds, "method": "new-team", "subscription": 0,
                                             "invitedPlayers": [], "invites_allowed": 0})
        # print(regResponse.text)
        regRes = regResponse.json()["data"]
        if "status" in regResponse.text:
            if returnValue == 1:
                return regRes
            else:
                return True
        elif i == 9:
            print("Test Failed permanently at registration" + ' time-' + str(i), regRes.text)
            return "Failed"
        else:
            print("Test Failed at registration" + ' time-' + str(i), regRes.text)
            sleep(5)


def RandomTeamName():
    """This will generate a random team name for the given team"""

    alphaChoice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "Q", "R", "S",
                   "T", "U", "V", "W", "X", "Y", "Z"]
    teamname = "Team" + random.choice(alphaChoice) + random.choice(alphaChoice) + str(random.randint(1, 9999))
    return teamname


def RandomPlayerName():
    """This will generate a random player name for the given team"""
    alphaChoice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "Q", "R", "S",
                   "T", "U", "V", "W", "X", "Y", "Z"]
    playername = "Player" + random.choice(alphaChoice) + random.choice(alphaChoice) + str(random.randint(1, 9999))
    return playername


def RandomMobile():
    """This will generate a random mobile number"""
    ext = random.randint(10000000, 99999999)
    mobile = "+9199" + str(ext)
    return mobile


def RandomGender():
    """This will generate a random gender from the available list"""
    GenderList = ['M', 'F', 'I', 'O', 'NB', 'T']
    Gender = random.choice(GenderList)
    return Gender



def RandomOrganization():
    """This will generate a random organization for the player"""
    OrganizationList = [
        {"id": 483, "name": "Guru Gobind Singh Indraprastha University (GGSIPU), Delhi"},
        {"id": 591, "name": "Indian Institute of Management (IIM), Ranchi"},
        {"id": 597, "name": "Indian Institute of Management (IIM), Udaipur"},
        {"id": 122804, "name": "Global Institutes of Management (GIM), Amritsar"},
        {"id": 614, "name": "Indian Institute of Technology (IIT), Indore"},
        {"id": 122804, "name": "Global Institutes of Management (GIM), Amritsar"},
        {"id": 604, "name": "Indian Institute of Technology (IIT), Bombay"},
        {"id": 608, "name": "Indian Institute of Technology (IIT),  Roorkee"},
        {"id": 597, "name": "Indian Institute of Management (IIM), Udaipur"},
        {"id": 122804, "name": "Global Institutes of Management (GIM), Amritsar"}]

    organization = random.choice(OrganizationList)
    return organization


def ExploreFlow(self, environment, compIds):
    """This will be user's explore flow. Pass the access_token, environment
        (1 for Prod, 2 for Dev2, 3 for Beta, 4 for Dev1), compId!"""

    if environment == 1:
        envURL = "https://unstop.com"
    elif environment == 2:
        envURL = "https://dev2.dare2compete.com"
    elif environment == 3:
        envURL = "https://beta.dare2compete.com"
    elif environment == 4:
        envURL = "http://dev1.d2c.pw/"
    else:
        envURL = "https://unstop.com"

    # competitions api
    for z in range(0, 5):
        compRes = self.client.get(url=envURL + '/api/public/competition/' + str(compIds[0]),
                                  name='competition/' + str(compIds[0]), timeout=120,
                                  allow_redirects=False,
                                  headers={'Accept': 'application/json, text/plain, */*'})
        if "data" in compRes.text:
            break
        elif z == 4:
            print("Test Failed permanently at competition" + " time=" + str(z))
            print(compRes.text)
            sleep(99999999999999999)
        else:
            print("comp failed" + " time=" + str(z), compRes.text)
            sleep(2)
    else:
        sleep(10)

    # explore filters
    for z in range(0, 5):
        expRes = self.client.get(
            url=envURL + '/api/public/opportunity/search-result?opportunity=competitions&page=1&per_page=15&filters='
                         ',,,,&types=teamsize,payment,oppstatus,eligible,category',
            name='Explore-all-open',
            timeout=90, allow_redirects=False,
            headers={'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
                     'Accept': 'application/json, text/plain, */*',
                     'sec-ch-ua-mobile': '?0',
                     'sec-ch-ua-platform': '"macOS"'})
        if "data" in expRes.text:
            sleep(5)
            break
        elif z == 4:
            print("Test Failed permanently at explore" + " time=" + str(z))
            print(expRes.text)
            sleep(99999999999999999)
        else:
            print("explore failed" + " time=" + str(z), compRes.text)
            sleep(2)
    else:
        sleep(5)

    # hack for explore
    for z in range(0, 5):
        postRes = self.client.get(
            url=envURL + '/api/public/opportunity/search-result?opportunity=competitions&page=1&per_page=15&filters='
                         ',,,,&types=teamsize,payment,oppstatus,eligible,category',
            name='Explore-hackathons',
            timeout=120, allow_redirects=False,
            headers={'Accept': 'application/json, text/plain, */*'})
        if "data" in postRes.text:
            sleep(5)
            break
        if z == 4:
            print("Test Failed permanently at posts" + " time=" + str(z))
            print(postRes.text)
            sleep(99999999999999999)
        else:
            print("posts failed" + " time=" + str(z), compRes.text)
            sleep(2)
    else:
        sleep(5)

    # internships in explore
    for z in range(0, 5):
        intRes = self.client.get(
            url=envURL + '/api/public/opportunity/search-result?opportunity=internships&page=1&per_page=15&filters='
                         ',,,,,,&types=oppstatus,job_type,job_timing,paid_unpaid,working_days,eligible,category',
            name='opportunity=internships',
            timeout=90, allow_redirects=False,
            headers={'Accept': 'application/json, text/plain, */*'})
        if "data" in intRes.text:
            sleep(5)
            break
        if z == 4:
            print("Test Failed permanently at internships" + " time=" + str(z))
            print(intRes.text)
            sleep(99999999999999999)
        else:
            print("internships failed" + " time=" + str(z), intRes.text)
            sleep(2)
    else:
        sleep(5)

    # homepage in explore
    for z in range(0, 5):
        homeRes = self.client.get(
            url=envURL + '/api/public/get-banners/homepage',
            name='homepage',
            timeout=90, allow_redirects=False,
            headers={'Accept': 'application/json, text/plain, */*'})
        if "data" in homeRes.text:
            sleep(5)
            break
        if z == 4:
            print("Test Failed permanently at homepage" + " time=" + str(z))
            print(homeRes.text)
            sleep(99999999999999999)
        else:
            print("homepage failed" + " time=" + str(z), homeRes.text)
            sleep(2)
    else:
        sleep(5)

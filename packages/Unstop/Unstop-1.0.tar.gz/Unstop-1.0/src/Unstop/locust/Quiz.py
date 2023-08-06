import csv
import random
from time import sleep
import timeit, trace, webbrowser, base64, re, threading, test
from locust_plugins.csvreader import CSVReader


def RandomQuizAnswer():
    """This function will randomly return one option from A, B, C, D"""
    ranAnswer = random.choice(["A", "B", "C", "D"])
    return ranAnswer


def QuizReview(self, access_token, quiz_id, review, environment):
    """This function will submit quiz review. Pass the access_token, quiz_id, review message as str,  and environment
    (1 for Prod, 2 for Dev2, 3 for Beta, 4 for Dev1)"""
    # submit quiz review

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
        qRevRes = self.client.post(url=envURL + '/api/v2/quiz/' + str(quiz_id) + '/update-review',
                                   name='36.update-review', timeout=120, allow_redirects=False,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Authorization': 'Bearer ' + access_token},
                                   json={'review': review, 'rating': rating})
        # print(qRevRes.text)
        if "successs" in qRevRes.text:
            sleep(random.randint(10, 20))
            break
        elif i == 9:
            print("Test Failed permanently at quiz review" + ' time-' + str(i), "\n", qRevRes.text)
            sleep(99999999999999999)
        else:
            print("Test Failed at quiz review" + ' time-' + str(i), qRevRes.text)
            sleep(3)


def QuizFinish(self, access_token, quiz_id, environment):
    """This function will finish the quiz. Pass the access_token, quiz_id and environment (1 for Prod, 2 for Dev2, 3 for
        Beta, 4 for Dev1)"""

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

    # finish the quiz
    for i in range(0, 10):
        finResponse = self.client.post(url=envURL + '/api/v2/quiz/' + str(quiz_id) + '/finish',
                                       name='35.finish', timeout=120, allow_redirects=False,
                                       headers={'Accept': 'application/json, text/plain, */*',
                                                'Authorization': 'Bearer ' + access_token},
                                       json={'finish_type': 'finishBtn', 'is_demo': False})
        # print(finResponse.text)
        if "data" in finResponse.text:
            sleep(random.randint(10, 20))
            return True
        elif i == 9:
            print("Test Failed permanently at quiz Finish" + ' time-' + str(i), "\n", finResponse.text)
            sleep(99999999999999999)
        else:
            print("Test Failed at quiz finish" + ' time-' + str(i), finResponse.text)
            sleep(3)

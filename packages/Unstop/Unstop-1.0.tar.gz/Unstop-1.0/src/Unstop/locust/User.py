import csv
import random
from itertools import cycle
from time import sleep
import timeit, trace, webbrowser, base64, re, threading, test
from locust_plugins.csvreader import CSVReader


def LoginUser(self, email, password, environment, generateCSV):
    """This function will log in the user and create a CSV file with status records!
    Pass the email, password, environment (1 for Prod, 2 for Dev2, 3 for Beta, 4 for Dev1)
    and pass 1 for True and 0 for False in generateCSV, 1 will generate the CSV file."""

    # login
    if environment == 1:
        envURL = "https://unstop.com"
    elif environment == 2:
        envURL = "https://dev2.dare2compete.com"
    elif environment == 3:
        envURL = "https://beta.dare2compete.com"
    elif environment == 4:
        envURL = "https://dev1.d2c.pw"
    else:
        envURL = "https://unstop.com"

    for i in range(0, 10):
        response = self.client.post(url=envURL + '/api/user/login', name='user/login ~ time-' + str(i),
                                    timeout=120, allow_redirects=False,
                                    headers={'accept': 'application/json, text/plain, */*',
                                             'accept-encoding': 'gzip, deflate, br',
                                             'accept-language': 'en-US,en;q=0.9', 'cache-control': 'no-cache',
                                             'content-length': '235', 'content-type': 'application/json'},
                                    json={'grant_type': 'password', 'client_id': 2,
                                          'client_secret': 'JhtzMjAQQkd4hZVLslDOfDEkw6hSQytblrIjQBUd',
                                          'username': email, 'email': email,
                                          'password': password, 'scope': '*', 'network': '', 'access_token': '',
                                          })
        if "access_token" in response.text:
            loginData = response.json()
            # global access_token
            access_token = loginData["access_token"]
            user_email = loginData["email"]
            status = "Logged In"

            if generateCSV == 1:
                # CSV generation with status and email
                with open("/mnt/locust/user_login_status.csv", "a") as csvfile:
                    fieldnames = ['email', 'status']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    # writer.writeheader()
                    writer.writerow({
                        "email": user_email,
                        "status": status
                    })
                    sleep(15)
            else:
                sleep(10)

            return access_token
        elif "user_id" in response.text:
            revokeData = response.json()["data"]
            for t in range(0, 10):
                sleep(5)
                activeRevoke = self.client.post(url=envURL + '/api/user/revoke-active-session',
                                                name='revoke-active-session', timeout=120,
                                                allow_redirects=False,
                                                headers={'accept': 'application/json, text/plain, */*',
                                                         'accept-encoding': 'gzip, deflate, br',
                                                         'accept-language': 'en-US,en;q=0.9',
                                                         'content-length': '250',
                                                         'content-type': 'application/json'},
                                                json=[
                                                    revokeData[0]["id"], revokeData[1]["id"], revokeData[2]["id"]])
                sleep(5)
                if "Sessions revoked successfully" in activeRevoke.text:

                    if generateCSV == 1:
                        # CSV generation with status and email
                        status = "Revoked Login"
                        user_email = email

                        with open("/mnt/locust/user_login_status.csv", "a") as csvfile:
                            fieldnames = ['email', 'status']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            # writer.writeheader()
                            writer.writerow({
                                "email": user_email,
                                "status": status
                            })
                            sleep(10)
                    else:
                        sleep(10)
                    break
                elif t == 9:
                    if generateCSV == 1:
                        # CSV generation with status and email
                        status = "Revoked Failed permanently" + activeRevoke.text
                        user_email = email

                        with open("/mnt/locust/user_login_status.csv", "a") as csvfile:
                            fieldnames = ['email', 'status']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            # writer.writeheader()
                            writer.writerow({
                                "email": user_email,
                                "status": status
                            })
                            sleep(10)
                    else:
                        sleep(2)
                    print("test failed permanently at revoke session" + " time-" + str(t), "\n",
                          activeRevoke.text, email)
                    return "Revoke Failed"
                else:
                    print("test failed to revoke active session" + " time-" + str(t), activeRevoke.text, email)
                    sleep(5)
        elif i == 9:

            if generateCSV == 1:
                # CSV generation with status and email
                status = "Login Failed" + response.text
                user_email = email

                with open("/mnt/locust/user_login_status.csv", "a") as csvfile:
                    fieldnames = ['email', 'status']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    # writer.writeheader()
                    writer.writerow({
                        "email": user_email,
                        "status": status
                    })
                    sleep(10)
            else:
                sleep(10)
            print("Test Failed permanently at login" + " time=" + str(i), response.text, email)
            return "Login Failed"
        else:
            print("login failed" + " time=" + str(i), response.text, email)
            sleep(5)


def LogoutFromAll(self, access_token, environment):
    """ This function will log out the user from all the devices!
    Pass the access_token, and environment (1 for Prod, 2 for Dev2, 3 for Beta, 4 for Dev1)"""

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

    # logout from all
    for i in range(0, 10):
        response = self.client.get(url=envURL + '/api/logout-from-all-devices?type=all',
                                   name='logout-from-all-devices?type=all', timeout=120,
                                   allow_redirects=False,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Authorization': 'Bearer ' + access_token})
        if response.status_code == 200:
            return True
        elif i == 9:
            return "Logout from all Failed"
        else:
            print("logout from all failed" + " time-" + str(i), response.text)
            sleep(5)


def DummyUser(TestType):
    """This function will give a dummy user email. Pass TestType, i.e., 1 for AWS testing, else 0. Does not work
    correctly as of now!"""

    if TestType == 1:
        file = "/mnt/locust/file0.csv"
        email_reader = CSVReader(file)
        csvemail = next(email_reader)
        return csvemail[0]
    elif TestType == 0:
        file = "/Users/parasgupta/Downloads/emails_for_dummy2.csv"
        email_reader = CSVReader(file)
        csvemail = next(email_reader)
        return csvemail[0]


def UserWatchList(self, access_token, environment):
    """ This function will get the watchlist of the user! Pass the access_token, and environment (1 for Prod, 2 for
    Dev2, 3 for Beta, 4 for Dev1)"""

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

    for i in range(0, 10):
        watchRes = self.client.get(url=envURL + '/api/getMyWatchlist',
                                   name='getMyWatchlist', timeout=120, allow_redirects=False,
                                   headers={'Accept': 'application/json, text/plain, */*',
                                            'Authorization': 'Bearer ' + access_token})
        if "data" in watchRes.text:
            sleep(5)
            return True
        elif i == 9:
            print("Test Failed permanently at watchlist" + " time=" + str(i), watchRes.text)
            sleep(99999999999999999)
        else:
            print("watchlist failed" + " time=" + str(i), watchRes.text)
            sleep(3)


def UserUpcomingRegistered(self, access_token, environment):
    """ This function will get the watchlist of the user! Pass the access_token, and environment (1 for Prod, 2 for
    Dev2, 3 for Beta, 4 for Dev1)"""

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

    for i in range(0, 10):
        UpcomingRes = self.client.get(url=envURL + '/api/personalize/upcoming-registered',
                                      name='UpcomingResgistrations', timeout=120, allow_redirects=False,
                                      headers={'Accept': 'application/json, text/plain, */*',
                                               'Authorization': 'Bearer ' + access_token})
        if "data" in UpcomingRes.text:
            sleep(5)
            return True
        elif i == 9:
            print("Test Failed permanently at upcoming registered" + " time=" + str(i), UpcomingRes.text)
            sleep(99999999999999999)
        else:
            print("upcoming registered failed" + " time=" + str(i), UpcomingRes.text)
            sleep(3)


def UserCoins(self, access_token, environment):
    """ This function will get the coins of the user! Pass the access_token, and environment (1 for Prod, 2 for
    Dev2, 3 for Beta, 4 for Dev1)"""

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

    for i in range(0, 10):
        coinRes = self.client.get(url=envURL + '/api/get-user-coins',
                                  name='get-user-coins', timeout=120, allow_redirects=False,
                                  headers={'Accept': 'application/json, text/plain, */*',
                                           'Authorization': 'Bearer ' + access_token})
        if "coins" in coinRes.text:
            sleep(5)
            return True
        elif i == 9:
            print("Test Failed permanently ar user coins" + " time=" + str(i), coinRes.text)
            sleep(99999999999999999)
        else:
            print("coins failed" + " time=" + str(i), coinRes.text)
            sleep(3)


def UserPermissions(self, access_token, environment):
    """ This function will get the permissions of the user! Pass the access_token, and environment (1 for Prod, 2 for
    Dev2, 3 for Beta, 4 for Dev1)"""

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

    for i in range(0, 10):
        permissionRes = self.client.get(url=envURL + '/api/getUserPermissions',
                                        name='getUserPermissions', timeout=120, allow_redirects=False,
                                        headers={'Accept': 'application/json, text/plain, */*',
                                                 'Authorization': 'Bearer ' + access_token})
        if "data" in permissionRes.text:
            sleep(5)
            return True
        elif i == 9:
            print("Test Failed permanently at user permissions" + " time=" + str(i), permissionRes.text)
            sleep(99999999999999999)
        else:
            print("user permissions failed" + " time=" + str(i), permissionRes.text)
            sleep(3)


def UserAccounts(self, access_token, environment):
    """ This function will get the accounts of the user! Pass the access_token, and environment (1 for Prod, 2 for
    Dev2, 3 for Beta, 4 for Dev1)"""

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

    for i in range(0, 10):
        accountRes = self.client.get(url=envURL + '/api/my-all-accounts',
                                     name='my-all-accounts', timeout=120, allow_redirects=False,
                                     headers={'Accept': 'application/json, text/plain, */*',
                                              'Authorization': 'Bearer ' + access_token})
        if "data" in accountRes.text:
            sleep(3)
            return True
        elif i == 9:
            print("Test Failed permanently at all accounts" + " time=" + str(i), accountRes.text)
            sleep(9999999999999999999999)
        else:
            print("all accounts failed" + " time=" + str(i), accountRes.text)
            sleep(3)

# def get_user(TestType):
#     for i in range(0, 9000000000):
#         if TestType == 1:
#             file = "/mnt/locust/file0.csv"
#             email_reader = CSVReader(file)
#             csvemail1 = next(email_reader)
#             csvemail2 = next(email_reader)
#             csvemail3 = next(email_reader)
#             return [csvemail1, csvemail2, csvemail3]
#         elif TestType == 0:
#             file = "/Users/parasgupta/Downloads/emails_for_dummy2.csv"
#             email_reader = CSVReader(file)
#             emails = next(email_reader)
#             csvemail2 = next(email_reader)
#             csvemail3 = next(email_reader)
#             csvemailList = [csvemail1, csvemail2, csvemail3]
#             i += 1
#             return csvemailList, i

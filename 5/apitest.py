import requests
from termcolor import colored

catparm = 'wtf'
catparm2 = ''
catjpg = '595f280f557291a9750ebfb7'
catsay = 'says/something?color=color'
catjson = 'json=true'


def assertTest(endpoint: object, errorCode: object = int, site: object = str) -> object:
    url = site.format(endpoint)
    response = requests.request("GET", url)
    print("TEST: "+endpoint)
    try:
        assert response.status_code == errorCode
    except AssertionError:
        print(colored("Assertion error " + str(errorCode), "red"), colored("result:", "red"), colored(response, "red"), colored(endpoint, "red"))
        return
    print(colored('result test code', 'green'), colored(errorCode, 'green'), colored(':', 'green'), response, url)
    print("\n")


assertTest(catparm, 200, 'https://cataas.com/cat/{}')
assertTest(catparm, 404, 'https://cataas.com/cat/{}')
assertTest(catjpg, 200, 'https://cataas.com/cat/{}')
assertTest(catjpg, 404, 'https://cataas.com/cat/{}')
assertTest(catparm2, 200, 'https://cataas.com/cat/{}')
assertTest(catparm2, 404, 'https://cataas.com/cat/{}')
assertTest(catsay, 200, 'https://cataas.com/cat/{}')
assertTest(catjson, 200, 'https://cataas.com/cat?{}')
assertTest(catjson, 404, 'https://cataas.com/cat?{}')



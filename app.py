from flask import Flask, make_response
from flask import render_template
from flask import request
import random

def scramble(word):
    output = ""
    length = len(word)
    for i in range (length):
        output = output + word[length - i - 1]
    return(output)

def scrambleagain(word):
    output = ""
    length = len(word)
    for i in range (0, length, 2):
        if i == (length - 1):
            output = output + word[length - 1]
            break
        else:
            output = output + word[i + 1]
            output = output + word[i]
    return(output)

def game(scrambled):
    for country in country_list:
        if len(country) == len(scrambled):
            word = ""
            word2 = ""
            for x in range (len(scrambled)):
                answer = unscramble(country.lower(), scrambled, x)
                word = word + answer

                answer2 = unscramble(scrambled, country.lower(), x)
                word2 = word2 + answer2

            if len(scrambled) == len(word):
               if word2 == scrambled:
                   return (word)
                   country_found = True
                   break

def unscramble(country, scrambled, index):
    unscrambled = ""
    for i in range (len(scrambled)):
        if scrambled[i] == country[index]:
            unscrambled = scrambled [i]
    return (unscrambled)

country_list = ["United States", "Canada", "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos Islands", "Colombia", "Comoros", "Congo", "Cook Islands", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecudaor", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Fiji", "Finland", "France", "France, Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfork Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia South Sandwich Islands", "South Sudan", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbarn and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City State", "Venezuela", "Vietnam", "Virigan Islands", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe"]

def get_country():
    country = random.choice(country_list)
    y = scramble(country.lower())
    x = scrambleagain(y)
    return [x, country]

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def start():
    return render_template("index.html")

@app.route('/country_unscramble', methods = ['GET'])
def index():
    print ("get country unscramble page")
    z = get_country()
    resp = make_response(render_template("country_unscramble.html", country1 = z[0], heading = "Question 1", correct = 0, incorrect=0))
    cookie_string = request.headers.get('Cookie')
    if cookie_string is None:
        print(cookie_string) #prints None
        cookie_value = random.randint(10, 100000000)
        print(cookie_value)
        resp.set_cookie('usercookie', str(cookie_value))
        cookieValuestring = str(cookie_value)
        dict_cookies[cookieValuestring] = [0, 0, z[1]]
        print(dict_cookies)
    else:
        cookie_string = request.headers.get('Cookie')
        split_cookies = cookie_string.split('=')
        dict_cookies[split_cookies[1]] = [0, 0, z[1]]
    return resp

dict_cookies = {}

@app.route('/answer1', methods = ['POST'])
def answer1():
    print ("Answer page")
    answer = request.form['answer1']
    print (dict_cookies)
    cookie_string = request.headers.get('Cookie')
    split_cookies = cookie_string.split('=')
    print (split_cookies)
    key = split_cookies[1]
    if key in dict_cookies:
        list_cookies = dict_cookies[split_cookies[1]]
        correct = list_cookies[0]
        incorrect = list_cookies[1]
        correct_answer = list_cookies[2]
        if answer.lower() == (correct_answer.lower()):
            correct += 1
            z = get_country()
            dict_cookies[split_cookies[1]] = [correct, incorrect, z[1]]
            return render_template("country_unscramble.html", country1 = z[0], heading = "Correct", correct=correct, incorrect=incorrect )
        else:
            z = get_country()
            incorrect += 1
            dict_cookies[split_cookies[1]] = [correct, incorrect, z[1]]
            return render_template("country_unscramble.html", country1 = z[0], heading = "Incorrect, the correct answer was " + correct_answer , correct=correct, incorrect=incorrect)

if __name__ == '__main__':
    app.run()

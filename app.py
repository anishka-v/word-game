from flask import Flask
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

country_list = ["United States", "Canada", "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Cook Islands", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecudaor", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Fiji", "Finland", "France", "France, Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfork Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia South Sandwich Islands", "South Sudan", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbarn and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States minor outlying islands", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City State", "Venezuela", "Vietnam", "Virigan Islands", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe"]

def get_country():
    country = random.choice(country_list)
    print (country)
    y = scramble(country.lower())
    x = scrambleagain(y)
    return (x)

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    global z
    z = get_country()
    return render_template("index.html", country1 = z, heading = "Start", correct = 0, incorrect=0)

correct = 0
incorrect = 0

@app.route('/answer1', methods = ['POST'])
def answer1():
    answer = request.form['answer1']
    global z
    global correct
    global incorrect
    if answer.lower() == game(z):
        correct += 1
        z = get_country()
        return render_template("index.html", country1 = z, heading = "Correct", correct=correct, incorrect=incorrect )
    else:
        z = get_country()
        incorrect += 1
        return render_template("index.html", country1 = z, heading = "Incorrect", correct=correct, incorrect=incorrect)

if __name__ == '__main__':
    app.run()

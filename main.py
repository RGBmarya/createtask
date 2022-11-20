"""
University data stored in the dictionary "university_info" was obtained from the 
"2021 Best National University Rankings" by U.S. News & World Report: 
https://www.usnews.com/best-colleges/rankings/national-universities

Princeton University: https://www.usnews.com/best-colleges/princeton-university-2627
Harvard University: https://www.usnews.com/best-colleges/harvard-university-2155
Columbia University: https://www.usnews.com/best-colleges/columbia-university-2707
Massachusetts Institute of Technology: https://www.usnews.com/best-colleges/massachusetts-institute-of-technology-2178
Stanford University: https://www.usnews.com/best-colleges/stanford-university-1305
University of Pennsylvania: https://www.usnews.com/best-colleges/university-of-pennsylvania-3378
Johns Hopkins University: https://www.usnews.com/best-colleges/jhu-2077
University of California - Berkeley: https://www.usnews.com/best-colleges/university-of-california-berkeley-1312
New York University: https://www.usnews.com/best-colleges/nyu-2785
Purdue University - West Lafayette: https://www.usnews.com/best-colleges/purdue-university-west-lafayette-1825
Brigham Young University - Provo: https://www.usnews.com/best-colleges/byu-3670
"""

university_info = {
    "Princeton University": {
        "rank": 1,
        "cost": 71710,
        "enrollment": 8419,
        "acceptance_rate": 6,
        "major": "Social Sciences",
    },
    "Harvard University": {
        "rank": 2,
        "cost": 72391,
        "enrollment": 21015,
        "acceptance_rate": 5,
        "major": "Social Sciences",
    },
    "Columbia University": {
        "rank": 3,
        "cost": 79350,
        "enrollment": 24408,
        "acceptance_rate": 5,
        "major": "Social Sciences",
    },
    "Massachusetts Institute of Technology": {
        "rank": 4,
        "cost": 65818,
        "enrollment": 11520,
        "acceptance_rate": 7,
        "major": "Computer Science",
    },
    "Stanford University": {
        "rank": 6,
        "cost": 73424,
        "enrollment": 17249,
        "acceptance_rate": 4,
        "major": "Engineering",
    },
    "University of Pennsylvania": {
        "rank": 8,
        "cost": 76826,
        "enrollment": 22432,
        "acceptance_rate": 8,
        "major": "Business, Management, and Marketing",
    },
    "Johns Hopkins University": {
        "rank": 9,
        "cost": 73810,
        "enrollment": 27092,
        "acceptance_rate": 10,
        "major": "Neuroscience",
    },
    "University of California - Berkeley": {
        "rank": 22,
        "cost": 63536,
        "enrollment": 43695,
        "acceptance_rate": 17,
        "major": "Social Sciences",
    },
    "New York University": {
        "rank": 30,
        "cost": 74124,
        "enrollment": 52885,
        "acceptance_rate": 16,
        "major": "Visual and Performing Arts",
    },
    "Purdue University - West Lafayette": {
        "rank": 53,
        "cost": 38824,
        "enrollment": 44551,
        "acceptance_rate": 60,
        "major": "Engineering",
    },
    "Brigham Young University - Provo": {
        "rank": 80,
        "cost": 13778,
        "enrollment": 34395,
        "acceptance_rate": 67,
        "major": "Business, Management, and Marketing",
    }
}

def get_budget():
    while True:
        budget = int(input("What is your total yearly budget for tuition, fees, and board? (in $): "))
        if budget > 0 and budget:
            return budget
        print("Please enter a valid budget that is above $0.")

def collect_majors(dict):
    options = []
    for uni in dict:
        for k, v in dict[uni].items():
            if k == "major" and v not in options:
                options.append(v)
    return options

def display_options(list):
    for index, major in enumerate(list):
        print(f"{index + 1}. {major}")

def get_major():
    major_list = collect_majors(university_info)
    display_options(major_list)
    while True:
        selection = int(input("What is your preferred major? (Enter a number): "))
        if selection > 0 and selection <= len(major_list):
            return major_list[selection - 1]
        print("Invalid selection. Please enter a valid number.")

def get_acceptance_rate():
    while True:
        acceptance_rate = int(input("What is your preferred minimum acceptance rate? (in %): "))
        if acceptance_rate >= 0 and acceptance_rate <= 100:
            return acceptance_rate
        print("Please enter a valid acceptance rate that is between 0% and 100% (inclusive).")

def find_universities(budget, major, acceptance_rate):
    univ_options = {}
    for uni in university_info:
        if university_info[uni]["cost"] <= budget and university_info[uni]["major"] == major\
        and university_info[uni]["acceptance_rate"] >= acceptance_rate:
            univ_options[uni] = university_info[uni]
    if univ_options:
        return univ_options
    print("We were unable to find a university that fits your preferences. Please adjust your criteria.\n")

def display_universities(dict):
    print("\nThe following universities are suitable based on your preferences:\n")
    for uni in dict:
        print(uni)
        print(f"\tNational Rank: #{dict[uni]['rank']}")
        print(f"\tCost (Tuition, Fees, & Board): ${dict[uni]['cost']:,}")
        print(f"\tTotal Enrollment: {dict[uni]['enrollment']:,} students")
        print(f"\tAcceptance Rate: {dict[uni]['acceptance_rate']}%")
        print(f"\tPopular Major: {dict[uni]['major']}")
        print("\n")

def run():
    print("Welcome to ChooseMyCollege! Respond to the following prompts to \
receive a list of universities that fit your preferences.\n")
    while True:
        user_budget = get_budget()
        user_major = get_major()
        user_rate = get_acceptance_rate()
        user_univ = find_universities(user_budget, user_major, user_rate)
        if type(user_univ) == dict:
            display_universities(user_univ)
            break
    print("Thank you for using ChooseMyCollege. Good luck!")

run()

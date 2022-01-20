#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Variables X = {IT, CH, DE, PL, CZ, SK, HU, AT, SL) encodes 9 countries by their european code (2 letters)
# For every variable x from the set X, the field D[x] = {1,2,3,4,5,6,7,8,9} encodes 9 colors we want to attribute to every country
# Constraints on the  adjacent areas is for them to have different colors. We consider the following constraints set :
# C = {{IT <> CH}, {IT <> AT}, {IT <> SL}, {CH <> AT}, {CH <> DE}, {AT <> DE}, {AT <> SL}, {AT <> CZ}, {AT <> HU}, {AT <> SK}, {DE <> CZ}, {DE <> PL}, {PL <> CZ}, {PL <> SK}, {CZ <> SK}, {SK <> HU}, {HU <> SL}}

######################################################################################################################
# Functions
######################################################################################################################

def have_border(a, b, a_map):
    '''
    Inputs :
        - (type string) a, b = the two countries
        - (type dict of strings) a_map = dictionary of the map considered
    Output :
        A boolean true if the two countries are different and share a border, false otherwise
    '''
    if a==b:
        return False
    return (b in a_map[a])

def possibleColors(a, a_map, dict_color, set_colors):
    '''
    Inputs :
        - (type string) a = the country
        - (type dict of strings) a_map = dictionary of the map considered
        - (type dict of strings) dict_color = dictionary of colors affected
        - (type list of strings) set_colors = available colors
    Output :
        List of all possible colors for a country, depending on the colors of their neighbors
    '''
    cls = set_colors[:]
    for country in a_map[a] :
        if dict_color[country] in cls :
            cls.remove(dict_color[country])			
    return cls
	
def set_colors_func(number_of_colors) :
    '''
    Input :
        - (type int) number_of_colors = the number of colors considered
    Output :
        List of int index corresponding to colors we can use for coloration of countries
    '''
    try :
        set_colors=[i for i in range(1,number_of_colors+1)]
    except :
        set_colors=[1,2,3]
    return set_colors
######################################################################################################################
# Initialisation of their variables
######################################################################################################################
name=['Austria','Germany','Poland','Czech_Republic','Slovakia','Hungary','Slovenia','Italy','Switzerland']

# the map
europe_map = dict()
europe_map['Germany'] = ['Switzerland','Austria','Poland','Czech_Republic']
europe_map['Poland'] = ['Germany','Czech_Republic','Slovakia']
europe_map['Czech_Republic'] = ['Germany','Poland','Slovakia','Austria']
europe_map['Austria'] = ['Germany','Czech_Republic','Slovakia','Hungary','Slovenia','Italy','Switzerland']
europe_map['Slovakia'] = ['Czech_Republic','Hungary','Austria','Poland']
europe_map['Hungary'] = ['Slovakia','Austria','Slovenia']
europe_map['Slovenia'] = ['Italy','Austria','Hungary']
europe_map['Italy'] = ['Slovenia','Austria','Switzerland']
europe_map['Switzerland'] = ['Germany','Austria','Italy']

#the graph
#print(europe_map)

#list of countries
#for e in europe_map:
#	print(e)

#print(have_border('Germany','Poland',europe_map))
#print(have_border('Germany','Hungary',europe_map))

set_colors=[1,2,3,4,5,6,7,8,9]

#print(set_colors)

#
# Solve the problem
#

######################################################################################################################
# Naive algorithm
######################################################################################################################

# First simple algorithm. We have 9 different colors and we assign one by country.
def resolve_CSP_1(europe_map, set_colors) :
    '''
    Inputs :
        - (type dict of strings) a_map = dictionary of the map considered
        - (type list of strings) set_colors = available colors
    Output :
        List of couples (country, color)
    '''
    europe_list = list(europe_map.keys())
    list_final = []
    i = 0
    while len(list_final) < len(set_colors) :
        list_final.append((europe_list[i],set_colors[i]))
        i += 1
    return list_final

print('\n')
print('The naive algorithm for CSP resolution gives the following affectation :' + '\n')
print(resolve_CSP_1(europe_map,set_colors))
print('\n')


######################################################################################################################
# Efficient algorithm
######################################################################################################################

## We initialise the dictionary with all countries colored with the same color.
dict_color = dict()
for e in europe_map :
    dict_color[e] = 1

europe_list = list(europe_map.keys()) # We need to retrieve the list of all countries and sort it
europe_list.sort()
index_countries_to_color = len(name) - 1
possible_colors = [[] for i in europe_list] # Possible colors for each index

## We resolve the CSP
def resolve_CSP_2(europe_map, europe_list, index_countries_to_color, possible_colors, dict_color, set_colors) :
    '''
    Inputs :
        - (type dict of strings) europe_map = dictionary of the map considered
        - (type list of strings) europe_list = sorted list of countries
        - (type int) index_countries_to_color = Index variable for relaxing constraints through iterations
        - (type list of list of strings) possible_colors = list of possible colors for each country
        - (type dict of strings) dict_color = dictionary of colors affected
        - (type list of strings) set_colors = available colors
    Output :
        Dictionary of affectations between countries and colors (country as key and color as value)
    '''
    while index_countries_to_color > 1 :
        # We affect the list of all possible values
        possible_colors[index_countries_to_color] = possibleColors(europe_list[index_countries_to_color], europe_map, dict_color, set_colors)
        
        while not possible_colors[index_countries_to_color] :
            dict_color[europe_list[index_countries_to_color]] = 0
            index_countries_to_color += 1
        
        dict_color[europe_list[index_countries_to_color]] =  possible_colors[index_countries_to_color].pop(0)
        index_countries_to_color -= 1
        
    return dict_color

# We obtain a coloration using only 4 colors. This solution is minimum as the CSP becomes unconsistant if the domain D contains 3 colors or less.
if __name__ == '__main__':
    bool = True
    number_of_colors = len(europe_list)
    set_colors = set_colors_func(number_of_colors)
    while bool :
        try :
            resolve_CSP_2(europe_map, europe_list, index_countries_to_color, possible_colors, dict_color, set_colors)
        except IndexError:
            print('The minimum number of colors is ' + str(number_of_colors+1) + '\n')
            set_colors = set_colors_func(number_of_colors+1)
            print(resolve_CSP_2(europe_map, europe_list, index_countries_to_color, possible_colors, dict_color, set_colors))
            bool = False
        number_of_colors -= 1
        set_colors = set_colors_func(number_of_colors)

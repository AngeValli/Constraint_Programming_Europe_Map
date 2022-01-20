# Constraint Programming Europe_Map
Color a map with the minimum of different colors.

## The map
We consider a map made up of 9 countries which have to be colored. The maps' coloration has to respect the constraint of having the color of each country different from the country where it has a border.

![Map](Europe_Map.png)

We encode the colors as a set of integers, and the map itself is described by an adjency matrix, encoded into a dictionary.


## The problem

The constraint satisfaction problem is the following :

The set of parameters X = {IT, CH, DE, PL, CZ, SK, HU, AT, SL) encodes 9 countries by their european code (2 letters). For every variable x from the set X, the field D[x] = {1,2,3,4,5,6,7,8,9} encodes 9 colors we want to attribute to every country.
The constraint on countries which share a border is to have different colors, which can be described as the following constraints set C :
C = {{IT <> CH}, {IT <> AT}, {IT <> SL}, {CH <> AT}, {CH <> DE}, {AT <> DE}, {AT <> SL}, {AT <> CZ}, {AT <> HU}, {AT <> SK}, {DE <> CZ}, {DE <> PL}, {PL <> CZ}, {PL <> SK}, {CZ <> SK}, {SK <> HU}, {HU <> SL}}

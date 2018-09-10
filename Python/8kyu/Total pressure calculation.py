# https://www.codewars.com/kata/5b7ea71db90cc0f17c000a5a
#
# Given the moleculer mass of two molecules ( M1 and M2 ), their masses present ( m1 and m2 ) in a vessel of volume ( V ) at a specific temperature ( T ). Find the total pressure exerted by the molecules ( Ptotal ) .
# input
#
# Six values :
#
#     m1
#     m2
#     M1
#     M2
#     V
#     T
#
# output
#
# One value :
#
#     Ptotal
#
# notes
#
# Units for each of the following are given as under :
#
#     m1 = gram
#     m2 = gram
#     M1 = gram.mole-1
#     M2 = gram.mole-1
#     V = dm3
#     T = Celcius
#     Ptotal = atmpspheric pressure (atm)
#
# Remember : Temperature is given in Celcius while SI unit is Kelvin (K)
#
# 0 Celcius = 273.15Kelvin
#
# The gas constant (R) has value of 0.082dm3.atm.K-1.mol-1


def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    # pV=nRT
    # n = given_mass / molar_mass
    R =  0.082
    temp += 273.15

    p1= (given_mass1/molar_mass1)*R*temp/volume
    p2= (given_mass2/molar_mass2)*R*temp/volume

    return p1 + p2

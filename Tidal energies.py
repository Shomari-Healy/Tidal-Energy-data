# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 09:20:30 2023

@author: Shomari
"""

import matplotlib.pyplot as plt
from statistics import mean

####################################################
#characteristics of locations

#North sea
density = 1025 #kg/m^3 (density of sea water at 10 degrees celcius)
area = 570000 #km^2
depth = 90 #m
mass_ns = density * area * depth 

#Irish Sea
density = 1025 #kg/m^3 (density of sea water at 10 degrees celcius)
area = 100000 #km^2
depth = 60 #m
mass_is = density * area * depth

#English Channel
density = 1025 #kg/m^3 (density of sea water at 10 degrees celcius)
area = 75000 #km^2
depth = 100 #m
mass_ec = density * area * depth

#Bristol Channel
density = 0 #kg/m^3 (density of sea water at 10 degrees celcius)
area = 0 #km^2
depth = 0 #m
mass_bc = density * area * depth

print ("{:.2e}".format(mass_ns)) #5.26e+10
print ("{:.2e}".format(mass_is)) #6.15e+09
print ("{:.2e}".format(mass_ec)) #7.69e+09
print ("{:.2e}".format(mass_bc))

######################################################
#Calcualting kinetic energy of each loaction
#Current values of the each location

nsc = 1.6 #m/s
isc = 2.5 #m/s
ecc = 2.9 #m/s
#bcc = 2.1 #m/s

#kinetic energy
kinetic_energy_ns = 0.5 * mass_ns * nsc**2
kinetic_energy_is = 0.5 * mass_is * nsc**2
kinetic_energy_ec = 0.5 * mass_ec * nsc**2
kinetic_energy_bc = 0.5 * mass_bc * nsc**2

print (print ("{:.2e}".format(kinetic_energy_ns))) # 6.73e+10
print (print ("{:.2e}".format(kinetic_energy_is))) # 7.87e+09
print (print ("{:.2e}".format(kinetic_energy_ec))) # 9.84e+09
print (print ("{:.2e}".format(kinetic_energy_bc)))

##########################################################################
#Plot results

#Plot kinetic energy results in bar chart
sites = ['North Sea', 'Irish Sea', 'English Channel']
kinetic_energies = [kinetic_energy_ns, kinetic_energy_is, kinetic_energy_ec]

#plot bar chart
plt.bar(sites, kinetic_energies)

# Add axis labels and a title
plt.xlabel('Sites')
plt.ylabel('Energy (Joules)')
plt.title('Tidal Energy Estimates')

# Add a legend
plt.legend(['Energy estimates'])

# Display the graph
plt.show()

#potential_energies = [potential_energy_ns, potential_energy_bc, potential_energy_ec, potential_energy_is]

#fig, ax = plt.subplots()
#ax.bar(sites, kinetic_energies, label='Kinetic energy')
#ax.bar(sites, kinetic_energies, bottom=kinetic_energies, label='Kinetic energy')
#ax.set_ylabel('Energy (joules)')
#ax.legend()

#plt.show() #One value is (ns) is significantly larger than the other seas so need to find a way to stretch the graph so everything can fit - works fine without it

#Plot potential energy results in bar chart
sites = ['North Sea', 'British Channel', 'English Channel', 'Irish Sea']
kinetic_energies = [kinetic_energy_ns, kinetic_energy_bc, kinetic_energy_ec, kinetic_energy_is]
potential_energies = [potential_energy_ns, potential_energy_bc, potential_energy_ec, potential_energy_is]

#fig, ax = plt.subplots()
#ax.bar(sites, potential_energies, label='Potential energy')
#ax.bar(sites, kinetic_energies, bottom=potential_energies, label='Kinetic energy')
#ax.set_ylabel('Energy (joules)')
#ax.legend()

#####################################################################################
#Energy calculation for a head of water utlising tidal ranges from gauge data

#Lowestoft

# calculating the mass of water
π = 3.14
r = 9 # value in m
area_t = π * r * r

print (area_t) # 254.34 m^2

depth_t = 35 #value in m
density = 1025 #kg/m^3 (density of sea water at 10 degrees celcius)
mass_t = density * area_t * depth_t

print ("{:.2e}".format(mass_t)) #9.12e+06

#calculating the current

tidal_range = 1.94 # value in m
tidal_period = 12.4 # value in hours
tidal_current = tidal_range / tidal_period

#print ("{:.2e}".format(tidal_current)) #1.56e-01

#calculate the energy
kinetic_energy_t = 0.5 * mass_t * tidal_current**2
print ("{:.2e}".format(kinetic_energy_t)) #1.12e+05

#North Sea
mass_n = 9.12e+06
current_n = 1.6
kinetic_energy_n = 0.5 * mass_n * current_n**2

#Irish sea
mass_i = 9.12e+06
current_i = 2.5
kinetic_energy_i = 0.5 * mass_i * current_i**2

# English Channel
mass_e = 9.12e+06
current_e = 2.9
kinetic_energy_e = 0.5 * mass_e * current_e**2

# Bristol Channel 
mass_b = 9.12e+06
current_b = 2.1
kinetic_energy_b = 0.5 * mass_b * current_b**2

print ("{:.2e}".format(kinetic_energy_n)) #1.17e+07
print ("{:.2e}".format(kinetic_energy_i)) #2.85e+07
print ("{:.2e}".format(kinetic_energy_e)) #3.83e+07
print ("{:.2e}".format(kinetic_energy_b)) #2.01e+07
##############################
#Calculating power density
#North sea
cp = 0.35 #device efficeincy
density = 1025 #kg/m^3 (density of sea water at 10 degrees celcius)
area = 254.34
current_n = 1.6

pd_n = 0.5 * cp * density * area * current_n**3
print ("{:.2e}".format(pd_n)) #1.87e+05

#Irish Sea
cp = 0.35 #device efficeincy
density = 1025 #kg/m^3 (density of sea water at 10 degrees celcius)
area = 254.34
current_i = 2.5

pd_i = 0.5 * cp * density * area * current_i**3
print ("{:.2e}".format(pd_i)) #7.13e+05

#English Channel
cp = 0.35 #device efficeincy
density = 1025 #kg/m^3 (density of sea water at 10 degrees celcius)
area = 254.34
current_e = 2.9

pd_e = 0.5 * cp * density * area * current_e**3
print ("{:.2e}".format(pd_e)) #1.11e+06

#Bristol Channel
cp = 0.35 #device efficeincy
density = 1025 #kg/m^3 (density of sea water at 10 degrees celcius)
area = 254.34
current_b = 2.1

pd_b = 0.5 * cp * density * area * current_b**3
print ("{:.2e}".format(pd_b)) #4.23e+05

#d = 18
#density = 1025 #kg/m^3 (density of sea water at 10 degrees celcius)
#tidal_current = 1.56e-01

#pd = 0.5 * density * tidal_current**3
#a_swept = (π * d**2) / 4
#a_occupied = 15 * d**2

#api = pd * (a_swept/a_occupied)
#igc = (api * area_t) / 10**3
#aep = (igc * 24 * 365) / 10**3

#print (pd)
#print (a_swept)
#print (a_occupied)
#print (api)
#print (igc)
#print (aep)
######################################################################################
#Mean tidal ranges for the year (values in mm) and energy calcualtion for each site

####################North Sea###################

#Cromer - 2015

avg_tide = [7182, 7020, 7027, 7079, 7068, 7143, 7156, 7178, 7204, 7302, 7203] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_c = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_c= tidal_range_c/1000
velocity_c= water_level_c/seconds
kinetic_energy_c = 0.5 * mass_ns * velocity_cprint ("{:.2e}".format(velocity_c)) #1.05e-07
print (print ("{:.2e}".format(kinetic_energy_c))) # 2.91e-04

#North Shields - 2020

avg_tide = [6937, 6971, 7025, 7050, 7077, 7096, 7094, 7146, 7118] #didn't have data for one month
min_tide = min(avg_tide)
**2 

print (tidal_range_c) #282
max_tide = max(avg_tide)
tidal_range_n = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_n= tidal_range_n/1000
velocity_n= water_level_n/seconds
kinetic_energy_n = 0.5 * mass_ns * velocity_n**2 

print (tidal_range_n) #209
print ("{:.2e}".format(velocity_n)) #7.80e-08
print (print ("{:.2e}".format(kinetic_energy_n))) # 1.60e-04

#Lowestoft - 2021

avg_tide = [7184, 7049, 7066, 7127, 7093, 7106, 7125, 7165, 7215, 7297, 7151] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_l = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_l= tidal_range_l/1000
velocity_l= water_level_l/seconds
kinetic_energy_l = 0.5 * mass_ns * velocity_l**2 

print (tidal_range_l) #248
print ("{:.2e}".format(velocity_l)) #9.26e-08
print (print ("{:.2e}".format(kinetic_energy_l))) #2.25e-04

#Whitby - 2021

avg_tide = [7322, 7288, 7241, 7245, 7261, 7291, 7302, 7434, 7426] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_w = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_w= tidal_range_w/1000
velocity_w= water_level_w/seconds
kinetic_energy_w = 0.5 * mass_ns * velocity_w**2 

print (tidal_range_w) #193
print ("{:.2e}".format(velocity_w)) #7.21e-08
print (print ("{:.2e}".format(kinetic_energy_w))) # 1.37e-04

###################English Channel#########################

#Dover - 2017

avg_tide = [7010, 7013, 7023, 7076, 7105, 7114, 7119, 7160, 7192, 7217, 7177] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_d = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_d= tidal_range_d/1000
velocity_d= water_level_d/seconds
kinetic_energy_d = 0.5 * mass_ec * velocity_d**2 

print (tidal_range_d) #207
print ("{:.2e}".format(velocity_d)) #7.73e-08
print (print ("{:.2e}".format(kinetic_energy_d))) # 2.30e-05

#Devonport - 2021

avg_tide = [7138, 7242, 7023, 7047, 7148, 7108, 7143, 7141, 7171, 7184, 7143, 7218] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_de = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_de= tidal_range_de/1000
velocity_de= water_level_de/seconds
kinetic_energy_de = 0.5 * mass_ec * velocity_de**2 

print (tidal_range_de) #219
print ("{:.2e}".format(velocity_de)) #8.18e-08
print (print ("{:.2e}".format(kinetic_energy_de))) # 2.57e-05

#Newhaven - 2021

avg_tide = [7099, 7048, 6968, 6977, 7071, 7017, 7056, 7061, 7082] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_nh = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_nh= tidal_range_nh/1000
velocity_nh= water_level_nh/seconds
kinetic_energy_nh = 0.5 * mass_ec * velocity_nh**2 

print (tidal_range_nh) #131
print ("{:.2e}".format(velocity_nh)) #4.89e-08
print (print ("{:.2e}".format(kinetic_energy_nh))) # 9.19e-06

#Weymouth - 2021

avg_tide = [7074, 7101, 6941, 6948, 7019, 7034, 7029, 7081, 7073] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_we = (max_tide - min_tide)

print (tidal_range_we) #160
days = 31
seconds = days * 24 * 60 * 60
water_level_we= tidal_range_we/1000
velocity_we= water_level_we/seconds
kinetic_energy_we = 0.5 * mass_ec * velocity_we**2 

print (tidal_range_we) #160
print ("{:.2e}".format(velocity_we)) #5.97e-08
print (print ("{:.2e}".format(kinetic_energy_we))) # 1.37e-05

###################Irish sea###########################

#Holyhead -2019

avg_tide = [6987, 7084, 7054, 7063, 7001, 7053, 7065, 7121, 7084, 7204, 7193, 7251] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_h = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_h= tidal_range_h/1000
velocity_h= water_level_h/seconds
kinetic_energy_h = 0.5 * mass_is * velocity_h**2 

print (tidal_range_h) #264
print ("{:.2e}".format(velocity_h)) #9.86e-08
print (print ("{:.2e}".format(kinetic_energy_h))) # 2.99e-05

#Liverpool(gladstone dock) - 2017

avg_tide = [7122, 7199, 7225, 7204, 7210, 7253, 7329, 7257] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_liv = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_liv= tidal_range_liv/1000
velocity_liv= water_level_liv/seconds
kinetic_energy_liv = 0.5 * mass_is * velocity_liv**2 

print (tidal_range_liv) #207
print ("{:.2e}".format(velocity_liv)) #7.73e-08
print (print ("{:.2e}".format(kinetic_energy_liv))) # 1.84e-05

#Workington - 2021

avg_tide = [6833, 6970, 6795, 6681, 6842, 6760, 6794, 6818, 7010, 6907] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_wo = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_wo= tidal_range_wo/1000
velocity_wo= water_level_wo/seconds
kinetic_energy_wo = 0.5 * mass_is * velocity_wo**2 

print (tidal_range_wo) #329
print ("{:.2e}".format(velocity_wo)) #1.23e-07
print (print ("{:.2e}".format(kinetic_energy_wo))) # 4.64e-05

#Llandudno - 2021

avg_tide = [7103, 7204, 6989, 6935, 7082, 7009, 7045, 7056, 7103, 7187, 7102] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_ll = (max_tide - min_tide)

days = 31
seconds = days * 24 * 60 * 60
water_level_ll= tidal_range_ll/1000
velocity_ll= water_level_ll/seconds
kinetic_energy_ll = 0.5 * mass_is * velocity_ll**2 

print (tidal_range_ll) #269
print ("{:.2e}".format(velocity_ll)) #1.00e-07
print (print ("{:.2e}".format(kinetic_energy_ll))) # 3.10e-05

#####################Bristol Channel#######################

#Avonmouth - 2000

avg_tide = [6963, 7101, 7029, 7020, 7045, 7082, 7199, 7254, 7333, 7293] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_a = (max_tide - min_tide)

print (tidal_range_a) #370
days = 31
seconds = days * 24 * 60 * 60
water_level_n= tidal_range_n/1000
velocity_n= water_level_n/seconds
kinetic_energy_n = 0.5 * mass_ns * velocity_n**2 

print (tidal_range_n) #209
print ("{:.2e}".format(velocity_n)) #7.80e-08
print (print ("{:.2e}".format(kinetic_energy_n))) # 1.60e-04

#Mumbles - 2013

avg_tide = [7042, 6885, 6999, 6945, 6929, 6908, 6946, 6979, 6975, 7138, 6973, 7149] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_m = (max_tide - min_tide)

print (tidal_range_m) #264
days = 31
seconds = days * 24 * 60 * 60
water_level_n= tidal_range_n/1000
velocity_n= water_level_n/seconds
kinetic_energy_n = 0.5 * mass_ns * velocity_n**2 

print (tidal_range_n) #209
print ("{:.2e}".format(velocity_n)) #7.80e-08
print (print ("{:.2e}".format(kinetic_energy_n))) # 1.60e-04

#Milfordhaven - 2021

avg_tide = [7258, 7409, 7154, 7147, 7306, 7189, 7231, 7239, 7196, 7331] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_mi = (max_tide - min_tide)

print (tidal_range_mi) #262
days = 31
seconds = days * 24 * 60 * 60
water_level_n= tidal_range_n/1000
velocity_n= water_level_n/seconds
kinetic_energy_n = 0.5 * mass_ns * velocity_n**2 

print (tidal_range_n) #209
print ("{:.2e}".format(velocity_n)) #7.80e-08
print (print ("{:.2e}".format(kinetic_energy_n))) # 1.60e-04

#Newport -2021

avg_tide = [7115, 7283, 7156, 7199, 7188, 7279, 7336, 7206, 7227] #didn't have data for one month
min_tide = min(avg_tide)
max_tide = max(avg_tide)
tidal_range_ne = (max_tide - min_tide)

print (tidal_range_ne) #221
days = 31
seconds = days * 24 * 60 * 60
water_level_n= tidal_range_n/1000
velocity_n= water_level_n/seconds
kinetic_energy_n = 0.5 * mass_ns * velocity_n**2 

print (tidal_range_n) #209
print ("{:.2e}".format(velocity_n)) #7.80e-08
print (print ("{:.2e}".format(kinetic_energy_n))) # 1.60e-04

###################################################################
#Average energy for each location based on guage data

#North Sea 
gauge_energies = [kinetic_energy_c, kinetic_energy_n, kinetic_energy_l, kinetic_energy_w]
avg_k_energy = mean(gauge_energies)
print("{:.2e}".format(avg_k_energy)) # 2.20e-04

#English Channel
gauge_energies_ec = [kinetic_energy_d, kinetic_energy_de, kinetic_energy_nh, kinetic_energy_we]
avg_k_energy_ec = mean(gauge_energies_ec)
print("{:.2e}".format(avg_k_energy_ec)) # 1.79e-05

#Irish Sea 
gauge_energies_is = [kinetic_energy_h, kinetic_energy_liv, kinetic_energy_ll, kinetic_energy_wo]
avg_k_energy_is = mean(gauge_energies_is)
print("{:.2e}".format(avg_k_energy_is)) # 3.14e-05

# Bristol Channel
gauge_energies = [kinetic_energy_c, kinetic_energy_n, kinetic_energy_l, kinetic_energy_w]
avg_k_energy = mean(gauge_energies)
print("{:.2e}".format(avg_k_energy)) # 

#############################################################################
#Plot results

#Plot kinetic energy results in bar chart
loc = ['North Sea', 'English Channel', 'Irish Sea']
avg_kinteic_energies = [avg_k_energy, avg_k_energy_ec, avg_k_energy_is]

#plot bar chart
plt.bar(loc, avg_kinteic_energies)

# Add axis labels and a title
plt.xlabel('Sites')
plt.ylabel('Energy (Joules)')
plt.title('Tidal Energy Estimates - Guage data')

# Add a legend
plt.legend(['Energy estimates'])

# Display the graph
plt.show()






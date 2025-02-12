import math
import json
from datetime import datetime

PI = math.pi

# Defined Helper functions
def calCircumference(diameter):
    return PI * diameter

def calDiameter(circumference):
    return circumference / PI

def calVolume(diameter):
    radius = diameter / 2
    return (4/3) * PI * (radius**3)

def calOrbitalPeriod(distanceInAU):
    return (distanceInAU**3)**0.5

def calDistanceFromSun(orbitalPeriod):
    return (orbitalPeriod**2)**(1/3)

# Load JSON data from text file
with open('JSONPrettyPrint.txt', 'r') as file:
    data = json.load(file)

# Fetching Sun data from JSON file
sun = data
sunName = sun["Name"]
sunDiameter = sun.get("Diameter")
sunCircumference = sun.get("Circumference")

print(f"Sun: {sunName}")

if sunDiameter:
    print(f"Diameter of {sunName}: {sunDiameter:.2f} km")
    sunCircumference = calCircumference(sunDiameter)
    print(f"Circumference of {sunName}: {sunCircumference:.2f} km")
elif sunCircumference:
    print(f"Circumference of {sunName}: {sunCircumference:.2f} km")
    sunDiameter = calDiameter(sunCircumference)
    print(f"Diameter of {sunName}: {sunDiameter:.2f} km")

# Fetching planets data from JSON file
totalPlanetVolume = 0
for planet in sun["Planets"]:
    planetName = planet["Name"]
    planetDiameter = planet.get("Diameter")
    planetCircumference = planet.get("Circumference")
    planetDistanceFromSun = planet.get("DistanceFromSun")
    planetOrbitalPeriod = planet.get("OrbitalPeriod")

    print(f"\nPlanet: {planetName}")

    # Calculating distance from Sun and orbital period
    if planetDistanceFromSun:
        print(f"Distance from sun: {planetDistanceFromSun:.2f} au")
        totalOrbitalPeriod = calOrbitalPeriod(planetDistanceFromSun)
        print(f"Orbital period: {totalOrbitalPeriod:.2f} yr")
    elif planetOrbitalPeriod:
        print(f"Orbital period: {planetOrbitalPeriod:.2f} yr")
        totalDistanceFromSun = calDistanceFromSun(planetOrbitalPeriod)
        print(f"Distance from sun: {totalDistanceFromSun:.2f} au")

    # Calculating diameter and circumference of planets
    if planetDiameter:
        print(f"Diameter: {planetDiameter:,} km")
        totalCircumference = calCircumference(planetDiameter)
        print(f"Circumference: {totalCircumference:,.0f} km")
    elif planetCircumference:
        print(f"Circumference: {planetCircumference:,} km")
        totalDiameter = calDiameter(planetCircumference)
        print(f"Diameter: {totalDiameter:,.0f} km")

    # Adding planet volume to total volume
    if planetDiameter:
        totalPlanetVolume += calVolume(planetDiameter)

    # Fetching moons data from JSON file
    if "Moons" in planet:
        for moon in planet["Moons"]:
            moonName = moon["Name"]
            moonDiameter = moon.get("Diameter")
            moonCircumference = moon.get("Circumference")

            print(f"\n  Moon: {moonName}")
            if moonDiameter:
                print(f"  Diameter: {moonDiameter:,} km")
                totalMoonCircumference = calCircumference(moonDiameter)
                print(f"  Circumference: {totalMoonCircumference:,.0f} km")
            elif moonCircumference:
                print(f"  Circumference: {moonCircumference:,} km")
                totalMoonDiameter = calDiameter(moonCircumference)
                print(f"  Diameter: {totalMoonDiameter:,.0f} km")

# Comparing total planets volume with Sun volume
sunVolume = calVolume(sunDiameter)
fitsInSun = totalPlanetVolume < sunVolume
print("\nAll the planets volume added together could fit in the Sun:", fitsInSun)

current_date_time = datetime.now().strftime("%A, %B %d, %Y")
print("By Akash:", current_date_time)

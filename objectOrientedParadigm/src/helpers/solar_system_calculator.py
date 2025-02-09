import json
from datetime import datetime
from .sun import Sun
from .planet import Planet
from .moon import Moon

def main():
    # Loading input data from JSON file
    with open("src/resources/JSONPrettyPrint.json", "r") as file:
        data = json.load(file)

    # Fetching Sun's data
    sun = Sun(
        name=data["Name"],
        diameter=data.get("Diameter"),
        circumference=data.get("Circumference")
    )
    
    # Calculating missing values
    if not sun.diameter and sun.circumference:
        sun.diameter = sun.calDiameter()
    if not sun.circumference and sun.diameter:
        sun.circumference = sun.calCircumference()

    # Fetching Planets data
    for planetData in data["Planets"]:
        name = planetData["Name"]
        diameter = planetData.get("Diameter")
        circumference = planetData.get("Circumference")
        distanceFromSun = planetData.get("DistanceFromSun")
        orbitalPeriod = planetData.get("OrbitalPeriod")

        planet = Planet(
            name=name,
            diameter=diameter,
            circumference=circumference,
            distanceFromSun=distanceFromSun,
            orbitalPeriod=orbitalPeriod,
        )
        
        # Calculating missing values
        if not planet.diameter and planet.circumference:
            planet.diameter = planet.calDiameter()
        if not planet.circumference and planet.diameter:
            planet.circumference = planet.calCircumference()

        if not planet.orbitalPeriod:
            planet.orbitalPeriod = planet.calOrbitalPeriod()
        if not planet.distanceFromSun:
            planet.distanceFromSun = planet.calDistanceFromSun()

        #fetching Moon data
        for moonData in planetData.get("Moons", []):
            moonName = moonData["Name"]
            moonDiameter = moonData.get("Diameter")
            moonCircumference = moonData.get("Circumference")
            
            moon = Moon(
                name=moonName,
                diameter=moonDiameter,
                circumference=moonCircumference,)

            # Calculating missing values of Moon
            if not moon.diameter and moon.circumference:
                moon.diameter = moon.calDiameter()
            if not moon.circumference and moon.diameter:
                moon.circumference = moon.calCircumference()

            planet.appendMoon(moon)

        sun.appendPlanet(planet)

    # Print solar system information
    print(f"Sun: {sun.name}")
    print(f"Diameter of {sun.name}: {sun.diameter:,} km")
    print(f"Circumference of {sun.name}: {sun.circumference:,.0f} km\n")

    totalPlanetVolume = 0

    for planet in sun.planets:
        print(f"Planet: {planet.name}")

        if planet.distanceFromSun:
            print(f"Distance from sun: {planet.distanceFromSun:.2f} au")

        if planet.orbitalPeriod:
            print(f"Orbital period: {planet.orbitalPeriod:.2f} yr")

        if planet.diameter:
            print(f"Diameter: {planet.diameter:,.0f} km")

        print(f"Circumference: {planet.circumference:,.0f} km")

        for moon in planet.moons:
            print(f"  Moon: {moon.name}")

            if moon.diameter:
                print(f"  Diameter: {moon.diameter:,.0f} km")

            print(f"  Circumference: {moon.circumference:,.0f} km")

        totalPlanetVolume += planet.calVolume() or 0
        print()

    sunVolume = sun.calVolume()
    fitsInSun = totalPlanetVolume < sunVolume if sunVolume else False

    print(f"\nAll the planets' volumes added together could fit in the Sun: {fitsInSun}")

    currentDateTime = datetime.now().strftime("%A, %B %d, %Y")
    print(f"By Akash: {currentDateTime}")


if __name__ == "__main__":
    main()

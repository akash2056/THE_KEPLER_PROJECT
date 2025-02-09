🌌 The Kepler Project: Solar System Insights
🚀 Python Project: Procedural and Object-Oriented Paradigms
Project Overview
The Kepler Project is a Python-based application designed to calculate and analyze solar system attributes using both procedural programming and object-oriented programming (OOP) paradigms. The project leverages JSON data to compute critical metrics such as the Sun's volume, planets' orbital periods, distances from the Sun, circumferences, and diameters. It also explores relationships between celestial bodies like planets and their moons.
By implementing two distinct programming approaches, this project demonstrates the flexibility of Python in handling structured data while adhering to software engineering principles.

🌟 Features
Calculate key solar system metrics such as:
Orbital Period (Years)
Distance from the Sun (AU)
Circumference (km)
Diameter (km)
Volume Comparisons (e.g., total planet volumes vs. Sun’s volume)
Dynamically handle missing values for diameter or circumference.
Support for both procedural and object-oriented paradigms.
Modular file structure for scalability and maintainability.

🚀 Project Workflow
Procedural Paradigm (proceduralParadigm/)
Data Handling:
Load JSON data (JSONPrettyPrint.txt) containing details about the Sun, planets, and moons.
Use helper functions to calculate missing attributes dynamically.
Calculations:
Compute circumferences, diameters, orbital periods, and distances from the Sun.
Compare total planetary volumes against the Sun’s volume.
Output:
Print detailed solar system information in a structured format.
Object-Oriented Paradigm (objectOrientedParadigm/)
Class Design:
CelestialBody: Base class for all celestial bodies with shared methods for calculations.
Planet: Inherits from CelestialBody and adds attributes like distance from the Sun, orbital period, and moons.
Moon: Represents moons associated with planets.
Sun: Represents the Sun and contains a list of planets.
Dynamic Calculations:
Automatically calculate missing values (e.g., diameter or circumference) during runtime.
Use encapsulated methods in Planet to compute orbital period or distance from the Sun based on available data.
Output:
Generate an interactive report with detailed information about each celestial body.

📊 Findings & Insights
The combined volumes of all planets fit comfortably inside the Sun's volume.
Missing attributes like diameter or circumference are dynamically calculated using formulas during runtime.
Orbital periods and distances from the Sun are derived using Kepler's laws when not explicitly provided.

🛠️ Tools & Technologies
Python 3.x
JSON for structured data storage
Modular programming with OOP principles

🔗 How to Run
Procedural Paradigm:
Navigate to the proceduralParadigm/ directory:
bash cd THE_KEPLER_PROJECT/proceduralParadigm
Run the program: python proceduralAstro.py
Object-Oriented Paradigm:
Navigate to the objectOrientedParadigm/src/helpers/ directory:
bash cd THE_KEPLER_PROJECT/objectOrientedParadigm/src/helpers
Run the program: python solar_system_calculator.py

📅 Current Date:
Sunday, February 09, 2025, 1 AM EST
Feel free to contribute, report issues, or suggest improvements! 🚀 This write-up provides a professional overview of your project while aligning with your file structure and functionality!

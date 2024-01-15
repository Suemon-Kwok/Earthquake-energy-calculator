def earthquake_energy_calculator():
    # Importing the math module for the power function
    import math

    # Asking for user input
    M = float(input("Please enter the magnitude of the earthquake: "))

    # Calculating the energy in ergs
    E_ergs = 10 ** (11.8 + 1.5 * M)

    # Converting the energy to kilojoules (1 erg = 10^-10 kilojoules)
    E_kilojoules = E_ergs * 10 ** -10

    # Converting the energy to petajoules (1 kilojoule = 10^-12 petajoules)
    E_petajoules = E_kilojoules * 10 ** -12

    # Printing the results
    print(f"The input magnitude of {M} is equal to {E_ergs} ergs, which is also equal to {E_petajoules} petajoules.")

# Calling the function
earthquake_energy_calculator()

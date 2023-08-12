# Number Base Converter

This is a simple program that allows you to convert a decimal number to a different base and vice versa.

## Usage

1. Run the program.
2. You'll be prompted to enter a decimal number and a base value.

### OUTPUT Example:

```Enter a decimal number: 479.87
Enter a base value: 16
1DF.
Converted result: 1DF.DEB85
Converted back to decimal: 479.8699998855591
1DF.
Visual for Decimal to Base Conversion:
Calculating Decimal to Base conversion:
Input: 479.87 (Base 16)

Decimal to Base Conversion:

Integer Part Calculation:
     4 * (16^2)      = 1024
     7 * (16^1)      = 112
     9 * (16^0)      = 9

Fractional Part Calculation:
    8 * (16^-1)      = 0.5
    7 * (16^-2)      = 0.02734375

Final Result:
4 * (16^5) + 7 * (16^4) + 9 * (16^3) + 8 * (16^2) + 7 * (16^1) = 1DF.DEB85

---------------------------------

Visual for Base to Decimal Conversion:
Calculating Base to Decimal conversion:
Input: 1DF.DEB85 (Base 16)

Base to Decimal Conversion:

Integer Part Calculation:
     1 * (16^2)      = 256
    13 * (16^1)      = 208
    15 * (16^0)      = 15

Fractional Part Calculation:
    13 * (16^-1)     = 0.8125
    14 * (16^-2)     = 0.0546875
    11 * (16^-3)     = 0.002685546875
    8 * (16^-4)      = 0.0001220703125
    5 * (16^-5)      = 4.76837158203125e-06

Final Result:
1 * (16^8) + 13 * (16^7) + 15 * (16^6) + 13 * (16^5) + 14 * (16^4) + 11 * (16^3) + 8 * (16^2) + 5 * (16^1) = 479.8699998855591
```

## Requirements

> Python 3.x
## How to Run

1. Make sure you have Python 3.x installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the calculator.py and gui.py files.

## Run the command:

```python gui.py```

## License
> [!NOTE]
> This project is licensed under the MIT License - see the LICENSE file for details.

## Note
> [!IMPORTANT]
> Please make sure to update the paths and filenames according to your project structure. Also, feel free to add more sections or details as needed for your project.

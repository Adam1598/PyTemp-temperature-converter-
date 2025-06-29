# PyTemp   ----  My first Python Project

# Temperature Converter (Python CLI)

A simple and robust command-line temperature converter written in Python.  
Convert between Celsius, Fahrenheit, and Kelvin, with a history feature and the ability to save your conversion log to a text file in your Downloads folder.

---

## Features

- **Convert between:**  
  - Celsius ↔ Fahrenheit  
  - Celsius ↔ Kelvin  
  - Fahrenheit ↔ Celsius  
  - Fahrenheit ↔ Kelvin  
  - Kelvin ↔ Celsius  
  - Kelvin ↔ Fahrenheit
- **Conversion history**: All conversions are logged and viewable before quitting.
- **Export history**: Save your conversion history as a neatly formatted `.txt` file to your Downloads folder.
- **File name safety**: Prevents invalid and reserved Windows file names.
- **User-friendly**: Handles invalid input, Ctrl+C, and accidental errors gracefully.

---

## How to Run

1. **Requirements**  
   - Python 3.x (no external libraries required).

2. **Usage**  
   - Download/copy "PyTemp.exe".
   - Double-click the file
   - Follow the on-screen prompts to perform conversions.
   - To save your conversion history, type `Q` (capital or lowercase) at the main menu.

3. **Saving History**  
   - When you quit with history, you'll be prompted to name your file.
   - The program checks for invalid file names and warns if a file already exists.

4. **Graceful Exit**  
   - You can exit at any time with Ctrl+C.  
   - The script will prompt "Press Enter to exit..." before closing, so you'll always see the final message.

---

## Example

```
Hi! Choose a conversion.
 1. Celsius → Fahrenheit
 2. Fahrenheit → Celsius
 3. Celsius → Kelvin
 4. Kelvin → Celsius
 5. Fahrenheit → Kelvin
 6. Kelvin → Fahrenheit
 0. Quit without saving
 Q. Quit and save history to txt file

> 1
Great! Now input the value of the temperature you want to convert to Fahrenheit.
> 100

212.0 is your value in Fahrenheit!

Do another conversion?
...
```

---

## Notes

- By default, output history files are saved to your user's Downloads folder.
- All temperature calculations are rounded to two decimal places.
- The script is designed for Windows, but works on Linux/Mac (with a Downloads folder).

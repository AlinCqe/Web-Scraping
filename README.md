This is a basic script for searching product prices on Amazon.

Saves product name and price to a CSV file. (You can easily modify it to save data as JSON or into a database).


### How to Use

1. Make sure you have Python 3 installed.
2. Install required libraries:
    - beaufidulsoup4
    - requests
3. Run the script
4. Enter the product you want to search for (e.g., `RTX 4090` or `Ryzen 5500G`).
5. The matching results will be shown in the terminal and saved to `data.csv`.

### Notes
    - The script uses regext to match flexible product names(e.g., with or with out spaces)
    - It filters out items that cointaint 'PC' or 'Computer'(case sensitive) to avoid prebuilt



### THIS VERSION DOESNT GO THROUGH PAGES, ONLY SAVES DATA FROM THE FIRST ONE

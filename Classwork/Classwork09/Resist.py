# written by Arye Mindell
import sys
from MetricPrefix import prefix_to_value

def main():
    try:
        # Convert command line arguments (except the script name) to integers
        admitances = list(map(calcAdmittance, sys.argv[1:]))  # Skip the script name and convert
        print(1/sum(admitances))
    except ValueError as e:
        print("Error: Please ensure all arguments are integers.")
def calcAdmittance(r):
    admit = 0
    n=1
    for character in r:
        if(not character.isdigit()):
            r = r.replace(character,'')
            n = prefix_to_value(character)
            break
    admit = 1/(n*float(r))
    return admit    

main()
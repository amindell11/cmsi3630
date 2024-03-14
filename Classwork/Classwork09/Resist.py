# written by Arye Mindell
import sys
from MetricPrefix import prefix_to_value

def main():
    try:
        # Convert command line arguments (except the script name) to integers
        mode = sys.argv[1]
        if(mode == 'p'):
            admitances = list(map(calcAdmittance, sys.argv[2:]))  # Skip the script name and convert
            print(1/sum(admitances))
        elif(mode == 's'):
            resistances = list(map(calcResist, sys.argv[2:]))  # Skip the script name and convert
            print(sum(resistances))
        else:
            raise ValueError(f"improper mode: "+sys.argv[1])
    except ValueError as e:
        print("Error: Please ensure all arguments are correct.")
def calcAdmittance(r):
    return 1/calcResist(r)
def calcResist(r):
    resist = 0
    n=1
    for character in r:
        if(not character.isdigit()):
            r = r.replace(character,'')
            n = prefix_to_value(character)
            break
    resist = n*float(r)
    return resist      

main()
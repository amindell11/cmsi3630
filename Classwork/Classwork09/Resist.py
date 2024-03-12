# written by Arye Mindell
import sys

def main():
    try:
        # Convert command line arguments (except the script name) to integers
        admitances = list(map(calcAdmittance, sys.argv[1:]))  # Skip the script name and convert
        print(1/sum(admitances))
    except ValueError as e:
        print("Error: Please ensure all arguments are integers.")
def calcAdmittance(r):
    admit = 0
    if('k' in r) :
        r = r.replace('k','')
        admit = 1/(1000*float(r))
    else :
        admit = 1/float(r)
    return admit
main()
import linkedList
import sys

print(len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
if len(sys.argv) < 5:
    print("Run with arguments V, E, G, and DIST")
    exit()
V = sys.argv[1]
E = sys.argv[2]
G = sys.argv[3]
DIST = sys.argv[4]
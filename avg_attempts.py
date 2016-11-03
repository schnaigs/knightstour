import numpy
import re
import subprocess
import sys

def main():
    """Print the average number of attempts to find a successful knight's tour."""

    if not valid_input():
        sys.exit("usage: python avg_attempts.py rows cols attempts runs")

    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    attempts = int(sys.argv[3])
    runs = int(sys.argv[4])

    list_of_attempts = []

    for run in range(runs):
        output = subprocess.check_output(["python", "knightstour4.py",
                                          str(rows), str(cols), str(attempts)])

        try:
            found_kt_on_attempt = int(re.sub('^.*attempt #([0-9]+).*', '\\1', 
                                       output, 
                                       flags=re.DOTALL))
        
            # run found a successful knight's tour
            list_of_attempts.append(found_kt_on_attempt)
        except ValueError:    # run failed to find any knight's tours; 
		pass          # don't count it, don't do anything


    if list_of_attempts == []:
        sys.exit("no successful knights tours found")

    avg_attempts = numpy.mean(list_of_attempts)
    
    stddev = numpy.std(list_of_attempts) 
    print avg_attempts
    print stddev

def valid_input():
    """Returns True if input is valid, False otherwise."""

    if len(sys.argv) != 5:
        return False

    try:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
        attempts = int(sys.argv[3])
        runs = int(sys.argv[4])
    except ValueError:
        return False

    if rows < 1 or cols < 1 or attempts < 1 or runs < 1:
        return False

    return True


if __name__ == "__main__":
    main()

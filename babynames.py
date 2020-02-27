""" The babynames.py module takes as input one or more html
    file containing baby name ranking data and defines the
    extract_names method which extracts the data from the
    html file and returns a list containing the year
    followed by the name ranking pairs as a string.
    This data is print to standard output unless the
    --summary file flag is set, indicating the output should
    be print to a summary output file.

"""

import sys
import re

def extract_names(filename):
    """The extract_names function takes as input a filename to be
    opened and analyzed for baby name ranking information.
    The function returns a list where the first item is a
    string indicating the year and the rest of the items are
    name rank pair strings of the form "First_Name Rank".
    :param filename: The filename of the html file to be parsed.
    :type filename: String.
    :returns: Results list (List).
    :raises: None."""
    f = open(filename, 'r')
    file_data = f.read()

    year_p = re.compile(r'Popularity in ([0-9]{4})')
    year_m = year_p.search(file_data)
  
    name_rank_p = re.compile(r'<td>([1-9][0-9]*)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>')
    name_rank_m = name_rank_p.findall(file_data)

    name_dict = {}
    for rank in name_rank_m:
      boy_name = rank[1]
      girl_name = rank[2]
      for name in [girl_name, boy_name]:
        if name not in name_dict:
          name_dict[name] = rank[0]
        else:
          name_dict[name] = min(int(rank[0]), int(name_dict[name]))

    results = [year_m.groups()[0]]
    for k, v in sorted(name_dict.items()):
      results.append(str(k) + " " + str(v))

    return results


def main():
    """The main function performs command-line argument
    parsing and prints the results of analysis to either
    std out or a summary file depending on whether the
    --summaryfile flag is set.
    :returns: None.
    :raises: None."""
    args = sys.argv[1:]

    if not args:
      print 'usage: [--summaryfile] file [file ...]'
      sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
      summary = True
      del args[0]
  
    for arg in args:
      if summary:
      filename = arg + ".summary"
          out = open(filename, 'w')
      else:
    out = sys.stdout
      results = extract_names(arg)
      for item in results:
        out.write(str(item) + "\n")
      out.close()

if __name__ == '__main__':
    main()

import argparse
import pdb
import logging as lg

import analysis.csv as c_an
import analysis.xml as x_an

lg.basicConfig(level=lg.DEBUG)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--datafile",help="""CSV file containing pieces of
        information about the members of parliament""")
    parser.add_argument("-e", "--extension", help="""King of of file to analyse. Is it a CSV of an XML?""")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    try:
        datafile = args.datafile
        if datafile == None:
            raise Warning('You must indicate a datafile!')
    except Warning as e:
        lg.warning(e)
    else:
        if args.extension == 'xml':
            x_an.launch_analysis(datafile)
        elif args.extension == 'csv':
            c_an.launch_analysis(datafile)
    finally:
        lg.info('#################### Analysis is over ######################')

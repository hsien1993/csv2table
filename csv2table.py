import argparse 
#import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='input csv file')
parser.add_argument('-c', '--caption', default='',
                    help='caption of the table')
parser.add_argument('-l', '--label', default='',
                    help='label of the table')
parser.add_argument('-s', '--style', default='',
                    help='style of the table')
parser.add_argument('-t', '--tab', action='store_true',
                    help='print with indention or not')
args = parser.parse_args()

tab = '    ' if args.tab else '' 

with open(args.filename) as f:
    if len(args.style) > 0:
        style = args.style.strip('{').strip('}')
    else:
        n_row = f.readline().count(',')
        style = '@{}|c|' + 'c|'*n_row + '@{}'

f = open(args.filename)
print '\\begin{table}'
print tab + '\\label{' + args.label + '}'
print tab + '\\caption{' + args.caption + '}'
print tab + '\\centering'
print tab + '\\begin{tabular}' + '{' + style + '}'
print tab*2 + '\\hline'
for l in f:
    print tab*2 + l.replace(',',' & ').replace('\n','\\\\')
    print tab*2 + '\\hline'
print tab + '\\end{tabular}'
print '\\end{table}'
    


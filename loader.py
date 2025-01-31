import csv
import json
from utils import readf

def get_task_loader(args):
    file = f'data/{args.task}/{args.div}.csv' if args.div else f'data/{args.task}.csv'
    rows = csv.reader(open(file))
    if args.task == 'intersection':
        loader = ((row[1], row[2], row[3]) for row in rows) 
    else:
        loader = ((row[1], row[2]) for row in rows) 
         
    return loader

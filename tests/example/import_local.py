# Author: Jasmine Oliveira
# Date: 07/05/2016
# Imports all local files to database

import tables.molecules_table as mol_entry
import tables.peaks_table as p_entry
# import tables.molecules_tabl as mol_get
# import temp.remove.remove_molecules as mol_rem
# import temp.remove.remove_peaks as p_rem
# from queries import view_query

from config import *

# Connect to sqlite database
conn = sqlite3.connect(db_filepath)
cursor = conn.cursor()

while True:
    print "Choose an option: \n (a) Import all files in path\n (b) Import individual file\n (c) Remove a molecule entry \n (d) Remove all peaks \n (e) View a row"
    input = raw_input()


    if input == 'a':
        print "Enter category: "
        category = input()
        print "Enter file directory : "
        path = raw_input()
        imported = 0

        # Insert known values
        for i in os.listdir(path):
            if i.endswith('.cat') or i.endswith('.lines'):
                name = (i.split("."))[0]
                filepath = os.path.join(path, i)
                # New Molecule entry
                #mid = mol_entry.get_mid(conn,name, category)
                #p_rem.remove_all(conn,mid)
                mid = mol_entry.new_molecule_entry(conn, name, category)
                # New Peaks entry
                try:
                    print "Importing: " + name
                    p_entry.import_file(conn,filepath, mid)
                    imported += 1
                except ImportError:
                    print "Error importing: " + name
    elif input == "b":
        print "Enter molecule name: "
        name = input()
        print "Enter category: "
        category = input()
        print "Enter filepath: "
        filepath = input()

        # New molecule entry
        mid = mol_entry.new_molecule_entry(conn, name, category)
        # New Peaks entry
        try:
            print "Importing: " + name
            p_entry.import_file(conn, filepath, mid)
        except ImportError:
            print "Error importing: " + name
    elif input == "c":
        print "Sorry - This feature is deprecated"
        # print "Enter mid: "
        # mid = input()
        # name = mol_get.getName(conn, mid)
        # mol_rem.remove_molecule(conn,mid)
        print "[ Removed molecule: " + name + " ]"

    elif input == "d":
        print "Sorry - This feature is deprecated"
        # print "Enter mid: "
        # name = mol_get.getName(conn, mid)
        # p_rem.remove_all(conn, mid)
        # print "[ Removed all peaks for: " + name + " ]"

    elif input == "e":
        print "Sorry - This feature is deprecated"
        # print "Enter tablename: "
        # table = input()
        # print "Enter appropriate id: "
        # id = input()
        # print view_query.row_view(table,id)
    else:
        print "Error. Incorrect input."
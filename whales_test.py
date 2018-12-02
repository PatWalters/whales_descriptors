#!/usr/bin/env python

import sys
from rdkit import Chem
from whales_descriptors import do_whales

suppl = Chem.SDMolSupplier(sys.argv[1])
x, labels = do_whales.main(suppl, charge_threshold=0, do_charge=True, property_name='')
x.columns = labels
x.to_csv("whales.csv", index=False)

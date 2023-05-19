"""
 Copyright (c) 2023 Beáta Ungurán All rights reserved.
 Use of this source code is governed by a BSD-style
 license that can be found in the LICENSE file.
 """

import os

# Define the path to the "tables" directory relative to the current file
ps_path = os. path.dirname(os.path.realpath(__file__))
ps_tables_path = os.path.join(ps_path, "..", "tables")

ps_allowances_path = os.path.join(ps_path, "..", "allowances")

prv_tables_path = os.path.join(ps_path, "..", "prv")
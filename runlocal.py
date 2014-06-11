#!/usr/bin/env python
import os
os.environ['MIITA_SETTING_FILE'] = '../setting_local.py'

import miita
miita.app.run(host='0.0.0.0', debug=True)

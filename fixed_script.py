Microsoft (R) File Expansion Utility
Copyright (c) Microsoft Corporation. Todos os direitos reservados.


from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'file.yaml'
file = file_location.open()
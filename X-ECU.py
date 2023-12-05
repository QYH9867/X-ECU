from module.Arm import Arm
from module.Tricore import Tricore

print('Which architecture is your ECU firmware?')
architecture=input('Please enter Arm or Tricore:')
file_name=input('Please enter the name of your ECU firmware:')
if architecture=='Arm':
    Arm(file_name)
elif architecture=='Tricore':
    Tricore(file_name)

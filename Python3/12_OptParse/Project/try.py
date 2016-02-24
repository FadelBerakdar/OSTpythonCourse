    #!/usr/bin/python3

from optparse import OptionParser


parser = OptionParser()
parser.add_option("-z",
                  "--zip_code",
                  action="store",
                  dest="zip_code",
                  help="Sets the zip code value of the Address object"
                  )

parser.add_option("-s",
                  "--state",
                  action="store",
                  dest="state",
                  default = "CA",
                  help="Sets the zip code value of the Address object"
                  )


opts, args = parser.parse_args()
opts_dict = vars(opts)
import  subprocess

subprocess.run("./propertyAddress.py", )


import shlex, subprocess

command_line = './propertyAddress.py -l WARNING -n Tom -a "my street" -c "San Diego" -s "CAC" -z 12345-1234'
args = shlex.split(command_line)

print(args[:11])
subprocess.Popen(args)








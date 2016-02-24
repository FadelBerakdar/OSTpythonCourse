__author__ = 'Fadel'
import sys

# build the dispatch table dict

switch = {
'capitalize':str.capitalize,
'title':str.title,
'upper':str.upper,
'lower':str.lower,
'exit':sys.exit
}


# build the list of options
options = switch.keys()


# create the prompts
prompt_opt = 'Enter a function name (%s): ' % ', '.join(options)
#'Pick an option from the list ({0}): '.format(', '.join(options))
prompt_str = 'Enter a string: '

while True:
    # request the option from the user
    opt_inp = input(prompt_opt)

    # get the option value (desired function) from the dispatch table dict

    option = switch.get(opt_inp, None)
    if not option:
        # option is not valid.
        # will not prompt for string until option is valid.
        print('Please select a valid option!')
    else:
        # If option is 'exit', exit immediately
        if opt_inp == 'exit':
            print("Goodbye for now!")

            option()


    # Option is valid and not 'exit'.
    # Request and process a string.

    str_inp = input(prompt_str)
    print(option(str_inp))
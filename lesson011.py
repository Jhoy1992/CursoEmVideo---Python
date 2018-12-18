# Colors on terminal
# Style: 0- None - 1 - Bold - 4 - Underline - 7 - Invert
# Text: 30 - White | 31 - Red | 32 - Green | 33 - Yellow
#       34 - Blue | 35 - Purple | 36 - Cyan | 37 - Gray
# back: 40 - 41 - 42 - 43 - 44 - 45 - 46 - 47 - Same paterns of the text.

colors = {'clean':'\033[m',
            'blue':'\033[34m',
            'yellow':'\033[33m', 
            'blackandwhite':'\033[7;30m'}

print('Pleased to meet you {}{}{}'.format(colors['blue'], 'Jhonatan', colors['clean']))

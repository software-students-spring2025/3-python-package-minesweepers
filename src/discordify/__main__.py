import discordify

def main():
    print('Enter one of the following functions: stutterify, uwuify, leetify, dumbify')
    func = input('>').strip()
    if func not in ['leetify','stutterify','uwuify','dumbify']:
        print('Invalid input.')
        return
    print('Enter the text you wish to transform:')
    text = input('>').strip()
    print('Here is your transformed text:')
    if func=='dumbify':
        print(discordify.dumbify(text))
    if func=='stutterify':
        print(discordify.stutterify(text))
    if func=='leetify':
        print(discordify.leetify(text))
    if func=='uwuify':
        print(discordify.uwuify(text))
    return 

if __name__=="__main__":
    main()
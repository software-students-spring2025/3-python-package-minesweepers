import discordify

def main():
    print('Enter one of the following functions: stutterify, uwuify, leetify, dummify')
    func = input('>').strip()
    if func not in ['leetify','stutterify','uwuify','dummify']:
        print('Invalid input.')
        return
    print('Enter the text you wish to transform:')
    text = input('>').strip()
    print('Here is your transformed text:')
    if func=='dummify':
        print(discordify.dummify(text))
    if func=='stutterify':
        print(discordify.stutterify(text))
    if func=='leetify':
        print(discordify.leetify(text))
    if func=='uwuify':
        print(discordify.uwuify(text))
    return 

if __name__=="__main__":
    main()
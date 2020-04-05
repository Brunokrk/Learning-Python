favorite_languages = {
    'jen': ['python','ruby'],
    'sarah':['C', 'Pascal'],
    'edward':['ruby', 'go'],
    'phill' : ['python','haskell'],
}
for name, languages in favorite_languages.items():
    print("\n"+ name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


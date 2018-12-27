

languages = {"Java":".java",'Perl':'.pl',"Shell":".sh",'Python':'.py'}

print(languages,type(languages),id(languages),len(languages),dict(enumerate(languages)))

print(languages.keys())

print(languages.values())

#print(languages.keys('Perl')) # TypeError: keys() takes no arguments (1 given)

#print(languages.values('Java')) # TypeError: keys() takes no arguments (1 given)

print(languages.get('Shell'))

print(languages.items())  # [(),(),(),()]


magicians = ['alice', 'david', 'carolina', 'charles', 'florence']
for magician in magicians: #A extensão do laço for respeita sua identação
    print(magician.title())


print(magicians[0:3])#exibe uma fatia da lista

#percorrendo uma fatia com um laço
for magician in magicians[:3]:
    print(magician.title())
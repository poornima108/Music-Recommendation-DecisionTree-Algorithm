import itertools

def generate_data():
    all_list = [
                ['north-north','north-east','north-south','north-west',
                'east-north','east-east','east-south','east-west',
                'south-north','south-east','south-south','south-west',
                'west-north','west-east','west-south','west-west'],
                [i for i in range(10,80)],
                ['male','female'],
                ['romantic','workout','pop']
               ]

    combs = list(map(list,list(itertools.product(*all_list))))

    for i in combs:
        if i[3] == 'romantic':
            if i[1] <=20:
                if i[0] == 'north-north':
                    i.append('minior-hindi-grp-1')
                elif i[0] == 'north-east':
                    i.append('minior-hindi-grp-2')
                elif i[0] == 'north-south':
                    i.append('minior-hindi-grp-3')
                elif i[0] == 'north-west':
                    i.append('minior-hindi-grp-4')

                elif i[0] == 'east-north':
                    i.append('minior-hindi-grp-5')
                elif i[0] == 'east-east':
                    i.append('minior-hindi-grp-6')
                elif i[0] == 'east-south':
                    i.append('minior-hindi-grp-7')
                elif i[0] == 'east-west':
                    i.append('minior-hindi-grp-8')

                elif i[0] == 'south-north':
                    i.append('minior-english-grp-1')
                elif i[0] == 'south-east':
                    i.append('minior-english-grp-2')
                elif i[0] == 'south-south':
                    i.append('minior-english-grp-3')
                elif i[0] == 'south-west':
                    i.append('minior-english-grp-4')

                elif i[0] == 'west-north':
                    i.append('minior-english-grp-5')
                elif i[0] == 'west-east':
                    i.append('minior-english-grp-6')
                elif i[0] == 'west-south':
                    i.append('minior-english-grp-7')
                elif i[0] == 'west-west':
                    i.append('minior-english-grp-8')
            else:
                if i[0] == 'north-north':
                    i.append('adult-hindi-grp-1')
                elif i[0] == 'north-east':
                    i.append('adult-hindi-grp-2')
                elif i[0] == 'north-south':
                    i.append('adult-hindi-grp-3')
                elif i[0] == 'north-west':
                    i.append('adult-hindi-grp-4')

                elif i[0] == 'east-north':
                    i.append('adult-hindi-grp-5')
                elif i[0] == 'east-east':
                    i.append('adult-hindi-grp-6')
                elif i[0] == 'east-south':
                    i.append('adult-hindi-grp-7')
                elif i[0] == 'east-west':
                    i.append('adult-hindi-grp-8')

                elif i[0] == 'south-north':
                    i.append('adult-english-grp-1')
                elif i[0] == 'south-east':
                    i.append('adult-english-grp-2')
                elif i[0] == 'south-south':
                    i.append('adult-english-grp-3')
                elif i[0] == 'south-west':
                    i.append('adult-english-grp-4')

                elif i[0] == 'west-north':
                    i.append('adult-english-grp-5')
                elif i[0] == 'west-east':
                    i.append('adult-english-grp-6')
                elif i[0] == 'west-south':
                    i.append('adult-english-grp-7')
                elif i[0] == 'west-west':
                    i.append('adult-english-grp-8')
                
        if i[3] == 'workout':
            if i[1] <=20:
                if i[0] == 'north-north':
                    i.append('minor-hindi-grp-9')
                elif i[0] == 'north-east':
                    i.append('minor-hindi-grp-10')
                elif i[0] == 'north-south':
                    i.append('minor-hindi-grp-11')
                elif i[0] == 'north-west':
                    i.append('minor-hindi-grp-12')

                elif i[0] == 'east-north':
                    i.append('minor-hindi-grp-13')
                elif i[0] == 'east-east':
                    i.append('minor-hindi-grp-14')
                elif i[0] == 'east-south':
                    i.append('minor-hindi-grp-15')
                elif i[0] == 'east-west':
                    i.append('minor-hindi-grp-16')

                elif i[0] == 'south-north':
                    i.append('minor-english-grp-9')
                elif i[0] == 'south-east':
                    i.append('minor-english-grp-10')
                elif i[0] == 'south-south':
                    i.append('minor-english-grp-11')
                elif i[0] == 'south-west':
                    i.append('minor-english-grp-12')

                elif i[0] == 'west-north':
                    i.append('minor-english-grp-13')
                elif i[0] == 'west-east':
                    i.append('minor-english-grp-14')
                elif i[0] == 'west-south':
                    i.append('minor-english-grp-15')
                elif i[0] == 'west-west':
                    i.append('minor-english-grp-16')
            else:
                if i[0] == 'north-north':
                    i.append('adult-hindi-grp-9')
                elif i[0] == 'north-east':
                    i.append('adult-hindi-grp-10')
                elif i[0] == 'north-south':
                    i.append('adult-hindi-grp-11')
                elif i[0] == 'north-west':
                    i.append('adult-hindi-grp-12')

                elif i[0] == 'east-north':
                    i.append('adult-hindi-grp-13')
                elif i[0] == 'east-east':
                    i.append('adult-hindi-grp-14')
                elif i[0] == 'east-south':
                    i.append('adult-hindi-grp-15')
                elif i[0] == 'east-west':
                    i.append('adult-hindi-grp-16')

                elif i[0] == 'south-north':
                    i.append('adult-english-grp-9')
                elif i[0] == 'south-east':
                    i.append('adult-english-grp-10')
                elif i[0] == 'south-south':
                    i.append('adult-english-grp-11')
                elif i[0] == 'south-west':
                    i.append('adult-english-grp-12')

                elif i[0] == 'west-north':
                    i.append('adult-english-grp-13')
                elif i[0] == 'west-east':
                    i.append('adult-english-grp-14')
                elif i[0] == 'west-south':
                    i.append('adult-english-grp-15')
                elif i[0] == 'west-west':
                    i.append('adult-english-grp-16')

                
        if i[3] == 'pop':
            if i[1] <=20:
                if i[0] == 'north-north':
                    i.append('minor-hindi-grp-17')
                elif i[0] == 'north-east':
                    i.append('minor-hindi-grp-18')
                elif i[0] == 'north-south':
                    i.append('minor-hindi-grp-19')
                elif i[0] == 'north-west':
                    i.append('minor-hindi-grp-20')

                elif i[0] == 'east-north':
                    i.append('minor-hindi-grp-21')
                elif i[0] == 'east-east':
                    i.append('minor-hindi-grp-22')
                elif i[0] == 'east-south':
                    i.append('minor-hindi-grp-23')
                elif i[0] == 'east-west':
                    i.append('minor-hindi-grp-24')

                elif i[0] == 'south-north':
                    i.append('minor-english-grp-17')
                elif i[0] == 'south-east':
                    i.append('minor-english-grp-18')
                elif i[0] == 'south-south':
                    i.append('minor-english-grp-19')
                elif i[0] == 'south-west':
                    i.append('minor-english-grp-20')

                elif i[0] == 'west-north':
                    i.append('minor-english-grp-21')
                elif i[0] == 'west-east':
                    i.append('minor-english-grp-22')
                elif i[0] == 'west-south':
                    i.append('minor-english-grp-23')
                elif i[0] == 'west-west':
                    i.append('minor-english-grp-24')
            else:
                if i[0] == 'north-north':
                    i.append('adult-hindi-grp-17')
                elif i[0] == 'north-east':
                    i.append('adult-hindi-grp-18')
                elif i[0] == 'north-south':
                    i.append('adult-hindi-grp-19')
                elif i[0] == 'north-west':
                    i.append('adult-hindi-grp-20')

                elif i[0] == 'east-north':
                    i.append('adult-hindi-grp-21')
                elif i[0] == 'east-east':
                    i.append('adult-hindi-grp-22')
                elif i[0] == 'east-south':
                    i.append('adult-hindi-grp-23')
                elif i[0] == 'east-west':
                    i.append('adult-hindi-grp-24')

                elif i[0] == 'south-north':
                    i.append('adult-english-grp-17')
                elif i[0] == 'south-east':
                    i.append('adult-english-grp-18')
                elif i[0] == 'south-south':
                    i.append('adult-english-grp-19')
                elif i[0] == 'south-west':
                    i.append('adult-english-grp-20')

                elif i[0] == 'west-north':
                    i.append('adult-english-grp-21')
                elif i[0] == 'west-east':
                    i.append('adult-english-grp-22')
                elif i[0] == 'west-south':
                    i.append('adult-english-grp-23')
                elif i[0] == 'west-west':
                    i.append('adult-english-grp-24')
    for i in combs:
        s = i[-1]
        if i[2] == 'male':
            i[-1] = 'male-'+s
        else:
            i[-1] = 'female-'+s
    file = open("tdata.txt","a")
    for i in combs:
        for j in i:
            file.write("%s,"%(j))
        file.write("\n")
    return combs
generate_data()

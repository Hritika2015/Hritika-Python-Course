student_data = {'id1':
                {'name':['Tiwsterly'],
                'class':['V'],
                'favourite_color':'Bright Blue & Bright pink mixed'},
                #2
                'id2':
                 {'name':['Rediwe'],
                'class':['V'],
                'favourite_color':''
                ' Sparkley,Dazziling Red '},
                #3
                 'id3':
                  {'name':['Flowerywe'],
                'class':['V'],
                'favourite_color':'Light,soft Pink & Pastel White'},
                #4
                'id4':
                 {'name':['PrinceyFlowed'],
                'class':['V'],
                'favourite_color':'Light,Prince Blue & Little,shining dots of cyan'},


}
result={}
for key,value in student_data.items():
 if value not in result.values():
  result[key]=value
print(result)



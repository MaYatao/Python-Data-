import  json
from countries_codes   import  get_country_code
import  pygal_maps_world.maps   
from  pygal.style  import  RotateStyle   as  RS
from  pygal.style  import  LightColorizedStyle  as  LCS

#将数据加载到一个列表
filename='/home/tao/Desktop/py/data/pouplation/population_data.json'
with   open(filename)  as f:
    pop_data=json.load(f)


#创建一个包含人口数量的字典
cc_population={}
for pop_dict  in pop_data:
    if   pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))
       # print(country_name+":"+str(population))
        code=get_country_code(country_name)

        if  code:
            #print(code+":"+str(population))
            cc_population[code]=population
        #else:
         #   print("Error-"+country_name)

cc_pops_1,cc_pops_2,cc_pops_3={},{},{},
for  cc,pop in  cc_population.items():
    if pop<10000000:
        cc_pops_1[cc]=pop
    elif  pop<1000000000:
        cc_pops_2[cc]=pop
    else:
        cc_pops_3[cc]=pop

#看看每组分别包含多少个国家
#print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))
cd


wm_style=RS('#336699',base_style=LCS)
wm=pygal_maps_world.maps.World(style=wm_style)
wm.title='World  Population  in  2010 ,by Country'
#wm.add('2010',cc_population)
wm.add('0-10m',cc_pops_1)
wm.add('10-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)

wm.render_to_file('world_population.svg')




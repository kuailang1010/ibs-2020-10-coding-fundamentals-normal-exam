fr = open("results.txt","r")
text = fr.readlines()

country_temp = []
n = 0
for line in text:
    
    if n == 0:
        pass
    else:
        country_temp.append(line)
    n += 1 
print(country_temp)

France_list = []
Sweden_list = []
Germany_list = []
year_list = []
data_list = []
for data in country_temp:

    data_list = data.split()
    x = data_list[0]
    France_list.append(x)
    
    y = data_list[1]
    Sweden_list.append(y)
    
    z = data_list[2]
    Germany_list.append(z)

    year = data_list[3]
    year_list.append(year)
    
    data_list = []

min_France = min(France_list)
min_France_index = France_list.index(min_France)

max_France = max(France_list)
max_France_index = France_list.index(max_France)

min_year_France = year_list[min_France_index]
max_year_France = year_list[max_France_index]

min_Sweden = min(Sweden_list)
min_Sweden_index = Sweden_list.index(min_Sweden)

max_Sweden = max(Sweden_list)
max_Sweden_index = Sweden_list.index(max_Sweden)

min_year_Sweden = year_list[min_Sweden_index]
max_year_Sweden = year_list[max_Sweden_index]

min_Germany = min(Germany_list)
min_Germany_index = Germany_list.index(min_Germany)

max_Germany = max(Germany_list)
max_Germany_index = Germany_list.index(max_Germany)

min_year_Germany = year_list[min_Germany_index]
max_year_Germany = year_list[max_Germany_index]

print(f"France => {min_year_France}, {max_year_France}")
print(f"France => {min_year_Sweden}, {max_year_Sweden}")
print(f"France => {min_year_Germany}, {max_year_Germany}")

    



    



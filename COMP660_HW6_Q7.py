import pandas as pd
import re

#df = pd.read_csv('D:\Python Learning\Continuing Education COMP660\Module 6\FamousPeopleList.csv')
#print(df.head(5))

famous_list = ''' \
Marilyn Monroe (1926 – 1962) American actress, singer, model
Abraham Lincoln (1809 – 1865) US President during American civil war
Nelson Mandela (1918 – 2013)  South African President anti-apartheid campaigner
John F. Kennedy (1917 – 1963) US President 1961 – 1963
Martin Luther King (1929 – 1968)  American civil rights campaigner
Queen Elizabeth II (1926 – ) British monarch since 1954
Winston Churchill (1874 – 1965) British Prime Minister during WWII
Donald Trump (1946 – ) Businessman, US President.
Bill Gates (1955 – ) American businessman, founder of Microsoft
Muhammad Ali (1942 – 2016) American Boxer and civil rights campaigner
Mahatma Gandhi (1869 – 1948) Leader of Indian independence movement
Margaret Thatcher (1925 – 2013) British Prime Minister 1979 – 1990
Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun
Christopher Columbus (1451 – 1506) Italian explorer
Charles Darwin (1809 – 1882) British scientist, theory of evolution
Elvis Presley (1935 – 1977) American musician
Albert Einstein (1879 – 1955) German scientist, theory of relativity
Paul McCartney (1942 – ) British musician, member of Beatles
Queen Victoria ( 1819 – 1901) British monarch 1837 – 1901
Pope Francis (1936 – ) First pope from the Americas
Charles Francis (1936 – 1942) Fake entry for testing dupes
'''
famous_list = famous_list.upper()
famous_list = famous_list.replace('(','|')
famous_list = famous_list.replace(')','|')
#Replace carriage return with pipe
famous_list = famous_list.replace('\n','|')
famous_list = famous_list.split('|')

'''So the issue is that some of the people's descriptions have date ranges in them,
 which means we can't split the text by ' - '.
 Below we use three different loops to get every 3rd item in the list, offset by the starting item.
 We end up with three separate dataframes for name, lifespan, and desc. Then we have to merge them.'''

def GetNames(text, n):
    builtstring = ""
    for i in range(0, len(text)):
        if (i + 3) % n == 0:
            # print(text[i])
            builtstring = builtstring + text[i] + '|'
    return builtstring

def GetDates(text, n):
    builtstring = ""
    for i in range(0, len(text)):
        if (i + 2) % n == 0:
            # print(text[i])
            builtstring = builtstring + text[i] + '|'
    return builtstring

def GetDesc(text, n):
    builtstring = ""
    for i in range(2, len(text)):
        if (i + 4) % n == 0:
            # print(text[i])
            builtstring = builtstring + text[i] + '|'
    return builtstring

#Run each function to get an individual list of each parsed column.
#There's probably a more elegant way of doing this.
names = GetNames(famous_list,3).split('|')
dates = GetDates(famous_list,3).split('|')
desc = GetDesc(famous_list,3).split('|')

#Here we're converting each list into a data frame and naming them
#according to the names in the cols_list.
cols_list = ['name', 'lifespan', 'description']
df_names = pd.DataFrame(data = names, columns= [cols_list[0]])
df_lifespan = pd.DataFrame(data = dates, columns= [cols_list[1]])
df_desc = pd.DataFrame(data = desc, columns= [cols_list[2]])

#Here we're 'unioning' columns of each df
df_m = pd.concat([df_names, df_lifespan], axis=1)
df_fp = pd.concat([df_m,df_desc], axis = 1)

#Ways to print single columns
#print(df_fp['lifespan'])
#print(df_fp.name.to_string(index=False))

search_str =input('Enter some comma-separated characteristics to search for. e.g. italian,painter,scientist ')
search_upper = search_str.upper()
search_final =  search_upper.replace(",","|")

search_results = df_fp[df_fp['description'].str.contains(search_final, na=False)]

if search_results.empty:
    print(f"Sorry, there were no hits on your search: {search_str}")
else:
    print(search_results.to_string(index=False))

#If I had more time I would try to figure out how to do this search without converting
#the whole famous list to upper case.


#This is the solution to the 2nd half of the question
text = input('Please Enter the name of the famous individual: ')
#Convert to camel case if needed
text_camel = text.upper()
search_value = df_fp[df_fp['name'].str.contains(text_camel)]

#get_name = search_value.name[0]
#print(get_name)

if search_value.empty:
    print(f"Sorry, {text_camel.title()} did not make the top 20 cut!")
else:
    print(f"Yup, {text_camel.title()} did make the Top 20 cut!")





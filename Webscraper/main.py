# Import required module
import newspaper
import json


num = 1691000
dict1 = {"data":[]}
count=0
 #1691122
while(num<1691004):
# Assign url
    try:
        dict2={} 
        url = 'https://www.dawn.com/news/'+str(num)
        
        # Extract web data
        url_i = newspaper.Article(url="%s" % (url), language='en')
        url_i.download()
        url_i.parse()
        
        # Display scrapped data
        #print(url_i.text)
        #print(url_i.title)
        #print(url)
        #dict1[str(count)]=[url_i.title,url]
        dict2["id"]=str(count)
        dict2["headline"]=url_i.title
        dict2["url"]=url
        dict2["upvote"]=0
        dict2["downvote"]=0
        
        dict1["data"].append(dict2)
        
        count+=1
        
        
    except:
        print("error")
       #pass
    
    
    
    num+=1
    

json.dumps(dict1)
with open("this.json", 'w') as file_object:  #open the file in write mode
 json.dump(dict1, file_object)   # json.dump() function to stores the set of numbers in numbers.json file
    



        
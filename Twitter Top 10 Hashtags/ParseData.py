import json
from collections import defaultdict
from operator import itemgetter
import collections

#-----------------------------------------------------------------------------------------------------------------------
# Read in JSON file (collected tweets) then put them all in original_tweets list
original_tweets = []
original_file = open("TwitterData.json","r")
for line in original_file:
    try:
        data = json.loads(line)
        original_tweets.append(data)

    except Exception as ex:
        continue

#print(json.dumps(original_tweets[0]))

#-----------------------------------------------------------------------------------------------------------------------
# Collect "text" part of each tweets & Store them in text_value_list
text_value_list = []

origin_idx = 0
for origin_idx in range(len(original_tweets)):
    for key, text_value in original_tweets[origin_idx].items():
        if key == "text":
            text_value_list.append(text_value)
        if "text" not in original_tweets[origin_idx]:
            text_value_list.append("None")

#print "Text---" + str(len(text_value_list))
#print((text_value_list[46]))

#-----------------------------------------------------------------------------------------------------------------------
# Pickout hashtags from text & Count occurances of each hashtags
# For Finding hashtags in each tweet
hashtagsCount = []
for t in range(len(text_value_list)):
        result = defaultdict(int)
        for i in filter(lambda x:x[0]=='#', text_value_list[t].split()):
            result[i] += 1
            #print len(i)
            #print filter(lambda x:x[0]=='#', text_value_list[t].split())
        hashtagsCount.append(dict(result))
#print hashtagsCount
#print len(hashtagsCount)
#-----------------------------------------------------------------------------------------------------------------------
# Map all the hashtags to a dictionary map_result & Sort in descending order by value
# For Finding Top 10 Hashtags of all collected tweets
map_result = {}
sort_map_result = {}
no_hash = {"None": 0}
none_count = 0

for tagvalue in hashtagsCount:
    for tagkey in tagvalue.keys():
        map_result[tagkey] = map_result.get(tagkey,0)+tagvalue[tagkey]
    if(len(tagvalue)== 0):
        none_count += 1

#Sort numbers of hashtags (OrderedDict type)
sort_map_result = collections.OrderedDict(sorted(map_result.items(), key=itemgetter(1), reverse=True))

#print(map_result)
#print(sort_map_result)

#-----------------------------------------------------------------------------------------------------------------------
# Put the top ten hashtags in list "top_ten_hashtags_list"
top_ten_result = collections.OrderedDict({})
top_ten_hashtags_list = []
count = 0

#for topkey, topvalue in sort_map_result.items():
for topkey, topvalue in sort_map_result.iteritems():
    if count < 10:
        top_ten_result[topkey] = topvalue
        top_ten_hashtags_list.append(topkey.encode('utf-8'))
        count += 1

#print top_ten_hashtags_list

#-----------------------------------------------------------------------------------------------------------------------
# Parse tweets containing top 10 hashtags into its categories - top 10, other hashtags & no hashtags
top1 = []
top2 = []
top3 = []
top4 = []
top5 = []
top6 = []
top7 = []
top8 = []
top9 = []
top10 = []
others_hashtag_tweets = []  # Tweets Contain Hashtags > 1
None_hashtag_tweets = []    # Tweets with No Hashtags

idx_num = 0
for idx_num in range(len(text_value_list)):
    if top_ten_hashtags_list[0] in text_value_list[idx_num].encode('utf8'):
        top1.append(original_tweets[idx_num])
    elif top_ten_hashtags_list[1] in text_value_list[idx_num].encode('utf8'):
        top2.append(original_tweets[idx_num])
    elif top_ten_hashtags_list[2] in text_value_list[idx_num].encode('utf8'):
        top3.append(original_tweets[idx_num])
    elif top_ten_hashtags_list[3] in text_value_list[idx_num].encode('utf8'):
        top4.append(original_tweets[idx_num])
    elif top_ten_hashtags_list[4] in text_value_list[idx_num].encode('utf8'):
        top5.append(original_tweets[idx_num])
    elif top_ten_hashtags_list[5] in text_value_list[idx_num].encode('utf8'):
        top6.append(original_tweets[idx_num])
    elif top_ten_hashtags_list[6] in text_value_list[idx_num].encode('utf8'):
        top7.append(original_tweets[idx_num])
    elif top_ten_hashtags_list[7] in text_value_list[idx_num].encode('utf8'):
        top8.append(original_tweets[idx_num])
    elif top_ten_hashtags_list[8] in text_value_list[idx_num].encode('utf8'):
        top9.append(original_tweets[idx_num])
    elif top_ten_hashtags_list[9] in text_value_list[idx_num].encode('utf8'):
        top10.append(original_tweets[idx_num])
    elif len(filter(lambda x:x[0]=='#', text_value_list[idx_num].split())) > 1:
        others_hashtag_tweets.append(original_tweets[idx_num])
    else:
        None_hashtag_tweets.append(original_tweets[idx_num])

#-----------------------------------------------------------------------------------------------------------------------
#Checking total tweets before and after analyzing/parsing
print "Orignial total tweeets # --- "+ str(len(original_tweets))
print "\n"+"[ Final Result ]"+"\n"+"======================================================"
print "Top Ten:             "+str(len(top1)+len(top2)+len(top3)+len(top4)+len(top5)+len(top6)+len(top7)+len(top8)+len(top9)+len(top10))
print "Other hashtags:       "+str(len(others_hashtag_tweets))
print "None Hashtags:      "+str(len(None_hashtag_tweets))

print "Total Tweets # ---  "+str(len(top1)+len(top2)+len(top3)+len(top4)+len(top5)+len(top6)+len(top7)+len(top8)+len(top9)+len(top10)+len(others_hashtag_tweets)+len(None_hashtag_tweets))

# Output top 10 hashtags in order to a JSON file
#with open('outfile.json','w') as file:
#    json.dump(top_ten_result, file)

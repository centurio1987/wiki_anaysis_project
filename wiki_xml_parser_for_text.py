
# coding: utf-8

# In[2]:

from xml.etree.ElementTree import parse, ElementTree


# In[3]:

tree = parse("/Users/KYD/Documents/wiki_project/kowiki-20151226-pages-articles-multistream.xml")


# In[4]:

root = tree.getroot()


# In[7]:

page_tag = root.find('{http://www.mediawiki.org/xml/export-0.10/}page')


# In[10]:

revision_tag = page_tag.find('{http://www.mediawiki.org/xml/export-0.10/}revision')


# In[14]:

text_tag = revision_tag.find('{http://www.mediawiki.org/xml/export-0.10/}text')


# In[19]:

output_path = "/Users/KYD/Documents/wiki_project/seperated_xml"


# In[20]:

ElementTree(text_tag).write(output_path + "/text.xml", encoding="utf-8", xml_declaration=True)


# # 일단 지금은 아래 부분 필요 없음

# In[ ]:

for i, page in enumarate(page_tags):
    if i > 10:
        break
    ElementTree(text_tag).write(output_path + "/page"+i+".xml", encoding="utf-8", xml_declaration=True)


# In[ ]:




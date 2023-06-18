To implement the uniqueness of the items, here is a step-by-step breakdown:
  
1. generate the unique id and color feature
  We use timestamp + 1~100000 random number to generate a unique item id
```python
def generate_id():
  timestamp = int(time.time() * 1000) 
  random_num = random.randint(1, 100000) 
  unique_id = str(timestamp) + str(random_num) 
  return unique_id
```  
  In order to make it discrete enough, the color feature is more random and as unique as possible, the id is hashed.
  Based on these, we initialize a simple tree picture,  just for demo. In the complete product, this part will be omitted, and the items of the same template will be processed by random color through the edge detection technique described later.
  the generation of the name of each item, we also initialize a simple adjective and name database, when the item is drawn, the name will be simultaneously and randomly generated.
  
  for the demo, we generated two items. Although there is only one type of item, it is mainly to illustrate the random generation of colors and nicknames.

![image](https://github.com/Ja5onYang/forecarest-GoodG4m3/assets/135325526/da611a84-2531-4b98-a196-5b8fcc06c71d)
![image](https://github.com/Ja5onYang/forecarest-GoodG4m3/assets/135325526/6c0179d5-ab95-4d78-ac42-6d305113d26f)

  Also, the corresponding information will be stored in order to call it anytime.
![image](https://github.com/Ja5onYang/forecarest-GoodG4m3/assets/135325526/0581bbcc-7d66-4a58-a5c7-4e378d93b37e)
![image](https://github.com/Ja5onYang/forecarest-GoodG4m3/assets/135325526/2350256e-9a11-44bd-a6e2-f416198b1e7b)

2. edge detection/segmentation

   we use python to make it possible to identify the contour of the item. Theoretically, by segmenting the shape, we can do the processing mentioned above.
   Here is an example:

![image](https://github.com/Ja5onYang/forecarest-GoodG4m3/assets/135325526/b2e743be-64be-4c75-9a54-ab4d867eabfd)


![image](https://github.com/Ja5onYang/forecarest-GoodG4m3/assets/135325526/c3ae984c-e561-43ef-b018-d5a97b6f72ae)

![image](https://github.com/Ja5onYang/forecarest-GoodG4m3/assets/135325526/3d8033fa-ec5a-4491-850e-8547bfa84588)

3. generate a little story

   The ability of python can still make it. we import openai to generate an interesting story. Through some training samples, AI can automatically writes a short profile. We didn't actually implement this part, in theory it should work.

Limitations and Future Enhancements:
  1. The requirement of openai's API is very important, we have to have this to make it for the part of generating a litter story, instead of generating from the database, which is a little bit boring. Besides, in order to enrich the profile for each item, in the complete product, we will not constantly use the training samples like "this guy" in the code of 'little story'. We will consider appending like "this little girl" or "this boy", which requires further processing of the gender corresponding to the name in order to feedback the correct personal pronoun. (of course, users can customize the pronouns)
  2. The edge detection is for the whole contour (the whole tree), so the random change to the items may not be ideal, so we still need to look for more advanced models or algorithms.
  3.  When the number of our customers becomes huge, the solution that timestamp + random number may not be so appropriate, we need other complex and better solutions to make it as unique as possible.

reference:
  the code of edge detection is found in Yiyan ZENG's blog, we really appreciate to his excellent work.
  the original link: https://zhuanlan.zhihu.com/p/38739563


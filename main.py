from src.offlinedocs.scraper.fetcher import Fetcher
from bs4 import BeautifulSoup
import asyncio
import json

class Parser:
    
    async def parsing(self,url:str):
        fetch_obj = Fetcher()

        html = await fetch_obj.fetch(url)

        soup = BeautifulSoup(html, "lxml")
        
        for tag in soup(["header", "footer", "nav", "aside", "script", "style"]):
            tag.decompose()
        ParsedContent = soup.find("div", class_="ArticlePagePostLayout_containerFluid__q38gg")
        # for div in soup.find_all("div"):
        #     class_list = div.get("class")
        #     if class_list:
        #         for classes in class_list:
        #             if "article--viewer" in classes.lower():
        #                 ParsedTextContent = div
        #                 break
        #             else:
        #                 print("not found")
        # for div in soup.find_all("div"):
        #     classes = div.get("class")
        #     if classes and any("article" in cls.lower() for cls in classes):
        #         ParsedContent = div
        #         break
                
        ParsedTextContent = soup.get_text()
        

        await fetch_obj.close()
        return ParsedContent , soup
    # there is only two ways , one , include , exclude
    
    
    
    # def Data_handeling(self,ParsedContent):
       
    #     structured_content = []
       
       
        
    #     for element in ParsedContent.childere:
    #      if element.name is None:
    #          continue
    #      if element.name == "h1":
    #          print(element.name)
    #          #im going to save all this into a structted format with the json module so it saves docs , 
    #          structured_content.append(
    #              {"type":"h1" , "text" : element.get_text(strip=True)}
    #          )
    #      elif element.name == "h2":
    #          structured_content.append(
    #          {"type":"h2" , "text" : element.get_text(strip=True)}
    #          )
    #      elif element.name == "h3":
    #          structured_content.append(
    #          {"type":"h3" , "text" : element.get_text(strip=True)}
    #          )
    #      elif element.name == "h4":
    #          structured_content.append(
    #         {"type":"h4" , "text" : element.get_text(strip=True)}
    #          )
    #      elif element.name == "p":
    #          structured_content.append(
    #          {"type":"p" , "text" : element.get_text(strip=True)}
    #          )
    #     #  elif element.name == "h2":
    #     #      {"type":"h2" , "text" : element.get_text(strip=True)}
             
             
             
    #     return structured_content
    def Data_handeling(self, ParsedContent):
     structured_content = []
     heading_tags = {"h1", "h2", "h3", "h4", "p"}

     # Check if ParsedContent exists
     if ParsedContent is None:
         print("Error: ParsedContent is None. The div was not found.")
         return structured_content
     # there needs to be a proccess in which we detect blockqouotes and name it code 
     # Use find_all() to get ALL nested elements (not just direct children)
     for element in ParsedContent.find_all(heading_tags):
         text = element.get_text(strip=True)
         if text:  # Only add if there's actual text
             structured_content.append({
                 "type": element.name,
                 "text": text
             })

     return structured_content
       
    
    
    
    def Structual_Writing(self , structured_content , file_name ):
        data = {
            "content": structured_content
        }
        with open(file_name , "w" ,encoding="utf-8") as f:
            json.dump(data , f , indent=4 , ensure_ascii=False)
        # Destroy this after making sure everything works
        print("filed saved ")
        
        
        
    
async def main():
    parser = Parser()
    ParsedContent , soup = await parser.parsing("https://www.geeksforgeeks.org/python/python-data-types/")
        # Step 2: Handle / structure data
    structured_data = parser.Data_handeling(ParsedContent)

    # Step 3: Save as JSON (or extend to Markdown / Rich)
    parser.Structual_Writing(structured_data , "test.json")




asyncio.run(main(),debug=True)
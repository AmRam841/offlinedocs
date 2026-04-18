from ..Fetcher.fetcher import Fetcher
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
        
                
        ParsedTextContent = soup.get_text()
        

        await fetch_obj.close()
        return ParsedContent , soup
    # there is only two ways , one , include , exclude

    def Data_handeling(self, ParsedContent):
     structured_content = []
     heading_tags = {"h1", "h2", "h3", "h4", "p", "pre"}

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
        
        
        
    
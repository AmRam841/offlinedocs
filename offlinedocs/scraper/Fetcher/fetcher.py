# #Responsible only for:
# # Making HTTP requests -> 
# # Handling retries
# # Handling timeouts
# # Handling rate limiting
# # Setting headers
# # Must support:
# # Custom User-Agent
# # Retry with exponential backoff
# # Timeout protection
# # You should implement:
# # 3 retry attempts
# # Backoff: 1s → 2s → 4s
# # Detect 429 (Too Many Requests)
# # This teaches:
# # Networking reliability
# # Production-level HTTP handlin
# from bs4 import BeautifulSoup
# from bs4.element import Comment
# import urllib.request

# def tag_visible(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True


# def text_from_html(body):
#     soup = BeautifulSoup(body, 'html.parser')
#     texts = soup.findAll(text=True)
#     visible_texts = filter(tag_visible, texts)  
#     return u" ".join(t.strip() for t in visible_texts)

# html = urllib.request.urlopen('https://www.geeksforgeeks.org/dsa/analysis-algorithms-big-o-analysis/').read()
# print(text_from_html(html))

#Real code 
import httpx
import httpx_retries as hretry
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)   



class Fetcher:
    """
    a function for async fethcing 
    """
    def __init__(self):
        retry = hretry.Retry(total=5, backoff_factor=0.5)
        transport = hretry.RetryTransport(retry=retry)
    
        
        

        self.client = httpx.AsyncClient(
            timeout=10.0,
            follow_redirects=True,
            transport=transport,
            headers={
                "User-Agent": "MyCrawler/1.0"
            },
            limits= httpx.Limits(
                max_connections=100,
                max_keepalive_connections=20
            )
        )

    async def fetch(self, url: str):
         
        
        try:
            response = await self.client.get(url)
            
            response.raise_for_status()
            if response.status_code == 429:
                logger.warning(f"rate limited on {url}")
                
            return response.text

        except httpx.HTTPError as exc:
            
            logger.info(f"HTTP error for {url}: {exc}")
            raise
        # except httpx.Request as execreq:
        #     logger.info(f"Request err {execreq}")
        #     raise
        # except httpx.TransportError as execTranspoert:
        #     logger.info(f"Trasnport err : {execTranspoert}")
        #     raise
        # except httpx.NetworkError as execNetwork:
        #     logger.info(f"network err : {execNetwork}")
        #     raise

    async def close(self):
        await self.client.aclose()































































































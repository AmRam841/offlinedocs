import asyncio
from scraper.Parser.parser import Parser
async def main():
    parser = Parser()
    ParsedContent , soup = await parser.parsing("https://www.geeksforgeeks.org/python/python-data-types/")
        # Step 2: Handle / structure data
    structured_data = parser.Data_handeling(ParsedContent)

    # Step 3: Save as JSON (or extend to Markdown / Rich)
    parser.Structual_Writing(structured_data , "test.json")




asyncio.run(main(),debug=True)
# block game bot

[![license](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![pypi](https://img.shields.io/pypi/v/lilyweight?style=for-the-badge)](https://pypi.org/project/lilyweight/)

block game bot api Wrapper

## Information

Written without any external libraries other than `aiohttp` which is used to fetch data from the block game bot API.

This requires a block game bot API key. You may obtain one by joining [this](https://discord.gg/fruffy) Discord and messaging me (asov#0187).

## Credits
- [asov](https://github.com/noemtdev/) - Maker of Scammer List
- [timnoot](https://github.com/timnoot) - Helped me a lot in general


## Usage

```py
import asyncio

from blockgamebot.api import Scammers, itemImages

scammers = Scammers("BLOCKGAMEBOT_API_KEY")
images = itemImages()

async def main():

    # Get all scammers
    all_scammers = await scammers.get_all()
    print(all_scammers)

    # Lookup a scammer
    scammer = await scammers.lookup("asov")
    print(scammer)

    # Get an item image
    url = await images.get_image("bread", variation="enchanted") 
    # variation defaults to "normal" but it can also be "enchanted"

    print(url)


asyncio.run(main())
```

## API
If you don't want to use the Wrapper you can use the [API](https://api.nom-nom.link/).

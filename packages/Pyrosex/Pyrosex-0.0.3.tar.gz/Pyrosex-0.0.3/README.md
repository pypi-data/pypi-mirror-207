<p align="center">
    <a href="https://github.com/OTHFamily/pyrosex">
        <img src="https://docs.pyrosex.org/_static/pyrogram.png" alt="Pyrosex" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://pyrosex.org">
        Homepage
    </a>
    •
    <a href="https://docs.pyrosex.org">
        Documentation
    </a>
    •
    <a href="https://docs.pyrosex.org/releases">
        Releases
    </a>
    •
    <a href="https://t.me/OnTheHerd">
        News
    </a>
</p>

## Pyrosex

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

``` python
from pyrosex import Client, filters

app = Client("my_account")


@app.on_msg(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrosex!")


app.run()
```

**Pyrosex** is a modern, elegant and asynchronous [MTProto API](https://docs.pyrosex.org/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

### Support

If you'd like to support Pyrosex, you can consider:

- [Become a GitHub sponsor](https://github.com/sponsors/OTHFamily).
- [Become a LiberaPay patron](https://liberapay.com/OTHFamily).
- [Become an OpenCollective backer](https://opencollective.com/pyrosex).

### Installing

``` bash
pip3 install pyrosex
```

### Resources

- Check out the docs at https://docs.pyrosex.org to learn more about Pyrosex, get started right
away and discover more in-depth material for building your client applications.
- Join the official channel at https://t.me/OnTheHerd and stay tuned for news, updates and announcements.

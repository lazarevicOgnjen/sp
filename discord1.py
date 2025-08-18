import os
from dhooks import Webhook, Embed


WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN1')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[SP glavna stranica je azurirana - click here -](https://cs.elfak.ni.ac.rs/nastava/course/view.php?id=9)**",
        color=0x3498DB
    )

    hook.send("@everyone 📢 SP", embed=embed)

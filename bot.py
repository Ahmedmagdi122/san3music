from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "simo",
    api_id=29621516,
    api_hash="fa21d1a59b76b215cb366771255a13bf",
    bot_token="7335504991:AAHuIAqWGeFjtk6qe1TV5QQ8K-2XtHfxj4g",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    R_R_B0 = "R_R_B0"
    await bot.send_message(WT_F33, "** فشغيل الصانع عزيزي ديلر. **")
    print("[INFO]: ديــلــر قلبايي")
    await idle()

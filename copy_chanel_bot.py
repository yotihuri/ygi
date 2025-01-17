from telethon import TelegramClient, events, types

# API ID dan API Hash dari https://my.telegram.org/auth
API_ID = 23550680
API_HASH = "fd5a5f3981cb75f0f828a8b4eaa5f4ec"

# Nama file sesi (untuk menyimpan login Telegram)
SESSION_NAME = "copy_channel_bot"

# Channel sumber (tempat pesan berasal) dan channel tujuan (channel Anda)
SOURCE_CHANNEL = "https://t.me/OMNItech_koth"  # Ganti dengan username atau link channel sumber
TARGET_CHANNEL = "https://t.me/Antinuclearr"  # Ganti dengan username atau link channel tujuan

# Inisialisasi klien Telethon
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def copy_message(event):
    try:
        # Ambil teks dari pesan
        message_text = event.message.text or ""
        
        # Periksa apakah pesan memiliki tautan
        if "http" in message_text:
            # Kirim teks ke target channel tanpa gambar atau media
            await client.send_message(
                TARGET_CHANNEL,
                message=message_text,
            )
            print("Pesan teks dengan tautan berhasil disalin!")
        else:
            print("Pesan tidak memiliki tautan penting, diabaikan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyalin pesan: {e}")

# Menjalankan bot
print("Bot sedang berjalan...")
with client:
    client.run_until_disconnected()

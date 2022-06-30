if message.text.lower().startswith('https://www.tiktok.com/') or message.text.lower().startswith('https://vt.tiktok.com/') or message.text.lower().startswith('https://tiktok.com/') \
                            or message.text.lower().startswith('https://vm.tiktok.com/'):
                            await tiktok(message,os.getenv('THOST'),os.getenv('KEY'),os.getenv('TURL'))
                            break
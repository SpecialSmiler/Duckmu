import asyncio
from bilibili_api import live, sync
import json

room = live.LiveDanmaku(5050)


@room.on('DANMU_MSG')
async def on_danmuku(event):
    username = event["data"]["info"][2][1]
    content = event["data"]["info"][1]
    print('{0} : {1}'.format(username, content))


# @room.on('SEND_GIFT')
# async def on_gift(event):
#     print(event)

sync(room.connect())

# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())

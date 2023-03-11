from flask import Flask, request, jsonify
import json
import aiohttp
import asyncio
import time
import os
import boto3
import imghdr
import glob
from PIL import Image
from u2net_test import U2Net

TEMPFOLDER = os.path.join("temp", "")
IMG_THRESHOLD = 1200
U2NET = U2Net()

client = boto3.client(
    's3',
    aws_access_key_id='ASIAVHKGZ4RPXDIIGFUN',
    aws_secret_access_key='W+J2De6pCq4RuIT5x30hrwKj49hE5HygPqEMbWtE',
    aws_session_token='IQoJb3JpZ2luX2VjEMz//////////wEaCXVzLWVhc3QtMSJHMEUCIFLIOgV/ImI0y3FYZ/xNP+LXZjVQhltlny78/Z+L8GNJAiEAg8l3lA8yh706j5Krw3N4nNhzyTlyo4FvM0YVRY65IXAqoAIIhf//////////ARAAGgwzNTkzMTUxMzc2MzEiDNKTPYxpWIJFg+F8lSr0Aba5srtRkO9OesxbsDzJ8AKl3JU6cyIvLjCdIts/ghtz+MTvcRkwixXgkfvSA4Q3UNlM0amhwCsXIqdxH2fz/6rLdeHVnJJgmMHApPzTAgXqY4XxLwDWemibbCrJ6bIHRowJ2sGuiKip6LV7Bp03hIiHwvMO5xTYPgKW3Lnnk1u1k0ookVHjDqlGV+aOwJD6VQ3EzJSpUpFvFr3uJAuYy31poIoovObuiIZ7mxm0Ae/PnJl7z3LXbnzBkD5F0KbWC90jOFAP8NcClpJVMMkth9e1SBqu+pcDtjmnB0WyD0RWKqmi3lmA3O1QOQFoTDHpH+kfIDkw9vKvoAY6nQGsSEVX6CnKX17aoOU274ZBPuI3l/YRY2onXwTSY+UXjhDuoxpMk5G8jsSaebQ8ftzguuukeX1MBnuttRpyCNI5emuZJ+JcIagXBfXa0nnx7PSY29CL83iR9x6balc2iBQPJk/5o/kSaIboAhY8nRVr6lWYtGW7rc7YI0UxS94CNGJlWSPTcjGDLLu6/lS9vGw0J5VYxXMyqvkkSHO+'
)
app = Flask(__name__)

@app.route("/test", methods=["GET", "POST"])
def test():
    return {"message": "backend is working"}

'''
{
    "value":[
        {contentUrl...},
        {contentUrl...}
    ]
}
'''
@app.route("/", methods=["POST"])
def matt():
    data = json.loads(request.data.decode("gbk"), strict=False)
    data = data.get('value')
    if len(data) == 0:
        return jsonify({
            "result": "fail",
            "message": "List is Empty"
        })
    timestamp = time.time()
    path = os.path.join(TEMPFOLDER, str(timestamp), "")
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        return jsonify({
            "result": "fail",
            "message": "Temp Folder Exists"
        })
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(downImgs(loop, data, path))
    loop.close()
    print("DOWNLOAD OKAY")
    checkValidity(path)
    print("VALIDITY CHECKED")
    return U2Net.matt_model(path)

def checkValidity(path):
    checklst = glob.glob(path+os.sep+"*")
    for i in checklst:
        if imghdr.what(i) is None:
            os.remove(i)
        im = Image.open(i)
        (x,y) = im.size
        if x>IMG_THRESHOLD or y>IMG_THRESHOLD:
            if x>y:
                x_s = IMG_THRESHOLD
                y_s = int(y*x_s/x)
                im = im.resize((x_s, y_s))
                im.save(i)
            else:
                y_s = IMG_THRESHOLD
                x_s = int(x*y_s/y)
                im = im.resize((x_s, y_s))
                im.save(i)


async def downImgs(loop: asyncio.get_event_loop, data, path): #DOWNLOADER ASYNC CONCURRENT
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(downImg(session, path, data[_])) for _ in range(len(data))]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]
        print("ALLRESULTS:",all_results)

async def downImg(session, path, i): #DOWNLOADER WORKER
    filename = str(i.get('imageId'))+str(os.path.splitext(i.get('contentUrl'))[-1])
    file = await session.get(i.get('contentUrl'))
    filecode = await file.read()
    with open(os.path.join(path, filename), 'wb') as f:
        f.write(filecode)

app.run(debug=True, port=8090)
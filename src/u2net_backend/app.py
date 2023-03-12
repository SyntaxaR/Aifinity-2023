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
    data = request.data
    print(data)
    data = json.loads(data, encoding='gbk', strict=False)
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
    print("START DOWNLOADING")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(asyncio.wait_for(downImgs(loop, data, path), 10))
    except asyncio.TimeoutError:
        print("Timeout, skipping")
    loop.close()
    print("DOWNLOAD OKAY")
    checkValidity(path)
    print("VALIDITY CHECKED")
    r = U2NET.matt_model(path)
    return jsonify({"result": r})

def checkValidity(path):
    checklst = glob.glob(path+os.sep+"*")
    for i in checklst:
        if imghdr.what(i) is None:
            os.remove(i)
            continue
        im = Image.open(i)
        (x,y) = im.size
        if x>IMG_THRESHOLD or y>IMG_THRESHOLD:
            if x>y:
                x_s = IMG_THRESHOLD
                y_s = int(y*x_s/x)
                im = im.resize((x_s, y_s))
            else:
                y_s = IMG_THRESHOLD
                x_s = int(x*y_s/y)
                im = im.resize((x_s, y_s))
        print(os.path.splitext(i)[0]+"."+imghdr.what(i))
        im.save(os.path.splitext(i)[0]+".png", "PNG")
        os.remove(i)


async def downImgs(loop: asyncio.get_event_loop, data, path): #DOWNLOADER ASYNC CONCURRENT
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(downImg(session, path, data[_])) for _ in range(len(data))]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]
        print("ALLRESULTS:",all_results)

async def downImg(session, path, i): #DOWNLOADER WORKER
    try:
        filename = str(i.get('imageId'))+str(os.path.splitext(i.get('contentUrl'))[-1])
        file = await session.get(i.get('contentUrl'))
        filecode = await file.read()
        with open(os.path.join(path, filename), 'wb') as f:
            f.write(filecode)
    except BaseException as err:
        print("Error", str(err))

app.run(host='0.0.0.0', debug=True, port=8090)

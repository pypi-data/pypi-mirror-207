import os
from fastapi import FastAPI
import uvicorn
from fastapi.responses import FileResponse
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastmodel.backend.domain.dto.req_classes import SdInpaintReqDto, SdGenerateReqDto
from fastmodel.backend.util.str_util import safe_join, generate_random_string
from fastmodel.backend.inference.inference import inference_sd_inpaint, inference_sd_generate
from fastmodel.backend.util.img_util import img_base64_to_file
from fastmodel.backend.constant.biz_constants import app_abs_path
import argparse

base_dir = app_abs_path()  # 获取当前脚本所在的目录
print(base_dir)
static_resource_dir = os.path.join(base_dir, "frontend/edit-anything")  # 静态文件所在的目录
CSS_PATH_LIB = f"{static_resource_dir}/assets/css"
IMG_PATH_LIB = f"{static_resource_dir}/assets/img"
JS_PATH_LIB = f"{static_resource_dir}/js"
OUT_IMG_PATH_LIB = f"{base_dir}/frontend/edit-anything/tmp/img/out"

app = FastAPI()
app.mount("/static", StaticFiles(directory=static_resource_dir), name="static")


@app.get("/", response_class=HTMLResponse)
@app.get("/home", response_class=HTMLResponse)
async def server():
    return FileResponse(f"{static_resource_dir}/index.html")


@app.get("/assets/css/{path:path}")
async def build_resource(path: str):
    build_file = safe_join(CSS_PATH_LIB, path)
    return FileResponse(build_file)


@app.get("/js/{path:path}")
async def build_resource(path: str):
    js_file = safe_join(JS_PATH_LIB, path)
    return FileResponse(js_file)


@app.post("/gw/edit-anything/api/v1/bff/sd/inpaint")
async def sd_inpaint(body: SdInpaintReqDto):
    image_base64 = body.image
    mask_base64 = body.mask
    image = img_base64_to_file(image_base64, generate_random_string(6))
    mask = img_base64_to_file(mask_base64, generate_random_string(6))
    prompt = body.prompt
    args = parse_args()
    device = args.device
    inpaint_img_path = inference_sd_inpaint(image, mask, prompt, device, generate_random_string(7))

    return {
        "msg": "ok",
        "msgCode": "10000",
        "success": True,
        "total": 1,
        "data": {
            "imgBase64": None,
            "imgUrl": inpaint_img_path
        }
    }


@app.post('/gw/edit-anything/api/v1/bff/sd/generate')
async def sd_generate(body: SdGenerateReqDto):
    prompt = body.prompt
    width = body.width
    height = body.height
    args = parse_args()
    device = args.device
    generate_img_path = inference_sd_generate(prompt, width, height, device, generate_random_string(9))
    return {
        "msg": "ok",
        "msgCode": "10000",
        "success": True,
        "total": 1,
        "data": {
            "imgBase64": None,
            "imgUrl": generate_img_path
        }
    }


@app.get("/favicon.ico")
async def favicon():
    ico_file = safe_join(IMG_PATH_LIB, 'favicon.ico')
    return FileResponse(ico_file)


@app.get("/{path:path}")
async def img_outputs(path: str):
    img_file = safe_join(OUT_IMG_PATH_LIB, path)
    return FileResponse(img_file)


def parse_args():
    parser = argparse.ArgumentParser(description='Light Up Your Imagination From Edit-Anything')
    parser.add_argument(
        '-H',
        '--host',
        type=str,
        required=False,
        default='0.0.0.0',
        help='web server url, default=0.0.0.0'
    )
    parser.add_argument(
        '-P',
        '--port',
        type=int,
        required=False,
        default=9911,
        help='web server port, default=9911'
    )
    parser.add_argument(
        '-D',
        '--device',
        type=str,
        required=False,
        default='cpu',
        help='device type: cpu or cuda'
    )
    return parser.parse_args()


# init:
# 1. create tmp dirs to store temp files
def init():
    to_create_dirs = [
        f'{base_dir}/tmp/img/in',
        f'{base_dir}/tmp/img/out'
    ]
    for item in to_create_dirs:
        if not os.path.exists(item):
            os.makedirs(item)


def main():
    init()
    args = parse_args()
    uvicorn.run(app, host=args.host, port=args.port, timeout_keep_alive=600)


if __name__ == "__main__":
    main()

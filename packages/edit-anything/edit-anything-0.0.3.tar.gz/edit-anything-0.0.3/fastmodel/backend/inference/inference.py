import numpy as np
from diffusers import StableDiffusionInpaintPipeline
import torch
from fastmodel.backend.util.img_util import img_preprocess_sd_inpaint
from PIL import Image
from fastmodel.backend.constant.biz_constants import app_abs_path


def inference_sd_inpaint(image: str, mask: str, prompt: str, device: str, out_img: str):
    print(image, mask, prompt)
    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-inpainting",
        torch_dtype=torch.float,
    )
    pipe.to(device)
    #image and mask_image should be PIL images.
    #The mask structure is white for inpainting and black for keeping as s
    ori_img, mask_img, o_w, o_h = img_preprocess_sd_inpaint(
        image,
        mask
    )
    print(o_w,o_h)
    image = pipe(prompt=prompt, image=ori_img, mask_image=mask_img).images[0]
    image = np.array(image)
    image = Image.fromarray(image)
    image = image.resize((o_w, o_h))
    base_path = app_abs_path()
    out_img_path = f'{base_path}/frontend/edit-anything/tmp/img/out/{out_img}.png'
    image.save(out_img_path)

    return f'{out_img}.png'

if __name__ == '__main__':
    pass

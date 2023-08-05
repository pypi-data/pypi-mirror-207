import numpy as np
from PIL import Image
import base64
from io import BytesIO
from fastmodel.backend.constant.biz_constants import app_abs_path


def img_base64_to_file(img_base64: str, img_name: str):
    img_decode_data = base64.b64decode(img_base64.split(",")[1])
    img = Image.open(BytesIO(img_decode_data))
    base_path = app_abs_path()
    img_path = f'{base_path}/frontend/edit-anything/tmp/img/in/{img_name}.png'
    img.save(img_path)
    return img_path


def img_preprocess_sd_inpaint(img_path: str, mask_path: str):
    ori_img = Image.open(img_path)
    if ori_img is None:
        print(f'failed to load origin image: {img_path}')
        return
    o_w, o_h = ori_img.size

    mask_img = Image.open(mask_path)
    if mask_img is None:
        print(f'failed to load origin image: {mask_path}')
        return
    m_w, m_h = mask_img.size

    assert (o_w, o_h) == (m_w, m_h), \
        f'shape of the origin image and its mask image should be in same ' \
        f'shape, but got {(o_w, o_h)} vs {(m_w, m_h)}'

    # resize image and its mask to target shape (512, 512)
    if o_w != 512 or o_h != 512:
        ori_img = ori_img.resize((512, 512))
        mask_img = mask_img.resize((512, 512))

    # convert to RGB if image's format is RGBA
    if ori_img.mode == 'RGBA':
        rgb_image = Image.new('RGB', ori_img.size, (255, 255, 255))
        rgb_image.paste(ori_img, mask=ori_img.split()[3])
        ori_img = rgb_image

    ori_img = np.array(ori_img)

    # convert mask_img to grayscale
    mask_img = mask_img.convert('L')
    # make mask binary
    mask_img = np.array(mask_img)
    mask_img[mask_img < 128] = 0
    mask_img[mask_img > 128] = 255
    return Image.fromarray(ori_img), Image.fromarray(mask_img), o_w, o_h


if __name__ == '__main__':
    # # img_base64 = ''
    # # img_base64_to_file(img_base64=img_base64)
    # org_img_path = '/tmp/img/ori_img.png'
    # mask_img_path = '/tmp/img/mask_img.png'
    # ori_img, mask_img = img_preprocess_sd_inpaint(org_img_path, mask_img_path)
    # print(ori_img, mask_img)
    pass

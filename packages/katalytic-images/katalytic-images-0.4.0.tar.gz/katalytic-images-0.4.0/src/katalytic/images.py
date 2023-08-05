from pathlib import Path

import cv2
from cv2 import (
    imwrite as __cv2_imwrite,
    cvtColor as __cv2_cvtColor
)

import numpy as np
from numpy import (
    array as __np_array,
    ndarray as __np_ndarray
)

import PIL.Image
__PIL_Image_open = PIL.Image.open
__PIL_Image_Image = PIL.Image.Image

from katalytic.data.checks import is_iterable, is_number, is_sequence
from katalytic.pkg import get_version, mark

__version__, __version_info__ = get_version(__name__)


def bhwc(arr):
    if arr.shape == (0,):
        return (0, 0, 0, 0)
    elif arr.ndim == 1:
        return (1, *arr.shape, 1, 1)
    elif arr.ndim == 2:
        return (1, *arr.shape, 1)
    elif arr.ndim == 3:
        return (1, *arr.shape)
    elif arr.ndim == 4:
        return arr.shape
    else:
        raise ValueError(f'arr.ndim = {arr.ndim}')


def convert_image(image, before, after):
    if not isinstance(before, str):
        raise ValueError(f'type(before) = {type(before)!r}')
    elif not isinstance(after, str):
        raise ValueError(f'type(after) = {type(after)!r}')

    return_PIL = isinstance(image, PIL.Image.Image)
    image = load_image(image)

    conversion_code = f'COLOR_{before}2{after}'
    conversion_code = conversion_code.replace('gray', 'GRAY')
    conversion_code = getattr(cv2, conversion_code, None)

    if conversion_code:
        img = __cv2_cvtColor(image, conversion_code)
    elif before.startswith('binary') or after.startswith('binary'):
        raise NotImplementedError
    else:
        raise ValueError

    if return_PIL:
        return PIL.Image.fromarray(img)
    else:
        return img


def create_line(p1, p2, color, *, thickness=3, **kwargs):
    return {
        'type': 'line',
        'p1': tuple(map(int, p1)),
        'p2': tuple(map(int, p2)),
        'color': color,
        'thickness': thickness,
        **kwargs
    }


def create_circle(center, radius, color, *, thickness=3, **kwargs):
    return {
        'type': 'circle',
        'center': center,
        'radius': radius,
        'color': color,
        'thickness': thickness,
        **kwargs
    }


def create_rectangle(p1, p2, color, *, thickness=3, **kwargs):
    return {
        'type': 'rectangle',
        'p1': p1,#tuple(map(int, p1)),
        'p2': tuple(map(int, p2)),
        'color': color,
        'thickness': thickness,
        **kwargs
    }


def create_text(text, origin, color, *, font=cv2.FONT_HERSHEY_SIMPLEX, scale=1.25, thickness=3, bg=None, bg_pad=None, **kwargs):
    shape = {
        'type': 'text',
        'text': text,
        'origin': tuple(map(int, origin)),
        'color': color,
        'font': font,
        'font_scale': scale,
        'thickness': thickness,
        **kwargs
    }

    if bg is None:
        if bg_pad is None:
            return shape
        else:
            # bg_pad is set to None by default instead of 5 ot alert the user
            # when he sets <bg_pad> and forgets <bg>.
            # Otherwise the mistake would be ignored silently
            raise ValueError('<bg> is None, even though <bg_pad> is set to a value')

    if bg_pad is None:
        bg_pad = [5] * 4
    elif is_number(bg_pad):
        bg_pad = [bg_pad] * 4
    elif is_sequence(bg_pad):
        if len(bg_pad) == 2:
            bg_pad = [*bg_pad, *bg_pad]
        elif len(bg_pad) != 4:
            raise ValueError(f'<bg_pad> expects None, a number or a sequence like (horizontal, vertical) or (left, top, right, bottom). Got a sequence of length {len(bg_pad)}')
    else:
        raise TypeError(f'type(bg_pad) = {type(bg_pad)!r}')

    shape['background'] = {'color': bg, 'pad': bg_pad}
    return shape


def create_polylines(pts, color, *, thickness=3, is_closed=True, **kwargs):
    return {
        'type': 'polylines',
        'pts': pts,
        'color': color,
        'thickness': thickness,
        'is_closed': is_closed,
        **kwargs
    }


def create_mask(pts, color, **kwargs):
    return {
        'type': 'mask',
        'pts': pts,
        'color': color,
        **kwargs
    }


def draw(image, data):
    new_image = image.copy()
    draw_inplace(new_image, data)
    return new_image


def draw_inplace(image, data):
    if isinstance(data, dict):
        data = [data]
    elif not is_iterable(data):
        raise TypeError(f'type(data) = {type(data)!r}')

    for shape in data:
        draw_shape = _pick_draw_function(shape['type'])
        shape = _insert_defaults(shape)
        shape = _rename_kwargs(shape)

        if shape['type'] == 'text':
            # extract background info only after the call to
            # _insert_defaults() and _rename_kwargs()
            # Otherwise you might miscalculate the bg size and position
            bg = _get_text_bg(shape)
            if bg:
                draw_inplace(image, bg)
        elif shape['type'] in ('mask', 'polylines'):
            pts = shape['pts']
            if is_iterable(pts):
                if not is_iterable(pts[0][0]):
                    pts = [pts]

            if not isinstance(pts, np.ndarray):
                pts = np.array(pts, dtype=np.int32)
            elif pts.dtype != np.int32:
                pts = pts.astype(np.int32)

            shape['pts'] = pts

        del shape['type']
        draw_shape(image, **shape)


def _get_text_bg(text):
    bg = text.pop('background', None)
    if not bg:
        return None

    if is_sequence(bg) or is_number(bg):
        color = bg
        pad = 5 * text['fontScale']
    elif isinstance(bg, dict):
        color = bg.pop('color')
        pad = bg.pop('pad', 5 * text['fontScale'])
    else:
        raise TypeError(f'type(background) = {type(bg).__name__!r}')

    error_msg = f'Expected <pad> to be an int or a sequence like (horizontal, vertical) or (left, top, right, bottom). Got {pad!r}'

    if is_number(pad):
        pad = (pad, pad, pad, pad)
    elif is_sequence(pad):
        if len(pad) == 2:
            pad = (*pad, *pad)
        elif len(pad) == 4:
            pass
        else:
            raise ValueError(error_msg)
    else:
        raise ValueError(error_msg)

    kwargs = {k: text[k] for k in ['text', 'fontFace', 'fontScale', 'thickness']}
    (w, h), baseline = cv2.getTextSize(**kwargs)
    baseline += text['thickness'] * text['fontScale']
    if text.get('bottomLeftOrigin', False):
        raise NotImplementedError('Calculate baseline for bottomLeftOrigin=True')

    p1 = (text['org'][0] - pad[0], text['org'][1] - h - pad[1])
    p2 = (text['org'][0] + w + pad[2], text['org'][1] + baseline + pad[3])
    return {
        'type': 'rectangle',
        'color': color,
        'p1': tuple(map(int, p1)),
        'p2': tuple(map(int, p2)),
        'thickness': -1
    }


def _rename_kwargs(shape):
    conversion = {
        'font': 'fontFace',
        'font_scale': 'fontScale',
        'line_type': 'lineType',
        'draw_above_origin': 'bottomLeftOrigin',
        'p1': 'pt1',
        'p2': 'pt2',
        'origin': 'org',
        'is_closed': 'isClosed',
    }

    return {conversion.get(k, k): v for k, v in shape.items()}


def _pick_draw_function(shape_type):
    fn = {
        'arrowed_line': cv2.arrowedLine,
        'circle': cv2.circle,
        'contours': cv2.drawContours,
        'convex_polygon': cv2.fillConvexPoly,
        'ellipse': cv2.ellipse,
        'ellipse_polygon': cv2.ellipse2Poly,
        'line': cv2.line,
        'marker': cv2.drawMarker,
        'mask': cv2.fillPoly,
        'polylines': cv2.polylines,
        'rectangle': cv2.rectangle,
        'text': cv2.putText,
    }

    if shape_type not in fn:
        raise ValueError(f'Unknown shape: {shape_type!r}')
    else:
        return fn[shape_type]


def _insert_defaults(shape):
    defaults = {
        'circle': {'thickness': -1},
        'line': {'thickness': 3},
        'rectangle': {'thickness': -1},
        'text': {
            'font': cv2.FONT_HERSHEY_SIMPLEX,
            'font_scale': 1.25,
            'thickness': 3,
        },
        'polylines': {'is_closed': True, 'thickness': 3},
    }

    return {**defaults.get(shape['type'], {}), **shape}


@mark('load::png')
@mark('load::jpg')
@mark('load::jpeg')
def load_image(image, mode=None):
    if not(mode is None or isinstance(mode, str)):
        raise TypeError(f'mode expected None or str. Got {type(mode)!r}')

    if isinstance(image, (str, Path)):
        return __np_array(__PIL_Image_open(image))
    elif isinstance(image, __PIL_Image_Image):
        return __np_array(image)
    elif isinstance(image, __np_ndarray):
        return image.copy()
    else:
        raise TypeError(f'type(image) = {type(image)!r}')


def hwc(arr):
    return bhwc(arr)[1:]


def hw(arr):
    return bhwc(arr)[1:3]


def are_arrays_equal(image_1, image_2, check_type=False):
    image_1 = load_image(image_1)
    image_2 = load_image(image_2)

    if image_1.shape != image_2.shape:
        return False
    elif check_type and image_1.dtype != image_2.dtype:
        return False
    else:
        return (image_1 == image_2).all()


@mark('save::png')
@mark('save::jpg')
@mark('save::jpeg')
def save_image(image, path, *, exists='error', mode='RGB'):
    if not isinstance(mode, str):
        raise ValueError(f'type(mode) = {type(mode)!r}')
    elif exists not in ('error', 'skip', 'replace'):
        raise ValueError(f'exists must be one of \'error\', \'skip\', \'replace\'. Got {exists!r}')

    if Path(path).exists():
        if exists == 'error':
            raise FileExistsError(f'[Errno 17] File exists: {str(path)!r}')
        elif exists == 'skip':
            return

    if isinstance(image, __PIL_Image_Image):
        image = __np_array(image)

    if isinstance(image, __np_ndarray):
        if mode != 'BGR':
            image = convert_image(image, mode, 'BGR')

        __cv2_imwrite(str(path), image)
    elif isinstance(image, (str, Path)):
        from katalytic.files import copy_file
        copy_file(image, path, exists=exists)
    else:
        raise TypeError(f'type(image) = {type(image)!r}')

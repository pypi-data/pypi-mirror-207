import re
from statistics import mean

from katalytic.data import pop_max
from katalytic.data.checks import is_sequence


def calc_bbox_area(bbox, fmt):
    bbox = convert_bbox(bbox, fmt, 'xy_wh') if fmt != 'xy_wh' else bbox
    (_, _), (w, h) = bbox
    return w * h


def calc_bbox_center(bbox, fmt, *, as_int=False):
    """Optionally, convert the center to integer coordinates"""
    (x, y), (X, Y) = convert_bbox(bbox, fmt, 'xy_XY')
    cx, cy = (mean([x, X]), mean([y, Y]))

    if as_int:
        return (int(cx), int(cy))
    else:
        return (cx, cy)


def calc_IoB(bbox_1, fmt_1, bbox_2, fmt_2):
    intersection = intersect_bboxes(bbox_1, fmt_1, bbox_2, fmt_2)
    if intersection is None:
        return 0

    inter_area = calc_bbox_area(intersection, fmt_1)
    return inter_area / calc_bbox_area(bbox_1, fmt_1)


def calc_IoB_max(bbox_1, fmt_1, bbox_2, fmt_2):
    """Return the largest of (intersection over bbox_1) and (intersection over bbox_2)"""
    return max(
        calc_IoB(bbox_1, fmt_1, bbox_2, fmt_2),
        calc_IoB(bbox_2, fmt_2, bbox_1, fmt_1)
    )


def calc_IoU(bbox_1, fmt_1, bbox_2, fmt_2):
    intersection = intersect_bboxes(bbox_1, fmt_1, bbox_2, fmt_2)
    if intersection is None:
        return 0

    a1 = calc_bbox_area(bbox_1, fmt_1)
    a2 = calc_bbox_area(bbox_2, fmt_2)
    inter_area = calc_bbox_area(intersection, fmt_1)

    # the overlapping area is counted twice. Subtract it once
    union_area = a1 + a2 - inter_area
    return inter_area / union_area


def non_max_suppression(bboxes, format, *, max_IoU=0.5, scores=None):
    if not bboxes:
        return bboxes
    elif not format.endswith('s'):
        if scores:
            bboxes = set_bbox_scores(bboxes, scores, format, 'xyXYs')
        else:
            raise ValueError('If the format is not one of xyXYs, xyXY_s, xy_XY_s, xywhs, xywh_s, xy_wh_s, either change the call to non_max_suppression(..., scores=...) or use set_bbox_scores().')

    if format.endswith('s') and format != 'xyXYs':
        # standardise the format to simplify the implementation
        bboxes = [convert_bbox(bbox, format, 'xyXYs') for bbox in bboxes]

    kept, bboxes = pop_max(bboxes, key=lambda bbox: bbox[-1])

    # remove bboxes with IoU > max_IoU than the kept bbox
    bboxes = [b for b in bboxes if calc_IoU(b, 'xyXYs', kept, 'xyXYs') < max_IoU]

    # call recursively on the remaining bboxes
    kept = [kept, *non_max_suppression(bboxes, 'xyXYs', max_IoU=max_IoU)]

    if format != 'xyXYs':
        # convert to the original format
        kept = [convert_bbox(bbox, 'xyXYs', format) for bbox in kept]

    return kept


def set_bbox_scores(bboxes, scores, before, after):
    """You can insert scores or change the existing ones"""
    if len(bboxes) != len(scores):
        raise ValueError('bboxes and scores must have the same length')
    elif not after.endswith('s'):
        raise ValueError('after format must be one of xyXYs, xyXY_s, xy_XY_s, xywhs, xywh_s, xy_wh_s')
    elif not all(0 <= s <= 1 for s in scores):
        raise ValueError('scores must be in the range [0, 1]')

    if before != 'xyXY':
        bboxes = [convert_bbox(bbox, before, 'xyXY') for bbox in bboxes]

    bboxes = [(*bbox, s) for bbox, s in zip(bboxes, scores)]
    if after == 'xyXYs':
        return bboxes
    else:
        return [convert_bbox(bbox, 'xyXYs', after) for bbox in bboxes]


def calc_IoB_min(bbox_1, fmt_1, bbox_2, fmt_2):
    """Return the smallest of (intersection over bbox_1) and (intersection over bbox_2)"""
    return min(
        calc_IoB(bbox_1, fmt_1, bbox_2, fmt_2),
        calc_IoB(bbox_2, fmt_2, bbox_1, fmt_1)
    )


def convert_bbox(bbox, before, after):
    """There are too many combinations to make a function for each (before, after) pair"""
    if before not in _FORMATS:
        raise ValueError(f'Unknown before format {before!r}')
    elif after not in _FORMATS:
        raise ValueError(f'Unknown after format {after!r}')
    elif not is_bbox(bbox, before):
        raise ValueError(f'{bbox!r} is not in the {before!r} format')
    elif before == after:
        # I could just return the bbox, but I prefer to fail early
        # so the dev knows there might be a bug in his code
        # It makes the easy thing harder and the hard thing (debugging) easy
        raise ValueError(f'before and after formats are the same: {before!r}')
    elif after.endswith('s') and not before.endswith('s'):
        raise ValueError(f'Cannot convert from {before} to {after}')

    x = y = X = Y = w = h = s = None
    if before == 'xywh':      x,y,w,h = bbox
    elif before == 'xywhs':   x,y,w,h,s = bbox
    elif before == 'xywh_s':  (x,y,w,h), s = bbox
    elif before == 'xy_wh':   (x,y), (w,h) = bbox
    elif before == 'xy_wh_s': (x,y), (w,h), s = bbox
    elif before == 'xyXY':    x,y,X,Y = bbox
    elif before == 'xyXYs':   x,y,X,Y,s = bbox
    elif before == 'xyXY_s':  (x,y,X,Y), s = bbox
    elif before == 'xy_XY':   (x,y), (X,Y) = bbox
    elif before == 'xy_XY_s': (x,y), (X,Y), s = bbox

    if X is None:
        X = x + w
        Y = y + h
    elif w is None:
        w = X - x
        h = Y - y

    if after == 'xywh':      return x,y,w,h
    elif after == 'xywhs':   return x,y,w,h,s
    elif after == 'xywh_s':  return (x,y,w,h), s
    elif after == 'xy_wh':   return (x,y), (w,h)
    elif after == 'xy_wh_s': return (x,y), (w,h), s
    elif after == 'xyXY':    return x,y,X,Y
    elif after == 'xyXYs':   return x,y,X,Y,s
    elif after == 'xyXY_s':  return (x,y,X,Y), s
    elif after == 'xy_XY':   return (x,y), (X,Y)
    elif after == 'xy_XY_s': return (x,y), (X,Y), s


def intersect_bboxes(bbox_1, fmt_1, bbox_2, fmt_2):
    if fmt_1.endswith('s'):
        s = bbox_1[-1]

    bbox_1 = convert_bbox(bbox_1, fmt_1, 'xy_XY') if fmt_1 != 'xy_XY' else bbox_1
    bbox_2 = convert_bbox(bbox_2, fmt_2, 'xy_XY') if fmt_2 != 'xy_XY' else bbox_2

    (x1, y1), (X1, Y1) = bbox_1
    (x2, y2), (X2, Y2) = bbox_2

    x3, y3 = max(x1, x2), max(y1, y2)
    X3, Y3 = min(X1, X2), min(Y1, Y2)

    if (0 <= x3 < X3) and (0 <= y3 < Y3):
        bbox_3 = [(x3, y3), (X3, Y3)]
        if fmt_1.endswith('s'):
            bbox_3 = convert_bbox([*bbox_3, s], 'xy_XY_s', fmt_1)
        elif fmt_1 != 'xy_XY':
            bbox_3 = convert_bbox(bbox_3, 'xy_XY', fmt_1)

        return type(bbox_1)(bbox_3)
    else:
        return None


def is_bbox(bbox, fmt):
    if fmt not in _FORMATS:
        available = ", ".join(_FORMATS)
        raise ValueError(f'Unknown format {fmt!r}. Available formats: {available}')

    return _FORMATS[fmt](bbox)


def _is_xy_wh(bbox):
    """WARNING:
    Returns True if the bbox has the xy_XY format
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y), (w, h) = bbox
        return (x >= 0) and (y >= 0) and (w > 0) and (h > 0)
    except Exception:
        return False


def _is_xy_wh_s(bbox):
    """WARNING:
    Returns True if the bbox has the xy_XY format
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y), (w, h), s = bbox
        return (x >= 0) and (y >= 0) and (w > 0) and (h > 0) and 0 <= s <= 1
    except Exception:
        return False


def _is_xy_XY(bbox):
    """WARNING:
    Returns True if the bbox has the xy_wh format and x < w and y < h
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y), (X, Y) = bbox
        return (0 <= x < X) and (0 <= y < Y)
    except Exception:
        return False


def _is_xy_XY_s(bbox):
    """WARNING:
    Returns True if the bbox has the xywh format and x < w and y < h
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y), (X, Y), s = bbox
        return (0 <= x < X) and (0 <= y < Y) and 0 <= s <= 1
    except Exception:
        return False


def _is_xywh(bbox):
    """WARNING:
    Returns True if the bbox has the xyXY format
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y, w, h) = bbox
        return (x >= 0) and (y >= 0) and (w > 0) and (h > 0)
    except Exception:
        return False


def _is_xywh_s(bbox):
    """WARNING:
    Returns True if the bbox has the xyXY format
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y, w, h), s = bbox
        return (x >= 0) and (y >= 0) and (w > 0) and (h > 0) and 0 <= s <= 1
    except Exception:
        return False


def _is_xywhs(bbox):
    """WARNING:
    Returns True if the bbox has the xyXY format
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y, w, h, s) = bbox
        return (x >= 0) and (y >= 0) and (w > 0) and (h > 0) and 0 <= s <= 1
    except Exception:
        return False


def _is_xyXY(bbox):
    """WARNING:
    Returns True if the bbox has the xywh format and x < w and y < h
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y, X, Y) = bbox
        return (0 <= x < X) and (0 <= y < Y)
    except Exception:
        return False


def _is_xyXY_s(bbox):
    """WARNING:
    Returns True if the bbox has the xywh format and x < w and y < h
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y, X, Y), s = bbox
        return (0 <= x < X) and (0 <= y < Y) and 0 <= s <= 1
    except Exception:
        return False


def _is_xyXYs(bbox):
    """WARNING:
    Returns True if the bbox has the xywh format and x < w and y < h
    There's no way to check against that case

    Kept hidden to avoid cluttering the namespace
    """
    if not is_sequence(bbox):
        raise TypeError(f'Expected a sequence, got {type(bbox)}')

    try:
        (x, y, X, Y, s) = bbox
        return (0 <= x < X) and (0 <= y < Y) and 0 <= s <= 1
    except Exception:
        return False


# Define at the end of the file because it requires
# the functions to be already defined
_FORMATS = {
    'xyXY': _is_xyXY,
    'xyXY_s': _is_xyXY_s,
    'xyXYs': _is_xyXYs,
    'xy_XY': _is_xy_XY,
    'xy_XY_s': _is_xy_XY_s,
    'xy_wh': _is_xy_wh,
    'xy_wh_s': _is_xy_wh_s,
    'xywh': _is_xywh,
    'xywh_s': _is_xywh_s,
    'xywhs': _is_xywhs,
}

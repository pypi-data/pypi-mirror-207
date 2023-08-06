import re
from time import sleep
from typing import Literal

import arrow
import pyautogui as g
from hakai_api import Client

from ix_aims import imgs

g.PAUSE = 0.05


def move(img):
    if loc := g.locateOnScreen(img, grayscale=True, confidence=.95):
        g.moveTo(*g.center(loc))


def click(img):
    if loc := g.locateOnScreen(img, grayscale=True, confidence=.95):
        g.click(*g.center(loc))


def open_ix_capture():
    g.click(10, g.size().height)
    g.typewrite('ixcapture')
    g.hotkey('enter')


def go_to_processes_tab():
    click(imgs.processesBtn)


def click_yes():
    click(imgs.yesBtn)


def get_camera_params(d: 'Arrow', camera: Literal["rgb"] | Literal["nir"]):
    c = Client()
    cal = c.get(
        f"{c.api_root}/aco/camera_calibration?camera_type={camera}&valid_from<={d.isoformat()}&sort=-valid_from&limit=1").json()[
        0]
    return cal


def get_acquisitions(workorder):
    c = Client()
    res = c.get(
        f"{c.api_root}/aco/views/projects/phases/flights/dces?projectphase_num={workorder}&fields=acq_date,sess_num&distinct&sort=acq_date,sess_num")

    if res.status_code == 200:
        return res.json()
    else:
        res.raise_for_status()


def setup_work_order_day(recipe_name, save_folder, rgb_params, nir_params, year, doy):
    # New Recipe
    click(imgs.plusTab)
    g.hotkey('tab')
    g.hotkey('ctrl', 'a')
    g.hotkey('del')
    g.typewrite(recipe_name)

    # Skip prefix name
    g.hotkey('tab')

    # Save to Folder
    g.hotkey('tab')
    g.hotkey('ctrl', 'a')
    g.hotkey('del')
    g.typewrite(save_folder)

    # Skip rgb and nir watch
    g.hotkey('tab')
    g.hotkey('tab')

    # CIR system
    g.hotkey('tab')
    g.hotkey('c')

    # Skip camera
    g.hotkey('tab')

    # Output type tiff
    g.hotkey('tab')
    g.hotkey('t')

    # Output 4-band CIR
    for _ in range(6):
        g.hotkey('tab')
    g.hotkey('space')
    g.hotkey('tab')

    # LZW compression
    for _ in range(6):
        g.hotkey('tab')
    g.typewrite('l')

    # Calibration params
    for _ in range(2):
        g.hotkey('tab')

    for param in [
        'camera_sn',
        'pixel_size_mm',
        'focal_length_mm',
        'xp_mm',
        'yp_mm',
        'k1',
        'k2',
        'k3',
        'p1',
        'p2',
        'b1',
        'b2',
    ]:
        g.hotkey('tab')
        g.hotkey('del')
        g.typewrite(str(rgb_params[param]))

        g.hotkey('tab')
        g.hotkey('del')
        g.typewrite(str(nir_params[param]))

    # Select dirs
    # g.hotkey('tab')
    # g.hotkey('tab')
    # g.hotkey('enter')
    #
    # # Find ellipses buttons
    # sleep(1)
    # buttons = list(map(g.center, g.locateAllOnScreen(imgs.ellipseBtn, confidence=.95)))
    # assert len(buttons) == 2, "Could not find ellipses buttons"

    # Select RGB images
    #
    # rgb_btn = min(buttons, key=lambda b: b.y)
    # g.click(rgb_btn)

    # for _ in range(7):
    #     g.hotkey('tab')
    # g.typewrite("aco-uvic")
    # g.confirm("continue?")
    # g.hotkey("enter")
    # g.hotkey("tab")
    # g.typewrite(f"{year}_Acquisitions")
    # g.confirm("continue?")
    # g.hotkey("enter")
    # g.typewrite("01")
    # g.hotkey("enter")
    # g.typewrite(f"D{str(doy).zfill(3)}")
    # g.confirm("continue?")
    # g.hotkey("enter")

    # nir_btn = max(buttons, key=lambda b: b.y)

    # Click ellipses buttons



def check_work_order_param(value: str):
    """Check worker order matches regex dd_dddd_dd pattern"""
    assert re.match(r'\d{2}_\d{4}_\d{2}',
                    value), "Work order must be in format dd_dddd_dd"
    return value


def auto_ix(work_order: str):
    work_order = check_work_order_param(work_order)
    flights = get_acquisitions(work_order)

    # Open iXCapture
    # Use this if working in RDP client to activate the write window
    # g.hotkey("ctrl", "alt", "right")
    # g.click(1000, 1000)
    # open_ix_capture()
    sleep(5)
    # go_to_processes_tab()
    # sleep(2)
    # click_yes()

    for flight in flights:
        date = arrow.get(flight['acq_date'])
        sess = flight['sess_num']
        year = date.format('YYYY')
        doy = date.format('DDD')

        nir_params = get_camera_params(date, "nir")
        rgb_params = get_camera_params(date, "rgb")

        recipe_name = f"{work_order}_d{doy}"
        if sess:
            recipe_name += f"s{sess}"
        save_folder = f'C:\\CIR_files\\{year}'

        setup_work_order_day(recipe_name, save_folder, rgb_params, nir_params, year, doy)

import pychromecast
import pychromecast.controllers.dashcast as dashcast
import time

casts = pychromecast.get_chromecasts()

for cast in casts:
    if cast.device.friendly_name == 'the future':
        outcast = cast

d = dashcast.DashCastController()
outcast.register_handler(d)

time.sleep(1)

if not outcast.is_idle:
    outcast.quit_app()
    time.sleep(2)
else:
    time.sleep(2)


d.load_url('http://192.168.0.7:5050/HA')
time.sleep(2)
d.load_url('http://192.168.0.7:5050/HA')

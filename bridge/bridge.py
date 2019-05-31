#!/usr/bin/env python

import time

from ISY.controller import Controller


from devices.switch import Switch
from devices.dimmer import Dimmer
from devices.scene import Scene

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARN)



class Bridge (object):
    
    controller = None

    homie_devices = {} #indexed by container_type,device_address

    def __init__(self, address=None, username=None, password=None, homie_settings=None, mqtt_settings=None):

        self.homie_settings = homie_settings
        self.mqtt_settings = mqtt_settings

        self.controller = Controller(address=address,port=None,username=username,password=password,use_https=False,event_handler=self._isy_event_handler)

    def _isy_event_handler(self,container,item,event,*args):
        #print ('Event {} from {}: {} {}'.format(event,container.container_type,item.name,args))

        if container.container_type == 'Device':
            self._device_event_handler (item,event,args)
        elif container.container_type == 'Scene':
            self._scene_event_handler (item,event,args)

    def _device_event_handler(self,device,event,*args):
        #print ('device event',device.name,event)
        if event == 'add':
            if device.device_type == 'switch':
                switch = Switch (device,self.homie_settings,self.mqtt_settings)
            elif device.device_type == 'dimmer':
                switch = Dimmer (device,self.homie_settings,self.mqtt_settings)

    def _scene_event_handler(self,device,event,*args):
        #print ('device event',device.name,event)
        if event == 'add':
            scene = Scene (device,self.homie_settings,self.mqtt_settings)
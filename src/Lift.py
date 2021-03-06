#!/usr/bin/env python
# -*- coding: utf-8 -*-
#! @author : @ruhend (Mudigonda Himansh)


class Lift:
    def __init__(self, motion, location):
        self.motion = motion
        self.location = location

    def getLiftLOC(self):
        return self.location

    def setLiftLocation(self, _new_location):
        self.location = _new_location
        return self.getLiftLOC()

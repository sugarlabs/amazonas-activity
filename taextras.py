# -*- coding: utf-8 -*-
#Copyright (c) 2011 Walter Bender

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

from gettext import gettext as _

'''
Note: this file contains string from plugins and related projects that
are not included in the default packaaging of Turtle Art. The reason
for gathering these strings here is to enable us to use one common POT
file across all of these projects.

TODO: build some automated way of maintaining this file.
'''

# ACTIVITIES

TURTLEARTMINI_STRINGS = [
    _('Turtle Art Mini')
    ]

TURTLECONFUSION_STRINGS = [
    _('Turtle Confusion'),
    _('Select a challenge')
    ]

# PLUGINS

CURRENCY_STRINGS = [
    _('Palette of Mexican pesos'),
    _('Palette of Colombian pesos'),
    _('Palette of Rwandan francs'),
    _('Palette of US currencies'),
    _('Palette of Australian currencies'),
    _('Palette of Guaranies')
    ]

BUTIA_STRINGS = [
    #TRANS: Butia is the Arduino Robot Project from Uruguay
    #(http://www.fing.edu.uy/inco/proyectos/butia/)
    _('Turtle Art Butia'),
    _('Adjust LED intensity between 0 and 255.'),
    _('Returns the object gray level encountered him as a number between \
0 and 1023.'),
    _('Returns 1 when the button is press and 0 otherwise.'),
    _('Returns the level of ligth in the ambient as a number between \
0 and 1023.'),
    _('Returns the temperature in the ambient as a number between 0 and 255.'),
    _('Returns the distance from the object in front of the sensor as a \
number between 0 and 255.'),
    _('Returns 0 or 1 depending on the sensor inclination.'),
    _('Returns 1 when the sensors detects a magnetic field, 0 otherwise.'),
    _('Switchs from 0 to 1, the frequency depends on the vibration.'),
    _('LED'),
    _('pushbutton'),
    _('grayscale'),
    _('ambient light'),
    _('temperature'),
    _('distance'),
    _('tilt'),
    _('magnetic induction'),
    _('vibration'),
    _('Butia Robot'),
    _('delay Butia'),
    _('wait for argument seconds'),
    _('Butia battery charge'),
    _('Returns the battery charge as a number between 0 and 255.'),
    _('Butia speed'),
    _('Set the moving speed of the Butia motors as the value between \
0 and 1023, passed by argument.'),
    _('forward Butia'),
    _('Move the Butia robot forward.'),
    _('forward distance'),
    _('Move the Butia robot forward a predefined distance.'),
    _('backward Butia'),
    _('Move the Butia robot backward.'),
    _('backward distance'),
    _('Move the Butia robot backward a predefined distance.'),
    _('left Butia'),
    _('Move the Butia robot backward.'),
    _('right Butia'),
    _('Move the Butia robot backward.'),
    _('Turn x degrees'),
    _('Turn the Butia robot x degrees.'),
    _('stop Butia'),
    _('Move the Butia robot backward.'),
    _('print Butia'),
    _('Print text in Butia robot 32-character ASCII display.'),
    _('Butia')
    ]

FOLLOWME_STRINGS = [
    _('The camera was not found.')
    _('Error on the init of the camera.')
    _('FollowMe'))
    _('follow a RGB color'),
    _('follow a turtle color'),
    _('calibrate a color to follow'),
    _('x position'),
    _('return x position'),
    _('y position'),
    _('return y position')
    ]

SUMO_STRINGS = [
    _('Sumo Butia'),
    _('submit speed​​'),
    _('Send speeds the robot.'),
    _('set speed'),
    _('Set the default speed for the movement commands.'),
    _('move'),
    _('back'),
    _('stop'),
    _('turn left'),
    _('turn right'),
    _('angle to center'),
    #TRANS: dojo is the playing field
    _('Get the angle to the center of the dojo.'),
    _('angle to the opponent'),
    _('Get the angle to the center of the opponent.'),
    _('x coor.'),
    _('Get the x coordinate of the robot.'),
    _('y coor.'),
    _('Get the y coordinate of the robot.'),
    _('opponent x coor.'),
    _('Get the x coordinate of the opponent.'),
    _('opponent y coor.'),
    _('Get the y coordinate of the opponent.'),
    _('rotation'),
    _('Get SumBot rotation.'),
    _('opponent rotation'),
    _('Get the rotation of the opponent.'),
    _('distance to center'),
    #TRANS: dojo is the playing field
    _('Get the distance to the center of the dojo.'),
    _('distance to opponent'),
    _('Get the distance to the opponent.'),
    _('update information'),
    _('Update information from the server.')
    ]

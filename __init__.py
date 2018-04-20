
# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
__author__ = 'J'
 
LOGGER= getLogger(__name__)

class LotterySkill(MycroftSkill):
 
 def__init__(self):
              super(LotterySkill, self).__init__(name="LotterySkill")
   
 def initialize(self):
                 self.load_data_files(dirname(__file__))
                 
                 random_number_intent = IntentBuilder("LotteryIntent").\ 
                         require("NumbersKeyword").build()
                 self.register_intent(numbers_intent, self.handle_numbers_intent)
       
       
               def handle_numbers_intent(self, message):
                       self.speak_dialog("numbers")
                       num = random.randint(1,45)

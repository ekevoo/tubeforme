# -*- coding: utf-8 -*-
#
# Copyright 2008-2015, Ekevoo.com.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
#
from logging import getLogger, DEBUG, StreamHandler
from os.path import dirname, abspath, basename
from sys import path

if __name__ == '__main__':
    log = getLogger()
    log.setLevel(DEBUG)
    log.addHandler(StreamHandler())
    me = abspath(__file__)
    myfolder = dirname(me)
    mypackage = basename(myfolder)
    path.insert(0, dirname(myfolder))
    __import__(mypackage + '.main').main()

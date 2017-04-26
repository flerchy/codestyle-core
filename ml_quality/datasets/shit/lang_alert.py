# Copyright (C) 2009 <nanotube@users.sf.net> (http://pykeylogger.sourceforge.net/)
# Copyright (C) 2013 Shahar Kosti <shahar.kosti@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import threading, Queue

if os.name == 'posix':
    import pyxhook as hooklib
elif os.name == 'nt':
    import pyHook as hooklib
    import pythoncom, win32api, win32process
    import winsound

alert_sounds = {
    0x0409 : 'alert_en.wav',
    0x040D : 'alert_he.wav'
}

class ProcessThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.shouldStop = False
        
    def run(self):
        while self.shouldStop == False:
            try:
                event = self.queue.get(timeout=0.05)
                self.process_event(event)
            except Queue.Empty:
                pass
    
    def process_event(self, event):
        try:
            thread_id, process_id = \
                win32process.GetWindowThreadProcessId(event['window'])
            lang_id = win32api.GetKeyboardLayout(thread_id)
            self.process(event['key'], lang_id)
        except:
            pass
        
    def process(self, key, lang_id):
        try:
            if ord(key) < ord('A') or ord(key) > ord('Z'):
                return
            
            lang_id = (lang_id >> 16)
            if alert_sounds.has_key(lang_id):
                sound = alert_sounds[lang_id]
                self.play_sound(sound)
        except:
            pass
        
    def play_sound(self, path):
        winsound.PlaySound(path, winsound.SND_FILENAME | 
            winsound.SND_ASYNC | winsound.SND_NOWAIT)

class KeyListener:
    '''
    Listens to all keystrokes, enqueue events.
    '''
    def __init__(self):
        self.queue = Queue.Queue(0)
        self.hm = hooklib.HookManager()
        
        self.hm.HookKeyboard()
        self.hm.KeyDown = self.OnKeyDownEvent
        #self.hm.KeyUp = self.OnKeyUpEvent
    
    def start(self):
        self.process_thread = ProcessThread(self.queue)
        self.process_thread.start()
    
        if os.name == 'nt':
            pythoncom.PumpMessages()
        if os.name == 'posix':
            self.hashchecker.start()
            self.hm.start()
    
    def OnKeyDownEvent(self, event):
        '''
        Called when a key is pressed and inserts the event to the queue.
        '''        
        message = { 'window' : event.Window, 'key' : event.Key }
        self.queue.put(message)

listener = KeyListener()
listener.start()


# win32 language identifiers
# http://msdn.microsoft.com/en-us/library/windows/desktop/dd318691(v=vs.85).aspx
# http://msdn.microsoft.com/en-us/library/windows/desktop/dd318693(v=vs.85).aspx


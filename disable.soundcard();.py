import ctypes
import time
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def mute_system_volume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMute(1, None)

def disable_sound_card():
    try:
        ctypes.windll.winmm.waveOutSetVolume(None, 0)
        print("Sound card disabled.")
    except Exception as e:
        print(f"Failed to disable sound card: {e}")

if __name__ == "__main__":
    mute_system_volume()
    disable_sound_card()

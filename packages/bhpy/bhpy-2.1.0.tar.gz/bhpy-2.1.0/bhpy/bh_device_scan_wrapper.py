import logging
log = logging.getLogger(__name__)

try:
  from ctypes import c_int16, create_string_buffer, Structure, CDLL, c_char_p, c_uint8, c_void_p, c_char
  import argparse
  import pathlib
  import re
  import winreg
except ModuleNotFoundError as err:
  # Error handling
  log.error(err)
  raise

class HardwareScanResult(Structure):
  _fields_ = [("friendlyName", c_char * 32),
              ("serialNumber", c_char * 32),
              ("firmwareVersion", c_char * 32)]

class HardwareError(IOError):
  pass

class BHDeviceScanWrapper:
  versionStr = ""
  versionStrBuf = create_string_buffer(128)

  def __init__(self, dllPath = None):
    if dllPath is None:
      spcmPath = winreg.QueryValueEx(winreg.OpenKey(winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), 'SOFTWARE\\BH\\SPCM'), "FilePath")[0]
      dllPath = pathlib.Path(spcmPath).parent / "DLL/bh_device_scan.dll"
    else:
      dllPath = pathlib.Path(dllPath)
    
    try:
      self.__dll = CDLL(str(dllPath.absolute()))
    except FileNotFoundError as e:
      log.error(e)
      raise

    self.__get_dll_version = self.__dll.get_dll_version
    self.__get_dll_version.argtypes = [c_char_p, c_uint8]
    self.__get_dll_version.restype = c_int16

    self.__get_dll_version(self.versionStrBuf, c_uint8(128))
    self.versionStr = str(self.versionStrBuf.value)[2:-1]

    match = re.match(r"(\d+)\.(\d+)\.(\d+)", self.versionStr)
    major = int(match.group(1))
    minor = int(match.group(2))
    patch = int(match.group(3))
    if (major != 1):
      raise RuntimeError(f"Unable to load DLL: incompatible version. Version is: {major}.{minor}.{patch} Expected >= 1.0.0, < 2")

    self.__bhScanHardware = self.__dll.bh_scan_hardware
    self.__bhScanHardware.argtypes = [c_void_p]
    self.__bhScanHardware.restype = c_int16

  def bhScanHardware(self) -> list:
    arg1 = (HardwareScanResult * 32)()
    serialNumber = []

    for i in range(32):
      arg1[i].friendlyName = bytes(0)
      arg1[i].serialNumber = bytes(0)
      arg1[i].firmwareVersion = bytes(0)

    ret = self.__bhScanHardware(arg1)
    # Structure objects (arg1) are automatically passed byref

    if ret > 0:
      for i, modul in enumerate(arg1):
        if i < ret:
          serialNumber.append((str(modul.friendlyName)[2:-1], str(modul.serialNumber)[2:-1], str(modul.firmwareVersion)[2:-1]))
        else:
          break
    return serialNumber

def main():
  parser = argparse.ArgumentParser(prog="BH Device Scan DLL Wrapper", description="BH device scanning dll wrapper that provides python bindings to scan the system for all present BH devices, their serial number and firmware version.")
  parser.add_argument('dll_path', nargs='?', default=None)

  args = parser.parse_args()

  bhScan = BHDeviceScanWrapper(args.dll_path)
  print(bhScan.bhScanHardware())
  input("press enter...")

if __name__ == '__main__':
  main()
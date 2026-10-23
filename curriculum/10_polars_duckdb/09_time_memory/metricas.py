"""Contadores del SO; no importa motores ni toma medidas al importar."""
import os
import sys


def memoria_residente():
    """Pico absoluto desde arranque hasta esta lectura; no se puede reiniciar aqui."""
    if os.name == "nt":
        import ctypes
        from ctypes import wintypes

        class Contadores(ctypes.Structure):
            _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [
                (n, ctypes.c_size_t) for n in ("PeakWorkingSetSize", "WorkingSetSize",
                 "QuotaPeakPagedPoolUsage", "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage",
                 "QuotaNonPagedPoolUsage", "PagefileUsage", "PeakPagefileUsage")]
        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        psapi = ctypes.WinDLL("psapi", use_last_error=True)
        kernel.GetCurrentProcess.restype = wintypes.HANDLE
        psapi.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(Contadores), wintypes.DWORD]
        psapi.GetProcessMemoryInfo.restype = wintypes.BOOL
        c = Contadores()
        c.cb = ctypes.sizeof(c)
        if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(c), c.cb):
            raise ctypes.WinError(ctypes.get_last_error())
        return dict(metrica="PeakWorkingSetSize", pico_bytes=int(c.PeakWorkingSetSize),
                    residente_final_bytes=int(c.WorkingSetSize))
    if sys.platform.startswith("linux"):
        import resource
        # Linux devuelve KiB; esta rama no se verifico en la autoria Windows.
        return dict(metrica="ru_maxrss_linux", pico_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024),
                    residente_final_bytes=None)
    return dict(metrica="no_disponible", pico_bytes=None, residente_final_bytes=None)

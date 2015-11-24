import winreg
import sys


def uninstall_hyperspy_here():
    for env in ('qtconsole', 'notebook'):
        try:
            if sys.getwindowsversion()[0] < 6.:  # Older than Windows Vista:
                winreg.DeleteKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r'Software\Classes\Folder\Shell\HyperSpy_%s_here\Command' %
                    env)
                winreg.DeleteKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r'Software\Classes\Folder\Shell\HyperSpy_%s_here' %
                    env)
            else:  # Vista or newer
                winreg.DeleteKey(
                    winreg.HKEY_CLASSES_ROOT,
                    r'Directory\shell\hyperspy_%s_here\Command' %
                    env)
                winreg.DeleteKey(
                    winreg.HKEY_CLASSES_ROOT,
                    r'Directory\shell\hyperspy_%s_here' %
                    env)
                winreg.DeleteKey(
                    winreg.HKEY_CLASSES_ROOT,
                    r'Directory\Background\shell\hyperspy_%s_here\Command' %
                    env)
                winreg.DeleteKey(
                    winreg.HKEY_CLASSES_ROOT,
                    r'Directory\Background\shell\hyperspy_%s_here' %
                    env)
            print(("HyperSpy %s here correctly uninstalled" % env))
        except:
            print(("Failed to uninstall HyperSpy %s here" % env))

if __name__ == "__main__":
    uninstall_hyperspy_here()

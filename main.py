"""Personal Finance Manager - application entry point.

Run with:  python main.py
"""

import sys

try:
    from src.file_manager import ensure_dirs
    from src.menu import FinanceApp
except ImportError:  # pragma: no cover
    from file_manager import ensure_dirs
    from menu import FinanceApp


def main():
    ensure_dirs()
    try:
        FinanceApp().run()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())

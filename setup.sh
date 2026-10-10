#!/usr/bin/env python3
#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]; then
  echo "[-] Error: Please run setup.sh as root (sudo ./setup.sh)"
  exit 1
fi

SCRIPT_NAME="sundown.py"
TARGET_LINK="/usr/local/bin/sundown"

# Verify sundown.py exists in the current directory
if [ ! -f "$SCRIPT_NAME" ]; then
  echo "[-] Error: Could not find '$SCRIPT_NAME' in this directory."
  echo "Please make sure setup.sh is placed in the same folder as your tool."
  exit 1
fi

echo "[*] Granting execution permissions to $SCRIPT_NAME..."
chmod +x "$SCRIPT_NAME"

ABS_PATH=$(realpath "$SCRIPT_NAME")

echo "[*] Creating system-wide symlink at $TARGET_LINK..."
if [ -L "$TARGET_LINK" ] || [ -f "$TARGET_LINK" ]; then
  rm -f "$TARGET_LINK"
fi

ln -s "$ABS_PATH" "$TARGET_LINK"

echo "[+] Success! Sundown is now globally installed."
echo "[!] You can now run it from anywhere using: sudo sundown [flags]"

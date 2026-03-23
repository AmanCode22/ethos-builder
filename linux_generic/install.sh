#!/bin/bash


original_user="${SUDO_USER:-$USER}"
user_home=$(getent passwd "$original_user" | cut -d: -f6)
user_bin="$user_home/bin"

if [[ $EUID -ne 0 ]]; then
    echo "Warning: This script is not running with root privileges."
    read -p "Install for just $original_user in $user_bin? (y/N): " choice

    if [[ "$choice" =~ ^[Yy]$ ]]; then
        mkdir -p "$user_bin"
        cp bin/ethos "$user_bin/"
        cp bin/forge "$user_bin/"


        if [[ ":$PATH:" == *":$user_bin:"* ]]; then
            echo "$user_bin is already in PATH."
        else
            echo "Adding $user_bin to .bashrc..."
            echo "export PATH=\"\$PATH:$user_bin\"" >> "$user_home/.bashrc"
            echo "Added to .bashrc. Restart your terminal or run 'source ~/.bashrc'."
        fi
        echo "Installation for $original_user completed."
        exit 0
    else
        echo "Exiting."
        exit 1
    fi
fi


echo "Installing globally with root privileges..."
cp bin/ethos /usr/local/bin/ethos
cp bin/forge /usr/local/bin/forge
chmod +x /usr/local/bin/ethos /usr/local/bin/forge

echo "Installation completed for all users."

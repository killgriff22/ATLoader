#!/usr/bin/env zsh

# common grc.zsh paths
files=(
  /etc/grc.zsh               # default
  /usr/local/etc/grc.zsh     # homebrew darwin-x64
  /opt/homebrew/etc/grc.zsh  # homebrew darwin-arm64
  /usr/share/grc/grc.zsh     # Gentoo Linux (app-misc/grc)
)

# verify the file is readable and source it
for file in $files; do
  if [[ -r "$file" ]]; then
    source "$file"
    break
  fi
done

unset file files

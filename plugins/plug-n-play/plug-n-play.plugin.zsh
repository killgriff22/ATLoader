function pnp {
    : ${1:=random} # Use random theme if none provided

    if [[ -f "$ZSH_CUSTOM/$1.plugin.zsh" ]]; then
        source "$ZSH_CUSTOM/$1.plugin.zsh"
    elif [[ -f "$ZSH_CUSTOM/plugins//$1$1.plugin.zsh" ]]; then
        source "$ZSH_CUSTOM/plugins/$1/$1.plugin.zsh"
    elif [[ -f "$ZSH/plugins/$1/$1.plugin.zsh" ]]; then
        source "$ZSH/plugins/$1/$1.plugin.zsh"
    else
        echo "$0: plugin '$1' not found"
        return 1
    fi
}

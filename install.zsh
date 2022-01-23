cd $ZSH
git || printf "please install git" && exit
git clone https://github.com/killgriff22/ATLoader
cd ATLoader
cp @themes/ $ZSH
cp ./*.py $ZSH -r
cd ~/documents/
touch aliasesloader.zsh

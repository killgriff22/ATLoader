cd $ZSH
git clone https://github.com/killgriff22/ATLoader
cd ATLoader
cp -r @themes/ $ZSH
cp ./*.py $ZSH -r
cd ..
rm -rf ATLoader
cd ~/documents/
touch aliasesloader.zsh
